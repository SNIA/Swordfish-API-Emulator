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
#from api_emulator.utils import timestamp


_TEMPLATE = \
    {
        "@odata.context": "{rb}$metadata#Chassis/Links/Members/{id}/Links/ThermalMetrics/$entity",
        "@odata.id": "{rb}Chassis/{id}/ThermalMetrics",
        "@odata.type": "#ThermalMetrics.1.0.0.ThermalMetrics",
        "Id": "ThermalMetrics",
        "Name": "Thermal Metrics",
        #"Modified": None,
        "Temperatures": [
            {
                
                "@odata.id": "{rb}Chassis/{id}/Thermalmetrics#/Temperatures/0",
                "MemberId": "0",
                "Name": "CPU1 Temp",
                "SensorNumber": 42,
                "Status": {
                    "State": "Enabled",
                    "Health": "OK"
                },
                #"Units": "Celsius",
                "ReadingCelcius": 21,
                "UpperThresholdNonCritical": 42,
                "UpperThresholdCritical": 42,
                "UpperThresholdFatal": 42,
                "LowerThresholdNonCritical": 42,
                "LowerThresholdCritical": 5,
                "LowerThresholdFatal": 42,
                "MinimumValue": 0,
                "MaximumValue": 200,
                "PhysicalContext": "CPU",
                "RelatedItem": [
                {"@odata.id": "{rb}Systems/{id}#/Processors/0" }
            ]
        
                #"CorrelatableID": "ReferenceToAPotentialThingLikeAProcessor"
            },
            {
            "@odata.id": "{rb}Chassis/{id}/ThermalMetrics#/Temperatures/1",
            "MemberId": "1",
            "Name": "CPU2 Temp",
            "SensorNumber": 43,
            "Status": {
                "State": "Enabled",
                "Health": "OK"
            },
            "ReadingCelsius": 21,
            "UpperThresholdNonCritical": 42,
            "UpperThresholdCritical": 42,
            "UpperThresholdFatal": 42,
            "LowerThresholdNonCritical": 42,
            "LowerThresholdCritical": 5,
            "LowerThresholdFatal": 42,
            "MinReadingRange": 0,
            "MaxReadingRange": 200,
            "PhysicalContext": "CPU",
            "RelatedItem": [
                {"@odata.id": "{rb}Systems/{id}#/Processors/1" }
            ]
        },

            {
            "@odata.id": "{rb}Chassis/{id}/ThermalMetrics#/Temperatures/2",
            "MemberId": "2",
            "Name": "Chassis Intake Temp",
            "SensorNumber": 44,
            "Status": {
                "State": "Enabled",
                "Health": "OK"
            },
            "ReadingCelsius": 25,
            "UpperThresholdNonCritical": 30,
            "UpperThresholdCritical": 40,
            "UpperThresholdFatal": 50,
            "LowerThresholdNonCritical": 10,
            "LowerThresholdCritical": 5,
            "LowerThresholdFatal": 0,
            "MinReadingRange": 0,
            "MaxReadingRange": 200,
            "PhysicalContext": "Intake",
            "RelatedItem": [
                {"@odata.id": "{rb}Chassis/{id}" },
                {"@odata.id": "{rb}Systems/{id}" }
            ]
        }
    ],
    
           
        "Fans": [
            {
                "@odata.id":"{rb}Chassis/{id}/ThermalMetrics#/Fans/0",
                "MemberId":"0",
                "FanName": "BaseBoard System Fan",
                #"CorrelatableID": "Chassis/1/Fan1",
                "PhysicalContext": "Backplane",
                "Status": {
                    "State": "Enabled",
                    "Health": "OK"
                },
                "ReadingRPM": 2100,
                "UpperThresholdNonCritical": 42,
                "UpperThresholdCritical": 4200,
                "UpperThresholdFatal": 42,
                "LowerThresholdNonCritical": 42,
                "LowerThresholdCritical": 5,
                "LowerThresholdFatal": 42,
                "MinReadingRange": 0,
                "MaxReadingRange": 5000,
                "Redundancy" : [ 
                {"@odata.id": "{rb}Chassis/{id}/ThermalMetrics#/Redundancy/0"}
            ],
            "RelatedItem" : [
                {"@odata.id": "{rb}Systems/{id}" },
                {"@odata.id": "{rb}Chassis/{id}" }
            ] 

            },
            {
                "@odata.id": "{rb}Chassis/{id}/ThermalMetrics#/Fans/1",
                "MemberId": "1",
                "FanName": "BaseBoard System Fan Backup",
                #"CorrelatableID": "Chassis/1/Fan2",
                "PhysicalContext": "Backplane",
                "Status": {
                    "State": "Enabled",
                    "Health": "OK"
                },
                #"Units": "RPM",
                "ReadingRPM": 2100,
                "UpperThresholdNonCritical": 42,
                "UpperThresholdCritical": 4200,
                "UpperThresholdFatal": 42,
                "LowerThresholdNonCritical": 42,
                "LowerThresholdCritical": 5,
                "LowerThresholdFatal": 42,
                "MinReadingRange": 0,
                "MaxReadingRange": 5000,
                "Redundancy" : [
                {"@odata.id": "{rb}Chassis/{id}/PowerMetrics#/Redundancy/0"}
            ],
            "RelatedItem" : [
                {"@odata.id": "{rb}Systems/{id}" },
                {"@odata.id": "{rb}Chassis/{id}" }
            ] 

                
            }
        ],
        "Redundancy": [
            {
                "@odata.id": "{rb}Chassis/{id}/ThermalMetrics#/Redundancy/0",
                "MemberId": "0",
                "Name": "BaseBoard System Fans",
                #"ActiveCorrelatableIDs": [
                    #"/rest/v1/Chassis/1/Fan1",
                    #"/rest/v1/Chassis/1/Fan2"
                #],
                "RedundancySet": [
                { "@odata.id": "{rb}Chassis/{id}/ThermalMetrics#/Fans/0" },
                { "@odata.id": "{rb}Chassis/{id}/ThermalMetrics#/Fans/1" }
            ],

                "Mode": "N+1",
                "Status": {
                    "State": "Enabled",
                    "Health": "OK"
                },
                "MinNumNeeded": 1,
                "MaxNumSupported": 2
            }
        ]
    }


def get_thermal_metrics_template(rest_base, ident):
    """
    Returns a formatted template

    Arguments:
        rest_base - Base URL of the RESTful interface
        ident     - Identifier of the chassis
    """
    c = _TEMPLATE.copy()
    #c['Modified'] = timestamp()
    c['@odata.context'] = c['@odata.context'].format(rb=rest_base, id=ident)
    c['@odata.id'] = c['@odata.id'].format(rb=rest_base, id=ident)
    c['Redundancy'][0]['@odata.id']=c['Redundancy'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['Fans'][0]['@odata.id']=c['Fans'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['Fans'][1]['@odata.id']=c['Fans'][1]['@odata.id'].format(rb=rest_base,id=ident)
    c['Temperatures'][0]['@odata.id']=c['Temperatures'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['Temperatures'][0]['RelatedItem'][0]['@odata.id']=c['Temperatures'][0]['RelatedItem'][0]['@odata.id'].format(rb=rest_base,id=ident)
    
    c['Temperatures'][1]['@odata.id']=c['Temperatures'][1]['@odata.id'].format(rb=rest_base,id=ident)
    c['Temperatures'][1]['RelatedItem'][0]['@odata.id']=c['Temperatures'][1]['RelatedItem'][0]['@odata.id'].format(rb=rest_base,id=ident)
   
    c['Temperatures'][2]['@odata.id']=c['Temperatures'][2]['@odata.id'].format(rb=rest_base,id=ident)
    c['Temperatures'][2]['RelatedItem'][0]['@odata.id']=c['Temperatures'][2]['RelatedItem'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['Temperatures'][2]['RelatedItem'][1]['@odata.id']=c['Temperatures'][2]['RelatedItem'][1]['@odata.id'].format(rb=rest_base,id=ident)
    c['Fans'][0]['Redundancy'][0]['@odata.id']=c['Fans'][0]['Redundancy'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['Fans'][0]['RelatedItem'][0]['@odata.id']=c['Fans'][0]['RelatedItem'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['Fans'][0]['RelatedItem'][1]['@odata.id']=c['Fans'][0]['RelatedItem'][1]['@odata.id'].format(rb=rest_base,id=ident)
    c['Fans'][1]['Redundancy'][0]['@odata.id']=c['Fans'][1]['Redundancy'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['Fans'][1]['RelatedItem'][0]['@odata.id']=c['Fans'][1]['RelatedItem'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['Fans'][1]['RelatedItem'][1]['@odata.id']=c['Fans'][1]['RelatedItem'][1]['@odata.id'].format(rb=rest_base,id=ident)
    c['Redundancy'][0]['RedundancySet'][0]['@odata.id']=c['Redundancy'][0]['RedundancySet'][0]['@odata.id'].format(rb=rest_base,id=ident)
    c['Redundancy'][0]['RedundancySet'][1]['@odata.id']=c['Redundancy'][0]['RedundancySet'][1]['@odata.id'].format(rb=rest_base,id=ident)
    
    return c
