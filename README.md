
# OpenFabrics Management Framework (OFMF) - Reference implementation
Copyright 2016-2023 Storage Networking Industry Association (SNIA), USA. All rights reserved. For the full SNIA copyright policy, see [http://www.snia.org/about/corporate_info/copyright](http://www.snia.org/about/corporate_info/copyright)

The OFMF Reference implementation provides a basic implementation of the OpenFabrics Management Framework. This project is based (fork) on the [Swordfish API Emulator](https://github.com/SNIA/Swordfish-API-Emulator), that provides the support for interacting with a RedFish/SwordFish system via RESTful operations (create, read, update, and delete). Before contributing to this project, read our [license](https://github.com/OFMFWG/OFMF-Reference/blob/master/LICENSE.md) and make sure you agree with the terms.

The OFMF Reference implementation is maintained by the OpenFabrics Alliance, while the Swordfish API Emulator code is maintained on GitHub by the SNIA, and the Redfish Interface Emulator code is maintained on GitHub by the DMTF.

----

## Prerequisites for the emulator

The OFMF reference implementation requires Python 3.5 or higher, make sure to properly configure your system before attempting using this project. If not available on your system, please refer to the best practices for installing bython onto your operating system.

This project, by default uses virtualenv for separating the emulator environment from the main system python environment. Make sure virtualenv is available as part of your system python environment. Please note, using virtualenv is not a requirement for the OFMF Reference to properly function.

----
## Installing the Swordfish API Emulator using the Linux Setup Script


## Installing the OFMF Reference implementation

Run the 'setup.sh' script. This will install a complete, running instance of the emulator.

This script has three command line parameters: <br>
-p | --port PORT     -- Port to run the emulator on. Default is 5000. <br>
-w | --workspace DIR -- Directory to set up the emulator. Defaults to  `../Swordfish` <br>
-n | --no-start      -- Prepare the emulator but do not start it.


## Installing the Swordfish API Emulator Manually on Windows or Linux

The Redfish Interface Emulator must be installed first, and then the Swordfish API Emulator must be installed on top of the Redfish Interface Emulator installation. This can be done on Windows using the sequence of steps given below. The steps for installing the emulator on Linux are similar.


### These installation steps assume the following:

- The prerequisites for the emulator have been installed.
- The emulator is being installed in a folder named **Swordfish**. (This is only an example for the installation steps given below; the folder can have an arbitrary name and be located anywhere.)
- The GitHub code for the Redfish Interface Emulator is in a folder named **Redfish-Interface-Emulator**.
- The GitHub code for the Swordfish API Emulator is in a folder named **Swordfish-API-Emulator**.

### <u>Basic OFMF installation process</u>
We provide a (bash) script that automatically installs and runs the emulator on a Linux system. By default the emulator is installed in the `../OFMF` folder. However the destination folder can be changed when first isntalling the project.
The script will take care of creating a virtual environment called `venv` inside the installation folder annd will take care of installing all the requirements of the project.

To start the installation process, run:
```
./setup.sh
```

after completion this script will also execute the OFMF that will be listening on port `5050`. Use `CTRL-C` to exit the emulator and return to your shell.

### <u>Customizing the OFMF installation</u>
### Installation steps:

#### (1) Create a folder for the emulator.

This folder is where the Redfish Interface Emulator files will be combined with the Swordfish API Emulator files to install the Swordfish emulator. As an example in these instructions, this folder is named **Swordfish**.

#### (2) Remove unneeded files from the Redfish Interface Emulator: 

Remove Redfish static / starting mockups
```
rm -r Swordfish/api_emulator/redfish/static
```

Remove Redfish templates, and .py files.
```
rm -r Swordfish/api_emulator/redfish/templates
rm -r Swordfish/api_emulator/redfish/*.py
```

Copy over the Swordfish bits

echo "Applying Swordfish additions..."
```
cp -r api_emulator Swordfish/
cp -r "$BASE_DIR"/Resources Swordfish/
cp -r  "$BASE_DIR"/emulator-config.json Swordfish/
cp -r  "$BASE_DIR"/g.py Swordfish/
cp -r "$BASE_DIR"/emulator.py Swordfish/
cp -r "$BASE_DIR"/certificate_config.cnf Swordfish/
cp -r "$BASE_DIR"/v3.ext Swordfish/
```

#### (5) Install the Python packages required by the emulator.

In a command prompt window, install the Python packages required by the Swordfish emulator, specified in the requirements.txt by entering the following commands:

```
pip install -r requirements.txt
```


#### (4) To enable secure communications (https) and the use of sessions, create a self-signed key. 

```
# generating server key

echo "Generating private key"
openssl genrsa -out Swordfish/server.key 2048

# generating public key

echo "Generating public key"
openssl rsa -in Swordfish/server.key -pubout -out Swordfish/server_public.key


# Generating Certificate Signing Request using config file

echo "Generating Certificate Signing Request"
openssl req -new -key Swordfish/server.key -out Swordfish/server.csr -config Swordfish/certificate_config.cnf

echo "Generating self signed certificate"
openssl x509 -in Swordfish/server.csr -out Swordfish/server.crt -req -signkey Swordfish/server.key -days 365 -extfile Swordfish/v3.ext
```


#### (5) If desired, a simple test of the Swordish API Emulator installation can now be done by running the emulator and accessing the Redfish service root using a browser.

To run the emulator, open a command window, use ```cd``` commands to change to the **Swordfish** folder, and enter this com

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

Users can interact with the OFMF with any tool, command line or GUI based, that can send HTTP methods (GET, POST, DELETE, PATHC, PUT) to the below U
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

- The Swordfish API Emulator leverages the general structure of the Redfish Interface Emulator and some of the utility functions, but replaces most of the code for the Redfish and Swordfish services and objects.  This service functions in a fully dynamic mode, meaning that objects generally support modification according to the Redfish and Swordfish specifications.

- The Swordfish API Emulator supports the following headers:
  - RESP_HEADERS_CONTENT_TYPE
  - REQ_HEADERS_ODATA_VERSION
  - RESP_HEADERS_ALLOW_GET_OR_HEAD
  - RESP_HEADERS_CACHE_CONTROL
  - RESP_HEADERS_LINK_REL_DESCRIBED_BY
  - RESP_HEADERS_ALLOW_METHOD_NOT_ALLOWED

- The dynamic resources in the emulator can be populated via the emulator API using Create/Read/Update/Delete (CRUD) operations.  The Swordfish emulator supports all instances of Redfish and Swordfish objects, via all URI paths.  If additional objects are desired, the AutoGen tool can be used to create additional objects, and the paths can be added to  `resource_manager.py()` in the api_emulator\redfish directory.

- The following services are implemented as read-only services:
  - Task Service
  - Event Service

- The Account Service is implemented to only authenticate: 

  Username:  Administrator

  Password: Password 

- The emulator supports both Basic Authentication as well as Sessions.  For an overview of how to use sessions, see the "Redfish Schools Sessions" video here: https://www.youtube.com/watch?v=qpVvKX_bkVQ


### Operational Notes


Alternatively, users can use a browser to access http://localhost:5000/redfish/v1/ on the system where the emulator has been installed. If the emulator is working properly, the Redfish service root should be displayed on the browser.

----
