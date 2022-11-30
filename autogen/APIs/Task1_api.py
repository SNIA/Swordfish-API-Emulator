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

# Resource implementation for - /redfish/v1/TaskService/Tasks/{TaskId}/SubTasks/{TaskId2}
# Program name - Task1_api.py

import g
import json, os, random, string
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Task1 import get_Task1_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Task1 Collection API
class Task1CollectionAPI(Resource):
	def __init__(self):
		logging.info('Task1 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, TaskId):
		logging.info('Task1 Collection get called')
		path = os.path.join(self.root, 'TaskService/Tasks/{0}/SubTasks', 'index.json').format(TaskId)
		return get_json_data (path)

	# HTTP POST Collection
	def post(self, TaskId):
		logging.info('Task1 Collection post called')

		if request.data:
			config = json.loads(request.data)
			if "@odata.type" in config:
				if "Collection" in config["@odata.type"]:
					return "Invalid data in POST body", 400

		if TaskId in members:
			resp = 404
			return resp
		path = create_path(self.root, 'TaskService/Tasks/{0}/SubTasks').format(TaskId)
		parent_path = os.path.dirname(path)
		if not os.path.exists(path):
			os.mkdir(path)
			create_collection (path, 'Task', parent_path)

		res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		if request.data:
			config = json.loads(request.data)
			if "@odata.id" in config:
				return Task1API.post(self, TaskId, os.path.basename(config['@odata.id']))
			else:
				return Task1API.post(self, TaskId, str(res))
		else:
			return Task1API.post(self, TaskId, str(res))

	# HTTP PUT Collection
	def put(self, TaskId):
		logging.info('Task1 Collection put called')

		path = os.path.join(self.root, 'TaskService/Tasks/{0}/SubTasks', 'index.json').format(TaskId)
		put_object (path)
		return self.get(TaskId)

# Task1 API
class Task1API(Resource):
	def __init__(self):
		logging.info('Task1 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, TaskId, TaskId2):
		logging.info('Task1 get called')
		path = create_path(self.root, 'TaskService/Tasks/{0}/SubTasks/{02}', 'index.json').format(TaskId, TaskId2)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, TaskId, TaskId2):
		logging.info('Task1 post called')
		path = create_path(self.root, 'TaskService/Tasks/{0}/SubTasks/{02}').format(TaskId, TaskId2)
		collection_path = os.path.join(self.root, 'TaskService/Tasks/{0}/SubTasks', 'index.json').format(TaskId)

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Task1CollectionAPI.post(self, TaskId)

		if TaskId2 in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'TaskId':TaskId, 'TaskId2':TaskId2, 'rb':g.rest_base}
			config=get_Task1_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Task1API POST exit')
		return resp

	# HTTP PUT
	def put(self, TaskId, TaskId2):
		logging.info('Task1 put called')
		path = create_path(self.root, 'TaskService/Tasks/{0}/SubTasks/{02}', 'index.json').format(TaskId, TaskId2)
		put_object(path)
		return self.get(TaskId, TaskId2)

	# HTTP PATCH
	def patch(self, TaskId, TaskId2):
		logging.info('Task1 patch called')
		path = create_path(self.root, 'TaskService/Tasks/{0}/SubTasks/{02}', 'index.json').format(TaskId, TaskId2)
		patch_object(path)
		return self.get(TaskId, TaskId2)

	# HTTP DELETE
	def delete(self, TaskId, TaskId2):
		logging.info('Task1 delete called')
		path = create_path(self.root, 'TaskService/Tasks/{0}/SubTasks/{02}').format(TaskId, TaskId2)
		base_path = create_path(self.root, 'TaskService/Tasks/{0}/SubTasks').format(TaskId)
		return delete_object(path, base_path)

