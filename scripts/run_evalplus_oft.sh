#!/usr/bin/env bash
set -euo pipefail

# Run HumanEval+/MBPP+ generation + evaluation for an OFT checkpoint.
#
# Usage:
#   DATASET=humaneval bash scripts/run_evalplus_oft.sh
#   DATASET=mbpp bash scripts/run_evalplus_oft.sh
#
# Optional env overrides:
#   GPU_ID=1
#   MODEL_KEY=deepseek-ai/deepseek-coder-6.7b-base
#   MODEL_PATH=runs/oft_run2_fastlog
#   RUN_NAME=oft_run2_fastlog
#   OUTPUT_DIR=runs/evalplus_oft_run2_fastlog
#   MAX_NEW_TOKENS=512
#   N_PROBLEMS_PER_BATCH=8   (humaneval)
#   N_PROBLEMS_PER_BATCH=12  (mbpp)
#   N_SAMPLES_PER_PROBLEM=1
#   N_BATCHES=1
#   TEMPERATURE=0.0
#   TOP_P=1.0

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

DATASET="${DATASET:-humaneval}"
GPU_ID="${GPU_ID:-1}"
MODEL_KEY="${MODEL_KEY:-deepseek-ai/deepseek-coder-6.7b-base}"
MODEL_PATH="${MODEL_PATH:-runs/oft_run2_fastlog}"
RUN_NAME="${RUN_NAME:-oft_run2_fastlog}"
OUTPUT_DIR="${OUTPUT_DIR:-runs/evalplus_${RUN_NAME}}"
MAX_NEW_TOKENS="${MAX_NEW_TOKENS:-512}"
N_SAMPLES_PER_PROBLEM="${N_SAMPLES_PER_PROBLEM:-1}"
N_BATCHES="${N_BATCHES:-1}"
TEMPERATURE="${TEMPERATURE:-0.0}"
TOP_P="${TOP_P:-1.0}"

if [[ "${DATASET}" != "humaneval" && "${DATASET}" != "mbpp" ]]; then
  echo "DATASET must be one of: humaneval, mbpp" >&2
  exit 1
fi

if [[ "${DATASET}" == "humaneval" ]]; then
  N_PROBLEMS_PER_BATCH="${N_PROBLEMS_PER_BATCH:-8}"
else
  N_PROBLEMS_PER_BATCH="${N_PROBLEMS_PER_BATCH:-12}"
fi

if [[ ! -d "${MODEL_PATH}" ]]; then
  echo "MODEL_PATH not found: ${MODEL_PATH}" >&2
  exit 1
fi

python - <<'PY'
import importlib
missing = []
for m in ["transformers", "torch", "evalplus"]:
    try:
        importlib.import_module(m)
    except Exception:
        missing.append(m)
if missing:
    raise SystemExit("Missing packages: " + ", ".join(missing))
PY

export PYTHONPATH="${REPO_ROOT}/src:${PYTHONPATH:-}"
export CUDA_VISIBLE_DEVICES="${GPU_ID}"

mkdir -p "${OUTPUT_DIR}"
SAMPLES_PATH="${OUTPUT_DIR}/evalplus-${RUN_NAME}-${DATASET}.jsonl"

python -m experiments.text2code \
  --model_key "${MODEL_KEY}" \
  --model_name_or_path "${MODEL_PATH}" \
  --save_path "${SAMPLES_PATH}" \
  --dataset "${DATASET}" \
  --temperature "${TEMPERATURE}" \
  --top_p "${TOP_P}" \
  --max_new_tokens "${MAX_NEW_TOKENS}" \
  --n_problems_per_batch "${N_PROBLEMS_PER_BATCH}" \
  --n_samples_per_problem "${N_SAMPLES_PER_PROBLEM}" \
  --n_batches "${N_BATCHES}"

if [[ "${DATASET}" == "mbpp" ]]; then
  evalplus.sanitize "${SAMPLES_PATH}"
  SANITIZED_PATH="${SAMPLES_PATH%.jsonl}-sanitized.jsonl"
  evalplus.evaluate --dataset mbpp --samples "${SANITIZED_PATH}"
  echo "MBPP+ results generated from: ${SANITIZED_PATH}"
else
  evalplus.evaluate --dataset humaneval --samples "${SAMPLES_PATH}"
  echo "HumanEval+ results generated from: ${SAMPLES_PATH}"
fi
