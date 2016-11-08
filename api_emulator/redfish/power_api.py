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
Singleton API: GET, PATCH

"""
import g

import sys, traceback
from flask import Flask, request, make_response, render_template
from flask.ext.restful import reqparse, Api, Resource

from .templates.power import get_power_template

# config is instantiated by CreatePower()
config = {}
INTERNAL_ERROR = 500

# Power API
class PowerAPI(Resource):
    # Can't initialize the resource since the URI variables are not in the argument list.
    # Need the variables to set the Odata.id properties
    def __init__(self):
        print ('PowerAPI init called')

    # HTTP GET
    def get(self,ch_id):
        try:
            global config
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp

    # HTTP PATCH
    def patch(self, ch_id):
        print ('PowerAPI patch called')
        raw_dict = request.get_json(force=True)
        print (raw_dict)
        try:
            global config
            print (config)
            for key, value in raw_dict.items():
                print ('Update ' + key + ' to ' + value)
                config[key] = value
            print (config)
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp

    # HTTP PUT
    def put(self,ch_id):
         return 'PUT is not a valid command', 202

    # HTTP DELETE
    def delete(self,ch_id):
         return 'DELETE is not a valid command', 202

# Used to create a resource instance internally
class CreatePower(object):
    def __init__(self):
        print ('CreatePower init called')

    # PUT
    # - Create the resource (since URI variables are avaiable)
    def put(self,ch_id):
        print ('CreatePower put called')
        try:
            global config
            config=get_power_template(g.rest_base,ch_id)
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        print ('CreatePower put exit')
        return resp
