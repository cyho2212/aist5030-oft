from __future__ import annotations

import gzip
import json
from pathlib import Path
from typing import Any


class DS1000Problem(dict[str, Any]):
    @property
    def problem_id(self) -> int:
        return int(self["problem_id"])


class DS1000Dataset:
    def __init__(self, dataset_path: str, mode: str = "Completion"):
        if mode != "Completion":
            raise ValueError(
                "This DS-1000 adapter supports Completion mode only "
                "(the simplified DS-1000 format removed insertion mode)."
            )
        dataset_file = _resolve_dataset_file(Path(dataset_path))
        records = _load_records(dataset_file)
        grouped: dict[str, list[DS1000Problem]] = {}
        for record in records:
            metadata = record.get("metadata", {})
            lib = str(metadata.get("library", "Unknown"))
            problem = DS1000Problem(
                problem_id=int(metadata["problem_id"]),
                lib=lib,
                prompt=str(record["prompt"]),
                metadata=metadata,
            )
            grouped.setdefault(lib, []).append(problem)
        for problems in grouped.values():
            problems.sort(key=lambda p: p.problem_id)
        self.data = grouped


def _resolve_dataset_file(dataset_path: Path) -> Path:
    if dataset_path.is_file():
        return dataset_path
    candidates = [
        dataset_path / "ds1000.jsonl.gz",
        dataset_path / "ds1000.jsonl",
        dataset_path / "data" / "ds1000.jsonl.gz",
        dataset_path / "data" / "ds1000.jsonl",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(
        "Could not find DS-1000 data file. Expected one of: "
        + ", ".join(str(path) for path in candidates)
    )


def _load_records(dataset_file: Path) -> list[dict[str, Any]]:
    if dataset_file.suffix == ".gz":
        with gzip.open(dataset_file, "rt") as f:
            return [json.loads(line) for line in f if line.strip()]
    with dataset_file.open("r") as f:
        return [json.loads(line) for line in f if line.strip()]
