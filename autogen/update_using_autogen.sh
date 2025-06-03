#!/bin/bash
# 
# This script downloads the latest Redfish and Swordfish schema, 
# and generates updated API and Template files. 
# Refer to the update_emulator_files script to see what files 
# are no longer used from their generated form.
#
#

set -e

# Download and extract schema bundles
TMPDIR=$(mktemp -d)
SCHEMA_PATH="./metadata"
JSON_SCHEMA_PATH="./json_schema"

echo "Downloading Swordfish profile bundle..."
curl -L -o "$TMPDIR/swordfish-schema-bundle.zip" "https://snia.org/swordfish-schema-bundle/release/latest"

echo "Downloading Redfish CSDL/JSON schema bundle..."
curl -L -o "$TMPDIR/DSP8010.zip" "https://www.dmtf.org/sites/default/files/standards/documents/DSP8010.zip"

echo "Extracting Swordfish bundle..."
unzip -o "$TMPDIR/swordfish-schema-bundle.zip" -d "$TMPDIR/swordfish"

echo "Extracting Redfish bundle..."
unzip -o "$TMPDIR/DSP8010.zip" -d "$TMPDIR/redfish"

# Create target directories if they don't exist
mkdir -p "$SCHEMA_PATH"
mkdir -p "$JSON_SCHEMA_PATH"

echo "Copying CSDL/XML/metadata files to $SCHEMA_PATH..."
# Copy all files from found csdl and csdl-schema directories into $SCHEMA_PATH, preserving structure
find "$TMPDIR/redfish" -type d -iname "csdl" | while read -r dir; do
    rsync -a "$dir/" "$SCHEMA_PATH/"
done
find "$TMPDIR/swordfish" -type d -iname "csdl-schema" | while read -r dir; do
    rsync -a "$dir/" "$SCHEMA_PATH/"
done

echo "Copying JSON schema files to $JSON_SCHEMA_PATH..."
find "$TMPDIR/swordfish" "$TMPDIR/redfish" -type d -iname "json-schema" | while read -r dir; do
    rsync -a "$dir/" "$JSON_SCHEMA_PATH/"
done

# Clean up temp files
rm -rf "$TMPDIR"

# Set these variables to your actual schema locations
XML_SCHEMA_PATH="$SCHEMA_PATH"
RESOURCE_XML_URL="http://example.com/resource.xml"
SERVICE_XML_URL="http://example.com/service.xml"
RESOURCE_JSON_URL="http://example.com/resource.json"

echo "Generating all resource API implementations..."
python3 script_api.py "$SCHEMA_PATH"

echo "Generating all resource template code..."
python3 script_template.py "$XML_SCHEMA_PATH" "$JSON_SCHEMA_PATH"

echo "autogen actions to update templates and API files completed."
echo "Check add_resource/add_service_resource and add_import files for generated statements."