#!/usr/bin/env bash
set -euo pipefail

# One-command evaluation for oft_run2_fastlog:
# - HumanEval+
# - MBPP+
# - DS-1000

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

GPU_ID="${GPU_ID:-1}"
MODEL_KEY="${MODEL_KEY:-deepseek-ai/deepseek-coder-6.7b-base}"
MODEL_PATH="${MODEL_PATH:-runs/oft_run2_fastlog}"
RUN_NAME="${RUN_NAME:-oft_run2_fastlog}"

EVALPLUS_OUTPUT_DIR="${EVALPLUS_OUTPUT_DIR:-runs/evalplus_${RUN_NAME}}"
DS1000_OUTPUT_DIR="${DS1000_OUTPUT_DIR:-runs/ds1000_${RUN_NAME}}"
DS1000_RUN_NAME="${DS1000_RUN_NAME:-${RUN_NAME}_ds1000}"

DATASET=humaneval \
GPU_ID="${GPU_ID}" \
MODEL_KEY="${MODEL_KEY}" \
MODEL_PATH="${MODEL_PATH}" \
RUN_NAME="${RUN_NAME}" \
OUTPUT_DIR="${EVALPLUS_OUTPUT_DIR}" \
bash scripts/run_evalplus_oft.sh

DATASET=mbpp \
GPU_ID="${GPU_ID}" \
MODEL_KEY="${MODEL_KEY}" \
MODEL_PATH="${MODEL_PATH}" \
RUN_NAME="${RUN_NAME}" \
OUTPUT_DIR="${EVALPLUS_OUTPUT_DIR}" \
bash scripts/run_evalplus_oft.sh

GPU_ID="${GPU_ID}" \
MODEL_KEY="${MODEL_KEY}" \
MODEL_PATH="${MODEL_PATH}" \
OUTPUT_DIR="${DS1000_OUTPUT_DIR}" \
RUN_NAME="${DS1000_RUN_NAME}" \
bash scripts/run_ds1000_eval_oft.sh

echo "All evaluations finished."
echo "EvalPlus output dir: ${EVALPLUS_OUTPUT_DIR}"
echo "DS-1000 output dir: ${DS1000_OUTPUT_DIR}"
