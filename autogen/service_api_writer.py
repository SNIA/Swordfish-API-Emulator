import os
import re
from api_writer_utils import get_function_parameters, get_path_parameters


def write_service_program_header(resource_path, outfile, resource):
    """ Writes a program header """
    outfile.write('#\n')
    outfile.write('# Copyright (c) 2017-2021, The Storage Networking Industry Association.\n')
    outfile.write('#\n')
    outfile.write('# Redistribution and use in source and binary forms, with or without\n')
    outfile.write('# modification, are permitted provided that the following conditions are met:\n')
    outfile.write('#\n')
    outfile.write('# Redistributions of source code must retain the above copyright notice,\n')
    outfile.write('# this list of conditions and the following disclaimer.\n')
    outfile.write('#\n')
    outfile.write('# Redistributions in binary form must reproduce the above copyright notice,\n')
    outfile.write('# this list of conditions and the following disclaimer in the documentation\n')
    outfile.write('# and/or other materials provided with the distribution.\n')
    outfile.write('#\n')
    outfile.write('# Neither the name of The Storage Networking Industry Association (SNIA) nor\n')
    outfile.write('# the names of its contributors may be used to endorse or promote products\n')
    outfile.write('# derived from this software without specific prior written permission.\n')
    outfile.write('#\n')
    outfile.write('#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"\n')
    outfile.write('#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\n')
    outfile.write('#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE\n')
    outfile.write('#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE\n')
    outfile.write('#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR\n')
    outfile.write('#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF\n')
    outfile.write('#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS\n')
    outfile.write('#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN\n')
    outfile.write('#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)\n')
    outfile.write('#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF\n')
    outfile.write('#  THE POSSIBILITY OF SUCH DAMAGE.\n')
    outfile.write('\n')
    outfile.write("# Resource implementation for - {0}\n".format(resource_path))
    outfile.write('# Program name - {0}_api.py\n'.format(resource))
    outfile.write('\n')
    outfile.write('import g\n')
    outfile.write('import json, os\n')
    outfile.write('import traceback\n')
    outfile.write('import logging\n')
    outfile.write('\n')
    outfile.write('from flask import Flask, request\n')
    outfile.write('from flask_restful import Resource\n')
    outfile.write('from .constants import *\n')
    outfile.write('from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection\n')
    # outfile.write('from .templates.{0} import get_{0}_instance\n'.format(resource))
    outfile.write("\n")
    outfile.write("config = {}\n\n")
    outfile.write("INTERNAL_ERROR = 500\n\n")

    head, tail = os.path.split(resource_path)
    if('{' not in tail):
        outfile.write("# {0} does not have a Collection API\n\n".format(resource))
        outfile.write("\n")
    return

def write_service_singleton_api(outfile, resource, collection_path, instance):
    ''' Write the singleton resource API function '''
    outfile.write("# {0} API\n".format(resource))
    argument_string = "class {0}API(Resource):\n".format(resource)
    outfile.write(argument_string)
    outfile.write("\tdef __init__(self, **kwargs):\n")
    outfile.write("\t\tlogging.info('{0} init called')\n".format(resource))
    outfile.write("\t\tself.root = PATHS['Root']\n")
    outfile.write("\t\tself.auth = kwargs['auth']\n")
    outfile.write("\n")
    
    # Write GET method
    outfile.write("\t# HTTP GET\n")
    if instance == '':
        outfile.write("\tdef get(self):\n")
        outfile.write("\t\tlogging.info('{0} get called')\n".format(resource))
        if resource == 'ServiceRoot0' or resource == 'ServiceRoot1':
            outfile.write("\t\tpath = os.path.join(self.root, 'index.json')\n")
            outfile.write("\t\treturn get_json_data (path)\n")
        else:
            outfile.write("\t\tmsg, code = check_authentication(self.auth)\n\n")
            outfile.write("\t\tif code == 200:\n")
            outfile.write("\t\t\tpath = os.path.join(self.root, 'index.json')\n")
            outfile.write("\t\t\treturn get_json_data (path)\n")
    elif collection_path == '':
        outfile.write("\tdef get(self):\n")
        outfile.write("\t\tlogging.info('{0} get called')\n".format(resource))
        if resource == 'ServiceRoot0' or resource == 'ServiceRoot1':
            outfile.write("\t\tpath = os.path.join(self.root, '{0}', 'index.json')\n".format(instance))
            outfile.write("\t\treturn get_json_data (path)\n")
        else:
            outfile.write("\t\tmsg, code = check_authentication(self.auth)\n\n")
            outfile.write("\t\tif code == 200:\n")
            outfile.write("\t\t\tpath = os.path.join(self.root, 'index.json')\n")
            outfile.write("\t\t\treturn get_json_data (path)\n")
    else:
        original_path = collection_path[1:] + '/' + instance
        # print(original_path)
        arg_str = get_function_parameters(original_path)
        # print(arg_str)
        if arg_str == '':
            outfile.write("\tdef get(self):\n")
            outfile.write("\t\tlogging.info('{0} get called')\n".format(resource))
            if resource == 'ServiceRoot0' or resource == 'ServiceRoot1':
                outfile.write("\t\tpath = os.path.join(self.root, '{0}', 'index.json')\n".format(original_path))
                outfile.write("\t\treturn get_json_data (path)\n")
            else:
                outfile.write("\t\tmsg, code = check_authentication(self.auth)\n\n")
                outfile.write("\t\tif code == 200:\n")
                outfile.write("\t\t\tpath = os.path.join(self.root, '{0}', 'index.json')\n".format(original_path))
                outfile.write("\t\t\treturn get_json_data (path)\n")
        else:
            outfile.write("\tdef get(self, {0}):\n".format(arg_str))
            outfile.write("\t\tlogging.info('{0} get called')\n".format(resource))
            if resource == 'ServiceRoot0' or resource == 'ServiceRoot1':
                new_collection_path = get_path_parameters(original_path)
                outfile.write("\t\tpath = create_path(self.root, '{0}', 'index.json').format({1})\n".format(new_collection_path, arg_str))
                outfile.write("\t\treturn get_json_data (path)\n")
            else:
                outfile.write("\t\tmsg, code = check_authentication(self.auth)\n\n")
                outfile.write("\t\tif code == 200:\n")
                new_collection_path = get_path_parameters(original_path)
                outfile.write("\t\t\tpath = create_path(self.root, '{0}', 'index.json').format({1})\n".format(new_collection_path, arg_str))
                outfile.write("\t\t\treturn get_json_data (path)\n")
    if resource == 'ServiceRoot0' or resource == 'ServiceRoot1':
        pass
    else:
        outfile.write("\t\telse:\n")
        outfile.write("\t\t\treturn msg, code\n")
    outfile.write("\n")

    # Write POST method
    outfile.write("\t# HTTP POST\n")
    if collection_path != '' and arg_str != '':
        outfile.write("\tdef post(self, {0}):\n".format(arg_str))
    else:
        outfile.write("\tdef post(self):\n")
    outfile.write("\t\tlogging.info('{0} post called')\n".format(resource))
    outfile.write("\t\treturn 'POST is not a supported command for {0}API', 405\n".format(resource))
    outfile.write("\n")

    # Write PUT method
    outfile.write("\t# HTTP PUT\n")
    if collection_path != '' and arg_str != '':
        outfile.write("\tdef put(self, {0}):\n".format(arg_str))
    else:
        outfile.write("\tdef put(self):\n")
    outfile.write("\t\tlogging.info('{0} put called')\n".format(resource))
    outfile.write("\t\treturn 'PUT is not a supported command for {0}API', 405\n".format(resource))
    outfile.write("\n")

    # Write PATCH method
    outfile.write("\t# HTTP PATCH\n")
    if collection_path != '' and arg_str != '':
        outfile.write("\tdef patch(self, {0}):\n".format(arg_str))
    else:
        outfile.write("\tdef patch(self):\n")
    outfile.write("\t\tlogging.info('{0} patch called')\n".format(resource))
    outfile.write("\t\treturn 'PATCH is not a supported command for {0}API', 405\n".format(resource))
    outfile.write('\n')

    # Write DELETE method
    outfile.write("\t# HTTP DELETE\n")
    if collection_path != '' and arg_str != '':
        outfile.write("\tdef delete(self, {0}):\n".format(arg_str))
    else:
        outfile.write("\tdef delete(self):\n")
    outfile.write("\t\tlogging.info('{0} delete called')\n".format(resource))
    outfile.write("\t\treturn 'DELETE is not a supported command for {0}API', 405\n".format(resource))
    outfile.write('\n\n')
    return

def write_servicetype_collection_api(outfile, resource, collection_path):
    ''' Write the collection servicetype API function '''
    outfile.write("# {0} Collection API\n".format(resource))
    argument_string = "class {0}CollectionAPI(Resource):\n".format(resource)
    outfile.write(argument_string)

    # Write init method
    outfile.write("\tdef __init__(self, **kwargs):\n")
    
    outfile.write("\t\tlogging.info('{0} Collection init called')\n".format(resource))
    outfile.write("\t\tself.root = PATHS['Root']\n")
    outfile.write("\t\tself.auth = kwargs['auth']\n")
    outfile.write("\n")

    # Write GET method
    outfile.write("\t# HTTP GET\n")
    arg_str = get_function_parameters(collection_path[1:])
    if arg_str == collection_path[1:] or not arg_str:
        outfile.write("\tdef get(self):\n")
        outfile.write("\t\tlogging.info('{0} Collection get called')\n".format(resource))
        outfile.write("\t\tmsg, code = check_authentication(self.auth)\n\n")
        outfile.write("\t\tif code == 200:\n")
        outfile.write("\t\t\tpath = os.path.join(self.root, '{0}', 'index.json')\n".format(collection_path[1:]))
    else:
        outfile.write("\tdef get(self, {0}):\n".format(arg_str))
        outfile.write("\t\tlogging.info('{0} Collection get called')\n".format(resource))
        outfile.write("\t\tmsg, code = check_authentication(self.auth)\n\n")
        outfile.write("\t\tif code == 200:\n")

        new_collection_path = get_path_parameters(collection_path[1:])
        outfile.write("\t\t\tpath = os.path.join(self.root, '{0}', 'index.json').format({1})\n".format(new_collection_path, arg_str))
    outfile.write("\t\t\treturn get_json_data (path)\n")
    outfile.write("\t\telse:\n")
    outfile.write("\t\t\treturn msg, code\n")
    outfile.write("\n")

    # Write POST method
    outfile.write("\t# HTTP POST\n")
    if arg_str != collection_path[1:] and arg_str:
        outfile.write("\tdef post(self, {0}):\n".format(arg_str))
    else:
        outfile.write("\tdef post(self):\n")
    outfile.write("\t\tlogging.info('{0} Collection post called')\n".format(resource))
    outfile.write("\t\treturn 'POST is not a supported command for {0}CollectionAPI', 405\n".format(resource))
    outfile.write("\n")

    # Write PUT method
    outfile.write("\t# HTTP PUT\n")
    if arg_str != collection_path[1:] and arg_str:
        outfile.write("\tdef put(self, {0}):\n".format(arg_str))
    else:
        outfile.write("\tdef put(self):\n")
    outfile.write("\t\tlogging.info('{0} Collection put called')\n".format(resource))
    outfile.write("\t\treturn 'PUT is not a supported command for {0}CollectionAPI', 405\n".format(resource))
    outfile.write("\n")

    # Write PATCH method
    outfile.write("\t# HTTP PATCH\n")
    if arg_str != collection_path[1:] and arg_str:
        outfile.write("\tdef patch(self, {0}):\n".format(arg_str))
    else:
        outfile.write("\tdef patch(self):\n")
    outfile.write("\t\tlogging.info('{0} Collection patch called')\n".format(resource))
    outfile.write("\t\treturn 'PATCH is not a supported command for {0}CollectionAPI', 405\n".format(resource))
    outfile.write('\n')

    # Write DELETE method
    outfile.write("\t# HTTP DELETE\n")
    if arg_str != collection_path[1:] and arg_str:
        outfile.write("\tdef delete(self, {0}):\n".format(arg_str))
    else:
        outfile.write("\tdef delete(self):\n")
    outfile.write("\t\tlogging.info('{0} Collection delete called')\n".format(resource))
    outfile.write("\t\treturn 'DELETE is not a supported command for {0}CollectionAPI', 405\n".format(resource))
    outfile.write('\n\n')
    return

def write_servicetype_singleton_api(outfile, resource, collection_path, instance):
    ''' Write the singleton resource API function '''
    outfile.write("# {0} API\n".format(resource))
    argument_string = "class {0}API(Resource):\n".format(resource)
    outfile.write(argument_string)
    outfile.write("\tdef __init__(self, **kwargs):\n")
    outfile.write("\t\tlogging.info('{0} init called')\n".format(resource))
    outfile.write("\t\tself.root = PATHS['Root']\n")
    outfile.write("\t\tself.auth = kwargs['auth']\n")
    outfile.write("\n")
    
    # Write GET method
    outfile.write("\t# HTTP GET\n")
    original_path = collection_path[1:] + '/' + instance
    arg_str = get_function_parameters(original_path)
    if arg_str == '':
        outfile.write("\tdef get(self):\n")
    else:
        outfile.write("\tdef get(self, {0}):\n".format(arg_str))
    outfile.write("\t\tlogging.info('{0} get called')\n".format(resource))
    outfile.write("\t\tmsg, code = check_authentication(self.auth)\n\n")
    outfile.write("\t\tif code == 200:\n")

    new_collection_path = get_path_parameters(original_path)
    if new_collection_path == '' or  new_collection_path == '/':
        outfile.write("\t\t\tpath = create_path(self.root, 'index.json')\n")
    else:
        outfile.write("\t\t\tpath = create_path(self.root, '{0}', 'index.json').format({1})\n".format(new_collection_path, arg_str))

    outfile.write("\t\t\treturn get_json_data (path)\n")
    outfile.write("\t\telse:\n")
    outfile.write("\t\t\treturn msg, code\n")
    outfile.write("\n")

    # Write POST method
    outfile.write("\t# HTTP POST\n")
    outfile.write("\tdef post(self, {0}):\n".format(arg_str))
    outfile.write("\t\tlogging.info('{0} post called')\n".format(resource))
    outfile.write("\t\treturn 'POST is not a supported command for {0}API', 405\n".format(resource))
    outfile.write("\n")

    # Write PUT method
    outfile.write("\t# HTTP PUT\n")
    outfile.write("\tdef put(self, {0}):\n".format(arg_str))
    outfile.write("\t\tlogging.info('{0} put called')\n".format(resource))
    outfile.write("\t\treturn 'PUT is not a supported command for {0}API', 405\n".format(resource))
    outfile.write("\n")

    # Write PATCH method
    outfile.write("\t# HTTP PATCH\n")
    outfile.write("\tdef patch(self, {0}):\n".format(arg_str))
    outfile.write("\t\tlogging.info('{0} patch called')\n".format(resource))
    outfile.write("\t\treturn 'PATCH is not a supported command for {0}API', 405\n".format(resource))
    outfile.write('\n')

    # Write DELETE method
    outfile.write("\t# HTTP DELETE\n")
    outfile.write("\tdef delete(self, {0}):\n".format(arg_str))
    outfile.write("\t\tlogging.info('{0} delete called')\n".format(resource))
    outfile.write("\t\treturn 'DELETE is not a supported command for {0}API', 405\n".format(resource))
    outfile.write('\n\n')
    return