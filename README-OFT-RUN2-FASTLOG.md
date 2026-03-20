# OFT Run2 Fastlog Guide

This guide is for the `cy/magicoder` repo and the `runs/oft_run2_fastlog` workflow.

It covers:
- package installation
- OFT finetuning
- generation + evaluation on HumanEval+, MBPP+, and DS-1000

## 1) Package Installation

From repo root (`/mnt/raid1/mzyu/CSY/cy/magicoder`):

```bash
bash scripts/setup_env.sh
```

If you prefer manual setup:

```bash
python -m pip install --upgrade pip
python -m pip install --upgrade pdm
pdm install -G dev
```

## 2) Build Training Data

Build the merged/shuffled dataset (`75k + 110k`):

```bash
python scripts/build_magicoder_75k_110k_shuffle.py
```

Output file:

```text
data/magicoder_75k_110k_shuffle.jsonl
```

## 3) Finetuning (OFT, fastlog config)

Run training (default is DeepSeek-Coder-6.7B base + OFT):

```bash
GPU_ID=1 OUTPUT_DIR=runs/oft_run2_fastlog bash scripts/run_oft_train_fastlog.sh
```

Recommended background run:

```bash
nohup env GPU_ID=1 OUTPUT_DIR=runs/oft_run2_fastlog \
  bash scripts/run_oft_train_fastlog.sh \
  > nohup_oft_run2_fastlog.log 2>&1 &
```

## 4) Evaluation: HumanEval+ and MBPP+

Use the trained adapter directory directly (default `MODEL_PATH=runs/oft_run2_fastlog`).

HumanEval+:

```bash
DATASET=humaneval GPU_ID=1 MODEL_PATH=runs/oft_run2_fastlog \
  RUN_NAME=oft_run2_fastlog \
  bash scripts/run_evalplus_oft.sh
```

MBPP+:

```bash
DATASET=mbpp GPU_ID=1 MODEL_PATH=runs/oft_run2_fastlog \
  RUN_NAME=oft_run2_fastlog \
  bash scripts/run_evalplus_oft.sh
```

## 5) Evaluation: DS-1000

Clone DS-1000 once:

```bash
cd /mnt/raid1/mzyu/CSY/cy
git clone https://github.com/xlang-ai/DS-1000.git
```

Run DS-1000 generation + evaluation:

```bash
cd /mnt/raid1/mzyu/CSY/cy/magicoder
GPU_ID=1 MODEL_PATH=runs/oft_run2_fastlog \
  RUN_NAME=oft_run2_fastlog_ds1000 \
  bash scripts/run_ds1000_eval_oft.sh
```

## 6) One-Command All Evaluation

Run HumanEval+ + MBPP+ + DS-1000 in sequence:

```bash
GPU_ID=1 MODEL_PATH=runs/oft_run2_fastlog \
  RUN_NAME=oft_run2_fastlog \
  bash scripts/run_oft_eval_all.sh
```

## 7) Output Paths

Main finetuning output:

```text
runs/oft_run2_fastlog
```

EvalPlus outputs:

```text
runs/evalplus_oft_run2_fastlog/
  evalplus-oft_run2_fastlog-humaneval.jsonl
  evalplus-oft_run2_fastlog-mbpp.jsonl
  evalplus-oft_run2_fastlog-mbpp-sanitized.jsonl
  *eval_results.json
```

DS-1000 outputs:

```text
runs/ds1000_oft_run2_fastlog/
/mnt/raid1/mzyu/CSY/cy/DS-1000/results/oft_run2_fastlog_ds1000-result.txt
```

## Notes

- `run_oft_train_ds1p3b.sh` name is historical; current default base model is 6.7B.
- If DS-1000 TensorFlow-related tasks fail, use the DS-1000 recommended Python/library environment for best fidelity.
