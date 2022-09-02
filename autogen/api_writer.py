from operator import pos
import re
from api_writer_utils import get_function_parameters, get_path_parameters, get_wildcard_parameters


def write_program_header(resource_path, outfile, resource_num):
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
    outfile.write('# Program name - {0}_api.py\n'.format(resource_num))
    outfile.write('\n')
    outfile.write('import g\n')
    outfile.write('import json, os\n')
    outfile.write('import traceback\n')
    outfile.write('import logging\n')
    outfile.write('\n')
    outfile.write('from flask import Flask, request\n')
    outfile.write('from flask_restful import Resource\n')
    outfile.write('from .constants import *\n')
    outfile.write('from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection\n')
    outfile.write('from .templates.{0} import get_{0}_instance\n'.format(resource_num))
    outfile.write("\n")
    outfile.write("members = []\n")
    outfile.write("member_ids = []\n")
    outfile.write("INTERNAL_ERROR = 500\n")
    outfile.write("\n")
    return

def write_collection_api(outfile, resource, resource_num, collection_path):
    ''' Write the collection resource API function '''
    outfile.write("# {0} Collection API\n".format(resource_num))
    argument_string = "class {0}CollectionAPI(Resource):\n".format(resource_num)
    outfile.write(argument_string)

    # Write init method
    outfile.write("\tdef __init__(self):\n")
    outfile.write("\t\tlogging.info('{0} Collection init called')\n".format(resource_num))
    outfile.write("\t\tself.root = PATHS['Root']\n\n")

    # Write GET method
    outfile.write("\t# HTTP GET\n")

    arg_str = get_function_parameters(collection_path[1:])
    if(arg_str == ''):
        outfile.write("\tdef get(self):\n")
    else:
        outfile.write("\tdef get(self, {0}):\n".format(arg_str))
    outfile.write("\t\tlogging.info('{0} Collection get called')\n".format(resource_num))

    new_collection_path = get_path_parameters(collection_path[1:])
    if collection_path == '':
        outfile.write("\t\tpath = os.path.join(self.root, 'index.json')\n")
    elif arg_str == '':
        outfile.write("\t\tpath = os.path.join(self.root, '{0}', 'index.json')\n".format(collection_path[1:]))
    else:
        outfile.write("\t\tpath = os.path.join(self.root, '{0}', 'index.json').format({1})\n".format(new_collection_path, arg_str))
    outfile.write("\t\treturn get_json_data (path)\n\n")

    # Write POST method
    outfile.write("\t# HTTP POST Collection\n")
    if(arg_str == ''):
        outfile.write("\tdef post(self):\n")
    else:
        outfile.write("\tdef post(self, {0}):\n".format(arg_str))
    outfile.write("\t\tlogging.info('{0} Collection post called')\n\n".format(resource_num))

    if(arg_str != ''):
        sub_arg = re.split(', ', arg_str)
        outfile.write("\t\tif {0} in members:\n".format(sub_arg[-1]))
        outfile.write("\t\t\tresp = 404\n")
        outfile.write("\t\t\treturn resp\n")
    
    if collection_path == '':
        outfile.write("\t\tpath = create_path(self.root)\n")
    elif arg_str == '':
        outfile.write("\t\tpath = create_path(self.root, '{0}')\n".format(collection_path[1:]))
    else:
        outfile.write("\t\tpath = create_path(self.root, '{0}').format({1})\n".format(new_collection_path, arg_str))
    outfile.write("\t\treturn create_collection (path, '{0}')\n\n".format(resource))

    # Write PUT method
    outfile.write("\t# HTTP PUT Collection\n")
    if(arg_str == ''):
        outfile.write("\tdef put(self):\n")
    else:
        outfile.write("\tdef put(self, {0}):\n".format(arg_str))
    
    if collection_path == '':
        outfile.write("\t\tpath = os.path.join(self.root, 'index.json')\n")
    elif arg_str == '':
        outfile.write("\t\tpath = os.path.join(self.root, '{0}', 'index.json')\n".format(collection_path[1:]))
    else:
        outfile.write("\t\tpath = os.path.join(self.root, '{0}', 'index.json').format({1})\n".format(new_collection_path, arg_str))
    outfile.write("\t\tput_object (path)\n")

    if(arg_str == ''):
        outfile.write("\t\treturn self.get(self.root)\n\n")
    else:
        sub_arg = re.split(', ', arg_str)
        outfile.write("\t\treturn self.get({0})\n\n".format(sub_arg[0]))
    return


def write_singleton_api(outfile, resource_num, collection_path, instance):
    ''' Write the singleton resource API function '''
    outfile.write("# {0} API\n".format(resource_num))
    argument_string = "class {0}API(Resource):\n".format(resource_num)
    outfile.write(argument_string)
    outfile.write("\tdef __init__(self):\n")
    outfile.write("\t\tlogging.info('{0} init called')\n".format(resource_num))
    outfile.write("\t\tself.root = PATHS['Root']\n")
    outfile.write("\n")
    
    # Write GET method
    outfile.write("\t# HTTP GET\n")
    original_path = collection_path[1:] + '/' + instance
    arg_str = get_function_parameters(original_path)

    if arg_str == '':
        outfile.write("\tdef get(self):\n")
    else:
        outfile.write("\tdef get(self, {0}):\n".format(arg_str))
    outfile.write("\t\tlogging.info('{0} get called')\n".format(resource_num))

    new_collection_path = get_path_parameters(original_path)
    if new_collection_path == '' or  new_collection_path == '/':
        outfile.write("\t\tpath = create_path(self.root, 'index.json')\n")
    else:
        outfile.write("\t\tpath = create_path(self.root, '{0}', 'index.json').format({1})\n".format(new_collection_path, arg_str))
    outfile.write("\t\treturn get_json_data (path)\n\n")

    # Write POST method
    outfile.write("\t# HTTP POST\n")
    outfile.write("\t# - Create the resource (since URI variables are available)\n")
    outfile.write("\t# - Update the members and members.id lists\n")
    outfile.write("\t# - Attach the APIs of subordinate resources (do this only once)\n")
    outfile.write("\t# - Finally, create an instance of the subordiante resources\n")

    if arg_str == '':
        outfile.write("\tdef post(self):\n")
    else:
        outfile.write("\tdef post(self, {0}):\n".format(arg_str))
    outfile.write("\t\tlogging.info('{0} post called')\n".format(resource_num))

    if arg_str == '':
        outfile.write("\t\tpath = create_path(self.root)\n")
    else:
        outfile.write("\t\tpath = create_path(self.root, '{0}').format({1})\n".format(new_collection_path, arg_str))

    collection_arg_str = get_function_parameters(collection_path[1:])
    post_collection_path = get_path_parameters(collection_path[1:])

    if post_collection_path == '':
        outfile.write("\t\tcollection_path = os.path.join(self.root, 'index.json')\n\n")
    if collection_arg_str == '':
        outfile.write("\t\tcollection_path = os.path.join(self.root, '{0}', 'index.json')\n\n".format(post_collection_path))
    else:
        outfile.write("\t\tcollection_path = os.path.join(self.root, '{0}', 'index.json').format({1})\n\n".format(post_collection_path, collection_arg_str))
    
    outfile.write("\t\t# Check if collection exists:\n")
    outfile.write("\t\tif not os.path.exists(collection_path):\n")

    if collection_arg_str == '':
        outfile.write("\t\t\t{0}CollectionAPI.post(self)\n\n".format(resource_num))
    else:
        outfile.write("\t\t\t{0}CollectionAPI.post(self, {1})\n\n".format(resource_num, collection_arg_str))

    inst = instance.replace('{', '').replace('}', '')
    if inst == '':
        outfile.write("\t\ttry:\n")
        outfile.write("\t\t\tglobal config\n")

        outfile.write("\t\t\twildcards = "+"{"+"'rb':g.rest_base"+"}"+"\n")
        outfile.write("\t\t\tconfig=get_{0}_instance(wildcards)\n".format(resource_num))
        outfile.write("\t\t\tconfig = create_and_patch_object (config, members, member_ids, path, collection_path)\n")
        outfile.write("\t\t\tresp = config, 200\n\n")
    else:
        outfile.write("\t\tif {0} in members:\n".format(inst))
        outfile.write("\t\t\tresp = 404\n")
        outfile.write("\t\t\treturn resp\n")
        outfile.write("\t\ttry:\n")
        outfile.write("\t\t\tglobal config\n")

        wildcard_str = get_wildcard_parameters(arg_str)
        outfile.write("\t\t\twildcards = "+"{"+"{0}'rb':g.rest_base".format(wildcard_str)+"}"+"\n")
        outfile.write("\t\t\tconfig=get_{0}_instance(wildcards)\n".format(resource_num))
        outfile.write("\t\t\tconfig = create_and_patch_object (config, members, member_ids, path, collection_path)\n")
        outfile.write("\t\t\tresp = config, 200\n\n")
    outfile.write("\t\texcept Exception:\n")
    outfile.write("\t\t\ttraceback.print_exc()\n")
    outfile.write("\t\t\tresp = INTERNAL_ERROR\n")
    outfile.write("\t\tlogging.info('{0}API POST exit')\n".format(resource_num))
    outfile.write("\t\treturn resp\n")
    outfile.write("\n")

    # Write PUT method
    outfile.write("\t# HTTP PUT\n")

    if arg_str == '':
        outfile.write("\tdef put(self):\n")
    else:
        outfile.write("\tdef put(self, {0}):\n".format(arg_str))
    outfile.write("\t\tlogging.info('{0} put called')\n".format(resource_num))

    if arg_str == '':
        outfile.write("\t\tpath = create_path(self.root, 'index.json')\n")
        outfile.write("\t\tput_object(path)\n")
        outfile.write("\t\treturn self.get()\n\n")
    else:
        sub_arg = re.split(', ', arg_str)
        if(len(sub_arg) == 2):
            outfile.write("\t\tpath = create_path(self.root, '{0}', 'index.json').format({1})\n".format(new_collection_path, arg_str))
        else:
            outfile.write("\t\tpath = os.path.join(self.root, '{0}', 'index.json').format({1})\n".format(new_collection_path, arg_str))
        outfile.write("\t\tput_object(path)\n")
        outfile.write("\t\treturn self.get({0})\n\n".format(arg_str))

    # Write PATCH method
    outfile.write("\t# HTTP PATCH\n")
    if arg_str == '':
        outfile.write("\tdef patch(self):\n")
    else:
        outfile.write("\tdef patch(self, {0}):\n".format(arg_str))
    outfile.write("\t\tlogging.info('{0} patch called')\n".format(resource_num))

    if arg_str == '':
        outfile.write("\t\tpath = create_path(self.root, 'index.json')\n")
        outfile.write("\t\tpatch_object(path)\n")
        outfile.write("\t\treturn self.get()\n\n")
    else:
        if(len(sub_arg) == 2):
            outfile.write("\t\tpath = create_path(self.root, '{0}', 'index.json').format({1})\n".format(new_collection_path, arg_str))
        else:
            outfile.write("\t\tpath = os.path.join(self.root, '{0}', 'index.json').format({1})\n".format(new_collection_path, arg_str))
        outfile.write("\t\tpatch_object(path)\n")
        outfile.write("\t\treturn self.get({0})\n\n".format(arg_str))

    # Write DELETE method
    outfile.write("\t# HTTP DELETE\n")

    if arg_str == '':
        outfile.write("\tdef delete(self):\n")
    else:
        outfile.write("\tdef delete(self, {0}):\n".format(arg_str))
    outfile.write("\t\tlogging.info('{0} delete called')\n".format(resource_num))

    if arg_str == '':
        outfile.write("\t\tpath = create_path(self.root)\n")
    else:
        outfile.write("\t\tpath = create_path(self.root, '{0}').format({1})\n".format(new_collection_path, arg_str))

    base_collection_path = get_path_parameters(collection_path[1:])
    base_arg_str = get_function_parameters(collection_path[1:])
    if base_collection_path == '':
        outfile.write("\t\tbase_path = create_path(self.root)\n")
    elif(base_arg_str == ''):
        outfile.write("\t\tbase_path = create_path(self.root, '{0}')\n".format(base_collection_path))
    else:
        outfile.write("\t\tbase_path = create_path(self.root, '{0}').format({1})\n".format(base_collection_path, base_arg_str))
    outfile.write("\t\treturn delete_object(path, base_path)")
    outfile.write('\n\n')
    return