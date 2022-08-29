#!/usr/bin/env python3
# Copyright Notice:
# Copyright 2017-2019 DMTF. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/blob/master/LICENSE.md

# EthernetInterface.py

import copy
import strgen
from api_emulator.utils import replace_recurse

_TEMPLATE = \
{
    "@Redfish.Copyright": "Copyright 2014-2019 DMTF. All rights reserved.",
    "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
    "@odata.id": "/redfish/v1/Chassis/{ch_id}",
    "@odata.type": "#Chassis.v1_4_0.Chassis",
    "Id": "{id}",
    "Name": "Computer System Chassis",
    "ChassisType": "RackMount",
    "Manufacturer": "ManufacturerName",
    "Model": "ProductModelName",
    "SKU": "",
    "SerialNumber": "2M220100SL",
    "PartNumber": "",
    "AssetTag": "CustomerWritableThingy",
    "IndicatorLED": "Lit",
    "PowerState": "On",
    "Location": {
        "@odata.type": "#Resource.v1_3_0.Location",
        "PostalAddress": {
            "Country": "US",
            "Territory": "TX",
            "District": "Harris",
            "City": "Houston",
            "Street": "TX-249",
            "HouseNumber": 19550,
            "Floor": "1",
            "Name": "Excellent dining establishment",
            "PostalCode": "77070-3002"
        },
        "Placement": {
            "Row": "North",
            "Rack": "WEB43",
            "RackOffsetUnits": "EIA_310",
            "RackOffset": 12
        }
    },
    "Status": {
        "State": "Enabled",
        "Health": "OK"
    },
    "HeightMm": 44.45,
    "WidthMm": 431.8,
    "DepthMm": 711,
    "WeightKg": 15.31,
    "Thermal": {
        "@odata.id": "/redfish/v1/Chassis/{ch_id}/Thermal"
    },
    "Power": {
        "@odata.id": "/redfish/v1/Chassis/{ch_id}/Power"
    },
    "NetworkAdapters": {
        "@odata.id": "/redfish/v1/Chassis/{ch_id}/NetworkAdapters"
    },
    "Links": {
        "ComputerSystems": [
            {
                "@odata.id": "/redfish/v1/Systems/{cs_id}"
            }
        ],
        "ContainedBy": {
            "@odata.id": "/redfish/v1/Chassis/{ch_id}"
        },
        "ManagedBy": [
            {
                "@odata.id": "/redfish/v1/Managers/{mgr_id}"
            }
        ],
        "ManagersInChassis": [
            {
                "@odata.id": "/redfish/v1/Managers/{mgr_id}"
            }
        ],
        "PCIeDevices": [
            {
                "@odata.id": "/redfish/v1/Chassis/{ch_id}/PCIeDevices/NIC"
            }
        ],
        "Oem": {}
    },
    "Oem": {}
}

def get_EthernetInterface_instance(wildcards):
    c = copy.deepcopy(_TEMPLATE)
    replace_recurse(c, wildcards)
    return c
