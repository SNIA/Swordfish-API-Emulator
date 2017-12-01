Copyright 2016 Storage Networking Industry Association (SNIA), USA. All rights reserved. For the full SNIA copyright policy, see http://www.snia.org/about/corporate_info/copyright

Contributors that are not SNIA members must first agree to the terms of the SNIA Contributor Agreement for Non-Members:  www.snia.org/cla 

# Swordfish-API-Emulator
The Swordfish API Emulator can emulate a Swordfish-based API statically (GET) or dynamically (POST, PATCH, DELETE)

# Extending the DMTF Redfish Interface Emulator
The Swordfish API Emulator utilizes the [DMTF Redfish Interface Emulator](https://github.com/DMTF/Redfish-Interface-Emulator). In that Github, the ./doc directory contains two HowTo's: one for emulator users and the other for developers.

Static emulation is accomplished by copying the mockups files into ./api_emulator/swordfish/static.

Dynamic emulation requires coding two files for each resource model: <resource\>\_api.py and ./templates/<resource\>.py. These files are placed the ./api_emulator/swordfish directory.

If a resource needs to be present at ServiceRoot, the ./api\_emulator/resource_manager.py file need to be modified.




# Swordfish Installation Steps:

1. Create an installation directory to install code, install python and create virtual Environment.
2. Copy the Redfish-Interface-Emulator files into the installation directory.
3. Open the Swordfish-API-Emulator files.
  -> copy the swordfish /api_emulator/swordfish files into redfish/api_emulator/redfish directory.
  -> copy the Swordfish-API-Emulator/api_emulator files into Redfish-Interface-Emulator/api_emulator directory(resource_manager.py and util.py files)
4. After Third step is completed, install all the dependencies and modules needed by Redfish-Interface-Emulator and Swordfish-API-Emulator


After completing all the above steps , the Swordfish API Emulator should be fully installed, and it should be possible to run it by entering “python emulator.py” at a command prompt.


