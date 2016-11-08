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

PCIePort_TEMPLATE={
    "@odata.context": "{rb}$metadata#PCIeSwitches/Members/{sw_id}/Ports/Members$entity",
    "@odata.type": "PCIePort.v1_0_0.PCIePort",
    "@odata.id": "{rb}PCIeSwitches/{sw_id}/Ports/{id}",
 
    "Id": "{id}",
    "Name": "PCIe Port",
    "Description": "PCIe port",
    "PortType": "Upstream",
    "PhysicalPort": "TRUE",

    "PortId": "2",
    "SpeedGBps": 4,
    "Width": 4,
    "MaxSpeedGBps": 8,
    "MaxWidth": 8,

    "OperationalState": "Up",
    "AdministrativeState": "Up",
    "Status": {
        "State": "Enabled",
        "Health": "OK"
    },
    
    "Actions": {
        "#PCIePort.SetState": {
            "target": "{rb}PCIeSwitches/{sw_id}/Ports/{id}/Actions/Port.SetState",
            "SetStateType@Redfish.AllowableValues": [
                "Up",
                "Down",
            ]
    },
}
    }


def get_PCIePort_template(rest_base,sw_id,ident):

    c = copy.deepcopy(PCIePort_TEMPLATE)

    c['@odata.context']=c['@odata.context'].format(rb=rest_base,sw_id=sw_id)
    c['@odata.id']=c['@odata.id'].format(rb=rest_base,sw_id=sw_id,id=ident)
    c['Id'] = c['Id'].format(id=ident)
    c['Actions']['#PCIePort.SetState']['target']=c['Actions']['#PCIePort.SetState']['target'].format(rb=rest_base,sw_id=sw_id,id=ident)

    return c
