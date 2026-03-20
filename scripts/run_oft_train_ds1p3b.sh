#!/usr/bin/env bash
set -euo pipefail

# Run from repo root:
#   bash scripts/run_oft_train_ds1p3b.sh
#
# Optional env overrides:
#   DATAFILE=/abs/path/to/magicoder_75k_110k_shuffle.jsonl
#   OUTPUT_DIR=runs/oft_run1
#   NUM_PROCESSES=1
#   GPU_ID=1
#   USE_FLASH_ATTENTION=False
#   DISABLE_TQDM=True
#   LOGGING_STEPS=10
#   LEARNING_RATE=2e-5
#   WARMUP_STEPS=80
#   MAX_GRAD_NORM=1.0
#   PER_DEVICE_TRAIN_BATCH_SIZE=1
#   GRADIENT_ACCUMULATION_STEPS=256
#   MAX_TRAINING_SEQ_LENGTH=1024
#   OFT_TARGET_MODULES=all-linear

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

DATAFILE="${DATAFILE:-${REPO_ROOT}/data/magicoder_75k_110k_shuffle.jsonl}"
OUTPUT_DIR="${OUTPUT_DIR:-runs/oft_run1}"
NUM_PROCESSES="${NUM_PROCESSES:-1}"
GPU_ID="${GPU_ID:-1}"
USE_FLASH_ATTENTION="${USE_FLASH_ATTENTION:-False}"
DISABLE_TQDM="${DISABLE_TQDM:-True}"
LOGGING_STEPS="${LOGGING_STEPS:-10}"
LEARNING_RATE="${LEARNING_RATE:-2e-5}"
WARMUP_STEPS="${WARMUP_STEPS:-80}"
MAX_GRAD_NORM="${MAX_GRAD_NORM:-1.0}"
PER_DEVICE_TRAIN_BATCH_SIZE="${PER_DEVICE_TRAIN_BATCH_SIZE:-1}"
GRADIENT_ACCUMULATION_STEPS="${GRADIENT_ACCUMULATION_STEPS:-256}"
MAX_TRAINING_SEQ_LENGTH="${MAX_TRAINING_SEQ_LENGTH:-1024}"
OFT_TARGET_MODULES="${OFT_TARGET_MODULES:-all-linear}"

if [[ ! -f "${DATAFILE}" ]]; then
  echo "Dataset file not found: ${DATAFILE}" >&2
  echo "Build it with: python scripts/build_magicoder_75k_110k_shuffle.py" >&2
  exit 1
fi

python - <<'PY'
import importlib
missing = []
for m in ["accelerate", "transformers", "datasets", "torch", "peft"]:
    try:
        importlib.import_module(m)
    except Exception:
        missing.append(m)
if missing:
    raise SystemExit(
        "Missing packages: "
        + ", ".join(missing)
        + ". Install with: pip install peft"
    )
PY

export PYTHONPATH="${REPO_ROOT}/src:${PYTHONPATH:-}"
export CUDA_VISIBLE_DEVICES="${GPU_ID}"
export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"

accelerate launch \
  --num_processes "${NUM_PROCESSES}" \
  --mixed_precision bf16 \
  -m magicoder.train \
  --model_key "deepseek-ai/deepseek-coder-6.7b-base" \
  --model_name_or_path "deepseek-ai/deepseek-coder-6.7b-base" \
  --use_flash_attention "${USE_FLASH_ATTENTION}" \
  --max_training_seq_length "${MAX_TRAINING_SEQ_LENGTH}" \
  --datafile_paths "${DATAFILE}" \
  --output_dir "${OUTPUT_DIR}" \
  --bf16 True \
  --num_train_epochs 1 \
  --per_device_train_batch_size "${PER_DEVICE_TRAIN_BATCH_SIZE}" \
  --gradient_accumulation_steps "${GRADIENT_ACCUMULATION_STEPS}" \
  --group_by_length False \
  --ddp_find_unused_parameters False \
  --logging_strategy steps \
  --logging_steps "${LOGGING_STEPS}" \
  --disable_tqdm "${DISABLE_TQDM}" \
  --log_level info \
  --optim adafactor \
  --max_grad_norm "${MAX_GRAD_NORM}" \
  --warmup_steps "${WARMUP_STEPS}" \
  --learning_rate "${LEARNING_RATE}" \
  --lr_scheduler_type linear \
  --use_oft True \
  --oft_block_size 32 \
  --oft_target_modules "${OFT_TARGET_MODULES}" \
  --oft_module_dropout 0.0
