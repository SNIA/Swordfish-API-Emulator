"""/* 
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




from . import utils
from .resource_dictionary import ResourceDictionary

from .static_loader import load_static
from .redfish.computer_system import ComputerSystem
from .redfish.computer_systems import ComputerSystemCollection
from .redfish.event_service import EventService, Subscriptions
from .redfish.event import Event

from .redfish.Chassis_api import ChassisCollectionAPI, ChassisAPI, CreateChassis
from .redfish.pcie_switch_api import PCIeSwitchesAPI, PCIeSwitchAPI



class ResourceManager(object):
    """
    ResourceManager Class

    Load static resources and dynamic resources
    Defines ServiceRoot
    """
    def __init__(self, rest_base, spec,mode,trays=None):
        """
        Arguments:
            rest_base - Base URL for the REST interface
            spec      - Which spec to use, Redfish or Chinook
            trays     - (Optional) List of trays to initially load into the
                        resource manager
        """

        self.rest_base = rest_base

        self.mode=mode
        self.spec = spec
        self.modified = utils.timestamp()
        self.uuid = str(uuid4())
        self.time = self.modified
        self.cs_puid_count = 0

        # Loads each resource into dictionary from the mockup
        self.resource_dictionary = ResourceDictionary()

        # Load Event and Chassis as dynamic resources
        self.AccountService = load_static('AccountService', 'redfish', mode, rest_base, self.resource_dictionary)
        self.Managers = load_static('Managers', 'redfish', mode, rest_base, self.resource_dictionary)
        #self.EventService = load_static('EventService', 'redfish', mode, rest_base, self.resource_dictionary)
        self.Registries = load_static('Registries', 'redfish', mode, rest_base, self.resource_dictionary)
        self.SessionService = load_static('SessionService', 'redfish', mode, rest_base, self.resource_dictionary)
        self.StorageSystems = load_static('StorageSystems', 'redfish', mode, rest_base, self.resource_dictionary)
        self.Systems = load_static('Systems', 'redfish', mode, rest_base, self.resource_dictionary)
        self.TaskService = load_static('TaskService', 'redfish', mode, rest_base, self.resource_dictionary)

        # Load dynamic resources (flask-restful method)
        #
        # Note: Corresponding resource should be commented out, above (if one exists)
        # - populate with a single chassis with Id=Test2
        g.api.add_resource(ChassisCollectionAPI, '/redfish/v1/Chassis/')
        g.api.add_resource(ChassisAPI,   '/redfish/v1/Chassis/<string:ident>')
        #config = CreateChassis()
        #out = config.put('Chassis2')
        #g.api.add_resource(SampleAPI, '/redfish/v1/Sample')
        g.api.add_resource(PCIeSwitchesAPI, '/redfish/v1/PCIeSwitches/')
        g.api.add_resource(PCIeSwitchAPI,   '/redfish/v1/PCIeSwitches/<string:ident>')

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
        g.api.add_resource(StoragePoolsChildAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/StoragePools/<string:storage_pools>/<string:values>')        
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
        g.api.add_resource(FileSystemsChildAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/FileSystems/<string:file_systems>/<string:values>')
        
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
        g.api.add_resource(VolumesChildAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/Volumes/<string:volumes>/<string:values>')
        




        # Load dynamic resources (flask method).
        # Note: The methods are defined later in this file
        #
        # Create computer system
        self.create_method = self._create_redfish
        self.remove_method = self._remove_redfish
        self.Systems = ComputerSystemCollection(rest_base)
        self.resource_dictionary.add_resource('Systems', self.Systems)

        # Event Service
        self.EventService = EventService(rest_base)
        self.EventSubscriptions = Subscriptions(rest_base)
        self.resource_dictionary.add_resource('EventService', self.EventService)
        self.resource_dictionary.add_resource('EventService/Subscriptions', self.EventSubscriptions)

        # Properties for used resources
        self.used_memory = 0
        self.used_procs = 0
        self.used_storage = 0
        self.used_network = 0

        # Properties for max resources
        self.max_memory = 4
        self.max_procs = 2
        self.max_storage = 120
        self.max_network = 1

        self.free_storage = []
        self.err_str = 'Insufficient amount of {0} to create pooled node'


    @property
    def configuration(self):
        """
        Configuration property
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
                'AccountService': {'@odata.id': self.rest_base + 'AccountService'},
                'EventService': {'@odata.id': self.rest_base + 'EventService'},
                'StorageServices': {'@odata.id': self.rest_base + 'StorageServices'},
                'StorageSystems': {'@odata.id': self.rest_base + 'StorageSystems'},
                'Registries': {'@odata.id': self.rest_base + 'Registries'},
                'Systems': {'@odata.id': self.rest_base + 'Systems'}
                
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

    def remove_pooled_node(self, cs_puid):
        """
        Delete the specified pooled node and free its resources.

        Throws a RemovePooledNodeError Exception if a problem is encountered.

        Arguments:
            cs_puid - CS_PUID of the pooed node to remove
        """
        self.remove_method(cs_puid)

    def get_resource(self, path):
        """
        Call Resource_Dictionary's get_resource
        """
        obj = self.resource_dictionary.get_resource(path)
        return obj

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

