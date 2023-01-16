#!/bin/bash
# Copyright (c) 2018-2023, The Storage Networking Industry Association.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# Neither the name of The Storage Networking Industry Association (SNIA) nor
# the names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
#  THE POSSIBILITY OF SUCH DAMAGE.

BASE_DIR=$(pwd)
WORK_DIR=../Swordfish

API_PORT=5000
SETUP_ONLY=

COMMON_NAME="$1"
EXTFILE=certificate_config.cnf

function print_help {
    cat <<EOF

Helper to set up a Swordfish emulator. This will take care of getting the
necessary source files ready and start a local instance of the emulator.

USAGE:

    $(basename $0) [--port PORT] [--workspace DIR] [--no-start]

Options:

    -p | --port PORT     -- Port to run the emulator on. Default is $API_PORT.

    -w | --workspace DIR -- Directory to set up the emulator. Defaults to
                            '$WORK_DIR'.

    -n | --no-start      -- Prepare the emulator but do not start it.

EOF
}

# Extract command line args
while [ "$1" != "" ]; do
    case $1 in
        -p | --port )
            shift
            API_PORT=$1
            ;;
        -w | --workspace )
            shift
            WORK_DIR=$1
            ;;
        -n | --no-start)
            SETUP_ONLY="true"
            ;;
        *)
            print_help
            exit 1
    esac
    shift
done

# Do some system sanity checks first
if ! [ -x "$(command -v python3)" ]; then
    echo "Error: python3 is required to run the emulator and executable not" \
         "found"
    echo ""
    echo "See https://www.python.org/downloads/ for installation instructions."
    echo ""
    exit 1
fi

if ! [ -x "$(command -v virtualenv)" ]; then
    echo "Error: virtualenv is required."
    echo ""
    echo "See https://virtualenv.pypa.io/en/stable/installation/ for" \
         "installation instructions."
    echo ""
    exit 1
fi

if ! [ -x "$(command -v git)" ]; then
    echo "Error: git is required."
    echo ""
    echo "See https://git-scm.com/book/en/v2/Getting-Started-Installing-Git" \
         "for installation instructions."
    echo ""
    exit 1
fi

echo "Creating workspace: '$WORK_DIR'..."
rm -fr $WORK_DIR
mkdir $WORK_DIR

# Get the Redfish base
echo "Getting Redfish emulator base files..."
git clone --depth 1 https://github.com/DMTF/Redfish-Interface-Emulator \
    $WORK_DIR

# Set up our virtual environment
echo "Setting up emulator Python virtualenv and requirements..."
# cd $WORK_DIR
virtualenv --python=python3 "$WORK_DIR"/venv
"$WORK_DIR"/venv/bin/pip install -q -r "$BASE_DIR"/requirements.txt

# Remove Redfish static / starting mockups
rm -r "$WORK_DIR"/api_emulator/redfish/static

# Remove Redfish templates, and .py files.
rm -rf "$WORK_DIR"/api_emulator/redfish/templates
rm -rf "$WORK_DIR"/api_emulator/redfish/*.py

# Copy over the Swordfish bits
echo "Applying Swordfish additions..."
cp -r -f "$BASE_DIR"/api_emulator "$WORK_DIR"/
cp -r -f "$BASE_DIR"/Resources "$WORK_DIR"/
cp -r -f "$BASE_DIR"/emulator-config.json "$WORK_DIR"/
cp -r -f "$BASE_DIR"/g.py "$WORK_DIR"/
cp -r -f "$BASE_DIR"/emulator.py "$WORK_DIR"/
cp -r -f "$BASE_DIR"/certificate_config.cnf "$WORK_DIR"/
cp -r -f "$BASE_DIR"/v3.ext "$WORK_DIR"/

# generating server key
echo "Generating private key"
openssl genrsa -out "$WORK_DIR"/server.key 2048

# generating public key
echo "Generating public key"
openssl rsa -in "$WORK_DIR"/server.key -pubout -out "$WORK_DIR"/server_public.key

# ## Update Common Name in External File
# /bin/echo "commonName              = $COMMON_NAME" >> $EXTFILE

# Generating Certificate Signing Request using config file
echo "Generating Certificate Signing Request"
openssl req -new -key "$WORK_DIR"/server.key -out "$WORK_DIR"/server.csr -config "$WORK_DIR"/$EXTFILE

echo "Generating self signed certificate"
openssl x509 -in "$WORK_DIR"/server.csr -out "$WORK_DIR"/server.crt -req -signkey "$WORK_DIR"/server.key -days 365 -extfile "$WORK_DIR"/v3.ext

if [ "$SETUP_ONLY" == "true" ]; then
    echo ""
    echo "Emulator files have been prepared. Run the following to start the" \
         "emulator:"
    echo ""
    echo "   cd $WORK_DIR"
    echo "   ./venv/bin/python emulator.py"
    echo ""
    exit 0
fi

# Start up the emulator
cat <<EOF

---------------------------------------------------------------------
Starting Swordfish emulator. Access the local instance using the URL:

   http://localhost:$API_PORT

$(tput bold)Press Ctrl-C when done.$(tput sgr0)
---------------------------------------------------------------------
EOF

cd "$WORK_DIR"
./venv/bin/python emulator.py -port $API_PORT

echo ""
echo "Emulator can be rerun from '$WORK_DIR' by running the command:"
echo ""
echo "venv/bin/python emulator.py"
echo ""
