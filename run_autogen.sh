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

AUTOGEN_DIR="$BASE_DIR"/autogen

function print_help {
            cat <<EOF

Helper to re-run the autogen tools and update the Redfish/Swordfish schema and templates.

USAGE:

    $(basename $0) [--xml-schema XML_DIRECTORY] [--json-schema JSON_DIRECTORY] [--create-templates] [--create-api-files]

Options:

    -x | --xml-schema XML_DIRECTORY    -- Directory with the XML Schema files. Default is $XML_Schema.

    -j | --json-schema JSON_DIRECTORY  -- Directory with the Json Schema files. Default is $JSON_Schema.

    -t | --create-templates            -- Create templates from the schema files.

    -a | --create-api-files            -- Create API files from the schema files.

EOF
}

# Extract command line args
while [ "$1" != "" ]; do
    case $1 in
        -x | --xml-schema )
            shift
            XML_Schema=$1
            ;;
        -j | --json-schema )
            shift
            JSON_Schema=$1
            ;;
        -t | --create-templates )
            CREATE_TEMPLATES="true"
            ;;
        -a | --create-api-files )
            CREATE_API_FILES="true"
            ;;
        *)
            print_help
            exit 1
    esac
    shift
done

# Do some system sanity checks first
if ! [ -x "$(command -v python3)" ]; then
    echo "Error: python3 is required to run autogen and executable not" \
         "found"
    echo ""
    echo "See https://www.python.org/downloads/ for installation instructions."
    echo ""
    exit 1
fi

if [ "$CREATE_TEMPLATES" == "true" ]; then
    cd $AUTOGEN_DIR
    python3 script_template.py $XML_Schema $JSON_Schema
fi

if [ "$CREATE_API_FILES" == "true" ]; then
    cd $AUTOGEN_DIR
    python3 script_api.py $XML_Schema
fi
