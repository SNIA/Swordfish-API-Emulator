#
# Copyright (c) 2016 Intel Corporation. All Rights Reserved.
# Copyright (c) 2016, The Storage Networking Industry Association.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. 
#
# Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
# Neither the name of The Storage Networking Industry Association (SNIA) nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

"""
Module for loading in static data
"""
import json
import os
import re

from .utils import process_id
from .exceptions import StaticLoadError
from .resource_dictionary import ResourceDictionary

# Resource dictionary

class Member():
    def __init__(self, config):
        self.config = config
        
    @property
    def configuration(self):
        return self.config

def load_static(name, spec, rest_base, resource_dictionary):
    """
    Loads the static data starting at the directory ./<spec>/static/<name>, recursively.
    
    Populates the resdict dictionary, with the file path as the key.

    Expects a single index.json file in each directory.  Ignores other files.

    Arguments:
        name      - Name of the static data
        spec      - Which spec the data is under, must be either redfish
                    or chinook
        rest_base - Base URL of the RESTful interface
    """
    # print ('load_static Name = ', name)
    try:
        assert spec.lower() in ['redfish', 'chinook'], 'Unknown spec: ' + spec
        dirname = os.path.dirname(__file__)
        base_dir = os.path.join(dirname, spec.lower(), 'static')
        index = os.path.join(dirname, spec, 'static', name, 'index.json')
        assert os.path.exists(index), 'Static file for ' + name + ' does not exist'

        startDir = os.path.join(dirname, spec, 'static', name)
        for dirName, subdirList, fileList in os.walk(startDir):
            # print('Found directory: %s' % dirName)
            for fname in fileList:
                if fname != 'index.json':
                    continue
                # read in file
                path = os.path.join(dirName,fname)
                f = open(path)
                index = json.load(f)
                m = Member(index)
                # create the Key by taking 'path' and remove the startpath fragement and the index.json filename
                startpath = os.path.join(dirname, spec, 'static')
                shortpath = os.path.relpath(path, startpath)
                (filepath, filename) =  os.path.split(shortpath)
                resource_dictionary.add_resource(filepath, m)
    except AssertionError as e:
        raise StaticLoadError(e.message)
    return shortpath
