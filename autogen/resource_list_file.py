import os
import re


def add_resource_file(resource_num, path):
    object_path = path.replace('{', '<string:').replace('}', '>')
    sub_path = re.split(r"\/", object_path)
    collection_path = '/' + sub_path[1]
    for i in range(len(sub_path)-3):
        collection_path =  collection_path + '/' + sub_path[i+2]
    
    add_resource_collection = 'g.api.add_resource({0}CollectionAPI, \'{1}\')\n'.format(resource_num, collection_path)
    add_resource_instance = 'g.api.add_resource({0}API, \'{1}\')\n\n'.format(resource_num, object_path)

    try:
        with open("add_resource", "a") as file:
            file.write(add_resource_collection)
            file.write(add_resource_instance)

        return 'Resource added in the "add_resource.txt" file'
    except:
        return 'Something went wrong'

def add_service_resource_file(resource_num, path):
    object_path = path.replace('{', '<string:').replace('}', '>')
    sub_path = re.split(r"\/", object_path)
    collection_path = '/' + sub_path[1]
    for i in range(len(sub_path)-3):
        collection_path =  collection_path + '/' + sub_path[i+2]

    add_resource_instance = ''
    add_resource_collection = ''
    if 'string' not in sub_path[-1]:
        add_resource_instance = 'g.api.add_resource({0}API, \'{1}\')\n\n'.format(resource_num, object_path)
    else:
        add_resource_collection = 'g.api.add_resource({0}CollectionAPI, \'{1}\')\n'.format(resource_num, collection_path)
        add_resource_instance = 'g.api.add_resource({0}API, \'{1}\')\n\n'.format(resource_num, object_path)

    try:
        with open("add_service_resource", "a") as file:
            if add_resource_collection:
                file.write(add_resource_collection)
                file.write(add_resource_instance)
            else:
                file.write(add_resource_instance)

        return 'Service Resource added in the "add_resource.txt" file'
    except:
        return 'Something went wrong'