# EventService Subscriptions API implementation
import os, json, uuid
from flask import request, make_response
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, send_event, send_event

SUBSCRIPTIONS_FILE = '/tmp/redfish_event_subscriptions.json'

def load_subscriptions():
    if os.path.exists(SUBSCRIPTIONS_FILE):
        with open(SUBSCRIPTIONS_FILE) as f:
            return json.load(f)
    return []

def save_subscriptions(subs):
    with open(SUBSCRIPTIONS_FILE, 'w') as f:
        json.dump(subs, f)

class EventServiceSubscriptionsAPI(Resource):
    def __init__(self, **kwargs):
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    def get(self):
        msg, code = check_authentication(self.auth)
        if code == 200:
            return {'Members': load_subscriptions(), 'Members@odata.count': len(load_subscriptions())}, 200
        else:
            return msg, code

    def post(self):
        msg, code = check_authentication(self.auth)
        if code == 200:
            data = request.get_json(force=True)
            # TODO: Validate against EventDestination schema
            sub_id = str(uuid.uuid4())
            odata_id = f"/redfish/v1/EventService/Subscriptions/{sub_id}"
            sub = {'@odata.id': odata_id, **data}
            subs = load_subscriptions()
            subs.append(sub)
            save_subscriptions(subs)
            resp = make_response(sub, 201)
            resp.headers['Location'] = odata_id
            return resp
        else:
            return msg, code
