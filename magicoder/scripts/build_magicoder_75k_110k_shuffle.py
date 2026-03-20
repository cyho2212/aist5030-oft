#!/usr/bin/env python3
import argparse
from pathlib import Path

from datasets import Dataset, concatenate_datasets, load_dataset


def _normalize_oss_instruct(dataset: Dataset) -> Dataset:
    normalized = dataset.map(
        lambda row: {
            "instruction": row["problem"],
            "response": row["solution"],
        },
        remove_columns=dataset.column_names,
        desc="Normalizing Magicoder_oss_instruct_75k",
    )
    return normalized


def _normalize_evol_instruct(dataset: Dataset) -> Dataset:
    if "instruction" not in dataset.column_names or "response" not in dataset.column_names:
        raise ValueError(
            "Expected columns `instruction` and `response` in evol dataset, got "
            f"{dataset.column_names}"
        )
    return dataset.select_columns(["instruction", "response"])


def _filter_empty_pairs(dataset: Dataset) -> Dataset:
    return dataset.filter(
        lambda row: bool(row["instruction"]) and bool(row["response"]),
        desc="Filtering empty instruction/response rows",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build a shuffled JSONL from Magicoder 75k + 110k datasets "
            "in instruction/response format."
        )
    )
    parser.add_argument(
        "--oss_dataset",
        default="ise-uiuc/Magicoder_oss_instruct_75k",
        help="HF dataset id for Magicoder OSS-Instruct 75k",
    )
    parser.add_argument(
        "--evol_dataset",
        default="ise-uiuc/Magicoder_evol_instruct_110k",
        help="HF dataset id for Magicoder Evol-Instruct 110k",
    )
    parser.add_argument(
        "--split",
        default="train",
        help="Dataset split to load from each HF dataset",
    )
    parser.add_argument(
        "--output_file",
        default="data/magicoder_75k_110k_shuffle.jsonl",
        help="Output JSONL path",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Shuffle seed",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Optional max number of rows after shuffling (0 means keep all)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print(f"Loading {args.oss_dataset}:{args.split}")
    oss = load_dataset(args.oss_dataset, split=args.split)
    print(f"Loading {args.evol_dataset}:{args.split}")
    evol = load_dataset(args.evol_dataset, split=args.split)

    oss = _normalize_oss_instruct(oss)
    evol = _normalize_evol_instruct(evol)

    merged = concatenate_datasets([oss, evol])
    merged = _filter_empty_pairs(merged)
    merged = merged.shuffle(seed=args.seed)

    if args.limit > 0:
        keep = min(args.limit, len(merged))
        merged = merged.select(range(keep))
        print(f"Applied limit: {keep} rows")

    output_path = Path(args.output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    merged.to_json(str(output_path), orient="records", lines=True, force_ascii=False)

    print(f"Wrote {len(merged)} rows to {output_path.resolve()}")
    print("Columns:", merged.column_names)


if __name__ == "__main__":
    main()
