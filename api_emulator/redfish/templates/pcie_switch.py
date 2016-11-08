#
# Copyright (c) 2016 Intel Corporation. All Rights Reserved.
# Copyright (c) 2016, The Storage Networking Industry Association.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. 
#
# Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
# Neither the name of The Storage Networking Industry Association (SNIA) nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import copy

PCIeSwitch_TEMPLATE={
    "@odata.type": "#PCIeSwitch.v1_0_0.PCIeSwitch",
    "@odata.context": "{rb}$metadata#PCIeSwitches/Members/$entity",
    "@odata.id": "{rb}PCIeSwitches/{id}",

    "Name": "PCIe Switch",
    "Id": "{id}",

    "TotalLanes": 196,
    "MaxLaneBandwidthGBps": 1,

    "Manufacturer": "Intel Corporation",
    "Model": "Intel PCIe Switch",
    "SerialNumber": "2M220100SL",
    "PartNumber": "",
    "Status": {
        "State": "Enabled",
        "Health": "OK"
    },

    "Ports": {
        "@odata.id": "{rb}PCIeSwitches/{id}/Ports"
    },
    "Devices": {
        "@odata.id": "{rb}PCIeSwitches/{id}/Devices"
    },
    "FunctionMaps": {
        "@odata.id": "{rb}PCIeSwitches/{id}/Zones"
    },
    "Links": {
        "Chassis": [
            {
                "@odata.id": "{rb}Chassis/1"
            }
        ],
        "ManagedBy": [
            {
                "@odata.id": "{rb}Managers/Manager_1"
            }
        ]
    },
    "Actions": {
        "#PCIeSwitch.Reset": {
            "target": "{rb}PCIeSwitches/{id}/Actions/PCIeSwitch.Reset",
            "SwitchResetType@Redfish.AllowableValues": [
                "On",
                "Off",
                "Restart",
            ]
        }
    }
}

def get_PCIeSwitch_template(rest_base,ident):

    # Perform deepcopy for dictionaries
    c=copy.deepcopy(PCIeSwitch_TEMPLATE)

    # Replace variables with correct values for this instance
    c['@odata.context'] = c['@odata.context'].format(rb=rest_base)
    c['@odata.id'] = c['@odata.id'].format(rb=rest_base, id=ident)
    c['Id'] = c['Id'].format(id=ident)
    c['Devices']['@odata.id']=c['Devices']['@odata.id'].format(rb=rest_base, id=ident)
    c['Ports']['@odata.id']=c['Ports']['@odata.id'].format(rb=rest_base, id=ident)
    c['FunctionMaps']['@odata.id']=c['FunctionMaps']['@odata.id'].format(rb=rest_base,id=ident)
    c['Links']['Chassis'][0]['@odata.id']=c['Links']['Chassis'][0]['@odata.id'].format(rb=rest_base)
    c['Links']['ManagedBy'][0]['@odata.id']=c['Links']['ManagedBy'][0]['@odata.id'].format(rb=rest_base)
    c['Actions']['#PCIeSwitch.Reset']['target']= c['Actions']['#PCIeSwitch.Reset']['target'].format(rb=rest_base,id=ident)

    return c
