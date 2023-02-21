Copyright 2016-2023 Storage Networking Industry Association (SNIA), USA. All rights reserved. For the full SNIA copyright policy, see [http://www.snia.org/about/corporate_info/copyright](http://www.snia.org/about/corporate_info/copyright)

Contributors that are not SNIA members must first agree to the terms of the SNIA Contributor Agreement for Non-Members:  [www.snia.org/cla](https://www.snia.org/cla)

----

# Swordfish-API-Emulator

The Swordfish API Emulator can emulate a Swordfish-based system that responds to create, read, update, and delete RESTful API operations to allow developers to model new Swordfish functionality, test clients, demonstrate Swordfish, and do other similar functions.

The Swordfish API Emulator extends the [DMTF Redfish Interface Emulator](https://github.com/DMTF/Redfish-Interface-Emulator) by adding code to an installation of the Redfish Interface Emulator code.

The Swordfish API Emulator code is maintained on GitHub by the SNIA, and the Redfish Interface Emulator code is maintained on GitHub by the DMTF.

----

## Prerequisites for the emulator

The Redfish Interface Emulator and the Swordfish API Emulator both require Python 3.5 or higher. If this is not already installed, go to www.python.org to download and install an appropriate version of Python.

It is recommended (but not required) to run the emulator using virtualenv, because it helps keep the emulator environment separate from other Python environments running on the same system.

----
## Installing the Swordfish API Emulator using the Linux Setup Script

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

To run the emulator, open a command window, use ```cd``` commands to change to the **Swordfish** folder, and enter this command:

```
python emulator.py
```

Use a browser to access http://localhost:5000/redfish/v1/ on the system where the emulator has been installed. If the emulator is working properly, the Redfish service root should be displayed on the browser, with two additional Swordfish resources added: StorageServices, and StorageSystems.

After this simple installation test, stop the emulator by closing the command prompt window.

The Swordfish API Emulator should now be ready to use in its default configuration.


### Running the emulator after it is installed

To run the emulator, open a command window, use ```cd``` commands to change to the **Swordfish** directory, and enter this command:

```
python emulator.py
```

To stop the emulator without closing the command prompt window, enter ```Control-C``` in the command prompt window. Note that the emulator might not appear to stop until another emulator API access is attempted. A web browser can be used to access the Redfish service root to force this to happen, if no other REST client is readily available.

The emulator can also be stopped by closing the command window.

----

## Notes about the Swordfish API Emulator

- The [Redfish Interface Emulator *README.md* file](https://github.com/DMTF/Redfish-Interface-Emulator/blob/master/README.md) should be reviewed before working with the Swordfish API Emulator or changing the default configuration.

- The configuration of the overall emulator is controlled by the *emulator-config.json* file in the directory where the emulator is installed. (This is the **Swordfish** folder in the installation steps above.) Instructions for using this file can be found in the Redfish Interface Emulator *README.md* file.

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

- Sometimes a ```Control-C``` in the command prompt window does not appear to immediately stop the emulator. When this occurs, the emulator will stop as soon as another emulator API access is attempted. A web browser can be used to access the Redfish service root to force this to happen, if no other REST client is readily available.

----
