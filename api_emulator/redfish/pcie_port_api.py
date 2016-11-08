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
PCIe Ports API  GET, POST
PCIe Port  API  GET, PUT

"""
import g

# Flask Imports
from flask import Flask, request, make_response, render_template
from flask.ext.restful import reqparse, Api, Resource

from .templates.pcie_port import get_PCIePort_template

members = []
member_ids = []

#PCIe Port API
class PCIePortAPI(Resource):
    def __init__(self):
        # Attach the dependent resources
        print ('PCIePortAPI init called')

    def get(self,sw_id,ident):
        try:
            global config
            resp = config, 200
        except OSError:
            resp = error_response('Resources directory does not exist', 400)
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp

    def put(self,sw_id,ident):
        try:
            global config
            config=get_PCIePort_template(g.rest_base,sw_id,ident)
            members.append(config)
            member_ids.append({'@odata.id': config['@odata.id']} )
            resp = config, 200
        except OSError:
            resp = error_response('Resources directory does not exist', 400)
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp

# PCIe Ports API
class PCIePortsAPI(Resource):
    def __init__(self):
        print ('PCIePortsAPI init called')
        self.rb = g.rest_base

        self.config = {
            '@odata.context': self.rb + '$metadata#PCIePorts',
            '@odata.id': self.rb + 'PCIePorts',
            '@odata.type': '#PCIePorts.1.0.0.PCIePorts',
            'Name': 'PCIe Ports Collection',
            'Links': {}
        }
        self.config['Links']['Member@odata.count'] = len(member_ids)
        self.config['Links']['Members'] = member_ids
        print ('PCIePortsAPI exit called')

    def get(self,sw_id):
        print ('PCIePortAPI get called')
        try:
            self.config['@odata.id'] = self.rb + 'Switches/' + sw_id + '/PCIePorts'
            resp = self.config, 200
        except OSError:
            resp = error_response('Resources directory does not exist', 400)
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp

    # The POST command should be for addeding multiple instances
    def post(self,sw_id):
        try:
#            g.api.add_resource(PCIePortAPI, '/redfish/v1/PCIePorts/<string:ident>')
            resp=self.config,200
        except PathError:
            resp = error_response('Attribute Does Not Exist', 404)
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp
