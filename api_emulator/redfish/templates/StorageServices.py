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

#get_StorageServices_instance()


import copy
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2015-2021 SNIA. All rights reserved.",
  "@odata.id": "{rb}StorageServices/{id}",
  "@odata.type": "#StorageService.v1_5_0.StorageService",
  "Name": "Storage Service {id}",
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
    c['DataProtectionLoSCapabilities']['@odata.id']=c['DataProtectionLoSCapabilities']['@odata.id'].format(**wildcards)
    c['DataSecurityLoSCapabilities']['@odata.id']=c['DataSecurityLoSCapabilities']['@odata.id'].format(**wildcards)
    c['DataStorageLoSCapabilities']['@odata.id']=c['DataStorageLoSCapabilities']['@odata.id'].format(**wildcards)
    c['IOPerformanceLoSCapabilities']['@odata.id']=c['IOPerformanceLoSCapabilities']['@odata.id'].format(**wildcards)
    c['IOConnectivityLoSCapabilities']['@odata.id']=c['IOConnectivityLoSCapabilities']['@odata.id'].format(**wildcards)

    return c
