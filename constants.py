# Copyright Notice:SNIA
# Copyright 2017 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/LICENSE.md



PATHS = {
    'Root': 'Resources/',
    
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
    'AddService':
    {
        'path': 'AddService/'

    }

}
