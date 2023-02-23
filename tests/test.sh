#!/bin/bash
TIMEOUT=30

wait_ofmf () {
    NOW=0
    ELAPSED=0
    START=$(date +"%s")
    while [ $ELAPSED -lt $TIMEOUT ]
    do
        curl http://localhost:5000/redfish/v1 > /dev/null 2>&1
        if [ $? -eq 0 ]
        then
            return 0
        fi
        # No need to go crazy here, let's sleep for a while
        sleep 1
        NOW=$(date +"%s")
        ELAPSED=$((${NOW} - ${START}))
    done

    return 1
}

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
echo "Script dir: $SCRIPT_DIR"

${SCRIPT_DIR}/../setup.sh -w ./emul -n

cp ${SCRIPT_DIR}/emulator-config-http.json ${SCRIPT_DIR}/../emul/emulator-config.json
cd ${SCRIPT_DIR}/../emul
./venv/bin/python emulator.py &
cd -

# wait for the OFMF service to be up of fail after TIMEOUT seconds
wait_ofmf
if [ $? -eq 1 ]
then
    echo "Timing out, the OFMF failed to start"
    exit 1
fi

python ${SCRIPT_DIR}/test.py