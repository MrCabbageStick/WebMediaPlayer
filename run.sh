#!/usr/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd "$SCRIPT_DIR"
source "./.venv/bin/activate"

PYTHON_FILE="./src/app.py"

if [[ -f "$PYTHON_FILE" ]]; then
    python "$PYTHON_FILE"

else
    echo "app.py file not found in directory: $SCRIPT_DIR/src"

fi


