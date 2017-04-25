Copyright 2016 Storage Networking Industry Association (SNIA), USA. All rights reserved. For the full SNIA copyright policy, see http://www.snia.org/about/corporate_info/copyright

Contributors that are not SNIA members must first agree to the terms of the SNIA Contributor Agreement for Non-Members:  www.snia.org/cla 

# Swordfish-API-Emulator
The Swordfish API Emulator can emulate a Swordfish-based API statically (GET) or dynamically (POST, PATCH, DELETE)

# Extending the DMTF Redfish Interface Emulator
The Swordfish API Emulator utilizes the [DMTF Redfish Interface Emulator](https://github.com/DMTF/Redfish-Interface-Emulator). In that Github, the ./doc directory contains two HowTo's: one for emulator users and the other for developers.

Static emulation is accomplished by copying the mockups files into ./api_emulator/swordfish/static.

Dynamic emulation requires coding two files for each resource model: <resource\>\_api.py and ./templates/<resource\>.py. These files are placed the ./api_emulator/swordfish directory.

If a resource needs to be present at ServiceRoot, the ./api\_emulator/resource_manager.py file need to be modified.

