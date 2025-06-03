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

# Resource implementation for - /redfish/v1/EventService/Subscriptions/{EventDestinationId}
# Program name - EventDestination_api.py

import g
import json, os, random, string
import traceback
import logging
from flask import request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, create_collection, send_event
from .templates.EventDestination import get_EventDestination_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

# Persistent storage for event subscriptions
SUBSCRIPTIONS_FILE = create_path(PATHS['Root'], 'EventService/Subscriptions', 'index.json')

def load_subscriptions():
    if os.path.exists(SUBSCRIPTIONS_FILE):
        with open(SUBSCRIPTIONS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_subscriptions(subs):
    os.makedirs(os.path.dirname(SUBSCRIPTIONS_FILE), exist_ok=True)
    with open(SUBSCRIPTIONS_FILE, 'w') as f:
        json.dump(subs, f, indent=2)

# EventDestination Collection API
class EventDestinationCollectionAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('EventDestination Collection init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self):
        logging.info('EventDestination Collection get called')
        msg, code = check_authentication(self.auth)
        if code == 200:
            path = create_path(self.root, 'EventService/Subscriptions', 'index.json')
            return get_json_data(path)
        else:
            return msg, code

    # HTTP POST Collection
    def post(self):
        logging.info('EventDestination Collection post called')
        msg, code = check_authentication(self.auth)
        if code == 200:
            config = json.loads(request.data) if request.data else {}
            if "@odata.type" in config and "Collection" in config["@odata.type"]:
                return "Invalid data in POST body", 400
            path = create_path(self.root, 'EventService/Subscriptions')
            parent_path = os.path.dirname(path)
            if not os.path.exists(path):
                os.mkdir(path)
                create_collection(path, 'EventDestination', parent_path)
            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            sub_id = os.path.basename(config.get('@odata.id', res))
            return EventDestinationAPI(auth=self.auth).post(sub_id)
        else:
            return msg, code

# EventDestination API
class EventDestinationAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('EventDestination init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self, EventDestinationId):
        logging.info('EventDestination get called')
        msg, code = check_authentication(self.auth)
        if code == 200:
            path = create_path(self.root, 'EventService/Subscriptions/{0}', 'index.json').format(EventDestinationId)
            return get_json_data(path)
        else:
            return msg, code

    # HTTP POST
    # - Create the resource (since URI variables are available)
    # - Update the members and members.id lists
    # - Attach the APIs of subordinate resources (do this only once)
    # - Finally, create an instance of the subordinate resources
    def post(self, EventDestinationId):
        logging.info('EventDestination post called')
        msg, code = check_authentication(self.auth)
        if code == 200:
            path = create_path(self.root, 'EventService/Subscriptions/{0}').format(EventDestinationId)
            redfish_path = create_path('/redfish/v1/', 'EventService/Subscriptions/{0}').format(EventDestinationId)
            collection_path = create_path(self.root, 'EventService/Subscriptions', 'index.json')
            
            # Check if collection exists:
            if not os.path.exists(collection_path):
                EventDestinationCollectionAPI().post(self)
            if EventDestinationId in members:
                return 404
            try:
                global config
                wildcards = {'EventDestinationId': EventDestinationId, 'rb': g.rest_base}
                config = get_EventDestination_instance(wildcards)
                config = create_and_patch_object(config, members, member_ids, path, collection_path)
                resp = config, 200
            except Exception:
                traceback.print_exc()
                resp = INTERNAL_ERROR
            logging.info('EventDestinationAPI POST exit')
            return resp
        else:
            return msg, code

    # HTTP PUT
    def put(self, EventDestinationId):
        logging.info('EventDestination put called')
        msg, code = check_authentication(self.auth)
        if code == 200:
            path = create_path(self.root, 'EventService/Subscriptions/{0}', 'index.json').format(EventDestinationId)
            redfish_path = create_path('/redfish/v1/', 'EventService/Subscriptions/{0}', 'index.json').format(EventDestinationId)
            put_object(path)
            # Update subscription
            subs = load_subscriptions()
            if EventDestinationId in subs:
                subs[EventDestinationId].update(json.loads(request.data))
                save_subscriptions(subs)
            # Redfish Event: ResourceChanged
            send_event(
                "ResourceChanged",
                "ResourceChanged",
                f"EventDestination {EventDestinationId} changed",
                "OK",
                path,
                subs[EventDestinationId] if EventDestinationId in subs else None
            )
            return self.get(EventDestinationId)
        else:
            return msg, code

    # HTTP PATCH
    def patch(self, EventDestinationId):
        logging.info('EventDestination patch called')
        msg, code = check_authentication(self.auth)
        if code == 200:
            path = create_path(self.root, 'EventService/Subscriptions/{0}', 'index.json').format(EventDestinationId)
            redfish_path = create_path('/redfish/v1/', 'EventService/Subscriptions/{0}', 'index.json').format(EventDestinationId)
            patch_object(path)
            # Update subscription
            subs = load_subscriptions()
            if EventDestinationId in subs:
                subs[EventDestinationId].update(json.loads(request.data))
                save_subscriptions(subs)
            # Redfish Event: ResourceChanged
            send_event(
                "ResourceChanged",
                "ResourceChanged",
                f"EventDestination {EventDestinationId} changed",
                "OK",
                path,
                subs[EventDestinationId] if EventDestinationId in subs else None
            )
            return self.get(EventDestinationId)
        else:
            return msg, code

    # HTTP DELETE
    def delete(self, EventDestinationId):
        logging.info('EventDestination delete called')
        msg, code = check_authentication(self.auth)
        if code == 200:
            path = create_path(self.root, 'EventService/Subscriptions/{0}').format(EventDestinationId)
            redfish_path = create_path('/redfish/v1/', 'EventService/Subscriptions/{0}').format(EventDestinationId)
            base_path = create_path(self.root, 'EventService/Subscriptions')
            # Remove subscription
            subs = load_subscriptions()
            if EventDestinationId in subs:
                del subs[EventDestinationId]
                save_subscriptions(subs)
            # Redfish Event: ResourceRemoved
            send_event(
                "ResourceRemoved",
                "ResourceRemoved",
                f"EventDestination {EventDestinationId} removed",
                "OK",
                path,
                None
            )
            return delete_object(path, base_path)
        else:
            return msg, code

# Helper for event delivery (simulate POST to subscriber destinations)
def deliver_event_to_subscribers(event):
    subs = load_subscriptions()
    for sub_id, sub in subs.items():
        dest = sub.get('Destination')
        if dest:
            # Here you would POST the event to the destination URL
            logging.info(f"Delivering event to {dest}: {event}")
            # Example: requests.post(dest, json=event)
            pass

