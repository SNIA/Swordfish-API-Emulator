#
# Copyright (c) 2017-2025, The Storage Networking Industry Association.
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

# Resource implementation for - /redfish/v1/ResourceBlocks/{ResourceBlockId}/Systems/{ComputerSystemId}/FabricAdapters/{FabricAdapterId}/SSDT/{SSDTId}
# Program name - RouteEntry15_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, create_collection, send_event
from .templates.RouteEntry15 import get_RouteEntry15_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# RouteEntry15 Collection API
class RouteEntry15CollectionAPI(Resource):
	def __init__(self, **kwargs):
		logging.info('RouteEntry15 Collection init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, ResourceBlockId, ComputerSystemId, FabricAdapterId):
		logging.info('RouteEntry15 Collection get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/SSDT', 'index.json').format(ResourceBlockId, ComputerSystemId, FabricAdapterId)
			return get_json_data(path)
		else:
			return msg, code

	# HTTP POST Collection
	def post(self, ResourceBlockId, ComputerSystemId, FabricAdapterId):
		logging.info('RouteEntry15 Collection post called')
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
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/SSDT').format(ResourceBlockId, ComputerSystemId, FabricAdapterId)
			parent_path = os.path.dirname(path)
			if not os.path.exists(path):
				os.mkdir(path)
				create_collection (path, 'RouteEntry', parent_path)

			res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
			if request.data:
				config = json.loads(request.data)
				if "@odata.id" in config:
					return RouteEntry15API.post(self, ResourceBlockId, ComputerSystemId, FabricAdapterId, os.path.basename(config['@odata.id']))
				else:
					return RouteEntry15API.post(self, ResourceBlockId, ComputerSystemId, FabricAdapterId, str(res))
			else:
				return RouteEntry15API.post(self, ResourceBlockId, ComputerSystemId, FabricAdapterId, str(res))
		else:
			return msg, code

# RouteEntry15 API
class RouteEntry15API(Resource):
	def __init__(self, **kwargs):
		logging.info('RouteEntry15 init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId):
		logging.info('RouteEntry15 get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/SSDT/{3}', 'index.json').format(ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId)
			return get_json_data (path)
		else:
			return msg, code

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId):
		logging.info('RouteEntry15 post called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/SSDT/{3}').format(ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId)
			redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/SSDT/{3}').format(ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId)
			collection_path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/SSDT', 'index.json').format(ResourceBlockId, ComputerSystemId, FabricAdapterId)

			# Check if collection exists:
			if not os.path.exists(collection_path):
				RouteEntry15CollectionAPI.post(self, ResourceBlockId, ComputerSystemId, FabricAdapterId)

			if SSDTId in members:
				resp = 404
				return resp
			try:
				global config
				wildcards = {'ResourceBlockId':ResourceBlockId, 'ComputerSystemId':ComputerSystemId, 'FabricAdapterId':FabricAdapterId, 'SSDTId':SSDTId, 'rb':g.rest_base}
				config=get_RouteEntry15_instance(wildcards)
				config = create_and_patch_object (config, members, member_ids, path, collection_path)
				resp = config, 200

				# Send ResourceCreated event with payload
				send_event("ResourceCreated","ResourceEvent.1.4.2.ResourceCreated", "The resource was created successfully.", "OK", redfish_path)
			except Exception:
				traceback.print_exc()
				resp = INTERNAL_ERROR
			logging.info('RouteEntry15API POST exit')
			return resp
		else:
			return msg, code

	# HTTP PUT
	def put(self, ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId):
		logging.info('RouteEntry15 put called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/SSDT/{3}', 'index.json').format(ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId)
			redfish_path = create_path('/redfish/v1', 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/SSDT/{3}', 'index.json').format(ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId)
			# Event logic for PUT
			old_version = None
			try:
				with open(path, 'r') as data_json:
					old_version = json.load(data_json)
			except Exception:
				old_version = {}
			health_changed_to = None
			state_changed = False
			new_state = None
			if request.data:
				new_version = json.loads(request.data)
				old_health = old_health = old_version['Status']['Health']
				new_health = new_version['Status']['Health']
				if old_health != new_health:
					health_changed_to = new_health
				old_state = old_version['Status']['State']
				new_state = new_version['Status']['State']
				if old_state != new_state:
					state_changed = True
			if old_version != new_version:
				send_event("ResourceChanged", "ResourceEvent.1.4.2.ResourceChanged", "One or more resource properties have changed.", "OK", redfish_path)
			if health_changed_to == 'OK':
				send_event("ResourceStatusChangedOK", "ResourceEvent.1.4.2.ResourceStatusChangedOK", f"The health of resource '{redfish_path}' has changed to OK.", "OK", redfish_path)
			if health_changed_to == 'Critical':
				send_event("ResourceStatusChangedCritical", "ResourceEvent.1.4.2.ResourceStatusChangedCritical", f"The health of resource '{redfish_path}' has changed to Critical.", "Critical", redfish_path)
			if health_changed_to == 'Warning':
				send_event("ResourceStatusChangedWarning", "ResourceEvent.1.4.2.ResourceStatusChangedWarning", f"The health of resource '{redfish_path}' has changed to Warning.", "Warning", redfish_path)
			if state_changed:
				send_event('ResourceStateChanged', 'ResourceEvent.1.4.2.ResourceStateChanged', f"The state of resource '{redfish_path}' has changed to {new_state}.", 'OK', redfish_path)
			put_object(path)
			return self.get(ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId)
		else:
			return msg, code

	# HTTP PATCH
	def patch(self, ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId):
		logging.info('RouteEntry15 patch called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/SSDT/{3}', 'index.json').format(ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId)
			redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/SSDT/{3}', 'index.json').format(ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId)
			# Event logic for PATCH
			if request.data:
				old_version = None
				try:
					with open(path, 'r') as data_json:
						old_version = json.load(data_json)
				except Exception:
					old_version = {}
				health_changed_to = None
				state_changed = False
				new_state = None
				new_version = json.loads(request.data)
				old_health = old_version['Status']['Health']
				new_health = new_version['Status']['Health']
				old_state = old_version['Status']['State']
				new_state = new_version['Status']['State']
				if old_version != new_version:
					send_event("ResourceChanged", "ResourceEvent.1.4.2.ResourceChanged", "One or more resource properties have changed.", "OK", redfish_path)
				if old_health != new_health:
					health_changed_to = new_health
				if old_state != new_state:
					state_changed = True
				if health_changed_to == 'OK':
					send_event("ResourceStatusChangedOK", "ResourceEvent.1.4.2.ResourceStatusChangedOK", f"The health of resource '{redfish_path}' has changed to OK.", "OK", redfish_path)
				if health_changed_to == 'Critical':
					send_event("ResourceStatusChangedCritical", "ResourceEvent.1.4.2.ResourceStatusChangedCritical", f"The health of resource '{redfish_path}' has changed to Critical.", "Critical", redfish_path)
				if health_changed_to == 'Warning':
					send_event("ResourceStatusChangedWarning", "ResourceEvent.1.4.2.ResourceStatusChangedWarning", f"The health of resource '{redfish_path}' has changed to Warning.", "Warning", redfish_path)
				if state_changed:
					send_event("ResourceStateChanged", "ResourceEvent.1.4.2.ResourceStateChanged", f"The state of resource '{redfish_path}' has changed to {new_state}.", "OK", redfish_path)
			patch_object(path)
			return self.get(ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId)
		else:
			return msg, code

	# HTTP DELETE
	def delete(self, ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId):
		logging.info('RouteEntry15 delete called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/SSDT/{3}').format(ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId)
			redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/SSDT/{3}').format(ResourceBlockId, ComputerSystemId, FabricAdapterId, SSDTId)
			base_path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/FabricAdapters/{2}/SSDT').format(ResourceBlockId, ComputerSystemId, FabricAdapterId)
			# Event logic for DELETE
			obj = get_json_data(path)
			delete_object(path, base_path)
			send_event("ResourceRemoved", "ResourceEvent.1.4.2.ResourceRemoved", "The resource was removed successfully.", "OK", redfish_path)
			return '', 204
		else:
			return msg, code

