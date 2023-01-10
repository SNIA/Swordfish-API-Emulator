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

# Resource implementation for - /redfish/v1/SessionService/Sessions/{SessionId}
# Program name - Session_api.py

import copy
from datetime import timedelta
from email import message
import json
import string

import requests
from api_emulator.account_service import AccountService
from api_emulator.redfish.templates.Session import get_Session_instance
import g
import os
import traceback
import logging
import random

from flask import Flask, request, jsonify, session, Response
import jwt
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, get_sessionValidation_error, update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection

members = []
member_ids = []
INTERNAL_ERROR = 500

# Session Collection API
class SessionCollectionAPI(Resource):
	def __init__(self, **kwargs):
		logging.info('Session Collection init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self):
		logging.info('Session Collection get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = os.path.join(self.root, 'SessionService/Sessions', 'index.json')
			return get_json_data(path)
		else:
			return msg, code

	# HTTP POST
	def post(self):
		logging.info('Session Collection post called')

		if request.data:
				config = json.loads(request.data)
				if "@odata.type" in config:
					if "Collection" in config["@odata.type"]:
						return "Invalid data in POST body", 400

		path = create_path(self.root, 'SessionService/Sessions')
		parent_path = os.path.dirname(path)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'Session', parent_path)
		
		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				print("Session Object : "+config['@odata.id'])
				return SessionAPI.post(self, os.path.basename(config['@odata.id']))
			else:
				print("Session Object : "+str(res))
				return SessionAPI.post(self, str(res))
		else:
			print("Session Object : "+str(res))
			return SessionAPI.post(self, str(res))

	# HTTP PUT
	def put(self):
		logging.info('Session Collection put called')
		return 'PUT is not a supported command for SessionCollectionAPI', 405

	# HTTP PATCH
	def patch(self):
		logging.info('Session Collection patch called')
		return 'PATCH is not a supported command for SessionCollectionAPI', 405

	# HTTP DELETE
	def delete(self):
		logging.info('Session Collection delete called')
		return 'DELETE is not a supported command for SessionCollectionAPI', 405


# Session API
class SessionAPI(Resource):
	def __init__(self, **kwargs):
		logging.info('Session init called')
		self.root = PATHS['Root']
		self.auth = kwargs['auth']

	# HTTP GET
	def get(self, SessionId):
		logging.info('Session get called')
		msg, code = check_authentication(self.auth)

		if code == 200:
			path = create_path(self.root, 'SessionService/Sessions/{0}', 'index.json').format(SessionId)
			return get_json_data(path)
		else:
			return msg, code


	# HTTP POST
	def post(self, SessionId):
		logging.info('Session post called')
		sessionService_path = os.path.join(self.root, 'SessionService', 'index.json')
		json_data = open(sessionService_path)
		data = json.load(json_data)
		sessionTimeout = data['SessionTimeout']

		path = create_path(self.root, 'SessionService/Sessions/{0}').format(SessionId)
		collection_path = os.path.join(self.root, 'SessionService/Sessions', 'index.json')

		# Check if collection exists:
		if not os.path.exists(collection_path):
			# SessionCollectionAPI.post(self)
			c_path = create_path(self.root, 'SessionService/Sessions')
			parent_path = os.path.dirname(c_path)
			os.mkdir(c_path)
			create_collection (c_path, 'Session', parent_path)

		if SessionId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'SessionId':SessionId, 'rb':g.rest_base}
			config=get_Session_instance(wildcards)

			if request.data:
				request_data = json.loads(request.data)
        		# Update the keys of payload in json file.
				for key, value in request_data.items():
					config[key] = value
			
			members.append(config)
			member_ids.append({'@odata.id': config['@odata.id']})

			config['Name'] = config['UserName'] + " " + "Session"

			username = config['UserName']
			password = config['Password']

			if not username or not password:
				return "The authentication credentials are missing", 401
			else:
				as_obj = AccountService()
				actual_password = as_obj.getPassword(username)
				if actual_password == None:
					return "Forbidden...Incorrect username, 403", 403
				elif actual_password != password:
					return "Forbidden...Incorrect password, 403", 403
				else:
					pass

			if not os.path.exists(path):
				os.mkdir(path)
			else:
        		# This will execute when POST is called for more than one time for a resource
				return "A creation request could not be completed because of conflict, 409", 409
			with open(os.path.join(path, "index.json"), "w") as fd:
				data = copy.deepcopy(config)
				del data['Password']
				fd.write(json.dumps(data, indent=4, sort_keys=True))
			
			g.app.permanent_session_lifetime = timedelta(seconds=sessionTimeout)
			session['UserName'] = config['UserName']
			print(session.get('UserName'))
			print("Session has been started with timeout : "+str(sessionTimeout))

    		# update the collection json file with new added resource
			update_collections_json(path=collection_path, link=config['@odata.id'])

			resp = config, 201

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('SessionAPI POST exit')
		return resp

	# HTTP PUT
	def put(self, SessionId):
		logging.info('Session put called')
		return 'PUT is not a supported command for SessionAPI', 405

	# HTTP PATCH
	def patch(self, SessionId):
		logging.info('Session patch called')
		return 'PATCH is not a supported command for SessionAPI', 405

	# HTTP DELETE
	def delete(self, SessionId):
		logging.info('Session delete called')
		print("Deleting object : "+SessionId)
		msg, code = check_authentication(self.auth)

		if code == 200:
			if session.get('UserName'):
				session.pop('UserName', None)
				print("Session Deleted")

			path = create_path(self.root, 'SessionService/Sessions/{0}').format(SessionId)
			base_path = create_path(self.root, 'SessionService/Sessions')
			return delete_object(path, base_path)
		else:
			return msg, code
