import os
import socket
import urllib, xmltodict, json

from generate_api import create_folder_under_current_directory, safe_input
from resource_list_file import add_import_statement, add_service_resource_file
from service_api_writer import write_service_program_header, write_service_singleton_api, write_servicetype_collection_api, write_servicetype_singleton_api

xml_schema_examples='''
https://redfish.dmtf.org/schemas/v1/SessionService_v1.xml
https://redfish.dmtf.org/schemas/v1/Session_v1.xml
https://redfish.dmtf.org/schemas/v1/MessageRegistryFile_v1.xml
'''

def write_service_program(resource_path, outfile, resource, collection_path, instance):
    """ Write the python program file """
    # for paths like - /redfish/v1/SessionService or /redfish/v1/AccountService
    if (collection_path == ''):
        write_service_program_header(resource_path, outfile, resource)
        write_service_singleton_api (outfile, resource, collection_path, instance)
    # for paths like - /redfish/v1/JobService/Log or /redfish/v1/TelemetryService/LogService or /redfish/v1/Managers/{ManagerId}/RemoteAccountService
    elif ('{' not in instance):
        write_service_program_header(resource_path, outfile, resource)
        write_service_singleton_api (outfile, resource, collection_path, instance)
    # for other paths like - /redfish/v1/SessionService/Sessions/{SessionId} or /redfish/v1/Managers/{ManagerId}/LogServices/{LogServiceId}
    else:
        write_service_program_header(resource_path, outfile, resource)
        write_servicetype_collection_api(outfile, resource,  collection_path)
        write_servicetype_singleton_api (outfile, resource, collection_path, instance)

def get_resource_paths(url):
    """ Extracting Redfish URIs from given XML schema """
    try:
        # fetch data from XML schema URL and converted into JSON object
        response = urllib.request.urlopen(url).read()
        xml_schema = xmltodict.parse(response)
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

def create_service_api_program(resource_path, program_name, resource, collection_path, instance):
    """ Call to write an API program file """
    with open(program_name, 'w') as outfile:
        write_service_program(resource_path, outfile, resource, collection_path, instance)
        return 'Created program {0}'.format(program_name)

if __name__=='__main__':
    schema_url = safe_input("Enter the XML schema URL for your resource type: ")
    resource, resource_paths = get_resource_paths(schema_url)
    num = 0

    new_path = create_folder_under_current_directory("Service_APIs")
    print(new_path)
    # change os current path to newly created directory path
    os.chdir(new_path)

    # if Redfish URIs has only one path
    if(type(resource_paths) is str):
        if resource_paths == '/redfish/v1':
            resource_paths = resource_paths + '/'
        head, tail= os.path.split(resource_paths)
        head = head.replace('/redfish/v1', '')
        resource_num = resource
        program_name = '{0}_api.py'.format(resource_num)
        status = create_service_api_program(resource_paths, program_name, resource_num, head, tail)
        print(status)

        # creates add_resource lines of code for resource_manager.py
        print(add_import_statement(resource_num))
        print(add_service_resource_file(resource_num, resource_paths))
    # if Redfish URIs has list of paths
    elif(type(resource_paths) is list):
        for path in resource_paths:
            if path == '/redfish/v1':
                path = path + '/'
            head, tail= os.path.split(path)
            head = head.replace('/redfish/v1', '')
            # base program name is different for different paths
            resource_num = resource + str(num)
            program_name = '{0}_api.py'.format(resource_num)
            num = num + 1
            status = create_service_api_program(path, program_name, resource_num, head, tail)
            print(status)

            # creates add_resource lines of code for resource_manager.py
            print(add_import_statement(resource_num))
            print(add_service_resource_file(resource_num, path))