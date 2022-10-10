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

# Resource implementation for - /redfish/v1/Chassis/{ChassisId}/FabricAdapters/{FabricAdapterId}/RSP-VCAT/{VCATEntryId}
# Program name - VCATEntry6_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.VCATEntry6 import get_VCATEntry6_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# VCATEntry6 Collection API
class VCATEntry6CollectionAPI(Resource):
	def __init__(self):
		logging.info('VCATEntry6 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ChassisId, FabricAdapterId):
		logging.info('VCATEntry6 Collection get called')
		path = os.path.join(self.root, 'Chassis/{0}/FabricAdapters/{1}/RSP-VCAT', 'index.json').format(ChassisId, FabricAdapterId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, ChassisId, FabricAdapterId):
		logging.info('VCATEntry6 Collection post called')

		if FabricAdapterId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/RSP-VCAT').format(ChassisId, FabricAdapterId)
		return create_collection (path, 'VCATEntry')

	# HTTP PUT Collection
	def put(self, ChassisId, FabricAdapterId):
		logging.info('VCATEntry6 Collection put called')

		path = os.path.join(self.root, 'Chassis/{0}/FabricAdapters/{1}/RSP-VCAT', 'index.json').format(ChassisId, FabricAdapterId)
		put_object (path)
		return self.get(ChassisId)

# VCATEntry6 API
class VCATEntry6API(Resource):
	def __init__(self):
		logging.info('VCATEntry6 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, ChassisId, FabricAdapterId, VCATEntryId):
		logging.info('VCATEntry6 get called')
		path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/RSP-VCAT/{2}', 'index.json').format(ChassisId, FabricAdapterId, VCATEntryId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ChassisId, FabricAdapterId, VCATEntryId):
		logging.info('VCATEntry6 post called')
		path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/RSP-VCAT/{2}').format(ChassisId, FabricAdapterId, VCATEntryId)
		collection_path = os.path.join(self.root, 'Chassis/{0}/FabricAdapters/{1}/RSP-VCAT', 'index.json').format(ChassisId, FabricAdapterId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			VCATEntry6CollectionAPI.post(self, ChassisId, FabricAdapterId)

		if VCATEntryId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'ChassisId':ChassisId, 'FabricAdapterId':FabricAdapterId, 'VCATEntryId':VCATEntryId, 'rb':g.rest_base}
			config=get_VCATEntry6_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('VCATEntry6API POST exit')
		return resp

	# HTTP PUT
	def put(self, ChassisId, FabricAdapterId, VCATEntryId):
		logging.info('VCATEntry6 put called')
		path = os.path.join(self.root, 'Chassis/{0}/FabricAdapters/{1}/RSP-VCAT/{2}', 'index.json').format(ChassisId, FabricAdapterId, VCATEntryId)
		put_object(path)
		return self.get(ChassisId, FabricAdapterId, VCATEntryId)

	# HTTP PATCH
	def patch(self, ChassisId, FabricAdapterId, VCATEntryId):
		logging.info('VCATEntry6 patch called')
		path = os.path.join(self.root, 'Chassis/{0}/FabricAdapters/{1}/RSP-VCAT/{2}', 'index.json').format(ChassisId, FabricAdapterId, VCATEntryId)
		patch_object(path)
		return self.get(ChassisId, FabricAdapterId, VCATEntryId)

	# HTTP DELETE
	def delete(self, ChassisId, FabricAdapterId, VCATEntryId):
		logging.info('VCATEntry6 delete called')
		path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/RSP-VCAT/{2}').format(ChassisId, FabricAdapterId, VCATEntryId)
		base_path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/RSP-VCAT').format(ChassisId, FabricAdapterId)
		return delete_object(path, base_path)

