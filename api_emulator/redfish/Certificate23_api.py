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

# Resource implementation for - /redfish/v1/ResourceBlocks/{ResourceBlockId}/Systems/{ComputerSystemId}/Certificates/{CertificateId}
# Program name - Certificate23_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, create_collection, send_event
from .templates.Certificate23 import get_Certificate23_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Certificate23 Collection API
class Certificate23CollectionAPI(Resource):
	def __init__(self, **kwargs):
		logging.info('Certificate23 Collection init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, ResourceBlockId, ComputerSystemId):
		logging.info('Certificate23 Collection get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Certificates', 'index.json').format(ResourceBlockId, ComputerSystemId)
			return get_json_data(path)
		else:
			return msg, code

	# HTTP POST Collection
	def post(self, ResourceBlockId, ComputerSystemId):
		logging.info('Certificate23 Collection post called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			if request.data:
				config = json.loads(request.data)
				if "@odata.type" in config:
					if "Collection" in config["@odata.type"]:
						return "Invalid data in POST body", 400

			if ComputerSystemId in members:
				resp = 404
				return resp
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Certificates').format(ResourceBlockId, ComputerSystemId)
			parent_path = os.path.dirname(path)
			if not os.path.exists(path):
				os.mkdir(path)
				create_collection (path, 'Certificate', parent_path)

			res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
			if request.data:
				config = json.loads(request.data)
				if "@odata.id" in config:
					return Certificate23API.post(self, ResourceBlockId, ComputerSystemId, os.path.basename(config['@odata.id']))
				else:
					return Certificate23API.post(self, ResourceBlockId, ComputerSystemId, str(res))
			else:
				return Certificate23API.post(self, ResourceBlockId, ComputerSystemId, str(res))
		else:
			return msg, code

# Certificate23 API
class Certificate23API(Resource):
	def __init__(self, **kwargs):
		logging.info('Certificate23 init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, ResourceBlockId, ComputerSystemId, CertificateId):
		logging.info('Certificate23 get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Certificates/{2}', 'index.json').format(ResourceBlockId, ComputerSystemId, CertificateId)
			return get_json_data (path)
		else:
			return msg, code

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ResourceBlockId, ComputerSystemId, CertificateId):
		logging.info('Certificate23 post called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Certificates/{2}').format(ResourceBlockId, ComputerSystemId, CertificateId)
			redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Systems/{1}/Certificates/{2}').format(ResourceBlockId, ComputerSystemId, CertificateId)
			collection_path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Certificates', 'index.json').format(ResourceBlockId, ComputerSystemId)

			# Check if collection exists:
			if not os.path.exists(collection_path):
				Certificate23CollectionAPI.post(self, ResourceBlockId, ComputerSystemId)

			if CertificateId in members:
				resp = 404
				return resp
			try:
				global config
				wildcards = {'ResourceBlockId':ResourceBlockId, 'ComputerSystemId':ComputerSystemId, 'CertificateId':CertificateId, 'rb':g.rest_base}
				config=get_Certificate23_instance(wildcards)
				config = create_and_patch_object (config, members, member_ids, path, collection_path)
				resp = config, 200

				# Send ResourceCreated event with payload
				send_event("ResourceCreated","ResourceEvent.1.4.2.ResourceCreated", "The resource was created successfully.", "OK", redfish_path)
			except Exception:
				traceback.print_exc()
				resp = INTERNAL_ERROR
			logging.info('Certificate23API POST exit')
			return resp
		else:
			return msg, code

	# HTTP PUT
	def put(self, ResourceBlockId, ComputerSystemId, CertificateId):
		logging.info('Certificate23 put called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Certificates/{2}', 'index.json').format(ResourceBlockId, ComputerSystemId, CertificateId)
			redfish_path = create_path('/redfish/v1', 'ResourceBlocks/{0}/Systems/{1}/Certificates/{2}', 'index.json').format(ResourceBlockId, ComputerSystemId, CertificateId)
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
			return self.get(ResourceBlockId, ComputerSystemId, CertificateId)
		else:
			return msg, code

	# HTTP PATCH
	def patch(self, ResourceBlockId, ComputerSystemId, CertificateId):
		logging.info('Certificate23 patch called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Certificates/{2}', 'index.json').format(ResourceBlockId, ComputerSystemId, CertificateId)
			redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Systems/{1}/Certificates/{2}', 'index.json').format(ResourceBlockId, ComputerSystemId, CertificateId)
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
			return self.get(ResourceBlockId, ComputerSystemId, CertificateId)
		else:
			return msg, code

	# HTTP DELETE
	def delete(self, ResourceBlockId, ComputerSystemId, CertificateId):
		logging.info('Certificate23 delete called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Certificates/{2}').format(ResourceBlockId, ComputerSystemId, CertificateId)
			redfish_path = create_path('/redfish/v1/', 'ResourceBlocks/{0}/Systems/{1}/Certificates/{2}').format(ResourceBlockId, ComputerSystemId, CertificateId)
			base_path = create_path(self.root, 'ResourceBlocks/{0}/Systems/{1}/Certificates').format(ResourceBlockId, ComputerSystemId)
			# Event logic for DELETE
			obj = get_json_data(path)
			delete_object(path, base_path)
			send_event("ResourceRemoved", "ResourceEvent.1.4.2.ResourceRemoved", "The resource was removed successfully.", "OK", redfish_path)
			return '', 204
		else:
			return msg, code

