#
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

#f_switch_ports_api.py

import json, os
import shutil

import traceback
import logging
import g
import urllib3

from flask import jsonify, request
from flask_restful import Resource
from api_emulator.utils import update_collections_json
from .constants import *
from .templates.fabric_switch_port import get_FabricSwitchPorts_instance

members =[]
member_ids = []
foo = False
config = {}
INTERNAL_ERROR = 500


def create_path(*args):
    trimmed = [str(arg).strip('/') for arg in args]
    return os.path.join(*trimmed)


# FabricsSwitchPorts API
class FabricsSwitchPortsAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('FabricsSwitchPortsAPI init called')
        self.root = PATHS['Root']
        self.fabrics = PATHS['Fabrics']['path']
        self.f_switches = PATHS['Fabrics']['f_switch']
        self.f_switch_ports = PATHS['Fabrics']['f_switch_port']

    # HTTP GET
    def get(self, fabric, f_switch, f_switch_port):
        path = create_path(self.root, self.fabrics, fabric, self.f_switches, f_switch, self.f_switch_ports, f_switch_port, 'index.json')
        try:
            f_switch_port_json = open(path)
            data = json.load(f_switch_port_json)
        except Exception as e:
            traceback.print_exc()
            raise Exception("Unable to read file because of following error::{}".format(e))
        return jsonify(data)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordiante resources
    def post(self, fabric, f_switch, f_switch_port):
        logging.info('FabricsSwitchPortsAPI PUT called')
        try:
            global config
            global foo

            wildcards = {'f_id':fabrics, 's_id': f_switch, 'fsp_id': f_switch_port, 'rb': g.rest_base}
            config=get_FabricSwitchPorts_instance(wildcards)

            members.append(config)
            member_ids.append({'@odata.id': config['@odata.id']})

            # Create instances of subordinate resources, then call put operation
            # not implemented yet

            path = create_path(self.root, self.fabrics, fabric, self.f_switches, f_switch, self.f_switch_ports, f_switch_port)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                # This will execute when POST is called for more than one time for a resource
                return config, 500
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            # update the collection json file with new added resource
            collection_path = os.path.join(self.root, self.fabrics, fabric, self.f_switches, f_switch, self.f_switch_ports, f_switch_port, 'index.json')
            update_collections_json(path=collection_path, link=config['@odata.id'])
            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('FabricsSwitchPortsAPI put exit')
        return resp

	# HTTP PATCH
    def patch(self, fabric, f_switch, f_switch_port):
        path = os.path.join(self.root, self.fabrics, fabric,
                                       self.f_switches, f_switch, self.f_switch_ports, f_switch_port, 'index.json')
        try:
            # Read json from file.
            with open(path, 'r') as f_switch_port_json:
                data = json.load(f_switch_port_json)
                f_switch_port_json.close()

            request_data = json.loads(request.data)

            if request_data:
                # Update the keys of payload in json file.
                for key, value in request_data.items():
                    if key in data and data[key]:
                        data[key] = value

            # Write the updated json to file.
            with open(path, 'w') as f:
                json.dump(data, f)
                f.close()

        except Exception as e:
            return {"error": "Unable to read file because of following error::{}".format(e)}, 500

        json_data = self.get(fabrics, f_switch_port_json)
        return json_data

    # HTTP DELETE
    def delete(self, fabric, f_switch, f_switch_port):

        path = os.path.join(self.root, self.fabrics, fabric, self.f_switches, f_switch, self.f_switch_ports, f_switch_port).replace("\\","/")
        print (path)
        delPath = path.replace('Resources','/redfish/v1')
        path2 = os.path.join(self.root, self.fabrics, fabric, self.f_switches, self.f_switch_ports, f_switch_port, 'index.json').replace("\\","/")

        try:
            with open(path2,"r") as pdata:
                pdata = json.load(pdata)

            data = {
            "@odata.id":delPath
            }
            resp = 200
            jdata = data["@odata.id"].split('/')

            path1 = os.path.join(self.root, self.fabrics, fabric, self.f_switches, f_switch, self.f_switch_ports, jdata[len(jdata)-1])
            shutil.rmtree(path1)
            pdata['Members'].remove(data)
            pdata['Members@odata.count'] = int(pdata['Members@odata.count']) - 1

            with open(path2,"w") as jdata:
                json.dump(pdata,jdata)


        except Exception as e:
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(resp)


# FabricsSwitchPorts Collection API
class FabricsSwitchPortsCollectionAPI(Resource):

    def __init__(self):
        self.root = PATHS['Root']
        self.fabrics = PATHS['Fabrics']['path']
        self.f_switches = PATHS['Fabrics']['f_switch']
        self.f_switch_ports = PATHS['Fabrics']['f_switch_port']

    def get(self, fabric, f_switch):
        path = os.path.join(self.root, self.fabrics, fabric, self.f_switches, f_switch, self.f_switch_ports, 'index.json')
        try:
            f_switch_port_json = open(path)
            data = json.load(f_switch_port_json)
        except Exception as e:
            traceback.print_exc()
            return {"error": "Unable to read file because of following error::{}".format(e)}, 500

        return jsonify(data)

    def verify(self, config):
        # TODO: Implement a method to verify that the POST body is valid
        return True,{}

    # HTTP POST
    # POST should allow adding multiple instances to a collection.
    # For now, this only adds one instance.
    # TODO: 'id' should be obtained from the request data.
    def post(self, fabric, f_switch):
        logging.info('FabricsSwitchPortsCollectionAPI POST called')
        try:
            config = request.get_json(force=True)
            ok, msg = self.verify(config)
            if ok:
                # Save the new singleton
                singleton_name = os.path.basename(config['@odata.id'])
                path = os.path.join(self.root, self.fabrics, fabric, self.f_switches, f_switch, self.f_switch_ports, singleton_name)
                if not os.path.exists(path):
                    os.mkdir(path)
                with open(os.path.join(path, "index.json"), "w") as fd:
                    fd.write(json.dumps(config, indent=4, sort_keys=True))
                # Update the collection
                collection_path = os.path.join(self.root, self.fabrics, fabric, self.f_switches, f_switch, self.f_switch_ports,'index.json')
                update_collections_json(collection_path, config['@odata.id'])
                # Return a copy of the new singleton with a Created response
                resp = config, 201
            else:
                resp = msg, 400
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp


class CreateFabricsSwitchPorts (Resource):
    def __init__(self):
        self.root = PATHS['Root']
        self.fabrics = PATHS['Fabrics']['path']
        self.f_switches = PATHS['Fabrics']['f_switch']
        self.f_switch_ports = PATHS['Fabrics']['f_switch_port']

    # Attach APIs for subordinate resource(s). Attach the APIs for a resource collection and its singletons
    def put(self,fabrics):
        logging.info('CreateFabricsSwitchPorts put started.')
        try:
            path = create_path(self.root, self.fabrics, fabric, self.f_switches, f_switch, self.f_switch_ports)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                logging.info('The given path : {} already exists.'.format(path))
            config={

                      "@Redfish.Copyright": "Copyright 2015-2021 SNIA. All rights reserved.",
                      "@odata.id": "/redfish/v1/Fabrics/{fabrics}/Switches/{f_switches}/Ports",
                      "@odata.type": "#PortCollection.PortCollection",
                      "Name": "Port Collection",
                      "Members@odata.count": 0,
                      "Members": [
                      ]
                    }
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('CreateFabricsSwitchPorts put exit.')
        return resp
