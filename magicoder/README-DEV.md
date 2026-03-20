# Implementation Details of 🎩Magicoder

> [!WARNING]
> This documentation is still WIP. Raise an [issue](https://github.com/ise-uiuc/magicoder/issues) in case you found any errors.

## Data collection and generation

Make sure you have set up your `OPENAI_API_KEY` and optionally `OPENAI_BASE_URL`. Then run with

```bash
python src/magicoder/generate_data.py \
  --seed_code_start_index ${START_INDEX_OF_RAW_DATA} \
  --max_new_data ${MAX_DATA_TO_GENERATE} \
  --data_dir python \
  --tag python
```

To continue an interrupted run, use `--continue_from` flag:

```bash
python src/magicoder/generate_data.py \
  --seed_code_start_index ${START_INDEX_OF_RAW_DATA} \
  --max_new_data ${MAX_DATA_TO_GENERATE} \
  --data_dir python \
  --continue_from ${PATH_TO_DATA_FILE}
```

## Data cleaning and decontamination

After the data collection, clean and decontaminate the data with the following command:

```bash
python src/magicoder/clean_data.py --data_files {PATH_TO_DATA_FILE} --output_file {CLEANING_OUTPUT_PATH}

python -m magicoder.decontamination.find_substrings \
  --dataset_name "json" \
  --output_file ${DECONTAM_OUTPUT_PATH} \
  --output_dir ${OUTPUT_DIR} \
  --columns problem solution \
  --data_files ${PATH_TO_DATA_FILE}
```

You probably need to run this multiple times with different data files.

## Data preprocessing

Before instruction tuning, let's reformat the data into instruction-response pairs:
  
```bash
python src/magicoder/preprocess_data.py \
  --dataset_path json \
  --data_files ${DECONTAM_OUTPUT_PATH} \
  --output_file ${PREPROCESS_OUTPUT_PATH} \
  --key src-instruct
```

After that, you can combine all the `jsonl` files into one.

## Instruction tuning

Pointing the environment variable `CUDA_VISIBLE_DEVICES` to the GPUs you want to use, train the model with the following command to obtain Magicoder:

```bash
accelerate launch -m magicoder.train \
  --model_key $MODEL_KEY \
  --use_flash_attention True \
  --max_training_seq_length 1216 \
  --datafile_paths \
    ${PATH_TO_OSS_INSTRUCT} \
  --output_dir $MAGICODER_OUTPUT_DIR \
  --bf16 True \
  --num_train_epochs 2 \
  --per_device_train_batch_size 2 \
  --gradient_accumulation_steps 128 \
  --group_by_length False \
  --ddp_find_unused_parameters False \
  --logging_steps 1 \
  --log_level info \
  --optim adafactor \
  --max_grad_norm -1 \
  --warmup_steps 15 \
  --learning_rate 5e-5 \
  --lr_scheduler_type linear
```

For parameter-efficient finetuning with OFT, use the same pipeline with `--use_oft`:

```bash
accelerate launch -m magicoder.train \
  --model_key "deepseek-ai/deepseek-coder-1.3b-base" \
  --model_name_or_path "anyname" \
  --use_flash_attention True \
  --max_training_seq_length 1024 \
  --datafile_paths \
    "magicoder_75k_110k_shuffle.jsonl" \
  --output_dir "anyname-oft" \
  --bf16 True \
  --num_train_epochs 1 \
  --per_device_train_batch_size 2 \
  --gradient_accumulation_steps 128 \
  --group_by_length False \
  --ddp_find_unused_parameters False \
  --logging_steps 1 \
  --log_level info \
  --optim adafactor \
  --max_grad_norm -1 \
  --warmup_steps 15 \
  --learning_rate 5e-5 \
  --lr_scheduler_type linear \
  --use_oft True \
  --oft_block_size 32 \
  --oft_target_modules "all-linear" \
  --oft_module_dropout 0.0
```

To get Magicoder-S, continue the training with the following command:

```bash
accelerate launch -m magicoder.train \
  --model_key $MODEL_KEY \
  --model_name_or_path $MAGICODER_OUTPUT_DIR \
  --use_flash_attention True \
  --max_training_seq_length 1024 \
  --datafile_paths \
    ${PATH_TO_EVOL_INSTRUCT} \
  --output_dir $MAGICODER_S_OUTPUT_DIR \
  --bf16 True \
  --num_train_epochs 2 \
  --per_device_train_batch_size 2 \
  --gradient_accumulation_steps 128 \
  --group_by_length False \
  --ddp_find_unused_parameters False \
  --logging_steps 1 \
  --log_level info \
  --optim adafactor \
  --max_grad_norm -1 \
  --warmup_steps 15 \
  --learning_rate 5e-5 \
  --lr_scheduler_type linear
```
