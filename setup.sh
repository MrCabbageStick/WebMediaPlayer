#!/usr/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd "$SCRIPT_DIR"

python3 -m venv .venv

source "./.venv/bin/activate"

python -m pip install -r requirements.txt

if [[ ! -f "./src/database/web_player.sqlite" ]]; then
    cp "./src/database/web_player.empty.sqlite" "./src/database/web_player.sqlite"
fi

if [[ ! -f "./src/config.json" ]]; then
    cp "./src/config.empty.json" "./src/config.json"
fi