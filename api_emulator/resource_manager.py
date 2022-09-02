# Copyright Notice:
# Copyright 2016-2021 DMTF. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/blob/master/LICENSE.md
#
# The original DMTF contents of this file have been modified to support
# The SNIA Swordfish API Emulator. These modifications are subject to the following:
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
#  AND ANY EXPRESS OR IMfPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
#  THE POSSIBILITY OF SUCH DAMAGE.
#

# Resource Manager Module

# External imports

from api_emulator.redfish.Chassis_api import ChassisAPI, ChassisCollectionAPI
from api_emulator.redfish.Connection_api import ConnectionAPI, ConnectionCollectionAPI
from api_emulator.redfish.Drive1_api import Drive1API, Drive1CollectionAPI
from api_emulator.redfish.Endpoint0_api import Endpoint0API, Endpoint0CollectionAPI
from api_emulator.redfish.EndpointGroup3_api import EndpointGroup3API, EndpointGroup3CollectionAPI
from api_emulator.redfish.EthernetInterface0_api import EthernetInterface0API, EthernetInterface0CollectionAPI
from api_emulator.redfish.EthernetInterface6_api import EthernetInterface6API, EthernetInterface6CollectionAPI
from api_emulator.redfish.Fabric_api import FabricAPI, FabricCollectionAPI
from api_emulator.redfish.LogEntry0_api import LogEntry0API, LogEntry0CollectionAPI
from api_emulator.redfish.LogService0_api import LogService0API, LogService0CollectionAPI
from api_emulator.redfish.ManagerNetworkProtocol_api import ManagerNetworkProtocolAPI
from api_emulator.redfish.Manager_api import ManagerAPI, ManagerCollectionAPI
from api_emulator.redfish.MessageRegistryFile_api import MessageRegistryFileAPI, MessageRegistryFileCollectionAPI
from api_emulator.redfish.NetworkAdapter_api import NetworkAdapterAPI, NetworkAdapterCollectionAPI
from api_emulator.redfish.NetworkDeviceFunction_api import NetworkDeviceFunctionAPI, NetworkDeviceFunctionCollectionAPI
from api_emulator.redfish.Port0_api import Port0API, Port0CollectionAPI
from api_emulator.redfish.Port17_api import Port17API, Port17CollectionAPI
from api_emulator.redfish.ServiceRoot1_api import ServiceRoot1API
from api_emulator.redfish.SessionService_api import SessionServiceAPI
from api_emulator.redfish.Session_api import SessionAPI, SessionCollectionAPI
from api_emulator.redfish.Storage0_api import Storage0API, Storage0CollectionAPI
from api_emulator.redfish.StorageController0_api import StorageController0API, StorageController0CollectionAPI
from api_emulator.redfish.Switch_api import SwitchAPI, SwitchCollectionAPI
from api_emulator.redfish.Thermal_api import ThermalAPI
from api_emulator.redfish.Volume8_api import Volume8API, Volume8CollectionAPI
from api_emulator.redfish.Zone0_api import Zone0API, Zone0CollectionAPI

from . import utils
import os
import json
import urllib3
from uuid import uuid4
from threading import Thread
import logging
import copy
# Local imports
import g

from .static_loader import load_static
from .resource_dictionary import ResourceDictionary
from .exceptions import CreatePooledNodeError, RemovePooledNodeError

mockupfolders = []

# The ResourceManager __init__ method sets up the static and dynamic
# resources.
#
# When a resource is accessed, the resource is sought in the following
# order:
#   1. Dynamic resources for specific URIs
#   2. Default dynamic resources
#   3. Static resource dictionary
#
# This allows specific resources to be implemented as dynamic resources
# while leaving the remainder of the URI path as static resources.
#
# Static resources are loaded from the ./redfish/static directory.
# This directory is a copy of the one of the ./mockups directories.
#
# Dynamic resources are attached to endpoints using the Flask-restful
# mechanism, not the Flask mechanism.
#   - This involves associating an API class to a resource endpoint.
#     A collection resource requires the association of the collection
#     resource and the member resource(s).
#   - Once the API is added, explicit calls can be made to one or more
#     singleton resources that have been populated.
#   - The EgResource* and EgSubResource* files provide examples of how
#     to add dynamic resources.
#
# Note: There is one additional change that needs to be made in order
# to create multiple instances of a resource. The resource endpoint
# for a second instance will collide with the first, because flask does
# not re-use endpoint names for subordinate resources. This results
# in an assertion error failure:
#   "AssertionError: View function mapping is overwriting an existing
#   endpoint function"
#
# The fix would be to form unique endpoint names and pass them in
# with the call to api_add_resource(), as shown in the following:
#   api.add_resource(Todo, '/todo/<int:todo_id>', endpoint='todo_ep')

class ResourceManager(object):
    """
    ResourceManager Class

    Load static resources and dynamic resources
    Defines ServiceRoot
    """

    def __init__(self, rest_base, spec, mode, trays=None):
        """
        Arguments:
            rest_base - Base URL for the REST interface
            spec      - Which spec to use, Redfish or Chinook
            trays     - (Optional) List of trays to initially load into the
                        resource manager
        When a resource is accessed, the resource is sought in the following order
        1. Dynamic resource for specific URI
        2. Static resource dictionary
        """

        self.rest_base = rest_base

        self.mode = mode
        self.spec = spec
        self.modified = utils.timestamp()
        self.uuid = str(uuid4())
        self.time = self.modified
        self.cs_puid_count = 0

        # Load the static resources into the dictionary

        self.resource_dictionary = ResourceDictionary()
        mockupfolders = copy.copy(g.staticfolders)

        if "Redfish" in mockupfolders:
            logging.info('Loading Redfish static resources')
            self.ServiceRoot =       load_static('', 'redfish', mode, rest_base, self.resource_dictionary)

            self.AccountService =   load_static('AccountService', 'redfish', mode, rest_base, self.resource_dictionary)

            self.Registries =       load_static('Registries', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Registries =       load_static('Registries', 'redfish', mode, rest_base, self.resource_dictionary)
            self.SessionService =   load_static('SessionService', 'redfish', mode, rest_base, self.resource_dictionary)
            self.TaskService =      load_static('TaskService', 'redfish', mode, rest_base, self.resource_dictionary)
            self.EventService =     load_static('EventService', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Chassis =          load_static('Chassis', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Storage =          load_static('Storage', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Fabrics =          load_static('Fabrics', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Systems=           load_static('Systems', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Managers =         load_static('Managers', 'redfish', mode, rest_base, self.resource_dictionary)

#        if "Swordfish" in mockupfolders:
#            self.StorageServices = load_static('StorageServices', 'redfish', mode, rest_base, self.resource_dictionary)
#            self.StorageSystems = load_static('StorageSystems', 'redfish', mode, rest_base, self.resource_dictionary)

        # Attach APIs for dynamic resources
        g.api.add_resource(ServiceRoot1API, '/redfish/v1/')

        g.api.add_resource(ChassisCollectionAPI, '/redfish/v1/Chassis')
        g.api.add_resource(ChassisAPI, '/redfish/v1/Chassis/<string:ChassisId>')

        g.api.add_resource(Drive1CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/Drives')
        g.api.add_resource(Drive1API, '/redfish/v1/Chassis/<string:ChassisId>/Drives/<string:DriveId>')

        g.api.add_resource(NetworkAdapterCollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters')
        g.api.add_resource(NetworkAdapterAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>')

        g.api.add_resource(ThermalAPI, '/redfish/v1/Chassis/<string:ChassisId>/Thermal')

        g.api.add_resource(NetworkDeviceFunctionCollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/NetworkDeviceFunctions')
        g.api.add_resource(NetworkDeviceFunctionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/NetworkDeviceFunctions/<string:NetworkDeviceFunctionId>')

        g.api.add_resource(Port17CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Ports')
        g.api.add_resource(Port17API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Ports/<string:PortId>')

        g.api.add_resource(EthernetInterface6CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdaptersId>/NetworkDeviceFunctions/<string:NetworkDeviceFunctionId>/EthernetInterfaces')
        g.api.add_resource(EthernetInterface6API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdaptersId>/NetworkDeviceFunctions/<string:NetworkDeviceFunctionId>/EthernetInterfaces/<string:EthernetInterfaceId>')

        g.api.add_resource(FabricCollectionAPI, '/redfish/v1/Fabrics')
        g.api.add_resource(FabricAPI, '/redfish/v1/Fabrics/<string:FabricId>')

        g.api.add_resource(Endpoint0CollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Endpoints')
        g.api.add_resource(Endpoint0API, '/redfish/v1/Fabrics/<string:FabricId>/Endpoints/<string:EndpointId>')

        g.api.add_resource(SwitchCollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Switches')
        g.api.add_resource(SwitchAPI, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>')

        g.api.add_resource(Zone0CollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Zones')
        g.api.add_resource(Zone0API, '/redfish/v1/Fabrics/<string:FabricId>/Zones/<string:ZoneId>')

        g.api.add_resource(Port0CollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports')
        g.api.add_resource(Port0API, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports/<string:PortId>')

        g.api.add_resource(ConnectionCollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Connections')
        g.api.add_resource(ConnectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Connections/<string:ConnectionId>')

        g.api.add_resource(EndpointGroup3CollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/EndpointGroups')
        g.api.add_resource(EndpointGroup3API, '/redfish/v1/Fabrics/<string:FabricId>/EndpointGroups/<string:EndpointGroupId>')

        g.api.add_resource(ManagerCollectionAPI, '/redfish/v1/Managers')
        g.api.add_resource(ManagerAPI, '/redfish/v1/Managers/<string:ManagerId>')

        g.api.add_resource(EthernetInterface0CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/EthernetInterfaces')
        g.api.add_resource(EthernetInterface0API, '/redfish/v1/Managers/<string:ManagerId>/EthernetInterfaces/<string:EthernetInterfaceId>')

        g.api.add_resource(LogService0CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/LogServices')
        g.api.add_resource(LogService0API, '/redfish/v1/Managers/<string:ManagerId>/LogServices/<string:LogServiceId>')

        g.api.add_resource(ManagerNetworkProtocolAPI, '/redfish/v1/Managers/<string:ManagerId>/NetworkProtocol')

        g.api.add_resource(LogEntry0CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/LogServices/<string:LogServiceId>/Entries')
        g.api.add_resource(LogEntry0API, '/redfish/v1/Managers/<string:ManagerId>/LogServices/<string:LogServiceId>/Entries/<string:LogEntryId>')

        g.api.add_resource(MessageRegistryFileCollectionAPI, '/redfish/v1/Registries')
        g.api.add_resource(MessageRegistryFileAPI, '/redfish/v1/Registries/<string:MessageRegistryFileId>')

        g.api.add_resource(SessionServiceAPI, '/redfish/v1/SessionService')

        g.api.add_resource(SessionCollectionAPI, '/redfish/v1/SessionService/Sessions')
        g.api.add_resource(SessionAPI, '/redfish/v1/SessionService/Sessions/<string:SessionId>')

        g.api.add_resource(Storage0CollectionAPI, '/redfish/v1/Storage')
        g.api.add_resource(Storage0API, '/redfish/v1/Storage/<string:StorageId>')

        g.api.add_resource(StorageController0CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/Controllers')
        g.api.add_resource(StorageController0API, '/redfish/v1/Storage/<string:StorageId>/Controllers/<string:ControllerId>')

        g.api.add_resource(Volume8CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/Volumes')
        g.api.add_resource(Volume8API, '/redfish/v1/Storage/<string:StorageId>/Volumes/<string:VolumeId>')


    @property
    def configuration(self):
        """
        Configuration property - Service Root
        """
        config = {
            '@odata.context': self.rest_base + '$metadata#ServiceRoot',
            '@odata.type': '#ServiceRoot.v1_9_0.ServiceRoot',
            '@odata.id': self.rest_base,
            'Id': 'RootService',
            'Name': 'Root Service',
            'RedfishVersion': '1.6.0',
            'UUID': self.uuid,
            'Chassis': {'@odata.id': self.rest_base + 'Chassis'},
            #'Fabrics': {'@odata.id': self.rest_base + 'Fabrics'},
            # 'EgResources': {'@odata.id': self.rest_base + 'EgResources'},
            #'Managers': {'@odata.id': self.rest_base + 'Managers'},
            #'TaskService': {'@odata.id': self.rest_base + 'TaskService'},
            'SessionService': {'@odata.id': self.rest_base + 'SessionService'},
            #'StorageServices': {'@odata.id': self.rest_base + 'StorageServices'},
            #'StorageSystems': {'@odata.id': self.rest_base + 'StorageSystems'},
            #'AccountService': {'@odata.id': self.rest_base + 'AccountService'},
            #'EventService': {'@odata.id': self.rest_base + 'EventService'},
            'Registries': {'@odata.id': self.rest_base + 'Registries'},
            'Systems': {'@odata.id': self.rest_base + 'Systems'},
            'Storage': {'@odata.id': self.rest_base + 'Storage'},
            #'CompositionService': {'@odata.id': self.rest_base + 'CompositionService'}
        }

        return config

    @property
    def available_procs(self):
        return self.max_procs - self.used_procs

    @property
    def available_mem(self):
        return self.max_memory - self.used_memory

    @property
    def available_storage(self):
        return self.max_storage - self.used_storage

    @property
    def available_network(self):
        return self.max_network - self.used_network

    @property
    def num_pooled_nodes(self):
        if self.spec == 'Chinook':
            return self.PooledNodes.count
        else:
            return self.Systems.count

    def _create_redfish(self, rs, action):
        """
        Private method for creating a Redfish based pooled node

        Arguments:
            rs  - The requested pooled node
        """
        try:
            pn = ComputerSystem(rs, self.cs_puid_count + 1, self.rest_base, 'Systems')
            self.Systems.add_computer_system(pn)
        except KeyError as e:
            raise CreatePooledNodeError(
                'Configuration missing key: ' + e.message)
        try:
            # Verifying resources
            assert pn.processor_count <= self.available_procs, self.err_str.format('CPUs')
            assert pn.storage_gb <= self.available_storage, self.err_str.format('storage')
            assert pn.network_ports <= self.available_network, self.err_str.format('network ports')
            assert pn.total_memory_gb <= self.available_mem, self.err_str.format('memory')

            self.used_procs += pn.processor_count
            self.used_storage += pn.storage_gb
            self.used_network += pn.network_ports
            self.used_memory += pn.total_memory_gb
        except AssertionError as e:
            self._remove_redfish(pn.cs_puid)
            raise CreatePooledNodeError(e.message)
        except KeyError as e:
            self._remove_redfish(pn.cs_puid)
            raise CreatePooledNodeError(
                'Requested system missing key: ' + e.message)

        self.resource_dictionary.add_resource('Systems/{0}'.format(pn.cs_puid), pn)
        self.cs_puid_count += 1
        return pn.configuration

    def _remove_redfish(self, cs_puid):
        """
        Private method for removing a Redfish based pooled node

        Arguments:
            cs_puid - CS_PUID of the pooled node to remove
        """
        try:
            pn = self.Systems[cs_puid]

            # Adding back in used resources
            self.used_procs -= pn.processor_count
            self.used_storage -= pn.storage_gb
            self.used_network -= pn.network_ports
            self.used_memory -= pn.total_memory_gb

            self.Systems.remove_computer_system(pn)
            self.resource_dictionary.delete_resource('Systems/{0}'.format(cs_puid))

            if self.Systems.count == 0:
                self.cs_puid_count = 0
        except IndexError:
            raise RemovePooledNodeError(
                'No pooled node with CS_PUID: {0}, exists'.format(cs_puid))

    def get_resource(self, path):
        """
        Call Resource_Dictionary's get_resource
        """
        obj = self.resource_dictionary.get_resource(path)
        return obj


'''
    def remove_pooled_node(self, cs_puid):
        """
        Delete the specified pooled node and free its resources.

        Throws a RemovePooledNodeError Exception if a problem is encountered.

        Arguments:
            cs_puid - CS_PUID of the pooed node to remove
        """
        self.remove_method(cs_puid)

    def update_cs(self,cs_puid,rs):
        """
            Updates the power metrics of Systems/1
        """
        cs=self.Systems[cs_puid]
        cs.reboot(rs)
        return cs.configuration

    def update_system(self,rs,c_id):
        """
            Updates selected System
        """
        self.Systems[c_id].update_config(rs)

        event = Event(eventType='ResourceUpdated', severity='Notification', message='System updated',
                      messageID='ResourceUpdated.1.0.System', originOfCondition='/redfish/v1/System/{0}'.format(c_id))
        self.push_event(event, 'ResourceUpdated')
        return self.Systems[c_id].configuration

    def add_event_subscription(self, rs):
        destination = rs['Destination']
        types = rs['Types']
        context = rs['Context']

        allowedTypes = ['StatusChange',
                        'ResourceUpdated',
                        'ResourceAdded',
                        'ResourceRemoved',
                        'Alert']

        for type in types:
            match = False
            for allowedType in allowedTypes:
                if type == allowedType:
                    match = True

            if not match:
                raise EventSubscriptionError('Some of types are not allowed')

        es = self.EventSubscriptions.add_subscription(destination, types, context)
        es_id = es.configuration['Id']
        self.resource_dictionary.add_resource('EventService/Subscriptions/{0}'.format(es_id), es)
        event = Event()
        self.push_event(event, 'Alert')
        return es.configuration

    def push_event(self, event, type):
        # Retreive subscription list
        subscriptions = self.EventSubscriptions.configuration['Members']
        for sub in subscriptions:
            # Get event subscription
            event_channel = self.resource_dictionary.get_object(sub.replace('/redfish/v1/', ''))
            event_types = event_channel.configuration['EventTypes']
            dest_uri = event_channel.configuration['Destination']

            # Check if client subscribes for event type
            match = False
            for event_type in event_types:
                if event_type == type:
                    match = True

            if match:
                # Sending event response
                EventWorker(dest_uri, event).start()


class EventWorker(Thread):
    """
    Worker class for sending event messages to clients
    """
    def __init__(self, dest_uri, event):
        super(EventWorker, self).__init__()
        self.dest_uri = dest_uri
        self.event = event

    def run(self):
        try:
            request = urllib2.Request(self.dest_uri)
            request.add_header('Content-Type', 'application/json')
            urllib2.urlopen(request, json.dumps(self.event.configuration), 15)
        except Exception:
            pass
'''
