#!/usr/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd "$SCRIPT_DIR"

python3 -m venv .venv

source "./.venv/bin/activate"

python -m pip install -r requirements.txt