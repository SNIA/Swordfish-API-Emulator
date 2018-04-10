"""/* 
 * Copyright Notice:
 * Copyright 2016 Distributed Management Task Force, Inc. All rights reserved.
 * License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/LICENSE.md
 
 * The original DMTF contents of this file have been modified to support
 * The SNIA Swordfish API Emulator. These modifications are subject to the following:
 * Copyright (c) 2017, The Storage Networking Industry Association.
 *  
 * Redistribution and use in source and binary forms, with or without 
 * modification, are permitted provided that the following conditions are met:
 *  
 * Redistributions of source code must retain the above copyright notice, 
 * this list of conditions and the following disclaimer.
 *  
 * Redistributions in binary form must reproduce the above copyright notice, 
 * this list of conditions and the following disclaimer in the documentation 
 * and/or other materials provided with the distribution.
 *  
 * Neither the name of The Storage Networking Industry Association (SNIA) nor 
 * the names of its contributors may be used to endorse or promote products 
 * derived from this software without specific prior written permission.
 *  
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
 *  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
 *  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
 *  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
 *  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
 *  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
 *  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS  
 *  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
 *  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
 *  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
 *  THE POSSIBILITY OF SUCH DAMAGE.
 */"""
# Resource Manager Module

import os
import json
import urllib3
from uuid import uuid4
from threading import Thread
import logging
import copy

import g
from api_emulator.redfish.storageservices_api import *
from api_emulator.redfish.volumes_api import *
from api_emulator.redfish.storagepools_api import *
from api_emulator.redfish.drives_api import *
from api_emulator.redfish.filesystems_api import *
from api_emulator.redfish.storagegroups_api import *
from api_emulator.redfish.storagesubsystems_api import *
from api_emulator.redfish.endpoints_api import *
from api_emulator.redfish.endpointgroups_api import *
from api_emulator.redfish.classesofservice_api import *
from api_emulator.redfish.dataprotectionloscapabilities_api import *
from api_emulator.redfish.datasecurityloscapabilities_api import *
from api_emulator.redfish.datastorageloscapabilities_api import *
from api_emulator.redfish.ioperformanceloscapabilities_api import *
from api_emulator.redfish.ioconnectivityloscapabilities_api import *
from api_emulator.redfish.storagesystems_api import *
from . import utils
from .resource_dictionary import ResourceDictionary

from .static_loader import load_static
from .redfish.computer_system import ComputerSystem
from .redfish.computer_systems import ComputerSystemCollection
from .exceptions import CreatePooledNodeError, RemovePooledNodeError, EventSubscriptionError
from .redfish.event_service import EventService, Subscriptions
from .redfish.event import Event

from .redfish.EventService_api import EventServiceAPI, CreateEventService
from .redfish.Chassis_api import ChassisCollectionAPI, ChassisAPI, CreateChassis
from .redfish.ComputerSystem_api import ComputerSystemCollectionAPI, ComputerSystemAPI, CreateComputerSystem
from .redfish.Manager_api import ManagerCollectionAPI, ManagerAPI, CreateManager
from .redfish.pcie_switch_api import PCIeSwitchesAPI, PCIeSwitchAPI
from .redfish.eg_resource_api import EgResourceCollectionAPI, EgResourceAPI, CreateEgResource
from .redfish.power_api import PowerAPI, CreatePower
from .redfish.thermal_api import ThermalAPI, CreateThermal
from .redfish.ComputerSystem.ResetActionInfo_api import ResetActionInfo_API
from .redfish.ComputerSystem.ResetAction_api import ResetAction_API
from .redfish.processor import Processor, Processors
from .redfish.memory import Memory,MemoryCollection
from .redfish.simplestorage import SimpleStorage,SimpleStorageCollection
from .redfish.ethernetinterface import EthernetInterfaceCollection, EthernetInterface


from .redfish.CompositionService_api import CompositionServiceAPI
from .redfish.ResourceBlock_api import ResourceBlockCollectionAPI, ResourceBlockAPI, CreateResourceBlock
from .redfish.ResourceZone_api import ResourceZoneCollectionAPI, ResourceZoneAPI, CreateResourceZone

mockupfolders = []

# The __init__ method sets up the static and dynamic resources.
#
# When a resource is accessed, the resource is sought in the following order:
# 1. Dynamic resource for specific URI
#       2. Default dynamic resource
#       3. Static resource dictionary
#
# This structure allows specific resources to be implemented as dynamic while leaving the remainder
#   of the URI path as static resources.
#
# The static resource are loaded from the ./redfish/static directory.  This directory is just a copy
#   of the one of the ./mockups directories.
#
# For dynamic resources are attached using the Flask-restful mechanism, not the Flask mechanism.
#   - This involves associating an API class to a resoure endpoint.  A collection resource requires the
#       association of the collection resource and the member resource(s)
#   - Once the API is added, explicit calls can be made to populated one or more singleton resources
#   - The EgResource* provides an example of adding a dynamic resource.
#
# Note: There is one additional change that needs to be made in order to create multiple instances of a
#   resource.  The resource endpoint for the second instance collides with the first because flask
#   doesn't reuse the endpont name for the subordinate resources.  This results in an assertion failure
#       "AssertionError: View function mapping is overwriting an existing endpoint function"
#
#   The fix is form a unique endpoint names and pass it during the call to api_add_resource()
#      e.g. api.add_resource(Todo,  '/todo/<int:todo_id>', endpoint='todo_ep')
#

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
            self.AccountService =   load_static('AccountService', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Registries =       load_static('Registries', 'redfish', mode, rest_base, self.resource_dictionary)
            self.SessionService =   load_static('SessionService', 'redfish', mode, rest_base, self.resource_dictionary)
            self.TaskService =      load_static('TaskService', 'redfish', mode, rest_base, self.resource_dictionary)
            #self.StorageSystems = load_static('StorageSystems', 'redfish', mode, rest_base, self.resource_dictionary)
#        if "Swordfish" in mockupfolders:
#            self.SessionService = load_static('SessionService', 'redfish', mode, rest_base, self.resource_dictionary)			

        # Attach APIs for dynamic resources

        # EventService (singleton)
        g.api.add_resource(EventServiceAPI, '/redfish/v1/EventService',
                           resource_class_kwargs={'rb': g.rest_base, 'id': "EventService"})
        config = CreateEventService()
        out = config.__init__(resource_class_kwargs={'rb': g.rest_base})
        out = config.put("EventService")

        # Chassis Collection
        g.api.add_resource(ChassisCollectionAPI, '/redfish/v1/Chassis')
        g.api.add_resource(ChassisAPI, '/redfish/v1/Chassis/<string:ident>', resource_class_kwargs={'rb': g.rest_base})
        g.api.add_resource(ThermalAPI, '/redfish/v1/Chassis/<string:ident>/Thermal',
                           resource_class_kwargs={'rb': g.rest_base})
        g.api.add_resource(PowerAPI, '/redfish/v1/Chassis/<string:ident>/Power',
                           resource_class_kwargs={'rb': g.rest_base})

        # System Collection
        g.api.add_resource(ComputerSystemCollectionAPI, '/redfish/v1/Systems')
        g.api.add_resource(ComputerSystemAPI, '/redfish/v1/Systems/<string:ident>',
                           resource_class_kwargs={'rb': g.rest_base})

        g.api.add_resource(MemoryCollection, '/redfish/v1/Systems/<string:ident>/Memory',
                           resource_class_kwargs={'rb': g.rest_base,'suffix':'Systems'})
        g.api.add_resource(Memory, '/redfish/v1/Systems/<string:ident1>/Memory/<string:ident2>',
                           '/redfish/v1/CompositionService/ResourceBlocks/<string:ident1>/Memory/<string:ident2>')

        g.api.add_resource(Processors, '/redfish/v1/Systems/<string:ident>/Processors',
                           resource_class_kwargs={'rb': g.rest_base,'suffix':'Systems'})
        g.api.add_resource(Processor, '/redfish/v1/Systems/<string:ident1>/Processors/<string:ident2>',
                           '/redfish/v1/CompositionService/ResourceBlocks/<string:ident1>/Processors/<string:ident2>')

        g.api.add_resource(SimpleStorageCollection, '/redfish/v1/Systems/<string:ident>/SimpleStorage',
                           resource_class_kwargs={'rb': g.rest_base,'suffix':'Systems'})
        g.api.add_resource(SimpleStorage, '/redfish/v1/Systems/<string:ident1>/SimpleStorage/<string:ident2>',
                           '/redfish/v1/CompositionService/ResourceBlocks/<string:ident1>/SimpleStorage/<string:ident2>')

        g.api.add_resource(EthernetInterfaceCollection, '/redfish/v1/Systems/<string:ident>/EthernetInterfaces',
                           resource_class_kwargs={'rb': g.rest_base,'suffix':'Systems'})
        g.api.add_resource(EthernetInterface, '/redfish/v1/Systems/<string:ident1>/EthernetInterfaces/<string:ident2>',
                           '/redfish/v1/CompositionService/ResourceBlocks/<string:ident1>/EthernetInterfaces/<string:ident2>')

        g.api.add_resource(ResetActionInfo_API, '/redfish/v1/Systems/<string:ident>/ResetActionInfo',
                           resource_class_kwargs={'rb': g.rest_base})
        g.api.add_resource(ResetAction_API, '/redfish/v1/Systems/<string:ident>/Actions/ComputerSystem.Reset',
                           resource_class_kwargs={'rb': g.rest_base})

        # Manager Collection
        g.api.add_resource(ManagerCollectionAPI, '/redfish/v1/Managers')
        g.api.add_resource(ManagerAPI, '/redfish/v1/Managers/<string:ident>', resource_class_kwargs={'rb': g.rest_base})

        # PCIe Switch Collection
        g.api.add_resource(PCIeSwitchesAPI, '/redfish/v1/PCIeSwitches')
        g.api.add_resource(PCIeSwitchAPI, '/redfish/v1/PCIeSwitches/<string:ident>')

        # Example Resource Collection
        g.api.add_resource(EgResourceCollectionAPI, '/redfish/v1/EgResources')
        g.api.add_resource(EgResourceAPI, '/redfish/v1/EgResources/<string:ident>', resource_class_kwargs={'rb': g.rest_base})

        # Composition Service - API
        g.api.add_resource(CompositionServiceAPI, '/redfish/v1/CompositionService', resource_class_kwargs={'rb': g.rest_base, 'id': "CompositionService"})

        # Composition Service - Resource Block API
        g.api.add_resource(ResourceBlockCollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks')
        g.api.add_resource(ResourceBlockAPI,           '/redfish/v1/CompositionService/ResourceBlocks/<string:ident>', resource_class_kwargs={'rb': g.rest_base})

        # Composition Service - Resource Zone API
        g.api.add_resource(ResourceZoneCollectionAPI, '/redfish/v1/CompositionService/ResourceZones')
        g.api.add_resource(ResourceZoneAPI,           '/redfish/v1/CompositionService/ResourceZones/<string:ident>', resource_class_kwargs={'rb': g.rest_base})
		
		# Storage Services - API and Collection
        g.api.add_resource(StorageServicesCollectionAPI, '/redfish/v1/StorageServices')
        g.api.add_resource(StorageServicesAPI, '/redfish/v1/StorageServices/<string:storage_service>')
        g.api.add_resource(StorageGroupsCollectionAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/StorageGroups')
        g.api.add_resource(StorageGroupsAPI,
                           '/redfish/v1/StorageServices/<string:storage_service>/StorageGroups/<string:storage_groups>')
        g.api.add_resource(StoragePoolsCollectionAPI,
                           '/redfish/v1/StorageServices/<string:storage_service>/StoragePools')
        g.api.add_resource(StoragePoolsAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/StoragePools/<string:storage_pools>')                
        g.api.add_resource(DrivesCollectionAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/Drives')
        g.api.add_resource(DrivesAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/Drives/<string:drives>')

        g.api.add_resource(ClassesOfServiceCollectionAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/ClassesOfService')
        g.api.add_resource(ClassesOfServiceAPI,
                           '/redfish/v1/StorageServices/<string:storage_service>/ClassesOfService/<string:classes_of_service>')
        
        g.api.add_resource(DataProtectionLoSCapabilitiesAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/DataProtectionLoSCapabilities')
        g.api.add_resource(DataSecurityLoSCapabilitiesAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/DataSecurityLoSCapabilities')

        g.api.add_resource(DataStorageLoSCapabilitiesAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/DataStorageLoSCapabilities')
        g.api.add_resource(EndpointsCollectionAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/Endpoints')
        g.api.add_resource(EndpointsAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/Endpoints/<string:endpoints>')
        g.api.add_resource(EndpointGroupsCollectionAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/EndpointGroups')
        g.api.add_resource(EndpointGroupsAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/EndpointGroups/<string:endpoint_groups>')
        
        
        g.api.add_resource(FileSystemsCollectionAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/FileSystems')
        g.api.add_resource(FileSystemsAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/FileSystems/<string:file_systems>')        
        
        g.api.add_resource(IOConnectivityLoSCapabilitiesAPI,
                           '/redfish/v1/StorageServices/<string:storage_service>/IOConnectivityLoSCapabilities')

        g.api.add_resource(IOPerformanceLoSCapabilitiesAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/IOPerformanceLoSCapabilities')
        g.api.add_resource(StorageSubsystemsAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/StorageSubsystems')

        g.api.add_resource(VolumesCollectionAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/Volumes')
        g.api.add_resource(VolumesAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/Volumes/<string:volumes>')        
        # Storage Systems - API and Collection
        g.api.add_resource(StorageSystemsCollectionAPI, '/redfish/v1/StorageSystems')
        g.api.add_resource(StorageSystemsAPI, '/redfish/v1/StorageSystems/<string:storage_systems>')


    @property
    def configuration(self):
        """
        Configuration property - Service Root
        """
        config = {
            '@odata.context': self.rest_base + '$metadata#ServiceRoot',
            '@odata.type': '#ServiceRoot.1.0.0.ServiceRoot',
            '@odata.id': self.rest_base,
            'Id': 'RootService',
            'Name': 'Root Service',
            'ServiceVersion': '1.0.0',
            'UUID': self.uuid,
            'Links': {
                'Chassis': {'@odata.id': self.rest_base + 'Chassis'},
                'Managers': {'@odata.id': self.rest_base + 'Managers'},
                'TaskService': {'@odata.id': self.rest_base + 'TaskService'},
                'SessionService': {'@odata.id': self.rest_base + 'SessionService'},
				'StorageServices': {'@odata.id': self.rest_base + 'StorageServices'},
				'StorageSystems': {'@odata.id': self.rest_base + 'StorageSystems'},
                'AccountService': {'@odata.id': self.rest_base + 'AccountService'},
                'EventService': {'@odata.id': self.rest_base + 'EventService'},
                'Registries': {'@odata.id': self.rest_base + 'Registries'},
                'Systems': {'@odata.id': self.rest_base + 'Systems'},
                'CompositionService': {'@odata.id': self.rest_base + 'CompositionService'}
            }
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
