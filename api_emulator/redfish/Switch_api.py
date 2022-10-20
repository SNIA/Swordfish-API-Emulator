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

# Resource implementation for - /redfish/v1/Fabrics/{FabricId}/Switches/{SwitchId}
# Program name - Switch_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Switch import get_Switch_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Switch Collection API
class SwitchCollectionAPI(Resource):
	def __init__(self):
		logging.info('Switch Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, FabricId):
		logging.info('Switch Collection get called')
		path = os.path.join(self.root, 'Fabrics/{0}/Switches', 'index.json').format(FabricId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, FabricId):
		logging.info('Switch Collection post called')

		if FabricId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Fabrics/{0}/Switches').format(FabricId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'Switch')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return SwitchAPI.post(self, os.path.basename(config['@odata.id']))
			else:
				return SwitchAPI.post(self, str(res))
		else:
			return SwitchAPI.post(self, str(res))

	# HTTP PUT Collection
	def put(self, FabricId):
		logging.info('Switch Collection put called')

		path = os.path.join(self.root, 'Fabrics/{0}/Switches', 'index.json').format(FabricId)
		put_object (path)
		return self.get(FabricId)

# Switch API
class SwitchAPI(Resource):
	def __init__(self):
		logging.info('Switch init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, FabricId, SwitchId):
		logging.info('Switch get called')
		path = create_path(self.root, 'Fabrics/{0}/Switches/{1}', 'index.json').format(FabricId, SwitchId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, FabricId, SwitchId):
		logging.info('Switch post called')
		path = create_path(self.root, 'Fabrics/{0}/Switches/{1}').format(FabricId, SwitchId)
		collection_path = os.path.join(self.root, 'Fabrics/{0}/Switches', 'index.json').format(FabricId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			SwitchCollectionAPI.post(self, FabricId)

		if SwitchId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'FabricId':FabricId, 'SwitchId':SwitchId, 'rb':g.rest_base}
			config=get_Switch_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('SwitchAPI POST exit')
		return resp

	# HTTP PUT
	def put(self, FabricId, SwitchId):
		logging.info('Switch put called')
		path = create_path(self.root, 'Fabrics/{0}/Switches/{1}', 'index.json').format(FabricId, SwitchId)
		put_object(path)
		return self.get(FabricId, SwitchId)

	# HTTP PATCH
	def patch(self, FabricId, SwitchId):
		logging.info('Switch patch called')
		path = create_path(self.root, 'Fabrics/{0}/Switches/{1}', 'index.json').format(FabricId, SwitchId)
		patch_object(path)
		return self.get(FabricId, SwitchId)

	# HTTP DELETE
	def delete(self, FabricId, SwitchId):
		logging.info('Switch delete called')
		path = create_path(self.root, 'Fabrics/{0}/Switches/{1}').format(FabricId, SwitchId)
		base_path = create_path(self.root, 'Fabrics/{0}/Switches').format(FabricId)
		return delete_object(path, base_path)

