# EventService Events API implementation
import g
import json, os, random, string
import traceback
import logging
import uuid, datetime

from flask import request
from flask_restful import Resource
from .constants import *
from api_emulator.utils import check_authentication, create_path, get_json_data, create_and_patch_object, delete_object, patch_object, put_object, create_collection, send_event, write_event
from .templates.Event import get_Event_instance

members = []
member_ids = []
INTERNAL_ERROR = 500

def create_event(event_type, message_id, message, severity, origin, extra=None):
    if event_type == "ResourceCreated":
        message = "The resource was created successfully."
        message_id = "ResourceEvent.1.4.2.ResourceCreated"
        severity = "OK"
    elif event_type == "ResourceModified":
        message = "The resource was modified successfully."
        message_id = "ResourceEvent.1.4.2.ResourceModified"
        severity = "OK"
    elif event_type == "ResourceUpdated":
        message = "The resource was updated successfully."
        message_id = "ResourceEvent.1.4.2.ResourceUpdated"
        severity = "OK"
    elif event_type == "ResourceDeleted":
        message = "The resource was deleted successfully."
        message_id = "ResourceEvent.1.4.2.ResourceDeleted"
        severity = "OK"

    event_id = str(uuid.uuid4())
    event = {
        '@odata.id': f"/redfish/v1/EventService/Events/{event_id}",
        'EventID': event_id,
        'MessageId': message_id,
        'Message': message,
        'MessageSeverity': severity,
        'EventTimestamp': datetime.datetime.utcnow().isoformat() + 'Z',
        'OriginOfCondition': origin
    }
    if extra:
        event.update(extra)

    # Post to the EventServiceEvents collection
    new_event_api = EventServiceEventsAPI(auth=None)  # No authentication needed for posting events
    new_event_api.post(event_id, event)
    # Send the event to any subscribers
    send_event_to_subscribers(event)
    return event

def send_event_to_subscribers(event):
    """
    Send the event to all subscribers in the EventDestination collection at /redfish/v1/EventService/Subscriptions.
    Each subscriber is expected to have a Destination field (URL) in its subscription object.
    """
    from urllib.parse import urlparse
    import requests

    # Load subscriptions from the Redfish collection file
    subs_path = create_path(PATHS['Root'], 'EventService/Subscriptions/index.json')
    if not os.path.exists(subs_path):
        logging.info('No EventService subscriptions found.')
        return
    with open(subs_path) as f:
        data = json.load(f)
        subscriptions = data.get('Members', [])
        logging.info(f"Found {len(subscriptions)} subscriptions in EventService.")

    for sub in subscriptions:
        # Extract the subscription ID from the @odata.id field
        odata_id = sub.get('@odata.id')
        if odata_id:
            sub_id = odata_id.rstrip('/').split('/')[-1]
            path = create_path(PATHS['Root'], 'EventService/Subscriptions', sub_id, 'index.json')
            logging.info(f"Processing subscription: {path}")
            jsondata = get_json_data(path)
        else:
            logging.warning("Subscription missing @odata.id field.")
            continue
        # Use the loaded jsondata for the actual member
        if 'Destination' in jsondata:
            dest_url = jsondata['Destination']
        else:
            dest_url = None
        logging.info('Destination URL: ' + str(dest_url))
        if not dest_url:
            logging.warning(f"Subscription {odata_id} missing Destination field.")
            continue
        try:
            # Send the event as JSON to the subscriber's destination
            resp = requests.post(dest_url, json=event, timeout=5, verify=False)
            if resp.status_code >= 200 and resp.status_code < 300:
                logging.info(f"Event sent to subscriber {dest_url} successfully.")
            else:
                logging.warning(f"Failed to send event to {dest_url}: {resp.status_code} {resp.text}")
        except Exception as e:
            logging.warning(f"Exception sending event to {dest_url}: {e}")


class EventServiceEventsAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('EventServiceEvents init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET
    def get(self, EventId):
        logging.info('Storage0 get called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            path = create_path(self.root, 'EventService/Events/{0}', 'index.json').format(EventId)
            return get_json_data (path)
        else:
            return msg, code

    # HTTP POST 
    def post(self, EventId, event_data=None):
        global config
        logging.info('EventServiceEvents post called')
        msg, code = check_authentication(self.auth)
        if code == 200:
            path = create_path(self.root, 'EventService/Events/{0}').format(EventId)
            collection_path = os.path.join(self.root, 'EventService/Events', 'index.json')
            # Check if collection exists:
            if not os.path.exists(collection_path):
                EventServiceEventsCollectionAPI.post(self)

            if EventId in members:
                resp = 404
                return resp
            try:
                
                # If event_data is provided, use it; otherwise, use global config
                if (event_data):
                    config = event_data
                    logging.info(f"Creating event with provided data: {event_data}")
                else:
                    wildcards = {'EventId': EventId, 'rb': g.rest_base}
                    config = get_Event_instance(wildcards)
                config = write_event(event_data, members, member_ids)
                resp = config, 200

            except Exception:
                traceback.print_exc()
                resp = INTERNAL_ERROR
            logging.info('EventServiceEvents POST exit')
            return resp
        else:
            return msg, code

class EventServiceEventsCollectionAPI(Resource):
    def __init__(self, **kwargs):
        logging.info('EventService Events Collection init called')
        self.root = PATHS['Root']
        self.auth = kwargs['auth']

    # HTTP GET (single event)
    def get(self, EventId):
        logging.info('EventServiceEvents collection get called')
        msg, code = check_authentication(self.auth)
        if code == 200:
            path = create_path(self.root, 'EventService/Events/{0}', 'index.json').format(EventId)
            return get_json_data(path)
        else:
            return msg, code
        
    # HTTP POST Collection
    def post(self):
        logging.info('EventService Events Collection post called')
        msg, code = check_authentication(self.auth)

        if code == 200:
            if request.data:
                config = json.loads(request.data)
                if "@odata.type" in config:
                    if "Collection" in config["@odata.type"]:
                        return "Invalid data in POST body", 400

            path = create_path(self.root, 'EventService/Events')
            parent_path = os.path.dirname(path)
            if not os.path.exists(path):
                os.mkdir(path)
                create_collection (path, 'EventService/Events', parent_path)

            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            if request.data:
                config = json.loads(request.data)
                if "@odata.id" in config:
                    return EventServiceEventsAPI.post(self, os.path.basename(config['@odata.id']))
                else:
                    return EventServiceEventsAPI.post(self, str(res))
            else:
                return EventServiceEventsAPI.post(self, str(res))
        else:
            return msg, code