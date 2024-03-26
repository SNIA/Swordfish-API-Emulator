#!/bin/bash
#
#
echo Cleanup Emulator files: remove template and API files:
rm ../api_emulator/redfish/templates/*.py
rm ../api_emulator/redfish/*_api.py

echo Copying updated API files
cp APIs/*_api.py ../api_emulator/redfish
cp Service_APIs/*_api.py ../api_emulator/redfish

echo Copying updated template files
cp Templates/*.py ../api_emulator/redfish/templates

echo Restore files in emulator that we don't want from autogen created files...
git restore ../api_emulator/redfish/templates/collection.py
git restore ../api_emulator/redfish/templates/Session.py
git restore ../api_emulator/redfish/SessionService_api.py
git restore ../api_emulator/redfish/Session_api.py

echo Remember to manually update the resource_manager file from the add_import and add_resource files in APIs and Service_APIs folders.

