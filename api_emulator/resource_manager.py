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
import os
import json
import urllib3
from uuid import uuid4
from threading import Thread
import logging
import copy
# Local imports
import g

from api_emulator.redfish.storage_api import *
from api_emulator.redfish.drives_api import *
from api_emulator.redfish.volumes_api import *
from api_emulator.redfish.storagecontrollers_api import *
from api_emulator.redfish.storagepools_api import *
from api_emulator.redfish.filesystems_api import *
from api_emulator.redfish.storagegroups_api import *
from api_emulator.redfish.storagesubsystems_api import *

from api_emulator.redfish.fabric_api import *
from api_emulator.redfish.f_switches_api import *
from api_emulator.redfish.f_switch_ports_api import *

from api_emulator.redfish.f_connections_api import *
from api_emulator.redfish.f_zones_api import *

from api_emulator.redfish.f_endpoints_api import *
from api_emulator.redfish.f_endpointgroups_api import *

from api_emulator.redfish.networkadapters_api import *
from api_emulator.redfish.networkdevicefunctions_api import *
from api_emulator.redfish.nwports_api import *

from api_emulator.redfish.storageservices_api import *
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
# Local imports (special case)
from .redfish.ComputerSystem_api import ComputerSystemCollectionAPI, ComputerSystemAPI, CreateComputerSystem
from .redfish.computer_systems import ComputerSystemCollection
from .exceptions import CreatePooledNodeError, RemovePooledNodeError, EventSubscriptionError
from .redfish.event_service import EventService, Subscriptions
from .redfish.event import Event
# EventService imports
from .redfish.EventService_api import EventServiceAPI, CreateEventService
from .redfish.Subscriptions_api import SubscriptionCollectionAPI, SubscriptionAPI, CreateSubscription

# SessionService imports
from .redfish.SessionService_api import SessionServiceAPI, CreateSessionService
from .redfish.sessions_api import SessionCollectionAPI, SessionAPI, CreateSession

# Chassis imports
from .redfish.Chassis_api import ChassisCollectionAPI, ChassisAPI, CreateChassis
from .redfish.power_api import PowerAPI, CreatePower
from .redfish.thermal_api import ThermalAPI, CreateThermal
# Manager imports
from .redfish.Manager_api import ManagerCollectionAPI, ManagerAPI, CreateManager
# EgResource imports
from .redfish.eg_resource_api import EgResourceCollectionAPI, EgResourceAPI, CreateEgResource
from .redfish.eg_subresource_api import EgSubResourceCollectionAPI, EgSubResourceAPI, CreateEgSubResource
# ComputerSystem imports
from .redfish.ComputerSystem_api import ComputerSystemCollectionAPI, ComputerSystemAPI, CreateComputerSystem
from .redfish.processor import Processor, Processors
from .redfish.memory import Memory, MemoryCollection
from .redfish.simplestorage import SimpleStorage, SimpleStorageCollection
from .redfish.ethernetinterface import EthernetInterfaceCollection, EthernetInterface
from .redfish.ResetActionInfo_api import ResetActionInfo_API
from .redfish.ResetAction_api import ResetAction_API
# PCIe Switch imports
from .redfish.pcie_switch_api import PCIeSwitchesAPI, PCIeSwitchAPI
# CompositionService imports
from .redfish.CompositionService_api import CompositionServiceAPI
from .redfish.ResourceBlock_api import ResourceBlockCollectionAPI, ResourceBlockAPI, CreateResourceBlock
from .redfish.ResourceZone_api import ResourceZoneCollectionAPI, ResourceZoneAPI, CreateResourceZone

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
            #self.AccountService =   load_static('AccountService', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Registries =       load_static('Registries', 'redfish', mode, rest_base, self.resource_dictionary)
            self.SessionService =   load_static('SessionService', 'redfish', mode, rest_base, self.resource_dictionary)
            #self.TaskService =      load_static('TaskService', 'redfish', mode, rest_base, self.resource_dictionary)
            #self.EventService =     load_static('EventService', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Chassis =          load_static('Chassis', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Storage =          load_static('Storage', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Fabrics =          load_static('Fabrics', 'redfish', mode, rest_base, self.resource_dictionary)
            #self.Systems=           load_static('Systems', 'redfish', mode, rest_base, self.resource_dictionary)
            #self.Managers =         load_static('Managers', 'redfish', mode, rest_base, self.resource_dictionary)

#        if "Swordfish" in mockupfolders:
#            self.StorageServices = load_static('StorageServices', 'redfish', mode, rest_base, self.resource_dictionary)
#            self.StorageSystems = load_static('StorageSystems', 'redfish', mode, rest_base, self.resource_dictionary)

        # Attach APIs for dynamic resources

        # EventService Resources
        g.api.add_resource(EventServiceAPI, '/redfish/v1/EventService',
                resource_class_kwargs={'rb': g.rest_base, 'id': "EventService"})
        # EventService SubResources
        g.api.add_resource(SubscriptionCollectionAPI, '/redfish/v1/EventService/Subscriptions')
        g.api.add_resource(SubscriptionAPI, '/redfish/v1/EventService/Subscriptions/<string:ident>',
                resource_class_kwargs={'rb': g.rest_base})

        # SessionService Resources
        g.api.add_resource(SessionServiceAPI, '/redfish/v1/SessionService',
                resource_class_kwargs={'rb': g.rest_base, 'id': "SessionService"})
        # SessionService SubResources
        g.api.add_resource(SessionCollectionAPI, '/redfish/v1/SessionService/Sessions')
        g.api.add_resource(SessionAPI, '/redfish/v1/SessionService/Sessions/<string:ident>',
                resource_class_kwargs={'rb': g.rest_base})

        # Chassis Resources
        g.api.add_resource(ChassisCollectionAPI, '/redfish/v1/Chassis')
        g.api.add_resource(ChassisAPI, '/redfish/v1/Chassis/<string:ident>',
                resource_class_kwargs={'rb': g.rest_base})
        # Chassis SubResources
        g.api.add_resource(ThermalAPI, '/redfish/v1/Chassis/<string:ident>/Thermal',
                resource_class_kwargs={'rb': g.rest_base})
        # Chassis SubResources
        g.api.add_resource(PowerAPI, '/redfish/v1/Chassis/<string:ident>/Power',
                resource_class_kwargs={'rb': g.rest_base})

        g.api.add_resource(DrivesCollectionAPI,
                            '/redfish/v1/Chassis/<string:chassis>/Drives')
        g.api.add_resource(DrivesAPI,
                            '/redfish/v1/Chassis/<string:chassis>/Drives/<string:drives>')

        g.api.add_resource(NetworkAdaptersCollectionAPI,
                            '/redfish/v1/Chassis/<string:chassis>/NetworkAdapters')
        g.api.add_resource(NetworkAdaptersAPI,
                            '/redfish/v1/Chassis/<string:chassis>/NetworkAdapters/<string:network_adapter>')

        g.api.add_resource(NetworkDeviceFunctionsCollectionAPI,
                            '/redfish/v1/Chassis/<string:chassis>/NetworkAdapters/<string:network_adapter>/NetworkDeviceFunctions')
        g.api.add_resource(NetworkDeviceFunctionsAPI,
                            '/redfish/v1/Chassis/<string:chassis>/NetworkAdapters/<string:network_adapter>/NetworkDeviceFunctions/<string:network_device_functions>')

        g.api.add_resource(NWPortsCollectionAPI,
                            '/redfish/v1/Chassis/<string:chassis>/NetworkAdapters/<string:network_adapter>/Ports')
        g.api.add_resource(NWPortsAPI,
                            '/redfish/v1/Chassis/<string:chassis>/NetworkAdapters/<string:network_adapter>/Ports/<string:nw_ports>')

        # Manager Resources
        g.api.add_resource(ManagerCollectionAPI, '/redfish/v1/Managers')
        g.api.add_resource(ManagerAPI, '/redfish/v1/Managers/<string:ident>', resource_class_kwargs={'rb': g.rest_base})

        # EgResource Resources (Example entries for attaching APIs)
        # g.api.add_resource(EgResourceCollectionAPI,
        #     '/redfish/v1/EgResources')
        # g.api.add_resource(EgResourceAPI,
        #     '/redfish/v1/EgResources/<string:ident>',
        #     resource_class_kwargs={'rb': g.rest_base})
        #
        # EgResource SubResources (Example entries for attaching APIs)
        # g.api.add_resource(EgSubResourceCollection,
        #     '/redfish/v1/EgResources/<string:ident>/EgSubResources',
        #     resource_class_kwargs={'rb': g.rest_base})
        # g.api.add_resource(EgSubResource,
        #     '/redfish/v1/EgResources/<string:ident1>/EgSubResources/<string:ident2>',
        #     resource_class_kwargs={'rb': g.rest_base})

        # System Resources
        g.api.add_resource(ComputerSystemCollectionAPI, '/redfish/v1/Systems')
        g.api.add_resource(ComputerSystemAPI, '/redfish/v1/Systems/<string:ident>',
                resource_class_kwargs={'rb': g.rest_base})
        # System SubResources
        g.api.add_resource(Processors, '/redfish/v1/Systems/<string:ident>/Processors',
                resource_class_kwargs={'rb': g.rest_base,'suffix':'Systems'})
        g.api.add_resource(Processor, '/redfish/v1/Systems/<string:ident1>/Processors/<string:ident2>',
                '/redfish/v1/CompositionService/ResourceBlocks/<string:ident1>/Processors/<string:ident2>')
        # System SubResources
        g.api.add_resource(MemoryCollection, '/redfish/v1/Systems/<string:ident>/Memory',
                 resource_class_kwargs={'rb': g.rest_base,'suffix':'Systems'})
        g.api.add_resource(Memory, '/redfish/v1/Systems/<string:ident1>/Memory/<string:ident2>',
                '/redfish/v1/CompositionService/ResourceBlocks/<string:ident1>/Memory/<string:ident2>')
        # System SubResources
        g.api.add_resource(SimpleStorageCollection, '/redfish/v1/Systems/<string:ident>/SimpleStorage',
                resource_class_kwargs={'rb': g.rest_base,'suffix':'Systems'})
        g.api.add_resource(SimpleStorage, '/redfish/v1/Systems/<string:ident1>/SimpleStorage/<string:ident2>',
                '/redfish/v1/CompositionService/ResourceBlocks/<string:ident1>/SimpleStorage/<string:ident2>')
        # System SubResources
        g.api.add_resource(EthernetInterfaceCollection, '/redfish/v1/Systems/<string:ident>/EthernetInterfaces',
                resource_class_kwargs={'rb': g.rest_base,'suffix':'Systems'})
        g.api.add_resource(EthernetInterface, '/redfish/v1/Systems/<string:ident1>/EthernetInterfaces/<string:ident2>',
                '/redfish/v1/CompositionService/ResourceBlocks/<string:ident1>/EthernetInterfaces/<string:ident2>')
        # System SubResources
        g.api.add_resource(ResetActionInfo_API, '/redfish/v1/Systems/<string:ident>/ResetActionInfo',
                resource_class_kwargs={'rb': g.rest_base})
        g.api.add_resource(ResetAction_API, '/redfish/v1/Systems/<string:ident>/Actions/ComputerSystem.Reset',
                resource_class_kwargs={'rb': g.rest_base})

        # Storage Resources
        g.api.add_resource(StorageCollectionAPI, '/redfish/v1/Storage')
        g.api.add_resource(StorageAPI, '/redfish/v1/Storage/<string:ident>',
                '/redfish/v1/Storage/<string:storage>')
        # Storage SubResources
        g.api.add_resource(StorageGroupsCollectionAPI,
                            '/redfish/v1/Storage/<string:storage>/StorageGroups')
        g.api.add_resource(StorageGroupsAPI,
                           '/redfish/v1/Storage/<string:storage>/StorageGroups/<string:storage_groups>')
        g.api.add_resource(StoragePoolsCollectionAPI,
                           '/redfish/v1/Storage/<string:storage>/StoragePools')
        g.api.add_resource(StoragePoolsAPI,
                            '/redfish/v1/Storage/<string:storage>/StoragePools/<string:storage_pools>')
        g.api.add_resource(VolumesCollectionAPI,
                            '/redfish/v1/Storage/<string:storage>/Volumes')
        g.api.add_resource(VolumesAPI,
                            '/redfish/v1/Storage/<string:storage>/Volumes/<string:volumes>')
        g.api.add_resource(StorageControllersCollectionAPI,
                            '/redfish/v1/Storage/<string:storage>/Controllers')
        g.api.add_resource(StorageControllersAPI,
                            '/redfish/v1/Storage/<string:storage>/Controllers/<string:storage_controllers>')

        # Fabric Resources
        g.api.add_resource(FabricCollectionAPI, '/redfish/v1/Fabrics')
        g.api.add_resource(FabricAPI, '/redfish/v1/Fabrics/<string:fabric>',
                        '/redfish/v1/Fabrics/<string:fabric>')
        # Fabric SubResources
        g.api.add_resource(FabricsEndpointsCollectionAPI,
                            '/redfish/v1/Fabrics/<string:fabric>/Endpoints')
        g.api.add_resource(FabricsEndpointsAPI,
                            '/redfish/v1/Fabrics/<string:fabric>/Endpoints/<string:f_endpoint>')
        g.api.add_resource(FabricsEndpointGroupsCollectionAPI,
                            '/redfish/v1/Fabrics/<string:fabric>/EndpointGroups')
        g.api.add_resource(FabricsEndpointGroupsAPI,
                            '/redfish/v1/Fabrics/<string:fabric>/EndpointGroups/<string:f_endpoint_group>')
        g.api.add_resource(FabricsZonesCollectionAPI,
                            '/redfish/v1/Fabrics/<string:fabric>/Zones')
        g.api.add_resource(FabricsZonesAPI,
                            '/redfish/v1/Fabrics/<string:fabric>/Zones/<string:f_zone>')
        g.api.add_resource(FabricsConnectionsCollectionAPI,
                            '/redfish/v1/Fabrics/<string:fabric>/Connections')
        g.api.add_resource(FabricsConnectionsAPI,
                            '/redfish/v1/Fabrics/<string:fabric>/Connections/<string:f_connection>')
        g.api.add_resource(FabricsSwitchesCollectionAPI,
                            '/redfish/v1/Fabrics/<string:fabric>/Switches')
        g.api.add_resource(FabricsSwitchesAPI,
                            '/redfish/v1/Fabrics/<string:fabric>/Switches/<string:f_switch>')
        g.api.add_resource(FabricsSwitchPortsCollectionAPI,
                            '/redfish/v1/Fabrics/<string:fabric>/Switches/<string:f_switch>/Ports/')
        g.api.add_resource(FabricsSwitchPortsAPI,
                            '/redfish/v1/Fabrics/<string:fabric>/Switches/<string:f_switch>/Ports/<string:f_switch_port>')
        # FileSystems
        g.api.add_resource(FileSystemsCollectionAPI,
                            '/redfish/v1/Storage/<string:storage>/FileSystems')
        g.api.add_resource(FileSystemsAPI,
                            '/redfish/v1/Storage/<string:storage>/FileSystems/<string:file_systems>')

        # PCIe Switch Resources
        #g.api.add_resource(PCIeSwitchesAPI, '/redfish/v1/PCIeSwitches')
        #g.api.add_resource(PCIeSwitchAPI, '/redfish/v1/PCIeSwitches/<string:ident>',
        #        resource_class_kwargs={'rb': g.rest_base})

        # Composition Service Resources
        g.api.add_resource(CompositionServiceAPI, '/redfish/v1/CompositionService',
                resource_class_kwargs={'rb': g.rest_base, 'id': "CompositionService"})
        # Composition Service SubResources
        g.api.add_resource(ResourceBlockCollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks')
        g.api.add_resource(ResourceBlockAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ident>',
                resource_class_kwargs={'rb': g.rest_base})
        # Composition Service SubResources
        g.api.add_resource(ResourceZoneCollectionAPI, '/redfish/v1/CompositionService/ResourceZones')
        g.api.add_resource(ResourceZoneAPI, '/redfish/v1/CompositionService/ResourceZones/<string:ident>',
                resource_class_kwargs={'rb': g.rest_base})

        # Storage Services - API and Collection
        g.api.add_resource(StorageServicesCollectionAPI, '/redfish/v1/StorageServices')
        g.api.add_resource(StorageServicesAPI, '/redfish/v1/StorageServices/<string:storage_service>')
        #g.api.add_resource(StorageGroupsCollectionAPI,
        #                    '/redfish/v1/StorageServices/<string:storage_service>/StorageGroups')
        #g.api.add_resource(StorageGroupsAPI,
        #                   '/redfish/v1/StorageServices/<string:storage_service>/StorageGroups/<string:storage_groups>')
        #g.api.add_resource(StoragePoolsCollectionAPI,
        #                   '/redfish/v1/StorageServices/<string:storage_service>/StoragePools')
        #g.api.add_resource(StoragePoolsAPI,
        #                    '/redfish/v1/StorageServices/<string:storage_service>/StoragePools/<string:storage_pools>')

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
        g.api.add_resource(IOConnectivityLoSCapabilitiesAPI,
                           '/redfish/v1/StorageServices/<string:storage_service>/IOConnectivityLoSCapabilities')
        g.api.add_resource(IOPerformanceLoSCapabilitiesAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/IOPerformanceLoSCapabilities')
        g.api.add_resource(StorageSubsystemsAPI,
                            '/redfish/v1/StorageServices/<string:storage_service>/StorageSubsystems')

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
            '@odata.type': '#ServiceRoot.v1_9_0.ServiceRoot',
            '@odata.id': self.rest_base,
            'Id': 'RootService',
            'Name': 'Root Service',
            'RedfishVersion': '1.6.0',
            'UUID': self.uuid,
            'Chassis': {'@odata.id': self.rest_base + 'Chassis'},
            'Fabrics': {'@odata.id': self.rest_base + 'Fabrics'},
            # 'EgResources': {'@odata.id': self.rest_base + 'EgResources'},
            #'Managers': {'@odata.id': self.rest_base + 'Managers'},
            #'TaskService': {'@odata.id': self.rest_base + 'TaskService'},
            'SessionService': {'@odata.id': self.rest_base + 'SessionService'},
            #'StorageServices': {'@odata.id': self.rest_base + 'StorageServices'},
            #'StorageSystems': {'@odata.id': self.rest_base + 'StorageSystems'},
            #'AccountService': {'@odata.id': self.rest_base + 'AccountService'},
            'EventService': {'@odata.id': self.rest_base + 'EventService'},
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
