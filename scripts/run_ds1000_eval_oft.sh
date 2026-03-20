#!/usr/bin/env bash
set -euo pipefail

# Run from repo root:
#   bash scripts/run_ds1000_eval_oft.sh
#
# Optional env overrides:
#   DS1000_ROOT=/mnt/raid1/mzyu/CSY/cy/DS-1000
#   DATASET_PATH=/mnt/raid1/mzyu/CSY/cy/DS-1000/data
#   MODEL_KEY=deepseek-ai/deepseek-coder-6.7b-base
#   MODEL_PATH=runs/oft_run2_fastlog/checkpoint-2000
#   OUTPUT_DIR=runs/ds1000_oft_run2_fastlog_ckpt2000
#   RUN_NAME=oft_run2_fastlog_ckpt2000
#   GPU_ID=1
#   TEMPERATURE=0.0
#   TOP_P=1.0
#   MAX_LENGTH=4096
#   N_SAMPLES_PER_BATCH=1
#   N_BATCHES=1
#   EXPECTED_COUNT=1000
#   SKIP_DS1000_TEST=False

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

DS1000_ROOT="${DS1000_ROOT:-/mnt/raid1/mzyu/CSY/cy/DS-1000}"
DATASET_PATH="${DATASET_PATH:-${DS1000_ROOT}/data}"
MODEL_KEY="${MODEL_KEY:-deepseek-ai/deepseek-coder-6.7b-base}"
MODEL_PATH="${MODEL_PATH:-runs/oft_run2_fastlog/checkpoint-2000}"
OUTPUT_DIR="${OUTPUT_DIR:-runs/ds1000_oft_run2_fastlog_ckpt2000}"
RUN_NAME="${RUN_NAME:-oft_run2_fastlog_ckpt2000}"
GPU_ID="${GPU_ID:-1}"
TEMPERATURE="${TEMPERATURE:-0.0}"
TOP_P="${TOP_P:-1.0}"
MAX_LENGTH="${MAX_LENGTH:-4096}"
N_SAMPLES_PER_BATCH="${N_SAMPLES_PER_BATCH:-1}"
N_BATCHES="${N_BATCHES:-1}"
EXPECTED_COUNT="${EXPECTED_COUNT:-1000}"
SKIP_DS1000_TEST="${SKIP_DS1000_TEST:-False}"

if [[ ! -d "${DS1000_ROOT}" ]]; then
  echo "DS1000_ROOT not found: ${DS1000_ROOT}" >&2
  echo "Clone with: git clone https://github.com/xlang-ai/DS-1000.git ${DS1000_ROOT}" >&2
  exit 1
fi

if [[ ! -f "${MODEL_PATH}/adapter_config.json" && ! -d "${MODEL_PATH}" ]]; then
  echo "MODEL_PATH not found: ${MODEL_PATH}" >&2
  exit 1
fi

if [[ -f "${DATASET_PATH}" ]]; then
  :
elif [[ -f "${DATASET_PATH}/ds1000.jsonl.gz" || -f "${DATASET_PATH}/ds1000.jsonl" ]]; then
  :
else
  echo "Could not find ds1000 data file from DATASET_PATH: ${DATASET_PATH}" >&2
  exit 1
fi

python - <<'PY'
import importlib
missing = []
for m in ["transformers", "torch", "tqdm"]:
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

python -m experiments.ds_1000 \
  --dataset_path "${DATASET_PATH}" \
  --model_key "${MODEL_KEY}" \
  --model_name_or_path "${MODEL_PATH}" \
  --output_dir "${OUTPUT_DIR}" \
  --mode Completion \
  --temperature "${TEMPERATURE}" \
  --top_p "${TOP_P}" \
  --max_length "${MAX_LENGTH}" \
  --n_samples_per_batch "${N_SAMPLES_PER_BATCH}" \
  --n_batches "${N_BATCHES}"

MODEL_KEY_SAFE="${MODEL_KEY//\//-}"
GENERATION_DIR="${OUTPUT_DIR}/${MODEL_KEY_SAFE}"
ANSWERS_PATH="${DS1000_ROOT}/data/${RUN_NAME}-answers.jsonl"
RESULT_PATH="${DS1000_ROOT}/results/${RUN_NAME}-result.txt"

python scripts/collect_ds1000_answers.py \
  --generation_dir "${GENERATION_DIR}" \
  --output_path "${ANSWERS_PATH}" \
  --sample_index 0 \
  --expected_count "${EXPECTED_COUNT}"

if [[ "${SKIP_DS1000_TEST}" == "True" ]]; then
  echo "Skipping DS-1000 execution test as requested."
  echo "Generated answers file: ${ANSWERS_PATH}"
  exit 0
fi

(
  cd "${DS1000_ROOT}"
  python test_ds1000.py --model "${RUN_NAME}"
)

if [[ -f "${RESULT_PATH}" ]]; then
  cp "${RESULT_PATH}" "${OUTPUT_DIR}/"
  echo "DS-1000 summary: ${RESULT_PATH}"
  echo "Copied summary to: ${OUTPUT_DIR}/$(basename "${RESULT_PATH}")"
else
  echo "Warning: expected result file not found: ${RESULT_PATH}" >&2
fi
