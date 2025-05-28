# EventService Events API implementation
import os, json, uuid, datetime
from flask import request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data

EVENTS_FILE = '/tmp/redfish_events.json'

def load_events():
    if os.path.exists(EVENTS_FILE):
        with open(EVENTS_FILE) as f:
            return json.load(f)
    return []

def save_events(events):
    with open(EVENTS_FILE, 'w') as f:
        json.dump(events, f)

def create_event(event_type, message_id, message, severity, origin, extra=None):
    event_id = str(uuid.uuid4())
    event = {
        '@odata.id': f"/redfish/v1/EventService/Events/{event_id}",
        'EventID': event_type,
        'MessageId': message_id,
        'Message': message,
        'Severity': severity,
        'DateTime': datetime.datetime.utcnow().isoformat() + 'Z',
        'Origin': origin
    }
    if extra:
        event.update(extra)
    events = load_events()
    events.append(event)
    save_events(events)
    return event

class EventServiceEventsAPI(Resource):
    def __init__(self, **kwargs):
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    def get(self):
        msg, code = check_authentication(self.auth)
        if code == 200:
            return {'Members': load_events(), 'Members@odata.count': len(load_events())}, 200
        else:
            return msg, code
