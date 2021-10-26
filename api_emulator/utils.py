# Copyright Notice:
# Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/blob/master/LICENSE.md
#
# The original DMTF contents of this file have been modified to support
# The SNIA Swordfish API Emulator. These modifications are subject to the following:
# Copyright (c) 2017-2021, The Storage Networking Industry Association.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# Neither the name of The Storage Networking Industry Association (SNIA) nor
# the names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
#  THE POSSIBILITY OF SUCH DAMAGE.
#
# utils.py

# Utilities used through out the library
#   timestamp()
#   process_id()
#   check_initialization

import os
import json
import datetime
import traceback
import shutil

from flask import jsonify, request
from functools import wraps
from api_emulator.redfish.templates.collection import get_Collection_instance

def timestamp():
    """
    Return an ISO timestamp with milliseconds removed
    """
    return datetime.datetime.now().isoformat().split('.')[0]


def process_id(odata_id, base_dir, rest_base):
    """
    Gets the index.html associated with the odata_id
    """
    index_dir = os.path.abspath(os.path.join(
        base_dir, odata_id.split(rest_base)[-1]))
    index_html = os.path.join(index_dir, 'index.json')
    assert os.path.exists(index_html), \
        '"{0}" does not exist'.format(index_html)
    with open(index_html, 'r') as f:
        index = json.load(f)
    return index


def check_initialized(func):
    """
r   Wrapper function to check if the initialized member variable
    has been set to True in a class.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        cls = args[0]
        if cls.initialized:
            raise RuntimeError('Object has already been initialized')
        return func(*args, **kwargs)
    return wrapper

def replace_recurse(c, wildcards):
    """
    Replaces wildcard values in 'c' with the replacements specified in
    'wildcards'

    The parameter 'wildcards' is a dictionary of wildcards and their replacement.
    Theoretically, any string can be used as the wildcard.  This code has been
    testing with the wildcards delimite by curly braces (e.g. {id})

    The paramerter 'c' starts as a dictionary, but during the recursion, c can
    become
        - a dictionary - recurse
        - a list - recurse on each list item
        - a string - replace wildcards
        - a float - do nothing
        - a int - do nothing
    """
    # print("recurse c: ", c)

    for k, v in c.items():
        if isinstance(v, dict):
            replace_recurse(c[k], wildcards)
        elif isinstance(v, list):
            for index, item in enumerate(v):
                replace_recurse(item, wildcards)
        elif isinstance (v, str):
            # print("key/value : ", k, "; ", v)
            # print("c[k] : ", c[k])
            c[k] = c[k].format(**wildcards)
            # print("c[k]2: ", c[k])

def update_collections_json(path, link):
    '''
    Update json files in collections folder respected resource.
    :param path: (str)
    :return: (None)
    '''
    # Read json from file.
    with open(path, 'r') as file_json:
        data = json.load(file_json)

    # Update the keys of payload in json file.
    data['Members@odata.count'] = int(data['Members@odata.count']) + 1
    data['Members'].append({"@odata.id": link})

    # Write the updated json to file.
    with open(path, 'w') as file_json:
        json.dump(data, file_json)

def create_path(*args):
    trimmed = [str(arg).strip('/') for arg in args]
    return os.path.join(*trimmed)

    # HTTP GET
def get_json_data(path):
    try:
        json_data = open(path)
        data = json.load(json_data)
    except Exception as e:
        traceback.print_exc()
        return {"error": "Unable to read file because of the following error::{}".format(e)}, 404
    return jsonify(data)

    # For POST Singleton API:
def create_and_patch_object (config, members, member_ids, path, collection_path):

    # If input body data, then update properties
    if request.data:
        request_data = json.loads(request.data)
        # Update the keys of payload in json file.
        for key, value in request_data.items():
            config[key] = value

    members.append(config)
    member_ids.append({'@odata.id': config['@odata.id']})

    # Create instances of subordinate resources, then call put operation
    # not implemented yet
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        # This will execute when POST is called for more than one time for a resource
        return config, 409
    with open(os.path.join(path, "index.json"), "w") as fd:
        fd.write(json.dumps(config, indent=4, sort_keys=True))

    # update the collection json file with new added resource
    update_collections_json(path=collection_path, link=config['@odata.id'])
    return config

def delete_object (path, base_path):

    delPath = path.replace('Resources','/redfish/v1').replace("\\","/")
    path2 = create_path(base_path, 'index.json').replace("\\","/")
    try:
        with open(path2,"r") as pdata:
            pdata = json.load(pdata)

        data = {
        "@odata.id":delPath
        }
        resp = 200
        jdata = data["@odata.id"].split('/')

        path1 = os.path.join(base_path, jdata[len(jdata)-1])
        shutil.rmtree(path1)
        pdata['Members'].remove(data)
        pdata['Members@odata.count'] = int(pdata['Members@odata.count']) - 1

        with open(path2,"w") as jdata:
            json.dump(pdata,jdata)

    except Exception as e:
        return {"error": "Unable to read file because of the following error::{}".format(e)}, 404

    return jsonify(resp)

def delete_collection (path, base_path):

    delPath = path.replace('Resources','/redfish/v1').replace("\\","/")
    path2 = create_path(base_path, 'index.json').replace("\\","/")
    try:
        with open(path2,"r") as pdata:
            pdata = json.load(pdata)

        data = {
        "@odata.id":delPath
        }
        resp = 200
        jdata = data["@odata.id"].split('/')

        path1 = os.path.join(base_path, jdata[len(jdata)-1])
        shutil.rmtree(path1)

        with open(path2,"w") as jdata:
            json.dump(pdata,jdata)

    except Exception as e:
        return {"error": "Unable to read file because of the following error::{}".format(e)}, 404

    return jsonify(resp)

def patch_object(path):
    try:
    # Read json from file.
        with open(path, 'r') as data_json:
            data = json.load(data_json)
            data_json.close()

        # If input body data, then update properties
        if request.data:
            request_data = json.loads(request.data)
            # Update the keys of payload in json file.
            for key, value in request_data.items():
                data[key] = value

        # Write the updated json to file.
        with open(path, 'w') as f:
            json.dump(data, f)
            f.close()

    except Exception as e:
        return {"error": "Unable to read file because of the following error:{}".format(e)}, 404

    return True

def put_object(path):
    if not os.path.exists(path):
        return {"error": "The requested object does not exist.:{}"}, 404
    try:
    # Read json from file.
    #    with open(path, 'r') as data_json:
    #        data = json.load(data_json)
    #        data_json.close()
        data = {}
        path = path.replace("\\","/")
        # If input body data, then update properties
        if request.data:
            request_data = json.loads(request.data)
            # Update the keys of payload in json file.
            for key, value in request_data.items():
                data[key] = value

        # Write the updated json to file.
        with open(path, 'w') as f:
            json.dump(data, f)
            f.close()

    except Exception as e:
        return {"error": "Unable to read file because of the following error:{}".format(e)}, 404

    return True

def create_collection (collection_path, collection_type):

    try:
        if not os.path.exists(collection_path):
            os.mkdir(collection_path)
        else:
            return {"error": "The collection {} already exists.::{}"}, 404

        global config

        path = collection_path.replace('Resources','/redfish/v1').replace("\\","/")
        wildcards = {'path': path, 'cType': collection_type}
        config=get_Collection_instance(wildcards)

        with open(os.path.join(collection_path, "index.json"), "w") as fd:
            fd.write(json.dumps(config, indent=4, sort_keys=True))

        resp = config, 200
    except Exception as e:
        traceback.print_exc()
        resp = 500
    return resp

def remove_json_object (config, property_id):
    # Iterate through the objects in the JSON and pop (remove)
    # the obj once we find it.
    for i in xrange(len(config)):
        if obj[i][property_id]:
            obj.pop(i)
            break
    return config
