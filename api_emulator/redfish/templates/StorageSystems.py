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

#get_StorageSystems_instance()


import copy
from flask import json

_TEMPLATE = \
{
  "@Redfish.Copyright": "Copyright 2015-2021 SNIA. All rights reserved.",
  "@odata.id": "{rb}StorageSystems/{id}",
  "@odata.type": "#StorageSystem.v1_0_1.StorageSystem",
  "Name": "Storage System {id}",
  "Id":"{id}",
  "Links": {
        "StorageServices": [
            {
                "@odata.id": "/redfish/v1/StorageServices"
            }
                ],
        },
  "SystemType": "Physical",
    "AssetTag": "free form asset tag",
    "Manufacturer": "Manufacturer Name",
    "HostedServices": "sample",
    "HostingRoles": "sample",
    "Model": "Model Name",
    "SKU": "",
    "SerialNumber": "2M220100SL",
    "PartNumber": "",
    "Description": "Description of server",
    "UUID": "00000000-0000-0000-0000-000000000000",
    "HostName": "web-srv344",
    "Status": {
        "State": "Enabled",
        "Health": "OK",
        "HealthRollup": "OK"
    },
    "IndicatorLED": "Off",
    "PowerState": "On",
    "Boot": {
        "BootSourceOverrideEnabled": "Once",
        "BootSourceOverrideMode": "UEFI",
        "BootSourceOverrideTarget": "Pxe",
        "BootSourceOverrideTarget@Redfish.AllowableValues": [
            "None",
            "Pxe",
            "Floppy",
            "Cd",
            "Usb",
            "Hdd",
            "BiosSetup",
            "Utilities",
            "Diags",
            "UefiTarget",
            "SDCard",
            "UefiHttp"
        ],
        "UefiTargetBootSourceOverride": "uefi device path"
    },
    "BiosVersion": "P79 v1.00 (09/20/2013)",
    "ProcessorSummary": {
        "Count": 8,
        "Model": "Multi-Core Intel(R) Xeon(R) processor 7xxx Series",
        "Status": {
            "State": "Enabled",
            "Health": "OK",
            "HealthRollup": "OK"
        }
    },
    "MemorySummary": {
        "TotalSystemMemoryGiB": 16,
        "MemoryMirroring" : "System",
        "Status": {
            "State": "Enabled",
            "Health": "OK",
            "HealthRollup": "OK"
        }
    },
    "TrustedModules": [
        {
          "Status": {
            "State": "Enabled",
            "Health": "OK"
           },
           "ModuleType":"TPM2_0",
           "FirmwareVersion": "3.1",
           "FirmwareVersion2": "1",
           "InterfaceTypeSelection": "None"
        }
    ],


  "Permissions": [
              {"Read": "True"},
              {"Write": "True"}],
  "Oem": []
}



def get_StorageSystems_instance(wildcards):
    """
    Instantiates and formats the template

    Arguments:
        wildcard - A dictionary of wildcards strings and their repalcement values
    """
    c = copy.deepcopy(_TEMPLATE)
    c['@odata.id'] = c['@odata.id'].format(**wildcards)
    c['Id'] = c['Id'].format(**wildcards)


    return c
