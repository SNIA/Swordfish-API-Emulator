# OpenFabrics Management Framework (OFMF) - Reference implementation

The OFMF Reference implementation provides a basic implementation of the OpenFabrics Management Framework. This project is based (fork) on the [Swordfish API Emulator](https://github.com/SNIA/Swordfish-API-Emulator), that provides the support for interacting with a RedFish/SwordFish system via RESTful operations (create, read, update, and delete). Before contributing to this project, read our [license](https://github.com/OFMFWG/OFMF-Reference/blob/master/LICENSE.md) and make sure you agree with the terms.

The OFMF Reference implementation is maintained by the OpenFabrics Alliance, while the Swordfish API Emulator code is maintained on GitHub by the SNIA, and the Redfish Interface Emulator code is maintained on GitHub by the DMTF.

----

## Prerequisites for the emulator

The OFMF reference implementation requires Python 3.5 or higher, make sure to properly configure your system before attempting using this project. If not available on your system, please refer to the best practices for installing bython onto your operating system.

This project, by default uses virtualenv for separating the emulator environment from the main system python environment. Make sure virtualenv is available as part of your system python environment. Please note, using virtualenv is not a requirement for the OFMF Reference to properly function.

----

## Installing the OFMF Reference implementation

### <u>Basic OFMF installation process</u>
We provide a (bash) script that automatically installs and runs the emulator on a Linux system. By default the emulator is installed in the `../OFMF` folder. However the destination folder can be changed when first isntalling the project.
The script will take care of creating a virtual environment called `venv` inside the installation folder annd will take care of installing all the requirements of the project.

To start the installation process, run:
```
./setup.sh
```

after completion this script will also execute the OFMF that will be listening on port `5050`. Use `CTRL-C` to exit the emulator and return to your shell.

### <u>Customizing the OFMF installation</u>

The `setup.sh` script provides parameters for configuring the installation of the OFMF:
```
./setup.sh -w DEST_FOLDER -p PORT -n
```

the `-w` argument can be used for installing the OFMF in a custom destination folder. The `-p` argument allows fo remulator to be started listening on an alternative port. Finally, the `-n` argument is used only for copy new files into the destination folder withour re-installing the entire environment. An example usage for the `-n` argument is when a developer makes changes to one of the files in the project and wants to test the changes. She would modify the source code of any of the files and then run the below command only to update the code base.

```
./setup.sh -n
```

After a successful installation, the OFMF can be started by running the below commands:

```
source INST_DIR/venv/bin/activate
python INST_DIR/emulator.py
```

where `INST_DIR` is the directory where the OFMF was initially installed.

----

## Interacting with the OFMF

Users can interact with the OFMF with any tool, command line or GUI based, that can send HTTP methods (GET, POST, DELETE, PATHC, PUT) to the below URI:

`http://localhost:5000/redfish/v1/`

An example using `curl`:

```
curl http://localhost:5000/redfish/v1/

{
  "@odata.id": "/redfish/v1",
  "@odata.type": "#ServiceRoot.v1_14_0.ServiceRoot",
  "Chassis": {
    "@odata.id": "/redfish/v1/Chassis"
  },
  "Fabrics": {
    "@odata.id": "/redfish/v1/Fabrics"
  },
  "Id": "RootService",
  "Links": {
    "Sessions": {
      "@odata.id": "/redfish/v1/SessionService/Sessions"
    }
  },
  "Managers": {
    "@odata.id": "/redfish/v1/Managers"
  },
  "Name": "Root Service",
  "RedfishVersion": "1.14.0",
  "Registries": {
    "@odata.id": "/redfish/v1/Registries"
  },
  "SessionService": {
    "@odata.id": "/redfish/v1/SessionService"
  },
  "Storage": {
    "@odata.id": "/redfish/v1/Storage"
  },
  "UUID": "92384634-2938-2342-8820-489239905423"
}

```

Alternatively, users can use a browser to access http://localhost:5000/redfish/v1/ on the system where the emulator has been installed. If the emulator is working properly, the Redfish service root should be displayed on the browser.

----
