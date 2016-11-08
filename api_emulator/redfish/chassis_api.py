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
Collection API  GET, POST
Singleton  API  GET, PUT, PATCH, DELETE

"""
import g

import sys, traceback
from flask import Flask, request, make_response, render_template
from flask.ext.restful import reqparse, Api, Resource

from .templates.chassis import get_Chassis_template
from .thermal_api import ThermalAPI, CreateThermal
from .power_api import PowerAPI, CreatePower


members = []
member_ids = []
foo = 'false'
INTERNAL_ERROR = 500

#Chassis API
class ChassisAPI(Resource):
    # Can't initialize the resource since the URI variables are not in the argument list.
    # Need the variables to set the Odata.id properties
    def __init__(self):
        print ('ChassisAPI init called')

    # HTTP GET
    def get(self,ident):
        try:
            # Find the entry with the correct value for Id
            for cfg in members:
                if (ident == cfg["Id"]):
                    break
            config = cfg
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp

    # HTTP PUT
    # - Create the resource (since URI variables are avaiable)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordiante resources
    def put(self,ident):
        print ('ChassisAPI put called')
        try:
            global config
            config=get_Chassis_template(g.rest_base,ident)
            members.append(config)
            member_ids.append({'@odata.id': config['@odata.id']})
            global foo
            # Attach URIs for subordiante resources
            if  (foo == 'false'):
                g.api.add_resource(ThermalAPI, '/redfish/v1/Chassis/<string:ch_id>/Thermal')
                g.api.add_resource(PowerAPI,   '/redfish/v1/Chassis/<string:ch_id>/Power')
                foo = 'true'
            # Create instances of subordinate resources, then call put operation
            cfg = CreateThermal()
            out = cfg.put(ident)
            cfg = CreatePower()
            out = cfg.put(ident)
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        print ('ChassisAPI put exit')
        return resp

    # HTTP PATCH
    def patch(self, ident):
        print ('ChassisAPI patch called')
        raw_dict = request.get_json(force=True)
        print (raw_dict)
        try:
            # Find the entry with the correct value for Id
            for cfg in members:
                if (ident == cfg["Id"]):
                    break
            config = cfg
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


    # HTTP DELETE
    def delete(self,ident):
        # print ('ChassisAPI delete called')
        try:
            idx = 0
            for cfg in members:
                if (ident == cfg["Id"]):
                    break
                idx += 1
            members.pop(idx)
            member_ids.pop(idx)
            resp = 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp


# Chassis Collection API (Chassis has the same form for singular and plural)
class ChassisCollectionAPI(Resource):
    def __init__(self):
        self.rb = g.rest_base
        self.config = {
            '@odata.context': self.rb + '$metadata#ChassisCollection',
            '@odata.id': self.rb + 'ChassisCollection',
            '@odata.type': '#ChassisCollection.1.0.0.ChassisCollection',
            'Name': 'Chassis Collection',
            'Links': {}
        }
        self.config['Links']['Member@odata.count'] = len(member_ids)
        self.config['Links']['Members'] = member_ids

    def get(self):
        try:
            resp = self.config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp

    # The POST command should be for adding multiple instances. For now, just add one.
    # Todo - Fix so the config can be passed in the data.
    def post(self):
        try:
            g.api.add_resource(ChassisAPI, '/redfish/v1/Chassis/<string:ident>')
            resp=self.config,200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp


# Used to create a resource instance internally
class CreateChassis(object):
    def __init__(self):
        print ('CreateChassis init called')

    def put(self,ident):
        print ('CreateChassis put called')
        try:
            global config
            config=get_Chassis_template(g.rest_base,ident)
            members.append(config)
            member_ids.append({'@odata.id': config['@odata.id']})
            g.api.add_resource(ThermalAPI, '/redfish/v1/Chassis/<string:ch_id>/Thermal')
            g.api.add_resource(PowerAPI, '/redfish/v1/Chassis/<string:ch_id>/Power')
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        print ('CreateChassis put exit')
        return resp
