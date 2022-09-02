# autogen
Resource implementation tool for Swordfish Emulator.

This tool contains 3 main programs -
- generate_api.py 
    - This program will create API implementation code for the resource in 'APIs' folder. 
    - Input to this program would be XML schema URL for the resource.
- generate_service_api.py
    - This program will create API implementation code for the service and/or subservice in 'Service APIs' folder. 
    - Input to this program would be XML schema URL for the service and/or subservice.
- generate_template.py
    - This program will generate template code for the resource in 'Templates' folder.
    - Input to this program would be JSON and XML schema URL for the resource.

This tool will also generate add_resource/add_service_resource files which conatin code to attach created APIs for dynamic resources.
You can copy the add_resource() calls from these file to the emulator's resource_manager.py program.