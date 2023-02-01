#!/bin/bash
set -x

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
echo "Script dir: $SCRIPT_DIR"

${SCRIPT_DIR}/../setup.sh -w ./emul -n

cp ${SCRIPT_DIR}/emulator-config-http.json ${SCRIPT_DIR}/../emul/emulator-config.json
cd ${SCRIPT_DIR}/../emul
./venv/bin/python emulator.py &
cd -

# Transform this into a loop waiting for the service to go up
sleep 20

python ${SCRIPT_DIR}/test.py