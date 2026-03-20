import inspect
from dataclasses import dataclass, field
from typing import Any, cast

import torch
from datasets import load_dataset
from transformers import HfArgumentParser, Trainer, TrainingArguments

from magicoder.llm_wrapper import (
    DecodingConfig,
    EncodingConfig,
    TokenizationContext,
    get_model_context,
    pad_sequences,
)
from magicoder.prompt_template import MAGICODER_PROMPT
from magicoder.utils import N_CORES


@dataclass(frozen=True)
class ModelArguments:
    model_key: str
    model_name_or_path: str | None = None


# Ignored index in CrossEntropyLoss
IGNORED_INDEX = -100


def map_dataset(
    examples: dict[str, list[str]],
    args: "Args",
    context: TokenizationContext,
) -> dict:
    instructions = examples["instruction"]
    responses = examples["response"]

    prompts = [
        MAGICODER_PROMPT.format(instruction=instruction, response="")
        for instruction in instructions
    ]
    completions = responses

    assert len(prompts) == len(completions)
    prompt_config = EncodingConfig(add_bos=True, add_eos=False)
    completion_config = EncodingConfig(add_bos=False, add_eos=True)
    prompt_id_batches = context.encode(prompt_config, prompts)
    completion_id_batches = context.encode(completion_config, completions)
    # prompt_id_batches = context.tokenization_context.encode(prompt_config, prompts)
    # completion_id_batches = context.tokenization_context.encode(
    #     completion_config, completions
    # )
    assert len(prompt_id_batches) == len(completion_id_batches)
    untruncated_input_ids = [
        (instruction_ids + response_ids)
        for instruction_ids, response_ids in zip(
            prompt_id_batches, completion_id_batches
        )
    ]
    exceeding_length = [
        len(input_id) > args.max_training_seq_length
        for input_id in untruncated_input_ids
    ]
    input_ids = [
        input_id[: args.max_training_seq_length] for input_id in untruncated_input_ids
    ]
    # NOTE: no need to set EOF to IGNORED_INDEX as it is *implicitly* ignored inside
    # the model.forward that shifts the logits left by 1
    labels = [
        (list(map(lambda _: IGNORED_INDEX, instruction_ids)) + response_ids)[
            : args.max_training_seq_length
        ]
        for instruction_ids, response_ids in zip(
            prompt_id_batches, completion_id_batches
        )
    ]
    # `len` of each returned value must be the same, which is required by `tokenizer.map`
    # After `map`, they are treated as individual pieces of data, not as a batch.
    assert len(input_ids) == len(labels)
    for input_id_batch, label_batch in zip(input_ids, labels):
        assert len(input_id_batch) == len(label_batch)
    return {
        "input_ids": input_ids,
        "labels": labels,
        "exceeding_length": exceeding_length,
    }


def get_data_collator(args: "Args", pad_token_id: int):
    """Pad input_ids to the right, create labels by setting the padding tokens to -100, and
    create attention_mask to ignore the padding tokens"""

    def collate(examples: list[dict[str, list[int]]]) -> dict[str, torch.Tensor]:
        input_ids_unpadded = [example["input_ids"] for example in examples]
        labels_unpadded = [example["labels"] for example in examples]
        padding_length = (
            args.max_training_seq_length if args.pad_to_max_length else None
        )
        input_ids = pad_sequences(
            input_ids_unpadded, pad_token_id, "right", padding_length=padding_length
        )
        labels = pad_sequences(
            labels_unpadded, IGNORED_INDEX, "right", padding_length=padding_length
        )

        assert input_ids.shape == labels.shape
        assert len(input_ids) == len(examples)
        # Enforced in `map_raw_dataset`
        assert input_ids.shape[-1] <= args.max_training_seq_length
        if args.pad_to_max_length:
            assert input_ids.shape[-1] == args.max_training_seq_length

        return {
            "input_ids": input_ids,
            "labels": labels,
            "attention_mask": input_ids.ne(pad_token_id),
        }

    return collate


@dataclass(frozen=True)
class Args:
    datafile_paths: list[str] = field(default_factory=list)
    max_training_seq_length: int = field(default=1216)
    pad_to_max_length: bool = field(default=False)
    eval_dataset_size: float = field(
        default=0.05, metadata={"help": "0--1 means ratio, >1 means number of examples"}
    )
    use_flash_attention: bool = field(default=False)
    use_oft: bool = field(
        default=False, metadata={"help": "Enable Orthogonal Finetuning (OFT) via PEFT."}
    )
    oft_r: int = field(
        default=0,
        metadata={"help": "OFT rank. Use either this or oft_block_size, not both."},
    )
    oft_block_size: int = field(
        default=32,
        metadata={
            "help": "OFT block size. Requires a PEFT version that supports oft_block_size."
        },
    )
    oft_target_modules: str = field(
        default="all-linear",
        metadata={
            "help": "Target modules for OFT. Use 'all-linear' or comma-separated module names."
        },
    )
    oft_module_dropout: float = field(default=0.0)
    oft_bias: str = field(
        default="none",
        metadata={"help": "Bias mode for OFT adapters: none, all, oft_only."},
    )
    oft_modules_to_save: str = field(
        default="",
        metadata={"help": "Optional comma-separated modules to keep trainable and save."},
    )
    oft_use_cayley_neumann: bool = field(default=True)
    oft_num_cayley_neumann_terms: int = field(default=5)
    oft_coft: bool = field(default=False)
    oft_eps: float = field(default=6e-5)
    oft_block_share: bool = field(default=False)
    oft_init_weights: bool = field(default=True)


def _parse_csv_list(text: str) -> list[str] | None:
    values = [item.strip() for item in text.split(",") if item.strip()]
    return values if values else None


def _parse_oft_target_modules(text: str) -> str | list[str]:
    normalized = text.strip()
    if not normalized:
        raise ValueError("`oft_target_modules` must not be empty when OFT is enabled.")
    if normalized == "all-linear":
        return normalized
    modules = _parse_csv_list(normalized)
    if modules is None:
        raise ValueError(
            "`oft_target_modules` must be 'all-linear' or a comma-separated list."
        )
    return modules


def _maybe_apply_oft(model: torch.nn.Module, args: "Args") -> torch.nn.Module:
    if not args.use_oft:
        return model

    try:
        from peft import OFTConfig, get_peft_model
    except ImportError as error:
        raise ImportError(
            "OFT is enabled but `peft` is not installed. "
            "Install it first, for example: `pip install peft`."
        ) from error

    supported_fields = set(inspect.signature(OFTConfig).parameters)

    config_kwargs: dict[str, Any] = {
        "task_type": "CAUSAL_LM",
        "inference_mode": False,
        "target_modules": _parse_oft_target_modules(args.oft_target_modules),
        "module_dropout": args.oft_module_dropout,
        "bias": args.oft_bias,
        "modules_to_save": _parse_csv_list(args.oft_modules_to_save),
        "coft": args.oft_coft,
        "eps": args.oft_eps,
        "block_share": args.oft_block_share,
        "init_weights": args.oft_init_weights,
        "use_cayley_neumann": args.oft_use_cayley_neumann,
        "num_cayley_neumann_terms": args.oft_num_cayley_neumann_terms,
    }
    config_kwargs = {
        key: value
        for key, value in config_kwargs.items()
        if key in supported_fields and value is not None
    }

    supports_block_size = "oft_block_size" in supported_fields
    if supports_block_size:
        if args.oft_r > 0 and args.oft_block_size > 0:
            raise ValueError("Set either `oft_r` or `oft_block_size`, not both.")
        if args.oft_r <= 0 and args.oft_block_size <= 0:
            raise ValueError("Set one of `oft_r` or `oft_block_size` to a positive value.")
        if args.oft_r > 0:
            config_kwargs["r"] = args.oft_r
        if args.oft_block_size > 0:
            config_kwargs["oft_block_size"] = args.oft_block_size
    else:
        if args.oft_r <= 0:
            raise ValueError(
                "This PEFT version does not support `oft_block_size`. "
                "Please set `oft_r` > 0 or upgrade PEFT."
            )
        config_kwargs["r"] = args.oft_r

    oft_config = OFTConfig(**config_kwargs)
    oft_model = get_peft_model(model, oft_config)
    if hasattr(oft_model, "print_trainable_parameters"):
        oft_model.print_trainable_parameters()
    return oft_model


def train():
    parser = HfArgumentParser((ModelArguments, TrainingArguments, Args))
    model_args, training_args, args = cast(
        tuple[ModelArguments, TrainingArguments, Args],
        parser.parse_args_into_dataclasses(),
    )
    dataset = load_dataset("json", data_files=args.datafile_paths, split="train")

    model_key = model_args.model_key
    if (model_name_or_path := model_args.model_name_or_path) is None:
        model_name_or_path = model_key

    tokenization_context = TokenizationContext.from_model_key(
        model_key, model_name_or_path
    )
    # if dataset_config.dpo_jsonl_path is None or dataset_config.dpo_sft:
    train_dataset = dataset.map(
        function=map_dataset,
        fn_kwargs=dict(args=args, context=tokenization_context),
        batched=True,
        num_proc=N_CORES,
        remove_columns=dataset.column_names,
        load_from_cache_file=False,  # not args.overwrite_cache
        desc="Running tokenizer on train dataset",
    )
    msg = f"#Examples truncated: {sum(train_dataset['exceeding_length'])} / {len(train_dataset)}"
    print(msg)
    # else:
    #     train_dataset = dataset

    # Transformers renamed this field in newer versions: evaluation_strategy -> eval_strategy.
    eval_strategy = getattr(
        training_args,
        "evaluation_strategy",
        getattr(training_args, "eval_strategy", "no"),
    )
    if hasattr(eval_strategy, "value"):
        eval_strategy = eval_strategy.value

    # Shuffling
    if training_args.eval_steps is None and eval_strategy == "no":
        train_dataset = train_dataset.shuffle(seed=training_args.seed)
        eval_dataset = None
    else:
        print("Splitting dataset")
        split_dataset = train_dataset.train_test_split(
            test_size=args.eval_dataset_size,
            shuffle=True,
            seed=training_args.seed,
        )
        train_dataset = split_dataset["train"]
        eval_dataset = split_dataset["test"]

    state = get_model_context(
        model_key,
        model_name_or_path,
        tokenization_context,
        inference_mode=False,
        use_flash_attention=args.use_flash_attention,
    )
    state.model = cast(Any, _maybe_apply_oft(state.model, args))

    print("Parallel mode:", training_args.parallel_mode)
    data_collator = get_data_collator(args, state.tokenization_context.pad_token_id)

    # neftune_noise_alpha
    trainer = Trainer(
        model=state.model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=data_collator,
        # eval_dataset=small_eval_dataset,
        # compute_metrics=compute_metrics,
    )

    # NOTE: the checkpoint will override the initialized model
    trainer.train(resume_from_checkpoint=training_args.resume_from_checkpoint)
    trainer.save_state()
    trainer.save_model(training_args.output_dir)
    state.tokenization_context.tokenizer.save_pretrained(training_args.output_dir)


if __name__ == "__main__":
    train()
