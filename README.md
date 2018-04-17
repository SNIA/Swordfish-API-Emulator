Copyright 2016-2018 Storage Networking Industry Association (SNIA), USA. All rights reserved. For the full SNIA copyright policy, see [http://www.snia.org/about/corporate_info/copyright](http://www.snia.org/about/corporate_info/copyright)

Contributors that are not SNIA members must first agree to the terms of the SNIA Contributor Agreement for Non-Members:  [www.snia.org/cla](www.snia.org/cla)

----

# Swordfish-API-Emulator

The Swordfish API Emulator can emulate a Swordfish-based system that responds to create, read, update, and delete RESTful API operations to allow developers to model new Swordfish functionality, test clients, demonstrate Swordfish, and do other similar functions.

The Swordfish API Emulator extends the [DMTF Redfish Interface Emulator](https://github.com/DMTF/Redfish-Interface-Emulator) by adding code to an installation of the Redfish Interface Emulator code.

The Swordfish API Emulator code is maintained on GitHub by the SNIA, and the Redfish Interface Emulator code is maintained on GitHub by the DMTF.

----

## Prerequisites for the emulator

The Redfish Interface Emulator and the Swordfish API Emulator both require Python 3.5 or higher. If this is not already installed, go to www.python.org to download and install an appropriate version of Python.

It is recommended (but not required) to run the emulator using virtualenv, because it helps keep the emulator environment separate from other Python environments running on the same system. If this is not already installed, enter the following command into a command prompt window to install virtualenv after Python is installed: ```pip install virtualenv```

----

## Installing the Swordfish API Emulator on Windows

The Redfish Interface Emulator must be installed first, and then the Swordfish API Emulator must be installed on top of the Redfish Interface Emulator installation. This can be done on Windows using the sequence of steps given below. The steps for installing the emulator on Linux are similar.


### These installation steps assume the following:

- The prerequisites for the emulator have been installed and virtualenv is being used.
- The emulator is being installed in a folder named **Swordfish** in the Documents directory. (This is only an example for the installation steps given below; the folder can have an arbitrary name and be located anywhere.)
- The GitHub code for the Redfish Interface Emulator is in a folder named **Redfish-Interface-Emulator**.
- The GitHub code for the Swordfish API Emulator is in a folder named **Swordfish-API-Emulator**.


### Installation steps:

#### (1) Create a virtualenv environment folder for the emulator.

This folder is where the Redfish Interface Emulator files will be combined with the Swordfish API Emulator files to install the Swordfish emulator. As an example in these instructions, this folder will be created inside the Documents folder and named **Swordfish**.

Open a new command prompt window and enter the following commands:

```
cd Documents
virtualenv Swordfish
```

#### (2) Copy the Redfish Interface Emulator files into the virtualenv environment folder.

Using the file explorer, go to the **Redfish-Interface-Emulator** folder, select and copy all the files using ```Control-A``` and ```Control-C```, then go to the **Swordfish** folder and paste all the files into it using ```Control-V```.

#### (3) Activate the virtualenv environment and install the Python packages that are required by the emulator.

In the command prompt window, activate the virtualenv environment in the **Swordfish** folder and install the Python packages required by the emulator by entering the following commands:

```
cd Swordfish
Scripts\activate
pip install setuptools markupsafe itsdangerous flask
pip install aniso8601 pytz flask_httpauth requests
pip install flask_restful StringGenerator==0.2.1 urllib3
```

The Redfish Interface Emulator and its dependencies should now be installed in its default configuration in the **Swordfish** folder.

#### (4) Copy the Swordfish API Emulator files into the virtualenv environment folder, and allow some of the Redfish Interface Emulator files to be overwritten.

Using the file explorer, go to the **Swordfish-API-Emulator** folder, select and copy all the files using ```Control-A``` and ```Control-C```, then go to the **Swordfish** folder and paste all the files into it using ```Control-V```.

Windows will indicate that some files in the destination have the same names. Select the Windows “Replace the files in the destination” option.

#### (5) Copy the Swordfish files for dynamic Swordfish objects into the proper Redfish Interface Emulator folder.

Using the file explorer, go to the **Swordfish\api_emulator\swordfish** folder, select and copy all the files using ```Control-A``` and ```Control-C```, then go to the **Swordfish\api_emulator\redfish** folder and paste all the files into it using ```Control-V```.

The Swordfish API Emulator and its dependencies should now be installed in its default configuration in the **Swordfish** folder.

#### (6) If desired, a simple test of the Redfish Interface Emulator installation can now be done by running the emulator and accessing the Redfish service root using a browser.

To run the emulator, enter the following command in the command prompt window (this assumes the virtualenv environment in the **Swordfish** folder is still activated from step 3 above):

```
python emulator.py
```

Use a browser to access http://localhost:5000/redfish/v1/ on the system where the emulator has been installed. If the emulator is working properly, the Redfish service root should be displayed on the browser, with two additional Swordfish resources added: StorageServices, and StorageSystems.

After this simple installation test, stop the emulator and exit the virtualenv virtual environment by closing the command prompt window.

The Swordfish API Emulator should now be ready to use in its default configuration.


### Running the emulator after it is installed

Enter the following commands in a new command prompt window to activate the virtualenv environment in the **Swordfish** folder and start the emulator:

```
cd Documents\Swordfish
Scripts\activate
python emulator.py
```

To stop the emulator and exit the virtualenv environment at the same time, close the command prompt window.

To stop the emulator without closing the command prompt window, enter ```Control-C``` in the command prompt window. Note that the emulator might not appear to stop until another emulator API access is attempted. A web browser can be used to access the Redfish service root to force this to happen, if no other REST client is readily available.

To exit the virtualenv environment without closing the command prompt window, the emulator must first be stopped, then enter ```deactivate``` in the command prompt window.

----

## Notes about the Swordfish API Emulator

- The [Redfish Interface Emulator *README.md* file](https://github.com/DMTF/Redfish-Interface-Emulator/blob/master/README.md) should be reviewed before working with the Swordfish API Emulator or changing the default configuration.

- The configuration of the overall emulator is controlled by the *emulator-config.json* file in the directory where the emulator is installed. (This is the *Swordfish* folder in the installation steps above.) Instructions for using this file can be found in the Redfish Interface Emulator *README.md* file.

- The Swordfish API Emulator code files generally do not overlap the Redfish Interface Emulator code files, but there are currently two files that must contain code for both the Redfish Interface Emulator and the Swordfish API Emulator:
  - *api_emulator\resource_manager.py*
  - *api_emulator\utils.py*

- The *api_emulator\resource_manager.py* file establishes which emulator resources are static and which emulator resources are dynamic. Create/Read/Update/Delete (CRUD) operations can be done on dynamic resources via the emulator API using REST operations, but static resources are read-only and cannot be changed via the emulator API.

- The Swordfish resources in the emulator are dynamic, and most of the Redfish resources are also dynamic, but four Redfish resources are currently still static in the default configuration of the Redfish Interface Emulator:
  - TaskService
  - SessionService
  - AccountService
  - Registries

- The static resources in the emulator are populated by placing appropriate JSON mockup folders into the *api_emulator\redfish\static* directory. Instructions for this can be found in the Redfish Interface Emulator *README.md* file. Note that the dynamic resources in the emulator are NOT populated or initialized by the mockups in this directory.

- The dynamic resources in the emulator can be populated via the emulator API using Create/Read/Update/Delete (CRUD) operations, and they can also be pre-populated by creating an appropriate JSON file that describes the desired dynamic resources for the Redfish Interface Emulator’s INFRAGEN Module. Instructions for using the INFRAGEN Module can be found in the Redfish Interface Emulator *README.md* file.

- The current default configuration of the Redfish Interface Emulator pre-populates several of the Redfish dynamic resources. Instructions for starting the emulator without any pre-populated dynamic resources can be found in the Redfish Interface Emulator *README.md* file.

- Sometimes a ```Control-C``` in the command prompt window does not appear to immediately stop the emulator. When this occurs, the emulator will stop as soon as another emulator API access is attempted. A web browser can be used to access the Redfish service root to force this to happen, if no other REST client is readily available.

----
