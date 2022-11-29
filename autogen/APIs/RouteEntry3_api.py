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

# Resource implementation for - /redfish/v1/Chassis/{ChassisId}/FabricAdapters/{FabricAdapterId}/MSDT/{MSDTId}
# Program name - RouteEntry3_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.RouteEntry3 import get_RouteEntry3_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# RouteEntry3 Collection API
class RouteEntry3CollectionAPI(Resource):
	def __init__(self):
		logging.info('RouteEntry3 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ChassisId, FabricAdapterId):
		logging.info('RouteEntry3 Collection get called')
		path = os.path.join(self.root, 'Chassis/{0}/FabricAdapters/{1}/MSDT', 'index.json').format(ChassisId, FabricAdapterId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ChassisId, FabricAdapterId):
		logging.info('RouteEntry3 Collection post called')

		if FabricAdapterId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/MSDT').format(ChassisId, FabricAdapterId)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'RouteEntry')

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return RouteEntry3API.post(self, ChassisId, FabricAdapterId, os.path.basename(config['@odata.id']))
			else:
				return RouteEntry3API.post(self, ChassisId, FabricAdapterId, str(res))
		else:
			return RouteEntry3API.post(self, ChassisId, FabricAdapterId, str(res))

	# HTTP PUT Collection
	def put(self, ChassisId, FabricAdapterId):
		logging.info('RouteEntry3 Collection put called')

		path = os.path.join(self.root, 'Chassis/{0}/FabricAdapters/{1}/MSDT', 'index.json').format(ChassisId, FabricAdapterId)
		put_object (path)
		return self.get(ChassisId)

# RouteEntry3 API
class RouteEntry3API(Resource):
	def __init__(self):
		logging.info('RouteEntry3 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ChassisId, FabricAdapterId, MSDTId):
		logging.info('RouteEntry3 get called')
		path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/MSDT/{2}', 'index.json').format(ChassisId, FabricAdapterId, MSDTId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ChassisId, FabricAdapterId, MSDTId):
		logging.info('RouteEntry3 post called')
		path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/MSDT/{2}').format(ChassisId, FabricAdapterId, MSDTId)
		collection_path = os.path.join(self.root, 'Chassis/{0}/FabricAdapters/{1}/MSDT', 'index.json').format(ChassisId, FabricAdapterId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			RouteEntry3CollectionAPI.post(self, ChassisId, FabricAdapterId)

		if MSDTId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ChassisId':ChassisId, 'FabricAdapterId':FabricAdapterId, 'MSDTId':MSDTId, 'rb':g.rest_base}
			config=get_RouteEntry3_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('RouteEntry3API POST exit')
		return resp

	# HTTP PUT
	def put(self, ChassisId, FabricAdapterId, MSDTId):
		logging.info('RouteEntry3 put called')
		path = os.path.join(self.root, 'Chassis/{0}/FabricAdapters/{1}/MSDT/{2}', 'index.json').format(ChassisId, FabricAdapterId, MSDTId)
		put_object(path)
		return self.get(ChassisId, FabricAdapterId, MSDTId)

	# HTTP PATCH
	def patch(self, ChassisId, FabricAdapterId, MSDTId):
		logging.info('RouteEntry3 patch called')
		path = os.path.join(self.root, 'Chassis/{0}/FabricAdapters/{1}/MSDT/{2}', 'index.json').format(ChassisId, FabricAdapterId, MSDTId)
		patch_object(path)
		return self.get(ChassisId, FabricAdapterId, MSDTId)

	# HTTP DELETE
	def delete(self, ChassisId, FabricAdapterId, MSDTId):
		logging.info('RouteEntry3 delete called')
		path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/MSDT/{2}').format(ChassisId, FabricAdapterId, MSDTId)
		base_path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/MSDT').format(ChassisId, FabricAdapterId)
		return delete_object(path, base_path)

