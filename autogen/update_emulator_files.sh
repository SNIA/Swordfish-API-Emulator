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

rm -rf ./tempfiles
echo "Incorporating new import/resource statements into resource_manager.py..."

# Incorporate new import/resource statements from all relevant files into resource_manager.py
RESOURCE_MANAGER="$(dirname "$0")/../api_emulator/resource_manager.py"
FILES=(
    "$(dirname "$0")/APIs/add_import"
    "$(dirname "$0")/APIs/add_resource"
    "$(dirname "$0")/Service_APIs/add_import"
    "$(dirname "$0")/Service_APIs/add_service_resource"
)

for FILE in "${FILES[@]}"; do
    if [ -f "$FILE" ]; then
        echo "Processing $FILE for new statements..."
        while IFS= read -r line; do
            if [[ "$FILE" == *add_import ]] && [[ "$line" == from* ]] && ! grep -Fxq "$line" "$RESOURCE_MANAGER"; then
                awk -v newline="$line" 'NR==1{print; next} /^from api_emulator.redfish.AccelerationFunction0_api import \*/{print; print newline; next} {print}' "$RESOURCE_MANAGER" > "$RESOURCE_MANAGER.tmp" && mv "$RESOURCE_MANAGER.tmp" "$RESOURCE_MANAGER"
                echo "Added import: $line"
            elif ([[ "$FILE" == *add_resource ]] || [[ "$FILE" == *add_service_resource ]]) && [[ "$line" == g.api.add_resource* ]]; then
                # Extract endpoint class from the line
                endpoint=$(echo "$line" | awk -F'[,(]' '{print $2}' | xargs)
                # Check for existing registration of this endpoint class
                if ! grep -E "g\.api\.add_resource\s*\(\s*$endpoint\s*," "$RESOURCE_MANAGER"; then
                    # Insert inside __init__ method of ResourceManager
                    awk -v newline="$line" '
                        BEGIN {inserted=0}
                        /def __init__\(self, rest_base, spec, mode, auth, trays=None\):/ {print; in_init=1; next}
                        in_init && /^\s*$/ && !inserted {print "        "newline; inserted=1}
                        {print}
                    ' "$RESOURCE_MANAGER" > "$RESOURCE_MANAGER.tmp" && mv "$RESOURCE_MANAGER.tmp" "$RESOURCE_MANAGER"
                    echo "Added resource to __init__: $line"
                else
                    echo "Duplicate endpoint $endpoint, skipping."
                fi
            fi
        done < "$FILE"
        echo "Finished processing $FILE."
    else
        echo "No $FILE found, skipping."
    fi
done

echo "All import/resource incorporation into resource_manager.py complete."

echo "Comparing add_import entries with resource_manager.py imports..."
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