import os
import sys
import requests

from generate_api import get_resource_paths
from template_writer import write_program_end, write_program_header, write_template

json_schema_examples='''
https://redfish.dmtf.org/schemas/v1/NetworkAdapter.v1_9_0.json
https://redfish.dmtf.org/schemas/v1/Port.v1_6_1.json
https://redfish.dmtf.org/schemas/v1/Chassis.v1_20_0.json
'''

xml_schema_examples='''
https://redfish.dmtf.org/schemas/v1/Port_v1.xml
https://redfish.dmtf.org/schemas/v1/Chassis_v1.xml
https://redfish.dmtf.org/schemas/v1/Drive_v1.xml
'''

def write_program(outfile, base_template_name, resource_path, json_schema):
    """ Write the python program file """
    write_program_header(outfile, base_template_name)
    write_template(outfile, resource_path, json_schema)
    write_program_end(outfile, base_template_name, resource_path)

def create_folder_under_current_directory(folder_name):
    """ Create a folder for API program file under current directory """
    current_path = os.getcwd()
    global orig_path
    orig_path = current_path
    new_path = os.path.join(current_path, folder_name)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return new_path
    
def safe_input(prompt):
    inp = input(prompt)
    try:
        return eval(inp)
    except:
        return inp

def main():
    ''' Excecution starts here. It asks user to provide json and xml URL for the resource'''
    # Set the default return value to indicate success.
    status = 0

    try:
        json_schema_url = safe_input("Enter the JSON schema URL for the resource: ")
        xml_schema_url = safe_input("Enter the XML schema URL for the resource: ")

        resource, resource_paths = get_resource_paths(xml_schema_url)
        num = 0

        new_path = create_folder_under_current_directory("Templates")
        print(new_path)
        # change os current path to newly created directory path
        os.chdir(new_path)

        json_schema = requests.get(json_schema_url).json()

        # if Redfish URIs has only one path
        if(type(resource_paths) is str):
            resource_num = resource
            program_name = '{0}.py'.format(resource_num)
             # Open the program file and write the program.
            with open(program_name, 'w') as outfile:
                write_program(outfile, resource_num, resource_paths, json_schema)
                print ('Created program {0}'.format(program_name))
        # if Redfish URIs has list of paths
        elif(type(resource_paths) is list):
            for path in resource_paths:
                resource_num = resource+str(num)
                program_name = '{0}.py'.format(resource_num)
                num = num +1
                 # Open the program file and write the program.
                with open(program_name, 'w') as outfile:
                    write_program(outfile, resource_num, path, json_schema)
                    print ('Created program {0}'.format(program_name))

    except EnvironmentError as environment_error:
        print (environment_error)
        status = -1
    except ValueError as value_error:
        print (value_error)
        status = -1
    return status

    
if __name__=='__main__':
    sys.exit(main())