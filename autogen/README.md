# autogen
Resource implementation tool for Swordfish Emulator.

To auto generate resource implementation for all Redfish/Swordfish resources, run script_api.py program.

This program will generate API implementation code for resources and services.

Run the following command:
``
python script_api.py [schema_path]
``

[schema_path] should be the path of XML schema directory.

To auto generate template code for all Redfish/Swordfish resources, run script_template.py program.

Run the following command:
``
python script_template.py [xml_schema_path] [json_schema_path]
``

[xml_schema_path] should be the path of XML schema directory.

[json_schema_path] should be the path of JSON schema directory.

To generate resource implementation for a specific resource use following programs:
- generate_api.py 
    - This program will create API implementation code for the resource in 'APIs' folder. 
    - Input to this program would be XML schema URL for the resource.
- generate_service_api.py
    - This program will create API implementation code for the service and/or subservice in 'Service APIs' folder. 
    - Input to this program would be XML schema URL for the service and/or subservice.

To generate template file for each individual resource, run following program -
- generate_template.py
    - This program will generate template code for the resource in 'Templates' folder.
    - Input to this program would be JSON and XML schema URL for the resource.

This tool also generates add_resource/add_service_resource and add_import files.
- add_resource/add_service_resource: contains "g.api.add_resource" statements for all implemented resource.
- add_import: contains import statements for generted classes
You can copy the contains from these files to the emulator's resource_manager.py program.
