#!/bin/bash
#
#

# Save files and restore:
mkdir ./tempfiles
cp ../api_emulator/redfish/templates/collection.py ./tempfiles/collection.py
cp ../api_emulator/redfish/templates/Session.py ./tempfiles/Session.py
cp ../api_emulator/redfish/templates/Event.py ./tempfiles/Event.py
cp ../api_emulator/redfish/templates/EventDestination.py ./tempfiles/EventDestination.py
cp ../api_emulator/redfish/SessionService_api.py ./tempfiles/SessionService_api.py
cp ../api_emulator/redfish/Session_api.py ./tempfiles/Session_api.py
cp ../api_emulator/redfish/EventDestination_api.py ./tempfiles/EventDestination_api.py
cp ../api_emulator/redfish/EventServiceEvents_api.py ./tempfiles/EventServiceEvents_api.py

echo Cleanup Emulator files: remove template and API files:
rm ../api_emulator/redfish/templates/*.py
rm ../api_emulator/redfish/*_api.py

echo Copying updated API files
cp APIs/*_api.py ../api_emulator/redfish
cp Service_APIs/*_api.py ../api_emulator/redfish

echo Copying updated template files
cp Templates/*.py ../api_emulator/redfish/templates

# Restore saved files:
cp  ./tempfiles/collection.py ../api_emulator/redfish/templates/
cp  ./tempfiles/Session.py ../api_emulator/redfish/templates/
cp  ./tempfiles/Event.py ../api_emulator/redfish/templates/
cp  ./tempfiles/EventDestination.py ../api_emulator/redfish/templates/
cp  ./tempfiles/SessionService_api.py ../api_emulator/redfish/
cp  ./tempfiles/Session_api.py ../api_emulator/redfish/
cp  ./tempfiles/EventDestination_api.py ../api_emulator/redfish/
cp  ./tempfiles/EventServiceEvents_api.py ../api_emulator/redfish/

echo Remember to manually update the resource_manager file from the add_import and add_resource files in APIs and Service_APIs folders.

# Compare add_import entries with resource_manager.py imports
MISSING_IMPORTS=()
while IFS= read -r import_line; do
    # Escape special characters for grep
    GREP_SAFE=$(printf '%s\n' "$import_line" | sed 's/[][\.*^$(){}?+|/]/\\&/g')
    if ! grep -q "$GREP_SAFE" ../api_emulator/resource_manager.py; then
        MISSING_IMPORTS+=("$import_line")
    fi
done < ./APIs/add_import

if [ ${#MISSING_IMPORTS[@]} -ne 0 ]; then
    echo "The following import statements are missing from api_emulator/resource_manager.py:"
    for missing in "${MISSING_IMPORTS[@]}"; do
        echo "$missing"
    done
else
    echo "All import statements from autogen/APIs/add_import are present in resource_manager.py."
fi