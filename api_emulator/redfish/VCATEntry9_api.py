#
# Copyright (c) 2017-2024, The Storage Networking Industry Association.
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

# Resource implementation for - /redfish/v1/ResourceBlocks/{ResourceBlockId}/Systems/{SystemId}/FabricAdapters/{FabricAdapterId}/RSP-VCAT/{VCATEntryId}
# Program name - VCATEntry9_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, create_collection
from .templates.VCATEntry9 import get_VCATEntry9_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# VCATEntry9 Collection API
class VCATEntry9CollectionAPI(Resource):
	def __init__(self, **kwargs):
		logging.info('VCATEntry9 Collection init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, ResourceBlockId, SystemId, FabricAdapterId):
		logging.info('VCATEntry9 Collection get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/RSP-VCAT', 'index.json').format(ResourceBlockId, SystemId, FabricAdapterId)
			return get_json_data(path)
		else:
			return msg, code

	# HTTP POST Collection
	def post(self, ResourceBlockId, SystemId, FabricAdapterId):
		logging.info('VCATEntry9 Collection post called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			if request.data:
				config = json.loads(request.data)
				if "@odata.type" in config:
					if "Collection" in config["@odata.type"]:
						return "Invalid data in POST body", 400

			if FabricAdapterId in members:
				resp = 404
				return resp
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/RSP-VCAT').format(ResourceBlockId, SystemId, FabricAdapterId)
			parent_path = os.path.dirname(path)
			if not os.path.exists(path):
				os.mkdir(path)
				create_collection (path, 'VCATEntry', parent_path)

			res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
			if request.data:
				config = json.loads(request.data)
				if "@odata.id" in config:
					return VCATEntry9API.post(self, ResourceBlockId, SystemId, FabricAdapterId, os.path.basename(config['@odata.id']))
				else:
					return VCATEntry9API.post(self, ResourceBlockId, SystemId, FabricAdapterId, str(res))
			else:
				return VCATEntry9API.post(self, ResourceBlockId, SystemId, FabricAdapterId, str(res))
		else:
			return msg, code

# VCATEntry9 API
class VCATEntry9API(Resource):
	def __init__(self, **kwargs):
		logging.info('VCATEntry9 init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, ResourceBlockId, SystemId, FabricAdapterId, VCATEntryId):
		logging.info('VCATEntry9 get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/RSP-VCAT/{3}', 'index.json').format(ResourceBlockId, SystemId, FabricAdapterId, VCATEntryId)
			return get_json_data (path)
		else:
			return msg, code

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ResourceBlockId, SystemId, FabricAdapterId, VCATEntryId):
		logging.info('VCATEntry9 post called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/RSP-VCAT/{3}').format(ResourceBlockId, SystemId, FabricAdapterId, VCATEntryId)
			collection_path = os.path.join(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/RSP-VCAT', 'index.json').format(ResourceBlockId, SystemId, FabricAdapterId)

			# Check if collection exists:
			if not os.path.exists(collection_path):
				VCATEntry9CollectionAPI.post(self, ResourceBlockId, SystemId, FabricAdapterId)

			if VCATEntryId in members:
				resp = 404
				return resp
			try:
				global config
				wildcards = {'ResourceBlockId':ResourceBlockId, 'SystemId':SystemId, 'FabricAdapterId':FabricAdapterId, 'VCATEntryId':VCATEntryId, 'rb':g.rest_base}
				config=get_VCATEntry9_instance(wildcards)
				config = create_and_patch_object (config, members, member_ids, path, collection_path)
				resp = config, 200

			except Exception:
				traceback.print_exc()
				resp = INTERNAL_ERROR
			logging.info('VCATEntry9API POST exit')
			return resp
		else:
			return msg, code

	# HTTP PUT
	def put(self, ResourceBlockId, SystemId, FabricAdapterId, VCATEntryId):
		logging.info('VCATEntry9 put called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/RSP-VCAT/{3}', 'index.json').format(ResourceBlockId, SystemId, FabricAdapterId, VCATEntryId)
			put_object(path)
			return self.get(ResourceBlockId, SystemId, FabricAdapterId, VCATEntryId)
		else:
			return msg, code

	# HTTP PATCH
	def patch(self, ResourceBlockId, SystemId, FabricAdapterId, VCATEntryId):
		logging.info('VCATEntry9 patch called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/RSP-VCAT/{3}', 'index.json').format(ResourceBlockId, SystemId, FabricAdapterId, VCATEntryId)
			patch_object(path)
			return self.get(ResourceBlockId, SystemId, FabricAdapterId, VCATEntryId)
		else:
			return msg, code

	# HTTP DELETE
	def delete(self, ResourceBlockId, SystemId, FabricAdapterId, VCATEntryId):
		logging.info('VCATEntry9 delete called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/RSP-VCAT/{3}').format(ResourceBlockId, SystemId, FabricAdapterId, VCATEntryId)
			base_path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/RSP-VCAT').format(ResourceBlockId, SystemId, FabricAdapterId)
			return delete_object(path, base_path)
		else:
			return msg, code

