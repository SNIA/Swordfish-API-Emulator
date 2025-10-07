#!/bin/bash

#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RESOURCE_MANAGER="$SCRIPT_DIR/../api_emulator/resource_manager.py"
ADD_IMPORT="$SCRIPT_DIR/APIs/add_import"
ADD_RESOURCE="$SCRIPT_DIR/APIs/add_resource"

normalize() {
    sed 's/[[:space:]]//g'
}

mapfile -t EXISTING_IMPORTS < <(grep '^from ' "$RESOURCE_MANAGER" | normalize)
# Ensure the script is run from the correct directory
if [[ ! -f "$RESOURCE_MANAGER" ]]; then
    echo "Error: resource_manager.py not found in expected location: $RESOURCE_MANAGER"
    exit 1
fi
# Read and normalize all import lines from resource_manager.py into an array
mapfile -t EXISTING_IMPORTS < <(grep '^from ' ../api_emulator/resource_manager.py | normalize)

echo "Checking for missing import statements in api_emulator/resource_manager.py..."
MISSING_IMPORTS=()
while IFS= read -r import_line; do
    import_norm=$(echo "$import_line" | normalize)
    found=0
    for rm_norm in "${EXISTING_IMPORTS[@]}"; do
        if [[ "$rm_norm" == "$import_norm" ]]; then
            found=1
            break
        fi
    done
    if [[ $found -eq 0 ]]; then
        MISSING_IMPORTS+=("$import_line")
    fi
done < ./APIs/add_import

if [ ${#MISSING_IMPORTS[@]} -ne 0 ]; then
    echo "The following import statements are missing from api_emulator/resource_manager.py (from add_import):"
    for missing in "${MISSING_IMPORTS[@]}"; do
        echo "$missing"
    done
else
    echo "All import statements from autogen/APIs/add_import are present in resource_manager.py."
fi

echo "Checking for missing resource import statements in api_emulator/resource_manager.py..."
MISSING_RESOURCE_IMPORTS=()
while IFS= read -r import_line; do
    import_norm=$(echo "$import_line" | normalize)
    found=0
    for rm_norm in "${EXISTING_IMPORTS[@]}"; do
        if [[ "$rm_norm" == "$import_norm" ]]; then
            found=1
            break
        fi
    done
    if [[ $found -eq 0 ]]; then
        MISSING_RESOURCE_IMPORTS+=("$import_line")
    fi
done < ./APIs/add_resource

if [ ${#MISSING_RESOURCE_IMPORTS[@]} -ne 0 ]; then
    echo "The following import statements are missing from api_emulator/resource_manager.py (from add_resource):"
    for missing in "${MISSING_RESOURCE_IMPORTS[@]}"; do
        echo "$missing"
    done
else
    echo "All import statements from autogen/APIs/add_resource are present in resource_manager.py."
fi