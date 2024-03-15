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

# Resource implementation for - /redfish/v1/Chassis/{ChassisId}/FabricAdapters/{FabricAdapterId}/Ports/{PortId}/GenZ/VCAT/{VCATEntryId}
# Program name - VCATEntry23_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, create_collection
from .templates.VCATEntry23 import get_VCATEntry23_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# VCATEntry23 Collection API
class VCATEntry23CollectionAPI(Resource):
	def __init__(self, **kwargs):
		logging.info('VCATEntry23 Collection init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, ChassisId, FabricAdapterId, PortId):
		logging.info('VCATEntry23 Collection get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'Chassis/{0}/FabricAdapters/{1}/Ports/{2}/GenZ/VCAT', 'index.json').format(ChassisId, FabricAdapterId, PortId)
			return get_json_data(path)
		else:
			return msg, code

	# HTTP POST Collection
	def post(self, ChassisId, FabricAdapterId, PortId):
		logging.info('VCATEntry23 Collection post called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			if request.data:
				config = json.loads(request.data)
				if "@odata.type" in config:
					if "Collection" in config["@odata.type"]:
						return "Invalid data in POST body", 400

			if PortId in members:
				resp = 404
				return resp
			path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/Ports/{2}/GenZ/VCAT').format(ChassisId, FabricAdapterId, PortId)
			parent_path = os.path.dirname(path)
			if not os.path.exists(path):
				os.mkdir(path)
				create_collection (path, 'VCATEntry', parent_path)

			res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
			if request.data:
				config = json.loads(request.data)
				if "@odata.id" in config:
					return VCATEntry23API.post(self, ChassisId, FabricAdapterId, PortId, os.path.basename(config['@odata.id']))
				else:
					return VCATEntry23API.post(self, ChassisId, FabricAdapterId, PortId, str(res))
			else:
				return VCATEntry23API.post(self, ChassisId, FabricAdapterId, PortId, str(res))
		else:
			return msg, code

# VCATEntry23 API
class VCATEntry23API(Resource):
	def __init__(self, **kwargs):
		logging.info('VCATEntry23 init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, ChassisId, FabricAdapterId, PortId, VCATEntryId):
		logging.info('VCATEntry23 get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/Ports/{2}/GenZ/VCAT/{3}', 'index.json').format(ChassisId, FabricAdapterId, PortId, VCATEntryId)
			return get_json_data (path)
		else:
			return msg, code

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ChassisId, FabricAdapterId, PortId, VCATEntryId):
		logging.info('VCATEntry23 post called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/Ports/{2}/GenZ/VCAT/{3}').format(ChassisId, FabricAdapterId, PortId, VCATEntryId)
			collection_path = os.path.join(self.root, 'Chassis/{0}/FabricAdapters/{1}/Ports/{2}/GenZ/VCAT', 'index.json').format(ChassisId, FabricAdapterId, PortId)

			# Check if collection exists:
			if not os.path.exists(collection_path):
				VCATEntry23CollectionAPI.post(self, ChassisId, FabricAdapterId, PortId)

			if VCATEntryId in members:
				resp = 404
				return resp
			try:
				global config
				wildcards = {'ChassisId':ChassisId, 'FabricAdapterId':FabricAdapterId, 'PortId':PortId, 'VCATEntryId':VCATEntryId, 'rb':g.rest_base}
				config=get_VCATEntry23_instance(wildcards)
				config = create_and_patch_object (config, members, member_ids, path, collection_path)
				resp = config, 200

			except Exception:
				traceback.print_exc()
				resp = INTERNAL_ERROR
			logging.info('VCATEntry23API POST exit')
			return resp
		else:
			return msg, code

	# HTTP PUT
	def put(self, ChassisId, FabricAdapterId, PortId, VCATEntryId):
		logging.info('VCATEntry23 put called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'Chassis/{0}/FabricAdapters/{1}/Ports/{2}/GenZ/VCAT/{3}', 'index.json').format(ChassisId, FabricAdapterId, PortId, VCATEntryId)
			put_object(path)
			return self.get(ChassisId, FabricAdapterId, PortId, VCATEntryId)
		else:
			return msg, code

	# HTTP PATCH
	def patch(self, ChassisId, FabricAdapterId, PortId, VCATEntryId):
		logging.info('VCATEntry23 patch called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'Chassis/{0}/FabricAdapters/{1}/Ports/{2}/GenZ/VCAT/{3}', 'index.json').format(ChassisId, FabricAdapterId, PortId, VCATEntryId)
			patch_object(path)
			return self.get(ChassisId, FabricAdapterId, PortId, VCATEntryId)
		else:
			return msg, code

	# HTTP DELETE
	def delete(self, ChassisId, FabricAdapterId, PortId, VCATEntryId):
		logging.info('VCATEntry23 delete called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/Ports/{2}/GenZ/VCAT/{3}').format(ChassisId, FabricAdapterId, PortId, VCATEntryId)
			base_path = create_path(self.root, 'Chassis/{0}/FabricAdapters/{1}/Ports/{2}/GenZ/VCAT').format(ChassisId, FabricAdapterId, PortId)
			return delete_object(path, base_path)
		else:
			return msg, code

