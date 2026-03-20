#!/usr/bin/env bash
set -euo pipefail

# 1.3B OFT debug run:
# - uses a small local subset for fast iteration
# - prints loss in plain logs (no tqdm)
# - limits total optimizer steps
#
# Usage:
#   bash scripts/run_oft_debug_ds1p3b.sh
#
# Optional env overrides:
#   GPU_ID=1
#   SOURCE_DATAFILE=data/magicoder_75k_110k_shuffle.jsonl
#   DATAFILE=data/magicoder_12k_debug.jsonl
#   DEBUG_ROWS=12000
#   OUTPUT_DIR=runs/debug_oft_ds1p3b
#   MAX_STEPS=60
#   LOGGING_STEPS=5
#   LEARNING_RATE=1e-5
#   WARMUP_STEPS=20
#   PER_DEVICE_TRAIN_BATCH_SIZE=2
#   GRADIENT_ACCUMULATION_STEPS=32

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

GPU_ID="${GPU_ID:-1}"
SOURCE_DATAFILE="${SOURCE_DATAFILE:-${REPO_ROOT}/data/magicoder_75k_110k_shuffle.jsonl}"
DATAFILE="${DATAFILE:-${REPO_ROOT}/data/magicoder_12k_debug.jsonl}"
DEBUG_ROWS="${DEBUG_ROWS:-12000}"
OUTPUT_DIR="${OUTPUT_DIR:-runs/debug_oft_ds1p3b}"
MAX_STEPS="${MAX_STEPS:-60}"
LOGGING_STEPS="${LOGGING_STEPS:-5}"
LEARNING_RATE="${LEARNING_RATE:-1e-5}"
WARMUP_STEPS="${WARMUP_STEPS:-20}"
PER_DEVICE_TRAIN_BATCH_SIZE="${PER_DEVICE_TRAIN_BATCH_SIZE:-2}"
GRADIENT_ACCUMULATION_STEPS="${GRADIENT_ACCUMULATION_STEPS:-32}"

if [[ ! -f "${SOURCE_DATAFILE}" ]]; then
  echo "Source data file not found: ${SOURCE_DATAFILE}" >&2
  exit 1
fi

if [[ ! -f "${DATAFILE}" ]]; then
  echo "Creating debug subset: ${DATAFILE} (rows=${DEBUG_ROWS})"
  mkdir -p "$(dirname "${DATAFILE}")"
  head -n "${DEBUG_ROWS}" "${SOURCE_DATAFILE}" > "${DATAFILE}"
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
    raise SystemExit("Missing packages: " + ", ".join(missing))
PY

export PYTHONPATH="${REPO_ROOT}/src:${PYTHONPATH:-}"
export CUDA_VISIBLE_DEVICES="${GPU_ID}"
export WANDB_DISABLED=true

accelerate launch \
  --num_processes 1 \
  --mixed_precision bf16 \
  -m magicoder.train \
  --model_key "deepseek-ai/deepseek-coder-1.3b-base" \
  --model_name_or_path "deepseek-ai/deepseek-coder-1.3b-base" \
  --use_flash_attention False \
  --max_training_seq_length 1024 \
  --datafile_paths "${DATAFILE}" \
  --output_dir "${OUTPUT_DIR}" \
  --bf16 True \
  --max_steps "${MAX_STEPS}" \
  --num_train_epochs 1 \
  --per_device_train_batch_size "${PER_DEVICE_TRAIN_BATCH_SIZE}" \
  --gradient_accumulation_steps "${GRADIENT_ACCUMULATION_STEPS}" \
  --group_by_length False \
  --ddp_find_unused_parameters False \
  --logging_strategy steps \
  --logging_steps "${LOGGING_STEPS}" \
  --disable_tqdm True \
  --report_to none \
  --log_level info \
  --optim adafactor \
  --max_grad_norm 1.0 \
  --warmup_steps "${WARMUP_STEPS}" \
  --learning_rate "${LEARNING_RATE}" \
  --lr_scheduler_type linear \
  --use_oft True \
  --oft_block_size 32 \
  --oft_target_modules "all-linear" \
  --oft_module_dropout 0.0
