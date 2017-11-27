

import copy
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2015-2017 SNIA. All rights reserved.",
  "@odata.context": "{rb}$metadata#StorageService.StorageService",
  "@odata.id": "{rb}StorageServices/{id}",
  "@odata.type": "#StorageServiceCollection.1.0.0.StorageServiceCollection",
  "Name": "Storage Service Collection",
  "Id":"{id}",
  "Links":[],  
  "ClassesOfService": {"@odata.id": "{rb}StorageServices/{id}/ClassesOfService"},
  "Drives": {"@odata.id": "{rb}StorageServices/{id}/Drives"},    
  "EndpointGroups": {"@odata.id": "{rb}StorageServices/{id}/EndpointGroups"},
  "Endpoints": {"@odata.id": "{rb}StorageServices/{id}/Endpoints"}, 
  "StorageGroups": {"@odata.id": "{rb}StorageServices/{id}/StorageGroups"},
  "StoragePools": {"@odata.id": "{rb}StorageServices/{id}/StoragePools"},
  "Volumes": {
    "@odata.id": "{rb}StorageServices/{id}/Volumes"
  },
  "StorageSubsystems": {"@odata.id": "{rb}StorageServices/{id}/StorageSubsystems"},
  "DataProtectionLoSCapabilities": {
      "@odata.id": "{rb}StorageServices/{id}/DataProtectionLoSCapabilities"
    },
    "DataSecurityLoSCapabilities": {
      "@odata.id": "{rb}StorageServices/{id}/DataSecurityLoSCapabilities"
    },
    "DataStorageLoSCapabilities": {
      "@odata.id": "{rb}StorageServices/{id}/DataStorageLoSCapabilities"
    },
    "IOConnectivityLoSCapabilities": {
      "@odata.id": "{rb}StorageServices/{id}/IOConnectivityLoSCapabilities"
    },
    "IOPerformanceLoSCapabilities": {
      "@odata.id": "{rb}StorageServices/{id}/IOPerformanceLoSCapabilities"

    },
    "FileSystems": {"@odata.id": "{rb}StorageServices/{id}/FileSystems"},
  
  "Permissions": [
              {"Read": "True"},
              {"Write": "True"}],
  "Oem": []
}



def get_StorageServices_instance(wildcards):
    """
    Instantiates and formats the template

    Arguments:
        wildcard - A dictionary of wildcards strings and their repalcement values
    """
    c = copy.deepcopy(_TEMPLATE)
    c['@odata.context'] = c['@odata.context'].format(**wildcards)
    c['@odata.id'] = c['@odata.id'].format(**wildcards)
    c['Id'] = c['Id'].format(**wildcards)
    c['Drives']['@odata.id']=c['Drives']['@odata.id'].format(**wildcards)
    c['ClassesOfService']['@odata.id']=c['ClassesOfService']['@odata.id'].format(**wildcards)
    c['EndpointGroups']['@odata.id']=c['EndpointGroups']['@odata.id'].format(**wildcards)
    c['Endpoints']['@odata.id']=c['Endpoints']['@odata.id'].format(**wildcards)
    c['StorageGroups']['@odata.id']=c['StorageGroups']['@odata.id'].format(**wildcards)
    c['StoragePools'] ['@odata.id']=c['StoragePools']['@odata.id'].format(**wildcards)
    c['Volumes']['@odata.id']=c['Volumes']['@odata.id'].format(**wildcards)
    c['FileSystems']['@odata.id']=c['FileSystems']['@odata.id'].format(**wildcards)
    c['StorageSubsystems']['@odata.id']=c['StorageSubsystems']['@odata.id'].format(**wildcards)
    c['DataProtectionLoSCapabilities']['@odata.id']=c['DataProtectionLoSCapabilities']['@odata.id'].format(**wildcards)
    c['DataSecurityLoSCapabilities']['@odata.id']=c['DataSecurityLoSCapabilities']['@odata.id'].format(**wildcards)
    c['DataStorageLoSCapabilities']['@odata.id']=c['DataStorageLoSCapabilities']['@odata.id'].format(**wildcards)
    c['IOPerformanceLoSCapabilities']['@odata.id']=c['IOPerformanceLoSCapabilities']['@odata.id'].format(**wildcards)
    c['IOConnectivityLoSCapabilities']['@odata.id']=c['IOConnectivityLoSCapabilities']['@odata.id'].format(**wildcards)
    

    return c

  
