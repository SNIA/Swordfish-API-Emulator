import os
import socket
import sys
import xmltodict, urllib, json
from generate_template import create_folder_under_current_directory, write_program

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
                latest_version = schema['edmx:Edmx']['edmx:DataServices']['Schema'][-1]['@Namespace']
            else:
                resource = schema['edmx:Edmx']['edmx:DataServices']['Schema'].get('@Namespace')
                latest_version = schema['edmx:Edmx']['edmx:DataServices']['Schema'].get('@Namespace')
        else:
            resource = None
            latest_version = None
        return resource, latest_version, path_list

    except urllib.error.HTTPError as e:
        return (e.code)
    except urllib.error.URLError as e:
        return ('URL_Error')
    except socket.timeout as e:
        return ('Connection timeout')

if __name__=='__main__':
    # xml_directory_path = "C:/Users/rkumbhoj/Downloads/DSP8010_2022.1/csdl/"
    # xml_directory_path = "C:/Users/rkumbhoj/Downloads/Swordfish_v1.2.4a_Schema/csdl-schema"
    # json_directory_path = "C:/Users/rkumbhoj/Downloads/DSP8010_2022.1/json-schema"
    # json_directory_path = "C:/Users/rkumbhoj/Downloads/Swordfish_v1.2.4a_Schema/json-schema"

    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("check command line arguments")
        exit()
    else:
        xml_directory_path = sys.argv[1]
        json_directory_path = sys.argv[2]
    
    if not os.path.exists(xml_directory_path):
        print("XML directory does not exists")
        exit()
    
    if not os.path.exists(json_directory_path):
        print("JSON directory does not exists")
        exit()
        
    new_path = create_folder_under_current_directory("Templates")
    os.chdir(new_path)

    for file in os.listdir(xml_directory_path):
        if 'Collection' not in file:
            print(file)
            xml_file = open(os.path.join(xml_directory_path, file), 'r')
            xml_content= xml_file.read()
            resource, latest_version, resource_paths = get_resource_paths(xml_content)
            num = 0

            if resource_paths == None:
                continue

            json_file_name = latest_version + '.json'
            json_file = open(os.path.join(json_directory_path, json_file_name), 'r')
            json_content= json.load(json_file)

            if(type(resource_paths) is str):
                if resource_paths == '/redfish/v1':
                    resource_paths = resource_paths + '/'
                head, tail= os.path.split(resource_paths)
                head = head.replace('/redfish/v1', '')
                resource_num = resource

                if '{' not in tail or 'SessionId' in tail or 'Registry' in tail or 'Service' in tail:
                    print("Template not created for resource - "+resource)
                    continue
                else:
                    program_name = '{0}.py'.format(resource_num)
                     # Open the program file and write the program.
                    with open(program_name, 'w') as outfile:
                        write_program(outfile, resource_num, resource_paths, json_content)
                        print ('Created program {0}'.format(program_name))

            elif(type(resource_paths) is list):
                for path in resource_paths:
                    if path == '/redfish/v1':
                        path = path + '/'
                    head, tail= os.path.split(path)
                    head = head.replace('/redfish/v1', '')
                    # base program name is different for different paths
                    resource_num = resource + str(num)
                 
                    if '{' not in tail or 'SessionId' in tail or 'Registry' in tail or 'Service' in tail:
                        print("Template not created for resource - "+resource)
                        break
                    else:
                        program_name = '{0}.py'.format(resource_num)
                        num = num + 1
                        # Open the program file and write the program.
                        with open(program_name, 'w') as outfile:
                            write_program(outfile, resource_num, path, json_content)
                            print ('Created program {0}'.format(program_name))