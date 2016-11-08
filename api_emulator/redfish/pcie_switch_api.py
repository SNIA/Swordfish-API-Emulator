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
PCIe Switches API  GET, POST
PCIe Switch   API  GET, PUT, PATCH, DELETE

"""
import g

import sys, traceback
from flask import Flask, request, make_response, render_template
from flask.ext.restful import reqparse, Api, Resource

from .templates.pcie_switch import get_PCIeSwitch_template
from .pcie_port_api import PCIePortsAPI, PCIePortAPI


members = []
member_ids = []
foo = 'false'
INTERNAL_ERROR = 500

#PCIe Switch API
class PCIeSwitchAPI(Resource):
    def __init__(self):
        print ('PCIeSwitchAPI init called')
        print ('PCIeSwitchAPI init exit')

    # HTTP GET
    def get(self,ident):
        try:
            # Find the entry with the correct value for Id
            for cfg in members:
                if (ident == cfg["Id"]):
                    break
            config = cfg
            resp = config, 200
        except OSError:
            resp = error_response('Resources directory does not exist', 400)
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp

    # HTTP PUT
    # - On the first call, we add the API for PCIeSwitches, because sw_id is not available in 'init'.
    # - TODO - debug why this returns a 500 error, on the second put call
    def put(self,ident):
        print ('PCIeSwitchAPI put called')
        try:
            global config
            config=get_PCIeSwitch_template(g.rest_base,ident)
            members.append(config)
            member_ids.append({'@odata.id': config['@odata.id']})
            global foo
            print ('var = ' + foo)
            g.api.add_resource(PCIePortsAPI, '/redfish/v1/PCIeSwitches/<string:sw_id>/Ports')
            g.api.add_resource(PCIePortAPI,  '/redfish/v1/PCIeSwitches/<string:sw_id>/Ports/<string:ident>')
            resp = config, 200
        except OSError:
            resp = error_response('Resources directory does not exist', 400)
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        print ('PCIeSwitchAPI put exit')
        return resp

    # HTTP PATCH
    def patch(self, ident):
        print ('PCIeSwitchAPI patch called')
        raw_dict = request.get_json(force=True)
        print (raw_dict)
        try:
        # schema.validate(raw_dict)
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
        except OSError:
            resp = error_response('Resources directory does not exist', 400)
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp


    # HTTP DELETE
    def delete(self,ident):
        # print ('PCIeSwitchAPI delete called')
        try:
            idx = 0
            for cfg in members:
                if (ident == cfg["Id"]):
                    break
                idx += 1
            members.pop(idx)
            member_ids.pop(idx)
            resp = 200
        except OSError:
            resp = error_response('Resources directory does not exist', 400)
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp


# PCIe Switches API
class PCIeSwitchesAPI(Resource):
    def __init__(self):
        self.rb = g.rest_base
        self.config = {
            '@odata.context': self.rb + '$metadata#PCIeSwitches',
            '@odata.id': self.rb + 'PCIeSwitches',
            '@odata.type': '#PCIeSwitches.1.0.0.PCIeSwitches',
            'Name': 'PCIe Switches Collection',
            'Links': {}
        }
        self.config['Links']['Member@odata.count'] = len(member_ids)
        self.config['Links']['Members'] = member_ids

    def get(self):
        try:
            resp = self.config, 200
        except OSError:
            resp = error_response('Resources directory does not exist', 400)
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp

    # The POST command should be for adding multiple instances. For now, just add one.
    # Todo - Fix so the config can be passed in the data.
    def post(self):
        try:
            g.api.add_resource(PCIeSwitchAPI, '/redfish/v1/PCIeSwitches/<string:ident>')
            resp=self.config,200
        except PathError:
            resp = error_response('Attribute Does Not Exist', 404)
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp
