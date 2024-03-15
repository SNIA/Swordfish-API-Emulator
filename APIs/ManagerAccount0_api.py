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

# Resource implementation for - /redfish/v1/AccountService/Accounts/{ManagerAccountId}
# Program name - ManagerAccount0_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, create_collection
from .templates.ManagerAccount0 import get_ManagerAccount0_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# ManagerAccount0 Collection API
class ManagerAccount0CollectionAPI(Resource):
	def __init__(self, **kwargs):
		logging.info('ManagerAccount0 Collection init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self):
		logging.info('ManagerAccount0 Collection get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'AccountService/Accounts', 'index.json')
			return get_json_data(path)
		else:
			return msg, code

	# HTTP POST Collection
	def post(self):
		logging.info('ManagerAccount0 Collection post called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			if request.data:
				config = json.loads(request.data)
				if "@odata.type" in config:
					if "Collection" in config["@odata.type"]:
						return "Invalid data in POST body", 400

			path = create_path(self.root, 'AccountService/Accounts')
			parent_path = os.path.dirname(path)
			if not os.path.exists(path):
				os.mkdir(path)
				create_collection (path, 'ManagerAccount', parent_path)

			res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
			if request.data:
				config = json.loads(request.data)
				if "@odata.id" in config:
					return ManagerAccount0API.post(self, os.path.basename(config['@odata.id']))
				else:
					return ManagerAccount0API.post(self, str(res))
			else:
				return ManagerAccount0API.post(self, str(res))
		else:
			return msg, code

# ManagerAccount0 API
class ManagerAccount0API(Resource):
	def __init__(self, **kwargs):
		logging.info('ManagerAccount0 init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, ManagerAccountId):
		logging.info('ManagerAccount0 get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'AccountService/Accounts/{0}', 'index.json').format(ManagerAccountId)
			return get_json_data (path)
		else:
			return msg, code

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, ManagerAccountId):
		logging.info('ManagerAccount0 post called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'AccountService/Accounts/{0}').format(ManagerAccountId)
			collection_path = os.path.join(self.root, 'AccountService/Accounts', 'index.json')

			# Check if collection exists:
			if not os.path.exists(collection_path):
				ManagerAccount0CollectionAPI.post(self)

			if ManagerAccountId in members:
				resp = 404
				return resp
			try:
				global config
				wildcards = {'ManagerAccountId':ManagerAccountId, 'rb':g.rest_base}
				config=get_ManagerAccount0_instance(wildcards)
				config = create_and_patch_object (config, members, member_ids, path, collection_path)
				resp = config, 200

			except Exception:
				traceback.print_exc()
				resp = INTERNAL_ERROR
			logging.info('ManagerAccount0API POST exit')
			return resp
		else:
			return msg, code

	# HTTP PUT
	def put(self, ManagerAccountId):
		logging.info('ManagerAccount0 put called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'AccountService/Accounts/{0}', 'index.json').format(ManagerAccountId)
			put_object(path)
			return self.get(ManagerAccountId)
		else:
			return msg, code

	# HTTP PATCH
	def patch(self, ManagerAccountId):
		logging.info('ManagerAccount0 patch called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'AccountService/Accounts/{0}', 'index.json').format(ManagerAccountId)
			patch_object(path)
			return self.get(ManagerAccountId)
		else:
			return msg, code

	# HTTP DELETE
	def delete(self, ManagerAccountId):
		logging.info('ManagerAccount0 delete called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'AccountService/Accounts/{0}').format(ManagerAccountId)
			base_path = create_path(self.root, 'AccountService/Accounts')
			return delete_object(path, base_path)
		else:
			return msg, code

