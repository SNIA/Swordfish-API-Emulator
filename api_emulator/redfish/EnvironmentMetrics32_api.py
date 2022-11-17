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

# Resource implementation for - /redfish/v1/Facilities/{FacilityId}/AmbientMetrics
# Program name - EnvironmentMetrics32_api.py

import g
import json, os
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import update_collections_json, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, delete_collection, create_collection

config = {}

INTERNAL_ERROR = 500

# EnvironmentMetrics32 does not have a Collection API


# EnvironmentMetrics32 API
class EnvironmentMetrics32API(Resource):
	def __init__(self):
		logging.info('EnvironmentMetrics32 init called')
		self.root = PATHS['Root']

	# HTTP GET
	def get(self, FacilityId):
		logging.info('EnvironmentMetrics32 get called')
		path = create_path(self.root, 'Facilities/{0}/AmbientMetrics', 'index.json').format(FacilityId)
		return get_json_data (path)

	# HTTP POST
	def post(self, FacilityId):
		logging.info('EnvironmentMetrics32 post called')
		return 'POST is not a supported command for EnvironmentMetrics32API', 405

	# HTTP PUT
	def put(self, FacilityId):
		logging.info('EnvironmentMetrics32 put called')
		return 'PUT is not a supported command for EnvironmentMetrics32API', 405

	# HTTP PATCH
	def patch(self, FacilityId):
		logging.info('EnvironmentMetrics32 patch called')
		return 'PATCH is not a supported command for EnvironmentMetrics32API', 405

	# HTTP DELETE
	def delete(self, FacilityId):
		logging.info('EnvironmentMetrics32 delete called')
		return 'DELETE is not a supported command for EnvironmentMetrics32API', 405

