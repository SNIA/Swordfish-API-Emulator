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

"""
PowerMetrics template
"""
from api_emulator.utils import timestamp

_TEMPLATE = \
    {
        "@odata.context": "{rb}$metadata#Chassis/Links/Members/{id}/Links/PowerMetrics/$entity",
        "@odata.id": "{rb}Chassis/{id}/PowerMetrics",
        "@odata.type": "#Power.1.0.0.PowerMetrics",
        "Id": "PowerMetrics",
        "Name": "Power",
	"PowerControl": [
        {
        "@odata.id": "{rb}Chassis/{id}/PowerMetrics#/PowerControl/0",
        "MemberId": "0",
	"Name": "System Power Control",
        "PowerConsumedWatts": 8000,
        "PowerRequestedWatts": 8500,
        "PowerAvailableWatts": 8500,
        "PowerCapacityWatts": 10000,
        "PowerAllocatedWatts": 8500,
        "PowerMetrics": {
            "IntervalInMin": 30,
            "MinConsumedWatts": 7500,
            "MaxConsumedWatts": 8200,
            "AverageConsumedWatts": 8000
        },
        "PowerLimit": {
            "LimitInWatts": 9000,
            "LimitException": "LogEventOnly",
            "CorrectionInMs": 42          
        },
	"RelatedItem": [ 
                {"@odata.id": "{rb}Systems/{id}"},
                {"@odata.id": "{rb}Chassis/{id}"},
                {"@odata.id": "{rb}Systems/{id}/Processors/1"},
                {"@odata.id": "{rb}Systems/{id}/Processors/2"}
            ],
    	    "Status": {
	            "State": "Enabled",
	            "Health": "OK"
	        },
	    "Oem": {}
        }
    ],
    "Voltages": [
        {
            "@odata.id": "{rb}Chassis/{id}/PowerMetrics#/Voltages/0",
            "MemberId": "0",
            "Name": "VRM1 Voltage",
            "SensorNumber": 11,
            "Status": {
                "State": "Enabled",
                "Health": "OK"
            },
            "ReadingVolts": 12,
            "UpperThresholdNonCritical": 12.5,
            "UpperThresholdCritical": 13,
            "UpperThresholdFatal": 15,
            "LowerThresholdNonCritical": 11.5,
            "LowerThresholdCritical": 11,
            "LowerThresholdFatal": 10,
            "MinReadingRange": 0,
            "MaxReadingRange": 20,
            "PhysicalContext": "VoltageRegulator",
            "RelatedItem": [
                {"@odata.id": "{rb}Systems/{id}" },
                {"@odata.id": "{rb}Chassis/{id}" }
            ]
        },
        {
            "@odata.id": "{rb}Chassis/{id}/PowerMetrics#/Voltages/1",
            "MemberId": "1",
            "Name": "VRM2 Voltage",
            "SensorNumber": 12,
            "Status": {
                "State": "Enabled",
                "Health": "OK"
            },
            "ReadingVolts": 5,
            "UpperThresholdNonCritical": 5.5,
            "UpperThresholdCritical": 7,
            "LowerThresholdNonCritical": 4.75,
            "LowerThresholdCritical": 4.5,
            "MinReadingRange": 0,
            "MaxReadingRange": 20,
            "PhysicalContext": "VoltageRegulator",
            "RelatedItem": [
                {"@odata.id": "{rb}Systems/{id}" },
                {"@odata.id": "{rb}Chassis/{id}" }
            ]
        }
    ],

        "PowerSupplies": [
            {
		"@odata.id": "{rb}Chassis/{id}/PowerMetrics#/PowerSupplies/0",
                "MemberId": "0",
                "Name": "Power Supply Bay 1",
                "Status": {
                    "State": "Enabled",
                    "Health": "Warning"
                },
                "Oem": {},
                "PowerSupplyType": "DC",
                "LineInputVoltageType": "DCNeg48V",
                "LineInputVoltage": -48,
                "PowerCapacityWatts": 400,
                "LastPowerOutputWatts": 192,
                "Model": "499253-B21",
                "FirmwareVersion": "1.00",
                "SerialNumber": "1z0000001",
                "PartNumber": "1z0000001A3a",
                "SparePartNumber": "0000001A3a",
		"RelatedItem": [
              { "@odata.id": "{rb}Chassis/{id}" }
            ],
            "Redundancy": [
              { "@odata.id": "{rb}Chassis/{id}/PowerMetrics#/Redundancy/0" }
            ]

		
            },
            {
		"@odata.id": "{rb}Chassis/{id}/PowerMetrics#/PowerSupplies/1",
                "MemberId": "1",
                "Name": "Power Supply Bay 2",
                "Status": {
                    "State": "Disabled",
                    "Health": "Warning"
                },
                "Oem": {},
                "PowerSupplyType": "AC",
                "LineInputVoltageType": "ACMidLine",
                "LineInputVoltage": 220,
                "PowerCapacityWatts": 400,
                "LastPowerOutputWatts": 190,
                "Model": "499253-B21",
                "FirmwareVersion": "1.00",
                "SerialNumber": "1z0000001",
                "PartNumber": "1z0000001A3a",
                "SparePartNumber": "0000001A3a",
		"RelatedItem": [
              { "@odata.id": "{rb}Chassis/{id}" }
            ],
            "Redundancy": [
              { "@odata.id": "{rb}Chassis/{id}/PowerMetrics#/Redundancy/0" }
            ]

            },
            {
		"@odata.id": "{rb}Chassis/{id}/PowerMetrics#/PowerSupplies/2",
                 "MemberId": "2",
		 "Name": "Power Supply Bay 3",
                 "Status": {
                    "State": "Absent"
                }
            }
        ],
        "Redundancy": [
            {
		"@odata.id": "{rb}Chassis/{id}/PowerMetrics#/Redundancy/0",
                "MemberId": "0",
                "Mode": "Failover",
                "Name": "PowerSupply Redundancy Group 1",
                "MaxNumSupported": 2,
                "MinNumNeeded": 1,
                "Status": {
                    "State": "Offline",
                    "Health": "OK"
                }
            }
        ],
        "Oem": {}
    }


def get_power_metrics_template(rest_base, ident):
    """
    Returns a formatted template

    Arguments:
        rest_base - Base URL of the RESTful interface
        ident     - Identifier of the chassis
    """
    c = _TEMPLATE.copy()
    c['@odata.context'] = c['@odata.context'].format(rb=rest_base, id=ident)
    c['@odata.id'] = c['@odata.id'].format(rb=rest_base, id=ident)
    c['PowerControl'][0]['@odata.id']=c['PowerControl'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['PowerControl'][0]['RelatedItem'][0]['@odata.id']=c['PowerControl'][0]['RelatedItem'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['PowerControl'][0]['RelatedItem'][1]['@odata.id']=c['PowerControl'][0]['RelatedItem'][1]['@odata.id'].format(rb=rest_base,id=ident)
    c['PowerControl'][0]['RelatedItem'][2]['@odata.id']=c['PowerControl'][0]['RelatedItem'][2]['@odata.id'].format(rb=rest_base,id=ident)
    c['PowerControl'][0]['RelatedItem'][3]['@odata.id']=c['PowerControl'][0]['RelatedItem'][3]['@odata.id'].format(rb=rest_base,id=ident)
    c['Voltages'][0]['@odata.id']=c['Voltages'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['Voltages'][0]['RelatedItem'][0]['@odata.id']=c['Voltages'][0]['RelatedItem'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['Voltages'][0]['RelatedItem'][1]['@odata.id']=c['Voltages'][0]['RelatedItem'][1]['@odata.id'].format(rb=rest_base,id=ident)
    c['Voltages'][1]['@odata.id']=c['Voltages'][1]['@odata.id'].format(rb=rest_base,id=ident)
    c['Voltages'][1]['RelatedItem'][0]['@odata.id']=c['Voltages'][1]['RelatedItem'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['Voltages'][1]['RelatedItem'][1]['@odata.id']=c['Voltages'][1]['RelatedItem'][1]['@odata.id'].format(rb=rest_base,id=ident)
    c['PowerSupplies'][0]['@odata.id']=c['PowerSupplies'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['PowerSupplies'][0]['RelatedItem'][0]['@odata.id']=c['PowerSupplies'][0]['RelatedItem'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['PowerSupplies'][0]['Redundancy'][0]['@odata.id']=c['PowerSupplies'][0]['Redundancy'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['PowerSupplies'][1]['@odata.id']=c['PowerSupplies'][1]['@odata.id'].format(rb=rest_base,id=ident)
    c['PowerSupplies'][1]['RelatedItem'][0]['@odata.id']=c['PowerSupplies'][1]['RelatedItem'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['PowerSupplies'][1]['Redundancy'][0]['@odata.id']=c['PowerSupplies'][1]['Redundancy'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['PowerSupplies'][2]['@odata.id']=c['PowerSupplies'][2]['@odata.id'].format(rb=rest_base,id=ident)
    c['Redundancy'][0]['@odata.id']=c['Redundancy'][0]['@odata.id'].format(rb=rest_base,id=ident)
    
    
    return c
