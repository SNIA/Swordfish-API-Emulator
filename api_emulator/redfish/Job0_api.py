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

# Resource implementation for - /redfish/v1/JobService/Jobs/{JobId}
# Program name - Job0_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection
from .templates.Job0 import get_Job0_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Job0 Collection API
class Job0CollectionAPI(Resource):
	def __init__(self):
		logging.info('Job0 Collection init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self):
		logging.info('Job0 Collection get called')
		path = os.path.join(self.root, 'JobService/Jobs', 'index.json')
		return get_json_data (path)

	# HTTP POST Collection
	def post(self):
		logging.info('Job0 Collection post called')

		path = create_path(self.root, 'JobService/Jobs')
		return create_collection (path, 'Job')

	# HTTP PUT Collection
	def put(self):
		logging.info('Job0 Collection put called')

		path = os.path.join(self.root, 'JobService/Jobs', 'index.json')
		put_object (path)
		return self.get(self.root)

# Job0 API
class Job0API(Resource):
	def __init__(self):
		logging.info('Job0 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, JobId):
		logging.info('Job0 get called')
		path = create_path(self.root, 'JobService/Jobs/{0}', 'index.json').format(JobId)
		return get_json_data (path)

	# HTTP POST
	# - Create the resource (since URI variables are available)
	# - Update the members and members.id lists
	# - Attach the APIs of subordinate resources (do this only once)
	# - Finally, create an instance of the subordiante resources
	def post(self, JobId):
		logging.info('Job0 post called')
		path = create_path(self.root, 'JobService/Jobs/{0}').format(JobId)
		collection_path = os.path.join(self.root, 'JobService/Jobs', 'index.json')

		# Check if collection exists:
		if not os.path.exists(collection_path):
			Job0CollectionAPI.post(self)

		if JobId in members:
			resp = 404
			return resp
		try:
			global config
			wildcards = {'JobId':JobId, 'rb':g.rest_base}
			config=get_Job0_instance(wildcards)
			config = create_and_patch_object (config, members, member_ids, path, collection_path)
			resp = config, 200

		except Exception:
			traceback.print_exc()
			resp = INTERNAL_ERROR
		logging.info('Job0API POST exit')
		return resp

	# HTTP PUT
	def put(self, JobId):
		logging.info('Job0 put called')
		path = os.path.join(self.root, 'JobService/Jobs/{0}', 'index.json').format(JobId)
		put_object(path)
		return self.get(JobId)

	# HTTP PATCH
	def patch(self, JobId):
		logging.info('Job0 patch called')
		path = os.path.join(self.root, 'JobService/Jobs/{0}', 'index.json').format(JobId)
		patch_object(path)
		return self.get(JobId)

	# HTTP DELETE
	def delete(self, JobId):
		logging.info('Job0 delete called')
		path = create_path(self.root, 'JobService/Jobs/{0}').format(JobId)
		base_path = create_path(self.root, 'JobService/Jobs')
		return delete_object(path, base_path)

