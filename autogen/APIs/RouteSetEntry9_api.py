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

# Resource implementation for - /redfish/v1/Systems/{ComputerSystemId}/FabricAdapters/{FabricAdapterId}/Ports/{PortId}/MPRT/{MPRTId}/RouteSet/{RouteId}
# Program name - RouteSetEntry9_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.RouteSetEntry9 import get_RouteSetEntry9_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# RouteSetEntry9 Collection API
class RouteSetEntry9CollectionAPI(Resource):
	def __init__(self):
		logging.info('RouteSetEntry9 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ComputerSystemId, FabricAdapterId, PortId, MPRTId):
		logging.info('RouteSetEntry9 Collection get called')
		path = os.path.join(self.root, 'Systems/{0}/FabricAdapters/{1}/Ports/{2}/MPRT/{3}/RouteSet', 'index.json').format(ComputerSystemId, FabricAdapterId, PortId, MPRTId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ComputerSystemId, FabricAdapterId, PortId, MPRTId):
		logging.info('RouteSetEntry9 Collection post called')

		if MPRTId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Systems/{0}/FabricAdapters/{1}/Ports/{2}/MPRT/{3}/RouteSet').format(ComputerSystemId, FabricAdapterId, PortId, MPRTId)
		return create_collection (path, 'RouteSetEntry')

	# HTTP PUT Collection
	def put(self, ComputerSystemId, FabricAdapterId, PortId, MPRTId):
		logging.info('RouteSetEntry9 Collection put called')

		path = os.path.join(self.root, 'Systems/{0}/FabricAdapters/{1}/Ports/{2}/MPRT/{3}/RouteSet', 'index.json').format(ComputerSystemId, FabricAdapterId, PortId, MPRTId)
		put_object (path)
		return self.get(ComputerSystemId)

# RouteSetEntry9 API
class RouteSetEntry9API(Resource):
	def __init__(self):
		logging.info('RouteSetEntry9 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ComputerSystemId, FabricAdapterId, PortId, MPRTId, RouteId):
		logging.info('RouteSetEntry9 get called')
		path = create_path(self.root, 'Systems/{0}/FabricAdapters/{1}/Ports/{2}/MPRT/{3}/RouteSet/{4}', 'index.json').format(ComputerSystemId, FabricAdapterId, PortId, MPRTId, RouteId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ComputerSystemId, FabricAdapterId, PortId, MPRTId, RouteId):
		logging.info('RouteSetEntry9 post called')
		path = create_path(self.root, 'Systems/{0}/FabricAdapters/{1}/Ports/{2}/MPRT/{3}/RouteSet/{4}').format(ComputerSystemId, FabricAdapterId, PortId, MPRTId, RouteId)
		collection_path = os.path.join(self.root, 'Systems/{0}/FabricAdapters/{1}/Ports/{2}/MPRT/{3}/RouteSet', 'index.json').format(ComputerSystemId, FabricAdapterId, PortId, MPRTId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			RouteSetEntry9CollectionAPI.post(self, ComputerSystemId, FabricAdapterId, PortId, MPRTId)

		if RouteId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ComputerSystemId':ComputerSystemId, 'FabricAdapterId':FabricAdapterId, 'PortId':PortId, 'MPRTId':MPRTId, 'RouteId':RouteId, 'rb':g.rest_base}
			config=get_RouteSetEntry9_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('RouteSetEntry9API POST exit')
		return resp

	# HTTP PUT
	def put(self, ComputerSystemId, FabricAdapterId, PortId, MPRTId, RouteId):
		logging.info('RouteSetEntry9 put called')
		path = os.path.join(self.root, 'Systems/{0}/FabricAdapters/{1}/Ports/{2}/MPRT/{3}/RouteSet/{4}', 'index.json').format(ComputerSystemId, FabricAdapterId, PortId, MPRTId, RouteId)
		put_object(path)
		return self.get(ComputerSystemId, FabricAdapterId, PortId, MPRTId, RouteId)

	# HTTP PATCH
	def patch(self, ComputerSystemId, FabricAdapterId, PortId, MPRTId, RouteId):
		logging.info('RouteSetEntry9 patch called')
		path = os.path.join(self.root, 'Systems/{0}/FabricAdapters/{1}/Ports/{2}/MPRT/{3}/RouteSet/{4}', 'index.json').format(ComputerSystemId, FabricAdapterId, PortId, MPRTId, RouteId)
		patch_object(path)
		return self.get(ComputerSystemId, FabricAdapterId, PortId, MPRTId, RouteId)

	# HTTP DELETE
	def delete(self, ComputerSystemId, FabricAdapterId, PortId, MPRTId, RouteId):
		logging.info('RouteSetEntry9 delete called')
		path = create_path(self.root, 'Systems/{0}/FabricAdapters/{1}/Ports/{2}/MPRT/{3}/RouteSet/{4}').format(ComputerSystemId, FabricAdapterId, PortId, MPRTId, RouteId)
		base_path = create_path(self.root, 'Systems/{0}/FabricAdapters/{1}/Ports/{2}/MPRT/{3}/RouteSet').format(ComputerSystemId, FabricAdapterId, PortId, MPRTId)
		return delete_object(path, base_path)

