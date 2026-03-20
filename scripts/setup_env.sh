#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

python -m pip install --upgrade pip
python -m pip install --upgrade pdm

# Install project + dev dependencies (accelerate/evalplus/etc.)
pdm install -G dev

echo "Environment setup complete."
echo "Activate your env, then run scripts from: ${REPO_ROOT}"
