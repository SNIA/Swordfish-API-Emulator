* [33mf6881a8[m[33m ([m[1;36mHEAD -> [m[1;32mwork_on_transactions[m[33m, [m[1;31morigin/work_on_transactions[m[33m)[m Copy of settings map to front of the emulator code, for quick reference
* [33m6458b39[m Simplifying authentication to get a base repository that works
* [33m2a39a67[m requirements.txt has the versions removed for compatibility to Red Hat clones
[31m|[m * [33m1f38958[m[33m ([m[1;32mmaster[m[33m)[m Copy of information from the bottom to the top to present options available.
[31m|[m * [33mf74dd05[m Changed the Cloud--->shared, fixed code incompatibilities and configuration commands, verified operation, fixed PORT to AGENTPORT, fixed read of port value for shared MODE
[31m|[m * [33meb1b183[m Mode is changed: cloud-->shared, Enable and Disable are fixed to match the current code
[31m|[m * [33me877da0[m emulator-config.json is not operational with the Authentication setup that is included in the current emulator.py.  I have borrowed entries from the previous version and turned off authentication to allow it to be fixed.
[31m|[m * [33m8b5dde1[m[33m ([m[1;32mmikea_code_fix_work[m[33m)[m Fix to get multiple OS versions and Python3 packages to work with the Reference run-time
[31m|[m[31m/[m  
*   [33mc2c8ef8[m[33m ([m[1;31morigin/master[m[33m, [m[1;31morigin/HEAD[m[33m)[m Merge pull request #9 from OFMFWG/test-gh-actions
[33m|[m[34m\[m  
[33m|[m * [33ma9c2a3a[m[33m ([m[1;31morigin/test-gh-actions[m[33m)[m Improved GH actions support
[33m|[m * [33m22117be[m Initial code stesting on push with GH actions
[33m|[m[33m/[m  
* [33mdbec4a8[m FIrst OFMF Reference project README
*   [33m681e081[m Merge pull request #86 from SNIA/create-dockerfile
[35m|[m[36m\[m  
[35m|[m * [33mea38a2e[m Update dockerfile
[35m|[m *   [33mc45f64d[m Merge branch 'master' into create-dockerfile
[35m|[m [1;31m|[m[35m\[m  
[35m|[m [1;31m|[m[35m/[m  
[35m|[m[35m/[m[1;31m|[m   
* [1;31m|[m [33m79d8aa7[m Update copyright
* [1;31m|[m   [33m830baa4[m Merge pull request #92 from SNIA/reeya_updated_emulator
[1;33m|[m[1;34m\[m [1;31m\[m  
[1;33m|[m * [1;31m|[m [33m92fb2be[m Update setup.sh
[1;33m|[m * [1;31m|[m [33m3072a78[m Create .gitignore
[1;33m|[m * [1;31m|[m [33m8e1a6d4[m Updating requirements and script.
[1;33m|[m * [1;31m|[m [33md7b6c19[m swordfish setup script updated
[1;33m|[m * [1;31m|[m [33mcb9b515[m AccountService resource added
[1;33m|[m * [1;31m|[m [33m0e4c341[m emulator setup changes
[1;33m|[m * [1;31m|[m [33mcc00712[m updated path in setup.sh
[1;33m|[m * [1;31m|[m [33m9cdb142[m Authentication added for all RF/SF resources
[1;33m|[m * [1;31m|[m [33ma21cc88[m autogen updated with authentication
[1;33m|[m * [1;31m|[m [33mb0ffed7[m Etag header changes
[1;33m|[m * [1;31m|[m [33m87b73cf[m details updated for version 3 certificate creation
[1;33m|[m * [1;31m|[m [33m46e1ede[m Etag header added
[1;33m|[m * [1;31m|[m [33m792f4d8[m Session time updated
[1;33m|[m * [1;31m|[m [33mef928a8[m Documentation added
[1;33m|[m * [1;31m|[m [33m0c52ad5[m new attribute added in config file - CERTIFICATE
[1;33m|[m * [1;31m|[m [33me34e126[m typo correction
[1;33m|[m * [1;31m|[m   [33ma868ec7[m Merge branch 'reeya_updated_emulator' of https://github.com/SNIA/Swordfish-API-Emulator into reeya_updated_emulator
[1;33m|[m [1;35m|[m[1;36m\[m [1;31m\[m  
[1;33m|[m [1;35m|[m * [1;31m|[m [33m170c7db[m Update build requirements.
[1;33m|[m * [1;36m|[m [1;31m|[m [33ma3699ae[m Updated required libraries for autogen & emulator
[1;33m|[m [1;36m|[m[1;36m/[m [1;31m/[m  
[1;33m|[m * [1;31m|[m [33mf26527b[m Add python build requirements to support Sessions
[1;33m|[m * [1;31m|[m [33md6c9ad4[m Update emulator.py
[1;33m|[m * [1;31m|[m [33mb686be0[m Updates in POST Collection
[1;33m|[m * [1;31m|[m [33ma3b17d7[m autogen update - POST collection method
[1;33m|[m * [1;31m|[m [33me981ea5[m Object creation autogen corrections updated
[1;33m|[m * [1;31m|[m [33md4441e6[m updated for AdvertisedFeatures.json get method
[1;33m|[m * [1;31m|[m [33mc1a0944[m Link to AccountService added
[1;33m|[m * [1;31m|[m [33m57387c9[m authentication functionallity added
[1;33m|[m * [1;31m|[m [33mb0543a4[m response header added
[1;33m|[m * [1;31m|[m [33mac0af67[m Update in error code
[1;33m|[m * [1;31m|[m [33ma2b9416[m POST to collection
[1;33m|[m * [1;31m|[m [33meb6c718[m delete session location on timeout
[1;33m|[m * [1;31m|[m   [33m14e4d13[m Merge branch 'reeya_updated_emulator' of https://github.com/SNIA/Swordfish-API-Emulator into reeya_updated_emulator
[1;33m|[m [31m|[m[32m\[m [1;31m\[m  
[1;33m|[m [31m|[m * [1;31m|[m [33mf6734c4[m Fix script issue.
[1;33m|[m * [32m|[m [1;31m|[m [33md102705[m Authentication and account service related changes
[1;33m|[m [32m|[m[32m/[m [1;31m/[m  
[1;33m|[m * [1;31m|[m [33m1b9bef3[m All RF/SW implementation, updated autogen
[1;33m|[m * [1;31m|[m [33mf5983d2[m Updated setup.sh for emulator changes
[1;33m|[m * [1;31m|[m [33m1c297e8[m added collection.py & constant.py, renamed Fabric
[1;33m|[m * [1;31m|[m [33m1853bc0[m autogen
[1;33m|[m * [1;31m|[m [33m8744450[m removed __pycache__ and updated autogen
[1;33m|[m * [1;31m|[m [33mc4b2818[m Redfish part removed & autogen added
[1;33m|[m * [1;31m|[m [33m0860161[m NVMe EBOF setup
[1;33m|[m[1;33m/[m [1;31m/[m  
[1;33m|[m * [33me41c9d9[m Updated dockerfile
[1;33m|[m * [33m2682984[m Update dockerfile
[1;33m|[m * [33md4c08e5[m Create dockerfile
[1;33m|[m[1;33m/[m  
*   [33m3632e65[m Merge pull request #82 from SNIA/filter-redfish.copyright
[33m|[m[34m\[m  
[33m|[m * [33mf73f694[m Update copyright.
[33m|[m * [33m8818656[m Filters to remove @Redfish.Copyright from returned JSON.
[33m|[m[33m/[m  
*   [33m2be9881[m Merge pull request #81 from SNIA/fix-serviceroot
[35m|[m[36m\[m  
[35m|[m * [33m2d72dc8[m Update setup script to copy new emulator.py file
[35m|[m * [33m6d259c6[m Add dynamic service root: GET / PATCH / PUT
[35m|[m[35m/[m  
*   [33me276880[m Merge pull request #80 from SNIA/fix-73-78-77-75-74-clean-up-CRUD-behaviors
[1;31m|[m[1;32m\[m  
[1;31m|[m * [33m07f28ee[m Update paths in GET
[1;31m|[m * [33md1a2349[m Partial updates
[1;31m|[m * [33mabd98e7[m Updated Network Adapters, NW Ports, NDFs
[1;31m|[m * [33m536b89e[m Update mc_ports_api.py
[1;31m|[m * [33maf51911[m Updated MediaControllers and MC Ports
[1;31m|[m * [33m2aea84d[m Remove StorageSubsystems
[1;31m|[m * [33m0e980ad[m Update MemoryChunks
[1;31m|[m * [33m85c2e92[m Update memory, memory domains
[1;31m|[m * [33me94333d[m Update fa_ports_api.py
[1;31m|[m * [33m701de70[m Update fabricadapters
[1;31m|[m * [33m2eb018b[m Update storagecontrollers_api.py
[1;31m|[m * [33m6e01e32[m Updated deletes
[1;31m|[m * [33mb33e33b[m Update volumes_api.py
[1;31m|[m * [33me2d2d40[m Update storage
[1;31m|[m * [33m613661f[m Create collection.py
[1;31m|[m * [33me18d18f[m Update switches.py
[1;31m|[m * [33m1a7b906[m Updated storage, volume, storagepools.
[1;31m|[m * [33mcdcbcea[m Update templates
[1;31m|[m * [33md606eef[m Update drives.py
[1;31m|[m * [33mbe47fbb[m Update constants.py
[1;31m|[m * [33m3afcfe6[m Updated
[1;31m|[m * [33m9d21594[m Update fabric_api.py
[1;31m|[m * [33m7efc729[m Updates.
[1;31m|[m * [33mca34e83[m Updated fabrics with POST/PATCH/PUT DELETE, collections have POST/PATCH/DELETE
[1;31m|[m * [33mb434a3f[m Updated POST/PATCH/DELETE for object and POST/DELETE for collection
[1;31m|[m * [33md5886a3[m Updated utils
[1;31m|[m[1;31m/[m  
* [33mdb06663[m Add odata files to mockups, resources.
*   [33md48086f[m Merge pull request #71 from SNIA/add-memory-support-for-ofa
[1;33m|[m[1;34m\[m  
[1;33m|[m * [33m00e9f7a[m Add Memory, MemoryDomains, FabricAdapter, MediaControllers
[1;33m|[m[1;33m/[m  
*   [33m5c84649[m Merge pull request #69 from SNIA/add-ofa-support
[1;35m|[m[1;36m\[m  
[1;35m|[m * [33m0bca109[m Fixes to dynamic fabric
[1;35m|[m[1;35m/[m  
*   [33ma7eeb4e[m Merge pull request #67 from SNIA/fix-66-redfish-updates
[31m|[m[32m\[m  
[31m|[m * [33m258e9a6[m Fix copyrights.
[31m|[m * [33mad46bf3[m Update to latest Redfish Interface Emulator.
[31m|[m * [33m3bc2153[m Update copyright.
[31m|[m * [33m5157d5b[m Initial fabrics objects.
[31m|[m * [33md881467[m Update startup.
[31m|[m * [33m11447e5[m Add import.
[31m|[m * [33ma5a67e6[m Add SessionService enablement.
[31m|[m * [33mf3bb9e8[m Fix path to subscriptions / event destination collection.
[31m|[m * [33mc80878a[m Add support for StorageControllers, Network Adapters, Network Device Functions and Ports.
[31m|[m * [33m35c30fd[m Updates.
[31m|[m * [33m1a0fb1f[m Add Storage.
[31m|[m * [33mb9f67fd[m Add Fabric.
[31m|[m * [33mbc778d6[m Fixes.
[31m|[m * [33m9dbe2b1[m Fix copyright
[31m|[m * [33m6238507[m Fix collection odata types and copyrights.
[31m|[m * [33m27c91eb[m Move mockups folder
[31m|[m * [33m9186c80[m Move mockups to ./Mockups folder
[31m|[m * [33m3493864[m Updates to starting image
[31m|[m * [33m93098b4[m Updates to change config from StorageService to /redfish/v1/Storage
[31m|[m * [33ma2b6772[m Updates to starting image
[31m|[m * [33m8105f58[m Updated copyrights.
[31m|[m * [33m5761784[m Updated to start from current mockups.
[31m|[m * [33m81d4cab[m Updates to match Redfish
[31m|[m[31m/[m  
*   [33mf1c6aff[m Merge pull request #64 from stmcginnis/ss_volumes
[33m|[m[34m\[m  
[33m|[m * [33m3817613[m Fix StorageService/1 Volume property link format
[33m|[m[33m/[m  
*   [33mbede5be[m Merge pull request #62 from SNIA/Resync-resource_manager.py
[35m|[m[36m\[m  
[35m|[m * [33m9f24a0c[m Update resource_manager.py
[35m|[m[35m/[m  
*   [33m424a6f6[m Merge pull request #59 from SNIA/chris-lionetti-patch-3
[1;31m|[m[1;32m\[m  
[1;31m|[m * [33mc9058e6[m Also a prettified JSON file
* [1;32m|[m   [33m27aed99[m Merge pull request #58 from SNIA/chris-lionetti-patch-2
[1;33m|[m[1;34m\[m [1;32m\[m  
[1;33m|[m * [1;32m|[m [33m0c451fb[m Updated the JSON to display properly.
[1;33m|[m [1;32m|[m[1;32m/[m  
* [1;32m|[m   [33mc338f1e[m Merge pull request #57 from SNIA/chris-lionetti-patch-1
[1;32m|[m[1;36m\[m [1;32m\[m  
[1;32m|[m [1;36m|[m[1;32m/[m  
[1;32m|[m[1;32m/[m[1;36m|[m   
[1;32m|[m * [33m61870cd[m Fixed the JSON formatting
[1;32m|[m[1;32m/[m  
*   [33m0090254[m Merge pull request #56 from SNIA/Fix-Collection-POST-Commands
[31m|[m[32m\[m  
[31m|[m * [33m853e629[m Update copyright dates
[31m|[m * [33m880f6dd[m Implement collection POST commands
[31m|[m[31m/[m  
* [33mbe0453d[m Update year in copyright
*   [33md197e27[m Merge pull request #54 from SNIA/MD-Version-API-Emulator-docs
[33m|[m[34m\[m  
[33m|[m * [33mf32860d[m Update Swordfish API Emulator Dev Guide.md
[33m|[m * [33ma97f55d[m Update Swordfish API Emulator User Guide.md
[33m|[m * [33m11889f2[m Update Swordfish API Emulator User Guide.md
[33m|[m * [33m05ac1c7[m Update Swordfish API Emulator Dev Guide.md
[33m|[m * [33m9942750[m Update Swordfish API Emulator Dev Guide.md
[33m|[m * [33mb238e0d[m Update Swordfish API Emulator User Guide.md
[33m|[m * [33mad7d1d8[m Update Swordfish API Emulator User Guide.md
[33m|[m * [33mbe52687[m Update Swordfish API Emulator Dev Guide.md
[33m|[m * [33m423e100[m Add files via upload
[33m|[m[33m/[m  
*   [33m601c186[m Merge pull request #52 from SNIA/Correct-URL-for-SNIA-CLA
[35m|[m[36m\[m  
[35m|[m * [33m9f66a32[m Update README.md
[35m|[m * [33mb2a4723[m Update README.md
[35m|[m[35m/[m  
*   [33m7645ce1[m Merge pull request #50 from stmcginnis/setup_script
[1;31m|[m[1;32m\[m  
[1;31m|[m * [33mdbcf4cd[m Add setup script to prepare the emulator
[1;31m|[m[1;31m/[m  
*   [33m6d6364e[m Merge pull request #49 from SNIA/Re-sync-with-Redfish-Interface-Emulator
[1;33m|[m[1;34m\[m  
[1;33m|[m * [33mfadfdfb[m Re-sync key files
[1;33m|[m[1;33m/[m  
*   [33m4356564[m Merge pull request #47 from SNIA/SNIA_01-08-18
[1;35m|[m[1;36m\[m  
[1;35m|[m * [33m5af9ad1[m Changes related to #46
[1;35m|[m[1;35m/[m  
*   [33m1d60b56[m Merge pull request #45 from SNIA/180715-Changes-to-simplify-install
[31m|[m[32m\[m  
[31m|[m * [33m0190666[m Removed copyright symbols
[31m|[m * [33mbdeb85f[m EOL issue
[31m|[m * [33m8604866[m Revert "Fix ending character issue"
[31m|[m * [33meef5a53[m Fix ending character issue
[31m|[m * [33mbe62d02[m Minor fix for JSON file
[31m|[m * [33m70c6874[m Update README.md
[31m|[m * [33m1168e1e[m Rename "swordfish" directory to "redfish"
[31m|[m[31m/[m  
*   [33m063b236[m Merge pull request #40 from SNIA/Swordfish-26thjune
[33m|[m[34m\[m  
[33m|[m * [33mb65d71e[m Fix Related To #38 PATCH update
[33m|[m * [33m9445aa7[m Fix related to #38 Patch update
* [34m|[m   [33m47b4275[m Merge pull request #42 from SNIA/fix-41-cleanup-files
[35m|[m[36m\[m [34m\[m  
[35m|[m * [34m|[m [33m223a7a2[m Delete files
[35m|[m[35m/[m [34m/[m  
* [34m|[m   [33mf386e58[m Merge pull request #36 from SNIA/SNIA-Doc
[34m|[m[1;32m\[m [34m\[m  
[34m|[m [1;32m|[m[34m/[m  
[34m|[m[34m/[m[1;32m|[m   
[34m|[m * [33me1dbf08[m Updated from comments
[34m|[m * [33m3687906[m Fix Related To Documentation #37 #36
[34m|[m * [33m83fe269[m Updated comments and edits
[34m|[m * [33m9e85339[m #37 Respond to comments embedded in developer documentation
[34m|[m * [33ma5f8537[m Added comments to emulator documentation
[34m|[m * [33m2a275c1[m Updated user doc
[34m|[m * [33mdd8910d[m Fix related to #35 #33 #32
* [1;32m|[m   [33m8908451[m Merge pull request #34 from SNIA/SNIA-21-05-18
[1;32m|[m[1;34m\[m [1;32m\[m  
[1;32m|[m [1;34m|[m[1;32m/[m  
[1;32m|[m[1;32m/[m[1;34m|[m   
[1;32m|[m * [33m5773fda[m Fix related to #32  DELETE  Swordfish resources
[1;32m|[m[1;32m/[m  
*   [33m75bacf2[m Merge pull request #24 from SNIA/Fix-deprecated-imports-180423
[1;35m|[m[1;36m\[m  
[1;35m|[m * [33md5e28a4[m Replace "flask.ext.restful" with "flask_restful"
[1;35m|[m[1;35m/[m  
*   [33m202ca11[m Merge pull request #23 from SNIA/README-update-180416
[31m|[m[32m\[m  
[31m|[m * [33m14eb2fa[m Update README
* [32m|[m   [33mf019beb[m Merge pull request #21 from stmcginnis/copyrights
[32m|[m[34m\[m [32m\[m  
[32m|[m [34m|[m[32m/[m  
[32m|[m[32m/[m[34m|[m   
[32m|[m * [33mea17fdb[m Fix copyright header format
[32m|[m[32m/[m  
*   [33m3b87a1e[m Merge pull request #22 from SNIA/Swordfish-2-9-2018
[35m|[m[36m\[m  
[35m|[m * [33m80c7035[m Latest copyright changes 3-19-2018
[35m|[m * [33m1075250[m Latest copyright changes 3-19-2018
[35m|[m * [33m31d822e[m Latest Changes 7-3-2018
[35m|[m * [33m460c88b[m Latest Changes 7-3-2018
[35m|[m * [33m50de531[m Latest Commit 1-3-2018
[35m|[m * [33mc057d87[m Latest Commit 1-3-2018
[35m|[m * [33me596844[m latest commit 22-2-2018
[35m|[m * [33m022464c[m Latest Changes 20th feb
[35m|[m * [33m0b3ca6b[m Latest Changes
[35m|[m * [33m14be892[m Latest 13th feb
[35m|[m * [33med80ff7[m Latest 12-2-2018
[35m|[m * [33mbe9d208[m Latest 12-2-2018
[35m|[m * [33m4bcb07f[m latest 12-2-2018
[35m|[m * [33ma0ce8ea[m latest
[35m|[m * [33m3ea239b[m latest
[35m|[m * [33m6b225d3[m latest
[35m|[m * [33m0b8a91f[m Latest Update 2-9-2018
[35m|[m[35m/[m  
*   [33madceca1[m Merge pull request #12 from SNIA/SNIA-API-27-11-17
[1;31m|[m[1;32m\[m  
[1;31m|[m * [33m3bcce6e[m Latest Updated Files 13-12-17
[1;31m|[m * [33ma3f872d[m Fixed compile errors
[1;31m|[m * [33m1f61832[m Latest Code On 1-12-17
[1;31m|[m * [33m4f7681f[m Latest Code On 30-11-17
[1;31m|[m * [33mf91062f[m Latest Code On 28-11-17
[1;31m|[m * [33m86d3444[m Update index.json
[1;31m|[m * [33mc34e244[m Latest Code On 28-11-17
[1;31m|[m * [33m414e5cd[m  Latest
* [1;32m|[m   [33mb2aa6b6[m Merge pull request #11 from SNIA/rahlvers-patch-1
[1;32m|[m[1;34m\[m [1;32m\[m  
[1;32m|[m [1;34m|[m[1;32m/[m  
[1;32m|[m[1;32m/[m[1;34m|[m   
[1;32m|[m * [33mb767380[m Update LICENSE.md
[1;32m|[m[1;32m/[m  
*   [33m5c61574[m Merge pull request #1 from SNIA/cleanup
[1;35m|[m[1;36m\[m  
[1;35m|[m * [33medfd48a[m remove files which should be obtained from Redfish Interface Emulator
[1;35m|[m[1;35m/[m  
* [33mb33c842[m Initial commit
* [33m98c9b01[m Update and rename LICENSE to LICENSE.md
* [33m370bbeb[m Update README.md
* [33mcb87c31[m Update README.md
* [33m7c3a8b5[m Initial commit
