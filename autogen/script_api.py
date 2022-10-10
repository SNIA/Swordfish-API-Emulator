import os, sys
import socket
import xmltodict, urllib, json

from generate_api import create_api_program, create_folder_under_current_directory
from generate_service_api import create_service_api_program
from resource_list_file import add_import_statement, add_resource_file, add_service_resource_file

def get_resource_paths(xml_content):
    """ Extracting Redfish URIs from given XML schema """
    try:
        # fetch data from XML schema and converted into JSON object
        xml_schema = xmltodict.parse(xml_content)
        json_data = json.dumps(xml_schema, indent=4)
        schema = json.loads(json_data)

        path_list = None
        schema_data = schema['edmx:Edmx']['edmx:DataServices']['Schema']
        if type(schema_data) == list:
            if 'EntityType' in schema_data[0]:
                if type(schema_data[0]['EntityType']) == dict:
                    for key, item in schema_data[0]['EntityType'].items():
                        if key == 'Annotation':
                            res = next((sub for sub in item if sub["@Term"] == "Redfish.Uris"), None)
                            if res != None:
                                path_list = res.get("Collection").get("String", None)
                            else:
                                path_list = None  
                else:
                    for key, item in schema_data[0]['EntityType'][0].items():
                        if key == 'Annotation':
                            res = next((sub for sub in item if sub["@Term"] == "Redfish.Uris"), None)
                            if res != None:
                                path_list = res.get("Collection").get("String", None)
                            else:
                                path_list = None
            else:
                path_list = None
        else:
            if schema_data.get('EntityType') :
                if type(schema_data['EntityType']) == dict:
                    for key, item in schema_data['EntityType'].items():
                        if key == 'Annotation':
                            res = next((sub for sub in item if sub["@Term"] == "Redfish.Uris"), None)
                            if res != None:
                                path_list = res.get("Collection").get("String", None)
                            else:
                                path_list = None    
                else:
                    for key, item in schema_data['EntityType'][0].items():
                        if key == 'Annotation':
                            res = next((sub for sub in item if sub["@Term"] == "Redfish.Uris"), None)
                            if res != None:
                                path_list = res.get("Collection").get("String", None)
                            else:
                                path_list = None
            else:
                path_list = None

        # get resource type from Namespace (Ex. Chassis, Port, NetworkAdapter, Manager, etc)
        if path_list != None:   
            if type(schema_data) == list:
                resource = schema['edmx:Edmx']['edmx:DataServices']['Schema'][0]['@Namespace']
            else:
                resource = schema['edmx:Edmx']['edmx:DataServices']['Schema'].get('@Namespace')
        else:
            resource = None
        return resource, path_list

    except urllib.error.HTTPError as e:
        return (e.code)
    except urllib.error.URLError as e:
        return ('URL_Error')
    except socket.timeout as e:
        return ('Connection timeout')

if __name__=='__main__':
    # directory_path = "C:/Users/rkumbhoj/Downloads/DSP8010_2022.1/csdl/"
    # directory_path = "C:/Users/rkumbhoj/Downloads/Swordfish_v1.2.4a_Schema/csdl-schema"

    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("check command line arguments")
        exit()
    else:
        directory_path = sys.argv[1]
    
    if not os.path.exists(directory_path):
        print("Directory does not exists")
        exit()

    resourceAPI_path = create_folder_under_current_directory("APIs")
    serviceAPI_path = create_folder_under_current_directory("Service_APIs")
 
    for file in os.listdir(directory_path):
        if 'Collection' not in file:
            print(file)
            xml_file = open(os.path.join(directory_path, file), 'r')
            xml_content= xml_file.read()
            resource, resource_paths = get_resource_paths(xml_content)
            num = 0

            if resource_paths == None:
                continue

            if(type(resource_paths) is str):
                if resource_paths == '/redfish/v1':
                    resource_paths = resource_paths + '/'
                head, tail= os.path.split(resource_paths)
                head = head.replace('/redfish/v1', '')
                resource_num = resource

                if '{' not in tail or 'SessionId' in tail or 'Registry' in tail or 'Service' in tail:
                    os.chdir(serviceAPI_path)
                    program_name = '{0}_api.py'.format(resource_num)
                    status = create_service_api_program(resource_paths, program_name, resource_num, head, tail)
                    print(status)

                    # creates add_resource lines of code for resource_manager.py
                    print(add_import_statement(resource_num))
                    print(add_service_resource_file(resource_num, resource_paths))
                else:
                    os.chdir(resourceAPI_path)
                    program_name = '{0}_api.py'.format(resource)
                    status = create_api_program(resource_paths, program_name, resource, resource_num, head, tail)
                    print(status)

                    # creates add_resource lines of code for resource_manager.py
                    print(add_import_statement(resource_num))
                    print(add_resource_file(resource_num, resource_paths))
            elif(type(resource_paths) is list):
                for path in resource_paths:
                    if path == '/redfish/v1':
                        path = path + '/'
                    head, tail= os.path.split(path)
                    head = head.replace('/redfish/v1', '')
                    # base program name is different for different paths
                    resource_num = resource + str(num)

                    if '{' not in tail or 'SessionId' in tail or 'Registry' in tail or 'Service' in tail:
                        os.chdir(serviceAPI_path)
                        program_name = '{0}_api.py'.format(resource_num)
                        num = num + 1
                        status = create_service_api_program(path, program_name, resource_num, head, tail)
                        print(status)

                        # creates add_resource lines of code for resource_manager.py
                        print(add_import_statement(resource_num))
                        print(add_service_resource_file(resource_num, path))
                    else:
                        os.chdir(resourceAPI_path)
                        program_name = '{0}_api.py'.format(resource_num)
                        num = num +1
                        status = create_api_program(path, program_name, resource, resource_num, head, tail)
                        print(status)

                        # creates add_resource lines of code for resource_manager.py
                        print(add_import_statement(resource_num))
                        print(add_resource_file(resource_num, path))
