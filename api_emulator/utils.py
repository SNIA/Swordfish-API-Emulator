 /* 
 * Copyright (c) 2017, The Storage Networking Industry Association.
 *  
 * Redistribution and use in source and binary forms, with or without 
 * modification, are permitted provided that the following conditions are met:
 *  
 * Redistributions of source code must retain the above copyright notice, 
 * this list of conditions and the following disclaimer.
 *  
 * Redistributions in binary form must reproduce the above copyright notice, 
 * this list of conditions and the following disclaimer in the documentation 
 * and/or other materials provided with the distribution.
 *  
 * Neither the name of The Storage Networking Industry Association (SNIA) nor 
 * the names of its contributors may be used to endorse or promote products 
 * derived from this software without specific prior written permission.
 *  
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
 *  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
 *  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
 *  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
 *  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
 *  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
 *  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS  
 *  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
 *  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
 *  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
 *  THE POSSIBILITY OF SUCH DAMAGE.
 */

# Utilities used through out the library
#   timestamp()
#   process_id()
#   check_initialization

import os
import json
import datetime
from functools import wraps


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
