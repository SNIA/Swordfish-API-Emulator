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
#

#constants.py

PATHS = {
    'Root': 'Resources/',

     'Systems': {
          'path': 'Systems/',
          'drives': 'Drives/',
          'fabric_adapters': 'FabricAdapters/',
          'fabric_adapter_ports': 'Ports/'
      },


    'Chassis': {
         'path': 'Chassis/',
         'drives': 'Drives/',
         'c_memory': 'Memory/',
         'memory_domains': 'MemoryDomains/',
         'md_chunks': 'MemoryChunks/',
         'network_adapter': 'NetworkAdapters/',
         'network_device_functions': 'NetworkDeviceFunctions/',
         'nw_ports': 'Ports',
         'media_controllers': 'MediaControllers/',
         'mc_ports': 'Ports'
    },

   'Fabrics': {
       'path': 'Fabrics/',
       'f_switch': 'Switches/',
       'f_switch_port': 'Ports/',
       'f_endpoint': 'Endpoints/',
       'f_zone': 'Zones/',
       'f_connection': 'Connections/',
       'f_endpoint_group': 'EndpointGroups/'
   },

    'Storage': {
        'path': 'Storage/',
        'storage_groups': 'StorageGroups/',
        'storage_pools': 'StoragePools/',
        'storage_controllers': 'Controllers/',
        'capacity_sources': 'CapacitySources/',
        'volumes': 'Volumes/',
        'client_end_point_groups': 'ClientEndpointGroups/',
        'server_end_point_groups': 'ServerEndpointGroups/',
        'drives': 'Drives/',
        'classes_of_service': 'ClassesOfService/',
        'data_protection_los_capabilities': 'DataProtectionLoSCapabilities/',
        'data_security_los_capabilities': 'DataSecurityLoSCapabilities/',
        'data_storage_los_capabilities': 'DataStorageLoSCapabilities/',
        'ioconnectivity_los_capabilities': 'IOConnectivityLoSCapabilities/',
        'ioperformance_los_capabilities': 'IOPerformanceLoSCapabilities/',
        'endpoints': 'Endpoints/',
        'endpoint_groups': 'EndpointGroups/',
        'file_systems': 'FileSystems/'
    },

    'StorageServices': {
        'path': 'StorageServices/',
        'storage_groups': 'StorageGroups/',
        'storage_pools': 'StoragePools/',
        'volumes': 'Volumes/',
        'client_end_point_groups': 'ClientEndpointGroups/',
        'server_end_point_groups': 'ServerEndpointGroups/',
        'drives': 'Drives/',
        'classes_of_service': 'ClassesOfService/',
        'data_protection_los_capabilities': 'DataProtectionLoSCapabilities/',
        'data_security_los_capabilities': 'DataSecurityLoSCapabilities/',
        'data_storage_los_capabilities': 'DataStorageLoSCapabilities/',
        'ioconnectivity_los_capabilities': 'IOConnectivityLoSCapabilities/',
        'ioperformance_los_capabilities': 'IOPerformanceLoSCapabilities/',
        'endpoints': 'Endpoints/',
        'endpoint_groups': 'EndpointGroups/',
	    'storage_subsystems':'StorageSubsystems/',
        'file_systems': 'FileSystems/'

    },

    'StorageSystems': {
        'path': 'StorageSystems/'

    },

    'AddService':
    {
        'path': 'AddService/'

    }

}
