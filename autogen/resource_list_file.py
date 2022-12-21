import os
import re


def add_import_statement(resource_num):
    add_import = 'from api_emulator.redfish.{0}_api import *\n'.format(resource_num)
    try:
        # with open("add_import", "a") as file:
        #     file.write(add_import)
        with open("add_import", "a+") as file:
            file.seek(0)
            for line in file:
                if add_import in line:
                    break
            else:
                file.write(add_import)
                return 'Import statement added in "add_import" file'
    except:
        return 'Something went wrong'

def add_resource_file(resource_num, path):
    object_path = path.replace('{', '<string:').replace('}', '>')
    sub_path = re.split(r"\/", object_path)
    collection_path = '/' + sub_path[1]
    for i in range(len(sub_path)-3):
        collection_path =  collection_path + '/' + sub_path[i+2]
    
    add_resource_collection = "g.api.add_resource({0}CollectionAPI, \'{1}\', resource_class_kwargs={{'auth': auth}})\n".format(resource_num, collection_path)
    add_resource_instance = "g.api.add_resource({0}API, \'{1}\', resource_class_kwargs={{'auth': auth}})\n\n".format(resource_num, object_path)

    try:
        # with open("add_resource", "a") as file:
        #     file.write(add_resource_collection)
        #     file.write(add_resource_instance)

        with open("add_resource", "a+") as file:
            file.seek(0)
            for line in file:
                if add_resource_collection in line:
                    break
            else:
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

    if 'string' not in sub_path[-1]:
        add_resource_instance = "g.api.add_resource({0}API, \'{1}\', resource_class_kwargs={{'auth': auth}})\n".format(resource_num, object_path)
        add_resource_collection = ""
    else:
        add_resource_collection = "g.api.add_resource({0}CollectionAPI, \'{1}\', resource_class_kwargs={{'auth': auth}})\n".format(resource_num, collection_path)
        add_resource_instance = "g.api.add_resource({0}API, \'{1}\', resource_class_kwargs={{'auth': auth}})\n".format(resource_num, object_path)

    try:
        # with open("add_service_resource", "a") as file:
        #     if add_resource_collection:
        #         file.write(add_resource_collection)
        #         file.write(add_resource_instance)
        #     else:
        #         file.write(add_resource_instance)

        # return 'Service Resource added in the "add_resource.txt" file'
        with open("add_service_resource", "a+") as file:
            file.seek(0)
            for line in file:
                # if add_resource_instance in line or add_resource_collection in line:
                if add_resource_instance != line:
                    continue
                else:
                    break
            else:
                if add_resource_collection != "":
                    file.write(add_resource_collection)
                    file.write(add_resource_instance)
                    file.write("\n")
                else:
                    file.write(add_resource_instance)
                    file.write("\n")
                return 'Resource added in the "add_resource.txt" file'
    except:
        # return 'Something went wrong'
        raise