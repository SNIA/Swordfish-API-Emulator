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
# md_chunks_api.py


import json, os
import traceback
import logging
import g
import urllib3
import shutil

from flask import jsonify, request
from flask_restful import Resource
from api_emulator.utils import update_collections_json
from .constants import *
from .templates.md_chunks import get_MDChunks_instance


members =[]
member_ids = []
foo = False
config = {}
INTERNAL_ERROR = 500



def create_path(*args):
    trimmed = [str(arg).strip('/') for arg in args]
    return os.path.join(*trimmed)


# MDChunksAPI API
class MDChunksAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('MDChunksAPI init called')
        self.root = PATHS['Root']
        self.chassis = PATHS['Chassis']['path']
        self.memory_domains = PATHS['Chassis']['memory_domains']
        self.md_chunks = PATHS['Chassis']['md_chunks']

    # HTTP GET
    def get(self, chassis, memory_domain, md_chunks):
        path = create_path(self.root, self.chassis, chassis, self.memory_domains, memory_domain, self.md_chunks, md_chunks, 'index.json')
        logging.info('Path 3 ==' + path)
        try:
            md_chunks_json = open(path)
            data = json.load(md_chunks_json)
        except Exception as e:
            traceback.print_exc()
            raise Exception("Unable read file because of following error::{}".format(e))
        return jsonify(data)

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordiante resources
    def post(self, chassis, memory_domain, md_chunks):
        logging.info('MDChunksAPI PUT called')
        try:
            global config
            global foo

            wildcards = {'c_id':chassis,'n_id': memory_domain, 'p_id': md_chunks, 'rb': g.rest_base}
            config=get_MDChunks_instance(wildcards)

            members.append(config)
            member_ids.append({'@odata.id': config['@odata.id']})

            # Create instances of subordinate resources, then call put operation
            # not implemented yet

            path = create_path(self.root, self.chassis, chassis, self.memory_domains, memory_domain, self.md_chunks, md_chunks)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                # This will execute when POST is called for more than one time for a resource
                return config, 500
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))


            # update the collection json file with new added resource
            collection_path = os.path.join(self.root, self.chassis, chassis, self.memory_domains, memory_domain, self.md_chunks, 'index.json')
            update_collections_json(path=collection_path, link=config['@odata.id'])



            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('MDChunksAPI put exit')
        return resp
	# HTTP PATCH
    def patch(self, chassis, memory_domain, md_chunks):
        path = os.path.join(self.root, self.chassis, chassis, self.memory_domains, memory_domain, self.md_chunks, md_chunks, 'index.json')
        try:
            # Read json from file.
            with open(path, 'r') as md_chunks_json:
                data = json.load(md_chunks_json)
                md_chunks_json.close()

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
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        json_data = self.get(chassis, memory_domain, md_chunks)
        return json_data

    # HTTP DELETE
    def delete(self, chassis, memory_domain, md_chunks):

        path = os.path.join(self.root, self.chassis, chassis, self.memory_domains, memory_domain, self.md_chunks, md_chunks).replace("\\","/")
        print (path)
        delPath = path.replace('Resources','/redfish/v1')
        path2 = os.path.join(self.root, self.chassis, chassis, self.memory_domains, memory_domain, self.md_chunks, 'index.json').replace("\\","/")
        try:
            with open(path2,"r") as pdata:
                pdata = json.load(pdata)

            data = {
            "@odata.id":delPath
            }
            resp = 200
            jdata = data["@odata.id"].split('/')

            path1 = os.path.join(self.root, self.chassis, chassis, self.memory_domains, memory_domain, self.md_chunks, jdata[len(jdata)-1])

            shutil.rmtree(path1)
            pdata['Members'].remove(data)
            pdata['Members@odata.count'] = int(pdata['Members@odata.count']) - 1

            with open(path2,"w") as jdata:
                json.dump(pdata,jdata)


        except Exception as e:
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(resp)


# MDChunks Collection API
class MDChunksCollectionAPI(Resource):

    def __init__(self):
        logging.info('MDChunksCollectionAPI init called')
        self.root = PATHS['Root']
        self.chassis = PATHS['Chassis']['path']
        self.memory_domains = PATHS['Chassis']['memory_domains']
        self.md_chunks = PATHS['Chassis']['md_chunks']

    def get(self, chassis, memory_domain):
        path = os.path.join(self.root, self.chassis, chassis, self.memory_domains, memory_domain, self.md_chunks, 'index.json')
        logging.info('Path 1 ==' + path)
        try:
            storage_controller_json = open(path)
            data = json.load(storage_controller_json)
        except Exception as e:
            traceback.print_exc()
            return {"error": "Unable read file because of following error::{}".format(e)}, 500

        return jsonify(data)

    def verify(self, config):
        # TODO: Implement a method to verify that the POST body is valid
        return True,{}

    # HTTP POST
    # POST should allow adding multiple instances to a collection.
    # For now, this only adds one instance.
    # TODO: 'id' should be obtained from the request data.
    def post(self, chassis, memory_domain):
        logging.info('MDChunksCollectionAPI POST called')
        try:
            config = request.get_json(force=True)
            ok, msg = self.verify(config)
            if ok:
                # Save the new singleton
                singleton_name = os.path.basename(config['@odata.id'])
                path = os.path.join(self.root, self.chassis, chassis, self.memory_domains, memory_domain, self.md_chunks, singleton_name)
                if not os.path.exists(path):
                    os.mkdir(path)
                with open(os.path.join(path, "index.json"), "w") as fd:
                    fd.write(json.dumps(config, indent=4, sort_keys=True))
                # Update the collection
                collection_path = os.path.join(self.root, self.chassis, chassis, self.memory_domains, memory_domain, self.md_chunks, 'index.json')
                update_collections_json(collection_path, config['@odata.id'])
                # Return a copy of the new singleton with a Created response
                resp = config, 201
            else:
                resp = msg, 400
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        return resp


class CreateMDChunk (Resource):
    def __init__(self):
        self.root = PATHS['Root']
        self.chassis = PATHS['Chassis']['path']
        self.memory_domains = PATHS['Chassis']['memory_domains']
        self.md_chunks = PATHS['Chassis']['md_chunks']

    # Attach APIs for subordinate resource(s). Attach the APIs for a resource collection and its singletons
    def put(self,chassis, memory_domain):
        logging.info('CreateMDChunk put started.')
        try:
            path = create_path(self.root, self.chassis, chassis, self.memory_domains, memory_domain, self.md_chunks)
            logging.info('Path 2 ==' + path)
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                logging.info('The given path : {} already Exist.'.format(path))
            config={
                      "@Redfish.Copyright": "Copyright 2015-2021 SNIA. All rights reserved.",
                      "@odata.type": "#PortCollection.PortCollection",
                      "Name": "Port Collection",
                      "Members@odata.count": 0,
                      "Members": [
                      ],
                      "Permissions": [
                                {"Read": "True"},
                                {"Write": "True"}]
                    }
            with open(os.path.join(path, "index.json"), "w") as fd:
                fd.write(json.dumps(config, indent=4, sort_keys=True))

            resp = config, 200
        except Exception:
            traceback.print_exc()
            resp = INTERNAL_ERROR
        logging.info('CreateMDChunk put exit.')
        return resp
