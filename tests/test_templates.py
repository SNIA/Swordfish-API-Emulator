

test_chassis = {
    "@odata.type": "#Chassis.v1_21_0.Chassis",
    "Id": "1",
    "Name": "Test Chassis",
    "PowerState": "On",
    "ChassisType": "Drawer",
    "Status": {
        "State": "Enabled",
        "Health": "OK",
        "HealthRollup": "OK"
    },
    "Action": {
        "#Chassis.Reset": {
            "target": "/redfish/v1/Chassis/1/Actions/Chassis.Reset/",
            "ResetType@Redfish.AllowableValues": [
                "On",
                "ForceOff",
                "PushPowerButton",
                "PowerCycle"
            ]
        }
    },
    "@odata.id": "/redfish/v1/Chassis/1",
    "@Redfish.Copyright": "Copyright 2022 OpenFabrics Alliance. All rights reserved."
}

test_system = {
    "@odata.id": "/redfish/v1/Systems/1",
    "@odata.type": "#ComputerSystem.1.00.0.ComputerSystem",
    "Id": "1",
    "Name": "Compute Node 1",
    "SystemType": "Physical",
    "Manufacturer": "Manufacturer Name",
    "Model": "Model Name",
    "SKU": "",
    "Status": {
        "State": "Enabled",
        "Health": "OK",
        "HealthRollUp": "OK"
    },
    "IndicatorLED": "Off",
    "Power": "On",
    "Boot": {
        "BootSourceOverrideEnabled": "Once",
        "BootSourceOverrideTarget": "Pxe",
        "BootSourceOverrideSupported": [
            "None",
            "Pxe",
            "Floppy",
            "Cd",
            "Usb",
            "Hdd",
            "BiosSetup",
            "Utilities",
            "Diags",
            "UefiTarget"
        ],
        "UefiTargetBootSourceOverride": "uefi device path"
    },
    "Processors": {
        "Count": 8,
        "Model": "Multi-Core Intel(R) Xeon(R) processor 7xxx Series",
        "Status": {
            "State": "Enabled",
            "Health": "OK",
            "HealthRollUp": "OK"
        }
    },
    "Memory": {
        "TotalSystemMemoryGB": 16,
        "Status": {
            "State": "Enabled",
            "Health": "OK",
            "HealthRollUp": "OK"
        }
    },
    "FabricAdapters": [
        { "@odata.id": "/redfish/1/Systems/1/FabricAdapters" }
    ],
    "Links": {
        "Chassis": [
            {
                "@odata.id": "/redfish/v1/Chassis/1"
            }
        ],
    }

}