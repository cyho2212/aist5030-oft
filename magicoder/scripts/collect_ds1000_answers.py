#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Collect Magicoder DS-1000 generations into DS-1000 answers jsonl."
    )
    parser.add_argument(
        "--generation_dir",
        type=Path,
        required=True,
        help="Directory like <output_dir>/<model_key_with_slashes_replaced_by_dashes>.",
    )
    parser.add_argument(
        "--output_path",
        type=Path,
        required=True,
        help="Path to write DS-1000 answers jsonl (one line per problem).",
    )
    parser.add_argument(
        "--sample_index",
        type=int,
        default=0,
        help="Which generated sample file to use per problem (default: 0).",
    )
    parser.add_argument(
        "--expected_count",
        type=int,
        default=1000,
        help="Expected number of problems. Script fails if mismatched.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.generation_dir.is_dir():
        raise FileNotFoundError(f"Generation directory not found: {args.generation_dir}")

    answers: list[dict[str, object]] = []
    missing: list[tuple[int, Path]] = []

    for q_dir in sorted(args.generation_dir.glob("*/Completion/q*")):
        problem_name = q_dir.name
        if not problem_name.startswith("q"):
            continue
        problem_id = int(problem_name[1:])
        sample_file = q_dir / f"{args.sample_index}.py"
        if not sample_file.is_file():
            missing.append((problem_id, sample_file))
            continue
        code = sample_file.read_text()
        answers.append({"id": problem_id, "code": code})

    answers.sort(key=lambda row: int(row["id"]))  # type: ignore[arg-type]

    if missing:
        first = missing[0]
        raise FileNotFoundError(
            f"Missing {len(missing)} sample files. First missing: "
            f"problem {first[0]} at {first[1]}"
        )

    if args.expected_count and len(answers) != args.expected_count:
        raise ValueError(
            f"Expected {args.expected_count} answers, found {len(answers)} "
            f"in {args.generation_dir}"
        )

    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    with args.output_path.open("w") as f:
        for row in answers:
            f.write(json.dumps(row) + "\n")

    print(f"Wrote {len(answers)} answers to {args.output_path}")


if __name__ == "__main__":
    main()
