# Copyright Notice:
# Copyright 2016-2021 DMTF. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/blob/master/LICENSE.md
#
# The original DMTF contents of this file have been modified to support
# The SNIA Swordfish API Emulator. These modifications are subject to the following:
# Copyright (c) 2017-2021, The Storage Networking Industry Association.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# Neither the name of The Storage Networking Industry Association (SNIA) nor
# the names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMfPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
#  THE POSSIBILITY OF SUCH DAMAGE.
#

# Resource Manager Module

# External imports

from api_emulator.redfish.AccelerationFunction0_api import *
from api_emulator.redfish.AccelerationFunction1_api import *
from api_emulator.redfish.AccelerationFunction2_api import *
from api_emulator.redfish.AccelerationFunction3_api import *
from api_emulator.redfish.AccelerationFunction4_api import *
from api_emulator.redfish.AddressPool_api import *
from api_emulator.redfish.Aggregate_api import *
from api_emulator.redfish.AggregationSource_api import *
from api_emulator.redfish.AllowDeny0_api import *
from api_emulator.redfish.AllowDeny1_api import *
from api_emulator.redfish.AllowDeny2_api import *
from api_emulator.redfish.AllowDeny3_api import *
from api_emulator.redfish.AllowDeny4_api import *
from api_emulator.redfish.AllowDeny5_api import *
from api_emulator.redfish.Battery_api import *
from api_emulator.redfish.BootOption0_api import *
from api_emulator.redfish.BootOption1_api import *
from api_emulator.redfish.BootOption2_api import *
from api_emulator.redfish.Cable_api import *
from api_emulator.redfish.Certificate0_api import *
from api_emulator.redfish.Certificate1_api import *
from api_emulator.redfish.Certificate2_api import *
from api_emulator.redfish.Certificate3_api import *
from api_emulator.redfish.Certificate4_api import *
from api_emulator.redfish.Certificate5_api import *
from api_emulator.redfish.Certificate6_api import *
from api_emulator.redfish.Certificate7_api import *
from api_emulator.redfish.Certificate8_api import *
from api_emulator.redfish.Certificate9_api import *
from api_emulator.redfish.Certificate10_api import *
from api_emulator.redfish.Certificate11_api import *
from api_emulator.redfish.Certificate12_api import *
from api_emulator.redfish.Certificate13_api import *
from api_emulator.redfish.Certificate14_api import *
from api_emulator.redfish.Certificate15_api import *
from api_emulator.redfish.Certificate16_api import *
from api_emulator.redfish.Certificate17_api import *
from api_emulator.redfish.Certificate18_api import *
from api_emulator.redfish.Certificate19_api import *
from api_emulator.redfish.Certificate20_api import *
from api_emulator.redfish.Certificate21_api import *
from api_emulator.redfish.Certificate22_api import *
from api_emulator.redfish.Certificate23_api import *
from api_emulator.redfish.Certificate24_api import *
from api_emulator.redfish.Certificate25_api import *
from api_emulator.redfish.Certificate26_api import *
from api_emulator.redfish.Certificate27_api import *
from api_emulator.redfish.Certificate28_api import *
from api_emulator.redfish.Certificate29_api import *
from api_emulator.redfish.Certificate30_api import *
from api_emulator.redfish.Certificate31_api import *
from api_emulator.redfish.Certificate32_api import *
from api_emulator.redfish.Certificate33_api import *
from api_emulator.redfish.Certificate34_api import *
from api_emulator.redfish.Certificate35_api import *
from api_emulator.redfish.Certificate36_api import *
from api_emulator.redfish.Certificate37_api import *
from api_emulator.redfish.Certificate38_api import *
from api_emulator.redfish.Certificate39_api import *
from api_emulator.redfish.Certificate40_api import *
from api_emulator.redfish.Certificate41_api import *
from api_emulator.redfish.Certificate42_api import *
from api_emulator.redfish.Certificate43_api import *
from api_emulator.redfish.Certificate44_api import *
from api_emulator.redfish.Certificate45_api import *
from api_emulator.redfish.Certificate46_api import *
from api_emulator.redfish.Certificate47_api import *
from api_emulator.redfish.Certificate48_api import *
from api_emulator.redfish.Certificate49_api import *
from api_emulator.redfish.Certificate50_api import *
from api_emulator.redfish.Certificate51_api import *
from api_emulator.redfish.Certificate52_api import *
from api_emulator.redfish.Certificate53_api import *
from api_emulator.redfish.Certificate54_api import *
from api_emulator.redfish.Certificate55_api import *
from api_emulator.redfish.Certificate56_api import *
from api_emulator.redfish.Certificate57_api import *
from api_emulator.redfish.Certificate58_api import *
from api_emulator.redfish.Certificate59_api import *
from api_emulator.redfish.Certificate60_api import *
from api_emulator.redfish.Certificate61_api import *
from api_emulator.redfish.Certificate62_api import *
from api_emulator.redfish.Certificate63_api import *
from api_emulator.redfish.Certificate64_api import *
from api_emulator.redfish.Certificate65_api import *
from api_emulator.redfish.Chassis_api import *
from api_emulator.redfish.Circuit0_api import *
from api_emulator.redfish.Circuit1_api import *
from api_emulator.redfish.Circuit2_api import *
from api_emulator.redfish.Circuit3_api import *
from api_emulator.redfish.Circuit4_api import *
from api_emulator.redfish.Circuit5_api import *
from api_emulator.redfish.Circuit6_api import *
from api_emulator.redfish.Circuit7_api import *
from api_emulator.redfish.Circuit8_api import *
from api_emulator.redfish.Circuit9_api import *
from api_emulator.redfish.Circuit10_api import *
from api_emulator.redfish.Circuit11_api import *
from api_emulator.redfish.Circuit12_api import *
from api_emulator.redfish.Circuit13_api import *
from api_emulator.redfish.Circuit14_api import *
from api_emulator.redfish.Circuit15_api import *
from api_emulator.redfish.ComponentIntegrity_api import *
from api_emulator.redfish.CompositionReservation_api import *
from api_emulator.redfish.ComputerSystem0_api import *
from api_emulator.redfish.ComputerSystem1_api import *
from api_emulator.redfish.ComputerSystem2_api import *
from api_emulator.redfish.ConnectionMethod_api import *
from api_emulator.redfish.Connection_api import *
from api_emulator.redfish.Control0_api import *
from api_emulator.redfish.Control1_api import *
from api_emulator.redfish.Control2_api import *
from api_emulator.redfish.Control3_api import *
from api_emulator.redfish.Control4_api import *
from api_emulator.redfish.Control5_api import *
from api_emulator.redfish.Drive0_api import *
from api_emulator.redfish.Drive1_api import *
from api_emulator.redfish.Drive2_api import *
from api_emulator.redfish.Drive3_api import *
from api_emulator.redfish.Drive4_api import *
from api_emulator.redfish.Drive5_api import *
from api_emulator.redfish.Drive6_api import *
from api_emulator.redfish.Drive7_api import *
from api_emulator.redfish.EndpointGroup0_api import *
from api_emulator.redfish.EndpointGroup1_api import *
from api_emulator.redfish.EndpointGroup2_api import *
from api_emulator.redfish.EndpointGroup3_api import *
from api_emulator.redfish.Endpoint0_api import *
from api_emulator.redfish.Endpoint1_api import *
from api_emulator.redfish.Endpoint2_api import *
from api_emulator.redfish.EthernetInterface0_api import *
from api_emulator.redfish.EthernetInterface1_api import *
from api_emulator.redfish.EthernetInterface2_api import *
from api_emulator.redfish.EthernetInterface3_api import *
from api_emulator.redfish.EthernetInterface4_api import *
from api_emulator.redfish.EthernetInterface5_api import *
from api_emulator.redfish.EthernetInterface6_api import *
from api_emulator.redfish.EventDestination_api import *
from api_emulator.redfish.ExternalAccountProvider0_api import *
from api_emulator.redfish.ExternalAccountProvider1_api import *
from api_emulator.redfish.FabricAdapter0_api import *
from api_emulator.redfish.FabricAdapter1_api import *
from api_emulator.redfish.Fabric_api import *
from api_emulator.redfish.Facility_api import *
from api_emulator.redfish.Fan_api import *
from api_emulator.redfish.GraphicsController_api import *
from api_emulator.redfish.HostInterface_api import *
from api_emulator.redfish.Job0_api import *
from api_emulator.redfish.Job1_api import *
from api_emulator.redfish.JsonSchemaFile_api import *
from api_emulator.redfish.KeyPolicy_api import *
from api_emulator.redfish.Key0_api import *
from api_emulator.redfish.Key1_api import *
from api_emulator.redfish.Key2_api import *
from api_emulator.redfish.License_api import *
from api_emulator.redfish.LogEntry0_api import *
from api_emulator.redfish.LogEntry1_api import *
from api_emulator.redfish.LogEntry2_api import *
from api_emulator.redfish.LogEntry3_api import *
from api_emulator.redfish.LogEntry4_api import *
from api_emulator.redfish.LogEntry5_api import *
from api_emulator.redfish.LogEntry6_api import *
from api_emulator.redfish.LogEntry7_api import *
from api_emulator.redfish.ManagerAccount0_api import *
from api_emulator.redfish.ManagerAccount1_api import *
from api_emulator.redfish.Manager_api import *
from api_emulator.redfish.MediaController_api import *
from api_emulator.redfish.MemoryChunks0_api import *
from api_emulator.redfish.MemoryChunks1_api import *
from api_emulator.redfish.MemoryChunks2_api import *
from api_emulator.redfish.MemoryChunks3_api import *
from api_emulator.redfish.MemoryDomain0_api import *
from api_emulator.redfish.MemoryDomain1_api import *
from api_emulator.redfish.MemoryDomain2_api import *
from api_emulator.redfish.MemoryDomain3_api import *
from api_emulator.redfish.Memory0_api import *
from api_emulator.redfish.Memory1_api import *
from api_emulator.redfish.Memory2_api import *
from api_emulator.redfish.Memory3_api import *
from api_emulator.redfish.Memory4_api import *
from api_emulator.redfish.Memory5_api import *
from api_emulator.redfish.MetricDefinition_api import *
from api_emulator.redfish.MetricReportDefinition_api import *
from api_emulator.redfish.MetricReport_api import *
from api_emulator.redfish.NetworkAdapter_api import *
from api_emulator.redfish.NetworkDeviceFunction_api import *
from api_emulator.redfish.NetworkInterface0_api import *
from api_emulator.redfish.NetworkInterface1_api import *
from api_emulator.redfish.NetworkInterface2_api import *
from api_emulator.redfish.NetworkInterface3_api import *
from api_emulator.redfish.NetworkInterface4_api import *
from api_emulator.redfish.NetworkPort_api import *
from api_emulator.redfish.OperatingConfig_api import *
from api_emulator.redfish.OutletGroup0_api import *
from api_emulator.redfish.OutletGroup1_api import *
from api_emulator.redfish.OutletGroup2_api import *
from api_emulator.redfish.OutletGroup3_api import *
from api_emulator.redfish.Outlet0_api import *
from api_emulator.redfish.Outlet1_api import *
from api_emulator.redfish.Outlet2_api import *
from api_emulator.redfish.Outlet3_api import *
from api_emulator.redfish.Outlet4_api import *
from api_emulator.redfish.PCIeDevice0_api import *
from api_emulator.redfish.PCIeDevice1_api import *
from api_emulator.redfish.PCIeDevice2_api import *
from api_emulator.redfish.PCIeDevice3_api import *
from api_emulator.redfish.PCIeFunction0_api import *
from api_emulator.redfish.PCIeFunction1_api import *
from api_emulator.redfish.PCIeFunction2_api import *
from api_emulator.redfish.PCIeFunction3_api import *
from api_emulator.redfish.Port0_api import *
from api_emulator.redfish.Port1_api import *
from api_emulator.redfish.Port2_api import *
from api_emulator.redfish.Port3_api import *
from api_emulator.redfish.Port4_api import *
from api_emulator.redfish.Port5_api import *
from api_emulator.redfish.Port6_api import *
from api_emulator.redfish.Port7_api import *
from api_emulator.redfish.Port8_api import *
from api_emulator.redfish.Port9_api import *
from api_emulator.redfish.Port10_api import *
from api_emulator.redfish.Port11_api import *
from api_emulator.redfish.Port12_api import *
from api_emulator.redfish.Port13_api import *
from api_emulator.redfish.Port14_api import *
from api_emulator.redfish.Port15_api import *
from api_emulator.redfish.Port16_api import *
from api_emulator.redfish.Port17_api import *
from api_emulator.redfish.Port18_api import *
from api_emulator.redfish.Port19_api import *
from api_emulator.redfish.Port20_api import *
from api_emulator.redfish.PowerDistribution0_api import *
from api_emulator.redfish.PowerDistribution1_api import *
from api_emulator.redfish.PowerDistribution2_api import *
from api_emulator.redfish.PowerDistribution3_api import *
from api_emulator.redfish.PowerDistribution4_api import *
from api_emulator.redfish.PowerDistribution5_api import *
from api_emulator.redfish.PowerDomain_api import *
from api_emulator.redfish.PowerSupply0_api import *
from api_emulator.redfish.PowerSupply1_api import *
from api_emulator.redfish.Processor0_api import *
from api_emulator.redfish.Processor1_api import *
from api_emulator.redfish.Processor2_api import *
from api_emulator.redfish.Processor3_api import *
from api_emulator.redfish.Processor4_api import *
from api_emulator.redfish.Processor5_api import *
from api_emulator.redfish.Processor6_api import *
from api_emulator.redfish.Processor7_api import *
from api_emulator.redfish.Processor8_api import *
from api_emulator.redfish.Processor9_api import *
from api_emulator.redfish.Processor10_api import *
from api_emulator.redfish.Processor11_api import *
from api_emulator.redfish.Processor12_api import *
from api_emulator.redfish.Processor13_api import *
from api_emulator.redfish.Processor14_api import *
from api_emulator.redfish.Processor15_api import *
from api_emulator.redfish.Processor16_api import *
from api_emulator.redfish.Processor17_api import *
from api_emulator.redfish.RegisteredClient_api import *
from api_emulator.redfish.ResourceBlock0_api import *
from api_emulator.redfish.ResourceBlock1_api import *
from api_emulator.redfish.Role0_api import *
from api_emulator.redfish.Role1_api import *
from api_emulator.redfish.RouteEntry0_api import *
from api_emulator.redfish.RouteEntry1_api import *
from api_emulator.redfish.RouteEntry2_api import *
from api_emulator.redfish.RouteEntry3_api import *
from api_emulator.redfish.RouteEntry4_api import *
from api_emulator.redfish.RouteEntry5_api import *
from api_emulator.redfish.RouteEntry6_api import *
from api_emulator.redfish.RouteEntry7_api import *
from api_emulator.redfish.RouteEntry8_api import *
from api_emulator.redfish.RouteEntry9_api import *
from api_emulator.redfish.RouteSetEntry0_api import *
from api_emulator.redfish.RouteSetEntry1_api import *
from api_emulator.redfish.RouteSetEntry2_api import *
from api_emulator.redfish.RouteSetEntry3_api import *
from api_emulator.redfish.RouteSetEntry4_api import *
from api_emulator.redfish.RouteSetEntry5_api import *
from api_emulator.redfish.RouteSetEntry6_api import *
from api_emulator.redfish.RouteSetEntry7_api import *
from api_emulator.redfish.RouteSetEntry8_api import *
from api_emulator.redfish.RouteSetEntry9_api import *
from api_emulator.redfish.SecureBootDatabase0_api import *
from api_emulator.redfish.SecureBootDatabase1_api import *
from api_emulator.redfish.SecureBootDatabase2_api import *
from api_emulator.redfish.Sensor0_api import *
from api_emulator.redfish.Sensor1_api import *
from api_emulator.redfish.Sensor2_api import *
from api_emulator.redfish.Sensor3_api import *
from api_emulator.redfish.Sensor4_api import *
from api_emulator.redfish.Sensor5_api import *
from api_emulator.redfish.Sensor6_api import *
from api_emulator.redfish.SerialInterface_api import *
from api_emulator.redfish.Signature0_api import *
from api_emulator.redfish.Signature1_api import *
from api_emulator.redfish.Signature2_api import *
from api_emulator.redfish.SimpleStorage0_api import *
from api_emulator.redfish.SimpleStorage1_api import *
from api_emulator.redfish.SimpleStorage2_api import *
from api_emulator.redfish.SimpleStorage3_api import *
from api_emulator.redfish.SimpleStorage4_api import *
from api_emulator.redfish.SoftwareInventory0_api import *
from api_emulator.redfish.SoftwareInventory1_api import *
from api_emulator.redfish.StorageController0_api import *
from api_emulator.redfish.StorageController1_api import *
from api_emulator.redfish.StorageController2_api import *
from api_emulator.redfish.StorageController3_api import *
from api_emulator.redfish.StorageController4_api import *
from api_emulator.redfish.StorageController5_api import *
from api_emulator.redfish.Storage0_api import *
from api_emulator.redfish.Storage1_api import *
from api_emulator.redfish.Storage2_api import *
from api_emulator.redfish.Storage3_api import *
from api_emulator.redfish.Storage4_api import *
from api_emulator.redfish.Storage5_api import *
from api_emulator.redfish.Switch_api import *
from api_emulator.redfish.Task0_api import *
from api_emulator.redfish.Task1_api import *
from api_emulator.redfish.Triggers_api import *
from api_emulator.redfish.USBController_api import *
from api_emulator.redfish.VCATEntry0_api import *
from api_emulator.redfish.VCATEntry1_api import *
from api_emulator.redfish.VCATEntry2_api import *
from api_emulator.redfish.VCATEntry3_api import *
from api_emulator.redfish.VCATEntry4_api import *
from api_emulator.redfish.VCATEntry5_api import *
from api_emulator.redfish.VCATEntry6_api import *
from api_emulator.redfish.VirtualMedia0_api import *
from api_emulator.redfish.VirtualMedia1_api import *
from api_emulator.redfish.VirtualMedia2_api import *
from api_emulator.redfish.VirtualMedia3_api import *
from api_emulator.redfish.VLanNetworkInterface0_api import *
from api_emulator.redfish.VLanNetworkInterface1_api import *
from api_emulator.redfish.VLanNetworkInterface2_api import *
from api_emulator.redfish.VLanNetworkInterface3_api import *
from api_emulator.redfish.VLanNetworkInterface4_api import *
from api_emulator.redfish.VLanNetworkInterface5_api import *
from api_emulator.redfish.VLanNetworkInterface6_api import *
from api_emulator.redfish.Volume0_api import *
from api_emulator.redfish.Volume1_api import *
from api_emulator.redfish.Volume2_api import *
from api_emulator.redfish.Volume3_api import *
from api_emulator.redfish.Volume4_api import *
from api_emulator.redfish.Volume5_api import *
from api_emulator.redfish.Volume6_api import *
from api_emulator.redfish.Volume7_api import *
from api_emulator.redfish.Volume8_api import *
from api_emulator.redfish.Volume9_api import *
from api_emulator.redfish.Volume10_api import *
from api_emulator.redfish.Volume11_api import *
from api_emulator.redfish.Volume12_api import *
from api_emulator.redfish.Volume13_api import *
from api_emulator.redfish.Volume14_api import *
from api_emulator.redfish.Volume15_api import *
from api_emulator.redfish.Volume16_api import *
from api_emulator.redfish.Volume17_api import *
from api_emulator.redfish.Volume18_api import *
from api_emulator.redfish.Volume19_api import *
from api_emulator.redfish.Zone0_api import *
from api_emulator.redfish.Zone1_api import *
from api_emulator.redfish.Capacity0_api import *
from api_emulator.redfish.Capacity1_api import *
from api_emulator.redfish.Capacity2_api import *
from api_emulator.redfish.Capacity3_api import *
from api_emulator.redfish.Capacity4_api import *
from api_emulator.redfish.Capacity5_api import *
from api_emulator.redfish.Capacity6_api import *
from api_emulator.redfish.Capacity7_api import *
from api_emulator.redfish.Capacity8_api import *
from api_emulator.redfish.ConsistencyGroup0_api import *
from api_emulator.redfish.ConsistencyGroup1_api import *
from api_emulator.redfish.ConsistencyGroup2_api import *
from api_emulator.redfish.ConsistencyGroup3_api import *
from api_emulator.redfish.FileShare0_api import *
from api_emulator.redfish.FileShare1_api import *
from api_emulator.redfish.FileShare2_api import *
from api_emulator.redfish.FileSystem0_api import *
from api_emulator.redfish.FileSystem1_api import *
from api_emulator.redfish.NVMeDomain_api import *
from api_emulator.redfish.NVMeFirmwareImage_api import *
from api_emulator.redfish.StorageGroup0_api import *
from api_emulator.redfish.StorageGroup1_api import *
from api_emulator.redfish.StorageGroup2_api import *
from api_emulator.redfish.StorageGroup3_api import *
from api_emulator.redfish.StoragePool0_api import *
from api_emulator.redfish.StoragePool1_api import *
from api_emulator.redfish.StoragePool2_api import *
from api_emulator.redfish.StoragePool3_api import *
from api_emulator.redfish.StoragePool4_api import *
from api_emulator.redfish.StoragePool5_api import *
from api_emulator.redfish.StoragePool6_api import *
from api_emulator.redfish.StoragePool7_api import *
from api_emulator.redfish.StoragePool8_api import *
from api_emulator.redfish.StoragePool9_api import *
from api_emulator.redfish.StoragePool10_api import *
from api_emulator.redfish.StoragePool11_api import *
from api_emulator.redfish.StoragePool12_api import *
from api_emulator.redfish.StoragePool13_api import *
from api_emulator.redfish.StoragePool14_api import *
from api_emulator.redfish.StoragePool15_api import *
from api_emulator.redfish.StoragePool16_api import *
from api_emulator.redfish.StoragePool17_api import *
from api_emulator.redfish.AccountService0_api import *
from api_emulator.redfish.AccountService1_api import *
from api_emulator.redfish.AggregationService_api import *
from api_emulator.redfish.Assembly0_api import *
from api_emulator.redfish.Assembly1_api import *
from api_emulator.redfish.Assembly2_api import *
from api_emulator.redfish.Assembly3_api import *
from api_emulator.redfish.Assembly4_api import *
from api_emulator.redfish.Assembly5_api import *
from api_emulator.redfish.Assembly6_api import *
from api_emulator.redfish.Assembly7_api import *
from api_emulator.redfish.Assembly8_api import *
from api_emulator.redfish.Assembly9_api import *
from api_emulator.redfish.Assembly10_api import *
from api_emulator.redfish.Assembly11_api import *
from api_emulator.redfish.Assembly12_api import *
from api_emulator.redfish.Assembly13_api import *
from api_emulator.redfish.Assembly14_api import *
from api_emulator.redfish.Assembly15_api import *
from api_emulator.redfish.Assembly16_api import *
from api_emulator.redfish.Assembly17_api import *
from api_emulator.redfish.Assembly18_api import *
from api_emulator.redfish.Assembly19_api import *
from api_emulator.redfish.Assembly20_api import *
from api_emulator.redfish.Assembly21_api import *
from api_emulator.redfish.Assembly22_api import *
from api_emulator.redfish.Assembly23_api import *
from api_emulator.redfish.Assembly24_api import *
from api_emulator.redfish.Assembly25_api import *
from api_emulator.redfish.Assembly26_api import *
from api_emulator.redfish.Assembly27_api import *
from api_emulator.redfish.Assembly28_api import *
from api_emulator.redfish.Assembly29_api import *
from api_emulator.redfish.Assembly30_api import *
from api_emulator.redfish.Assembly31_api import *
from api_emulator.redfish.Assembly32_api import *
from api_emulator.redfish.Assembly33_api import *
from api_emulator.redfish.Assembly34_api import *
from api_emulator.redfish.Assembly35_api import *
from api_emulator.redfish.Assembly36_api import *
from api_emulator.redfish.Assembly37_api import *
from api_emulator.redfish.Assembly38_api import *
from api_emulator.redfish.Assembly39_api import *
from api_emulator.redfish.Assembly40_api import *
from api_emulator.redfish.Assembly41_api import *
from api_emulator.redfish.Assembly42_api import *
from api_emulator.redfish.Assembly43_api import *
from api_emulator.redfish.Assembly44_api import *
from api_emulator.redfish.Assembly45_api import *
from api_emulator.redfish.Assembly46_api import *
from api_emulator.redfish.Assembly47_api import *
from api_emulator.redfish.Assembly48_api import *
from api_emulator.redfish.Assembly49_api import *
from api_emulator.redfish.Assembly50_api import *
from api_emulator.redfish.Assembly51_api import *
from api_emulator.redfish.Assembly52_api import *
from api_emulator.redfish.BatteryMetrics_api import *
from api_emulator.redfish.Bios0_api import *
from api_emulator.redfish.Bios1_api import *
from api_emulator.redfish.Bios2_api import *
from api_emulator.redfish.CertificateLocations_api import *
from api_emulator.redfish.CertificateService_api import *
from api_emulator.redfish.CompositionService_api import *
from api_emulator.redfish.EnvironmentMetrics0_api import *
from api_emulator.redfish.EnvironmentMetrics1_api import *
from api_emulator.redfish.EnvironmentMetrics2_api import *
from api_emulator.redfish.EnvironmentMetrics3_api import *
from api_emulator.redfish.EnvironmentMetrics4_api import *
from api_emulator.redfish.EnvironmentMetrics5_api import *
from api_emulator.redfish.EnvironmentMetrics6_api import *
from api_emulator.redfish.EnvironmentMetrics7_api import *
from api_emulator.redfish.EnvironmentMetrics8_api import *
from api_emulator.redfish.EnvironmentMetrics9_api import *
from api_emulator.redfish.EnvironmentMetrics10_api import *
from api_emulator.redfish.EnvironmentMetrics11_api import *
from api_emulator.redfish.EnvironmentMetrics12_api import *
from api_emulator.redfish.EnvironmentMetrics13_api import *
from api_emulator.redfish.EnvironmentMetrics14_api import *
from api_emulator.redfish.EnvironmentMetrics15_api import *
from api_emulator.redfish.EnvironmentMetrics16_api import *
from api_emulator.redfish.EnvironmentMetrics17_api import *
from api_emulator.redfish.EnvironmentMetrics18_api import *
from api_emulator.redfish.EnvironmentMetrics19_api import *
from api_emulator.redfish.EnvironmentMetrics20_api import *
from api_emulator.redfish.EnvironmentMetrics21_api import *
from api_emulator.redfish.EnvironmentMetrics22_api import *
from api_emulator.redfish.EnvironmentMetrics23_api import *
from api_emulator.redfish.EnvironmentMetrics24_api import *
from api_emulator.redfish.EnvironmentMetrics25_api import *
from api_emulator.redfish.EnvironmentMetrics26_api import *
from api_emulator.redfish.EnvironmentMetrics27_api import *
from api_emulator.redfish.EnvironmentMetrics28_api import *
from api_emulator.redfish.EnvironmentMetrics29_api import *
from api_emulator.redfish.EnvironmentMetrics30_api import *
from api_emulator.redfish.EnvironmentMetrics31_api import *
from api_emulator.redfish.EnvironmentMetrics32_api import *
from api_emulator.redfish.EnvironmentMetrics33_api import *
from api_emulator.redfish.EnvironmentMetrics34_api import *
from api_emulator.redfish.EnvironmentMetrics35_api import *
from api_emulator.redfish.EnvironmentMetrics36_api import *
from api_emulator.redfish.EnvironmentMetrics37_api import *
from api_emulator.redfish.EnvironmentMetrics38_api import *
from api_emulator.redfish.EnvironmentMetrics39_api import *
from api_emulator.redfish.EnvironmentMetrics40_api import *
from api_emulator.redfish.EnvironmentMetrics41_api import *
from api_emulator.redfish.EnvironmentMetrics42_api import *
from api_emulator.redfish.EnvironmentMetrics43_api import *
from api_emulator.redfish.EnvironmentMetrics44_api import *
from api_emulator.redfish.EnvironmentMetrics45_api import *
from api_emulator.redfish.EnvironmentMetrics46_api import *
from api_emulator.redfish.EnvironmentMetrics47_api import *
from api_emulator.redfish.EnvironmentMetrics48_api import *
from api_emulator.redfish.EnvironmentMetrics49_api import *
from api_emulator.redfish.EnvironmentMetrics50_api import *
from api_emulator.redfish.EventService_api import *
from api_emulator.redfish.JobService_api import *
from api_emulator.redfish.KeyService_api import *
from api_emulator.redfish.LicenseService_api import *
from api_emulator.redfish.LogService0_api import *
from api_emulator.redfish.LogService1_api import *
from api_emulator.redfish.LogService2_api import *
from api_emulator.redfish.LogService3_api import *
from api_emulator.redfish.LogService4_api import *
from api_emulator.redfish.LogService5_api import *
from api_emulator.redfish.LogService6_api import *
from api_emulator.redfish.LogService7_api import *
from api_emulator.redfish.ManagerDiagnosticData_api import *
from api_emulator.redfish.ManagerNetworkProtocol_api import *
from api_emulator.redfish.MemoryMetrics0_api import *
from api_emulator.redfish.MemoryMetrics1_api import *
from api_emulator.redfish.MemoryMetrics2_api import *
from api_emulator.redfish.MemoryMetrics3_api import *
from api_emulator.redfish.MemoryMetrics4_api import *
from api_emulator.redfish.MemoryMetrics5_api import *
from api_emulator.redfish.MemoryMetrics6_api import *
from api_emulator.redfish.MemoryMetrics7_api import *
from api_emulator.redfish.MemoryMetrics8_api import *
from api_emulator.redfish.MemoryMetrics9_api import *
from api_emulator.redfish.MemoryMetrics10_api import *
from api_emulator.redfish.MemoryMetrics11_api import *
from api_emulator.redfish.MemoryMetrics12_api import *
from api_emulator.redfish.MessageRegistryFile_api import *
from api_emulator.redfish.NetworkAdapterMetrics_api import *
from api_emulator.redfish.NetworkDeviceFunctionMetrics_api import *
from api_emulator.redfish.PCIeSlots_api import *
from api_emulator.redfish.PortMetrics0_api import *
from api_emulator.redfish.PortMetrics1_api import *
from api_emulator.redfish.PortMetrics2_api import *
from api_emulator.redfish.PortMetrics3_api import *
from api_emulator.redfish.PortMetrics4_api import *
from api_emulator.redfish.PortMetrics5_api import *
from api_emulator.redfish.PortMetrics6_api import *
from api_emulator.redfish.PortMetrics7_api import *
from api_emulator.redfish.PortMetrics8_api import *
from api_emulator.redfish.PortMetrics9_api import *
from api_emulator.redfish.PortMetrics10_api import *
from api_emulator.redfish.PortMetrics11_api import *
from api_emulator.redfish.PortMetrics12_api import *
from api_emulator.redfish.PortMetrics13_api import *
from api_emulator.redfish.PortMetrics14_api import *
from api_emulator.redfish.PortMetrics15_api import *
from api_emulator.redfish.PortMetrics16_api import *
from api_emulator.redfish.PortMetrics17_api import *
from api_emulator.redfish.PortMetrics18_api import *
from api_emulator.redfish.PortMetrics19_api import *
from api_emulator.redfish.PortMetrics20_api import *
from api_emulator.redfish.PowerDistributionMetrics0_api import *
from api_emulator.redfish.PowerDistributionMetrics1_api import *
from api_emulator.redfish.PowerDistributionMetrics2_api import *
from api_emulator.redfish.PowerDistributionMetrics3_api import *
from api_emulator.redfish.PowerDistributionMetrics4_api import *
from api_emulator.redfish.PowerDistributionMetrics5_api import *
from api_emulator.redfish.PowerEquipment_api import *
from api_emulator.redfish.PowerSubsystem_api import *
from api_emulator.redfish.PowerSupplyMetrics0_api import *
from api_emulator.redfish.PowerSupplyMetrics1_api import *
from api_emulator.redfish.Power_api import *
from api_emulator.redfish.ProcessorMetrics0_api import *
from api_emulator.redfish.ProcessorMetrics1_api import *
from api_emulator.redfish.ProcessorMetrics2_api import *
from api_emulator.redfish.ProcessorMetrics3_api import *
from api_emulator.redfish.ProcessorMetrics4_api import *
from api_emulator.redfish.ProcessorMetrics5_api import *
from api_emulator.redfish.ProcessorMetrics6_api import *
from api_emulator.redfish.ProcessorMetrics7_api import *
from api_emulator.redfish.ProcessorMetrics8_api import *
from api_emulator.redfish.ProcessorMetrics9_api import *
from api_emulator.redfish.ProcessorMetrics10_api import *
from api_emulator.redfish.ProcessorMetrics11_api import *
from api_emulator.redfish.ProcessorMetrics12_api import *
from api_emulator.redfish.ProcessorMetrics13_api import *
from api_emulator.redfish.ProcessorMetrics14_api import *
from api_emulator.redfish.ProcessorMetrics15_api import *
from api_emulator.redfish.ProcessorMetrics16_api import *
from api_emulator.redfish.ProcessorMetrics17_api import *
from api_emulator.redfish.ProcessorMetrics18_api import *
from api_emulator.redfish.ProcessorMetrics19_api import *
from api_emulator.redfish.ProcessorMetrics20_api import *
from api_emulator.redfish.SecureBoot0_api import *
from api_emulator.redfish.SecureBoot1_api import *
from api_emulator.redfish.SecureBoot2_api import *
from api_emulator.redfish.ServiceConditions_api import *
from api_emulator.redfish.ServiceRoot0_api import *
from api_emulator.redfish.ServiceRoot1_api import *
from api_emulator.redfish.SessionService_api import *
from api_emulator.redfish.Session_api import *
from api_emulator.redfish.SwitchMetrics_api import *
from api_emulator.redfish.TaskService_api import *
from api_emulator.redfish.TelemetryService_api import *
from api_emulator.redfish.ThermalMetrics_api import *
from api_emulator.redfish.ThermalSubsystem_api import *
from api_emulator.redfish.Thermal_api import *
from api_emulator.redfish.UpdateService_api import *
from api_emulator.redfish.ClassOfService0_api import *
from api_emulator.redfish.ClassOfService1_api import *
from api_emulator.redfish.DataProtectionLineOfService0_api import *
from api_emulator.redfish.DataProtectionLineOfService1_api import *
from api_emulator.redfish.DataProtectionLoSCapabilities_api import *
from api_emulator.redfish.DataSecurityLineOfService0_api import *
from api_emulator.redfish.DataSecurityLineOfService1_api import *
from api_emulator.redfish.DataSecurityLoSCapabilities_api import *
from api_emulator.redfish.DataStorageLineOfService0_api import *
from api_emulator.redfish.DataStorageLineOfService1_api import *
from api_emulator.redfish.DataStorageLoSCapabilities_api import *
from api_emulator.redfish.HostedStorageServices_api import *
from api_emulator.redfish.IOConnectivityLineOfService0_api import *
from api_emulator.redfish.IOConnectivityLineOfService1_api import *
from api_emulator.redfish.IOConnectivityLoSCapabilities_api import *
from api_emulator.redfish.IOPerformanceLineOfService0_api import *
from api_emulator.redfish.IOPerformanceLineOfService1_api import *
from api_emulator.redfish.IOPerformanceLoSCapabilities_api import *
from api_emulator.redfish.StorageService0_api import *
from api_emulator.redfish.StorageService1_api import *

from . import utils
import os
import json
import urllib3
from uuid import uuid4
from threading import Thread
import logging
import copy
# Local imports
import g

from .static_loader import load_static
from .resource_dictionary import ResourceDictionary
from .exceptions import CreatePooledNodeError, RemovePooledNodeError

mockupfolders = []

# The ResourceManager __init__ method sets up the static and dynamic
# resources.
#
# When a resource is accessed, the resource is sought in the following
# order:
#   1. Dynamic resources for specific URIs
#   2. Default dynamic resources
#   3. Static resource dictionary
#
# This allows specific resources to be implemented as dynamic resources
# while leaving the remainder of the URI path as static resources.
#
# Static resources are loaded from the ./redfish/static directory.
# This directory is a copy of the one of the ./mockups directories.
#
# Dynamic resources are attached to endpoints using the Flask-restful
# mechanism, not the Flask mechanism.
#   - This involves associating an API class to a resource endpoint.
#     A collection resource requires the association of the collection
#     resource and the member resource(s).
#   - Once the API is added, explicit calls can be made to one or more
#     singleton resources that have been populated.
#   - The EgResource* and EgSubResource* files provide examples of how
#     to add dynamic resources.
#
# Note: There is one additional change that needs to be made in order
# to create multiple instances of a resource. The resource endpoint
# for a second instance will collide with the first, because flask does
# not re-use endpoint names for subordinate resources. This results
# in an assertion error failure:
#   "AssertionError: View function mapping is overwriting an existing
#   endpoint function"
#
# The fix would be to form unique endpoint names and pass them in
# with the call to api_add_resource(), as shown in the following:
#   api.add_resource(Todo, '/todo/<int:todo_id>', endpoint='todo_ep')

class ResourceManager(object):
    """
    ResourceManager Class

    Load static resources and dynamic resources
    Defines ServiceRoot
    """

    def __init__(self, rest_base, spec, mode, auth_mode, trays=None):
        """
        Arguments:
            rest_base - Base URL for the REST interface
            spec      - Which spec to use, Redfish or Chinook
            trays     - (Optional) List of trays to initially load into the
                        resource manager
        When a resource is accessed, the resource is sought in the following order
        1. Dynamic resource for specific URI
        2. Static resource dictionary
        """

        self.rest_base = rest_base

        self.mode = mode
        self.spec = spec
        self.modified = utils.timestamp()
        self.uuid = str(uuid4())
        self.time = self.modified
        self.cs_puid_count = 0

        # Load the static resources into the dictionary

        self.resource_dictionary = ResourceDictionary()
        mockupfolders = copy.copy(g.staticfolders)

        if "Redfish" in mockupfolders:
            logging.info('Loading Redfish static resources')
            self.ServiceRoot =       load_static('', 'redfish', mode, rest_base, self.resource_dictionary)

            self.AccountService =   load_static('AccountService', 'redfish', mode, rest_base, self.resource_dictionary)

            self.Registries =       load_static('Registries', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Registries =       load_static('Registries', 'redfish', mode, rest_base, self.resource_dictionary)
            self.SessionService =   load_static('SessionService', 'redfish', mode, rest_base, self.resource_dictionary)
            self.TaskService =      load_static('TaskService', 'redfish', mode, rest_base, self.resource_dictionary)
            self.EventService =     load_static('EventService', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Chassis =          load_static('Chassis', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Storage =          load_static('Storage', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Fabrics =          load_static('Fabrics', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Systems=           load_static('Systems', 'redfish', mode, rest_base, self.resource_dictionary)
            self.Managers =         load_static('Managers', 'redfish', mode, rest_base, self.resource_dictionary)

#        if "Swordfish" in mockupfolders:
#            self.StorageServices = load_static('StorageServices', 'redfish', mode, rest_base, self.resource_dictionary)
#            self.StorageSystems = load_static('StorageSystems', 'redfish', mode, rest_base, self.resource_dictionary)

        # Attach APIs for dynamic resources
        g.api.add_resource(Capacity0CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/StoragePools/<string:StoragePoolId>/CapacitySources')
        g.api.add_resource(Capacity0API, '/redfish/v1/StorageServices/<string:StorageServiceId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>')

        g.api.add_resource(Capacity1CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/Volumes/<string:VolumeId>/CapacitySources')
        g.api.add_resource(Capacity1API, '/redfish/v1/StorageServices/<string:StorageServiceId>/Volumes/<string:VolumeId>/CapacitySources/<string:CapacitySourceId>')

        g.api.add_resource(Capacity2CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/FileSystems/<string:FileSystemId>/CapacitySources')
        g.api.add_resource(Capacity2API, '/redfish/v1/StorageServices/<string:StorageServiceId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>')

        g.api.add_resource(Capacity3CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/CapacitySources')
        g.api.add_resource(Capacity3API, '/redfish/v1/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>')

        g.api.add_resource(Capacity4CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/Volumes/<string:VolumeId>/CapacitySources')
        g.api.add_resource(Capacity4API, '/redfish/v1/Storage/<string:StorageId>/Volumes/<string:VolumeId>/CapacitySources/<string:CapacitySourceId>')

        g.api.add_resource(Capacity5CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/FileSystems/<string:FileSystemId>/CapacitySources')
        g.api.add_resource(Capacity5API, '/redfish/v1/Storage/<string:StorageId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>')

        g.api.add_resource(Capacity6CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/CapacitySources')
        g.api.add_resource(Capacity6API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>')

        g.api.add_resource(Capacity7CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Volumes/<string:VolumeId>/CapacitySources')
        g.api.add_resource(Capacity7API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Volumes/<string:VolumeId>/CapacitySources/<string:CapacitySourceId>')

        g.api.add_resource(Capacity8CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/FileSystems/<string:FileSystemId>/CapacitySources')
        g.api.add_resource(Capacity8API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>')

        g.api.add_resource(ConsistencyGroup0CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/ConsistencyGroups')
        g.api.add_resource(ConsistencyGroup0API, '/redfish/v1/Storage/<string:StorageId>/ConsistencyGroups/<string:ConsistencyGroupId>')

        g.api.add_resource(ConsistencyGroup1CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/ConsistencyGroups')
        g.api.add_resource(ConsistencyGroup1API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/ConsistencyGroups/<string:ConsistencyGroupId>')

        g.api.add_resource(ConsistencyGroup2CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/ConsistencyGroups')
        g.api.add_resource(ConsistencyGroup2API, '/redfish/v1/StorageServices/<string:StorageServiceId>/ConsistencyGroups/<string:ConsistencyGroupId>')

        g.api.add_resource(ConsistencyGroup3CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/Volumes/<string:VolumeId>/ConsistencyGroups')
        g.api.add_resource(ConsistencyGroup3API, '/redfish/v1/StorageServices/<string:StorageServiceId>/Volumes/<string:VolumeId>/ConsistencyGroups/<string:ConsistencyGroupId>')

        g.api.add_resource(FileShare0CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/FileSystems/<string:FileSystemsId>/ExportedFileShares')
        g.api.add_resource(FileShare0API, '/redfish/v1/Storage/<string:StorageId>/FileSystems/<string:FileSystemsId>/ExportedFileShares/<string:ExportedFileSharesId>')

        g.api.add_resource(FileShare1CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemsId>/Storage/<string:StorageId>/FileSystems/<string:FileSystemsId>/ExportedFileShares')
        g.api.add_resource(FileShare1API, '/redfish/v1/Systems/<string:ComputerSystemsId>/Storage/<string:StorageId>/FileSystems/<string:FileSystemsId>/ExportedFileShares/<string:ExportedFileSharesId>')

        g.api.add_resource(FileShare2CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/FileSystems/<string:FileSystemsId>/ExportedFileShares')
        g.api.add_resource(FileShare2API, '/redfish/v1/StorageServices/<string:StorageServiceId>/FileSystems/<string:FileSystemsId>/ExportedFileShares/<string:ExportedFileSharesId>')

        g.api.add_resource(FileSystem0CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/FileSystems')
        g.api.add_resource(FileSystem0API, '/redfish/v1/StorageServices/<string:StorageServiceId>/FileSystems/<string:FileSystemId>')

        g.api.add_resource(FileSystem1CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/FileSystems')
        g.api.add_resource(FileSystem1API, '/redfish/v1/Storage/<string:StorageId>/FileSystems/<string:FileSystemId>')

        g.api.add_resource(NVMeDomainCollectionAPI, '/redfish/v1/NVMeDomains')
        g.api.add_resource(NVMeDomainAPI, '/redfish/v1/NVMeDomains/<string:NVMeDomainId>')

        g.api.add_resource(NVMeFirmwareImageCollectionAPI, '/redfish/v1/NVMeDomains/<string:DomainId>/AvailableFirmwareImages')
        g.api.add_resource(NVMeFirmwareImageAPI, '/redfish/v1/NVMeDomains/<string:DomainId>/AvailableFirmwareImages/<string:FirmwareImageId>')

        g.api.add_resource(StorageGroup0CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/StorageGroups')
        g.api.add_resource(StorageGroup0API, '/redfish/v1/StorageServices/<string:StorageServiceId>/StorageGroups/<string:StorageGroupId>')

        g.api.add_resource(StorageGroup1CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/Volumes/<string:VolumeId>/StorageGroups')
        g.api.add_resource(StorageGroup1API, '/redfish/v1/StorageServices/<string:StorageServiceId>/Volumes/<string:VolumeId>/StorageGroups/<string:StorageGroupId>')

        g.api.add_resource(StorageGroup2CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/StorageGroups')
        g.api.add_resource(StorageGroup2API, '/redfish/v1/Storage/<string:StorageId>/StorageGroups/<string:StorageGroupId>')

        g.api.add_resource(StorageGroup3CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/Volumes/<string:VolumeId>/StorageGroups')
        g.api.add_resource(StorageGroup3API, '/redfish/v1/Storage/<string:StorageId>/Volumes/<string:VolumeId>/StorageGroups/<string:StorageGroupId>')

        g.api.add_resource(StoragePool0CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/StoragePools')
        g.api.add_resource(StoragePool0API, '/redfish/v1/StorageServices/<string:StorageServiceId>/StoragePools/<string:StoragePoolId>')

        g.api.add_resource(StoragePool1CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/StoragePools/<string:StoragePoolId>/AllocatedPools')
        g.api.add_resource(StoragePool1API, '/redfish/v1/StorageServices/<string:StorageServiceId>/StoragePools/<string:StoragePoolId>/AllocatedPools/<string:AllocatedPoolId>')

        g.api.add_resource(StoragePool2CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools')
        g.api.add_resource(StoragePool2API, '/redfish/v1/StorageServices/<string:StorageServiceId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools/<string:ProvidingPoolId>')

        g.api.add_resource(StoragePool3CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/Volumes/<string:VolumeId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools')
        g.api.add_resource(StoragePool3API, '/redfish/v1/StorageServices/<string:StorageServiceId>/Volumes/<string:VolumeId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools/<string:StoragePoolId>')

        g.api.add_resource(StoragePool4CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/Volumes/<string:VolumeId>/AllocatedPools')
        g.api.add_resource(StoragePool4API, '/redfish/v1/StorageServices/<string:StorageServiceId>/Volumes/<string:VolumeId>/AllocatedPools/<string:StoragePoolId>')

        g.api.add_resource(StoragePool5CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools')
        g.api.add_resource(StoragePool5API, '/redfish/v1/StorageServices/<string:StorageServiceId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools/<string:StoragePoolId>')

        g.api.add_resource(StoragePool6CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/StoragePools')
        g.api.add_resource(StoragePool6API, '/redfish/v1/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>')

        g.api.add_resource(StoragePool7CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/AllocatedPools')
        g.api.add_resource(StoragePool7API, '/redfish/v1/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/AllocatedPools/<string:AllocatedPoolId>')

        g.api.add_resource(StoragePool8CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools')
        g.api.add_resource(StoragePool8API, '/redfish/v1/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools/<string:ProvidingPoolId>')

        g.api.add_resource(StoragePool9CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/Volumes/<string:VolumeId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools')
        g.api.add_resource(StoragePool9API, '/redfish/v1/Storage/<string:StorageId>/Volumes/<string:VolumeId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools/<string:StoragePoolId>')

        g.api.add_resource(StoragePool10CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/Volumes/<string:VolumeId>/AllocatedPools')
        g.api.add_resource(StoragePool10API, '/redfish/v1/Storage/<string:StorageId>/Volumes/<string:VolumeId>/AllocatedPools/<string:StoragePoolId>')

        g.api.add_resource(StoragePool11CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools')
        g.api.add_resource(StoragePool11API, '/redfish/v1/Storage/<string:StorageId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools/<string:StoragePoolId>')

        g.api.add_resource(StoragePool12CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StoragePools')
        g.api.add_resource(StoragePool12API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>')

        g.api.add_resource(StoragePool13CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/AllocatedPools')
        g.api.add_resource(StoragePool13API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/AllocatedPools/<string:AllocatedPoolId>')

        g.api.add_resource(StoragePool14CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools')
        g.api.add_resource(StoragePool14API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools/<string:ProvidingPoolId>')

        g.api.add_resource(StoragePool15CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Volumes/<string:VolumeId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools')
        g.api.add_resource(StoragePool15API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Volumes/<string:VolumeId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools/<string:StoragePoolId>')

        g.api.add_resource(StoragePool16CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Volumes/<string:VolumeId>/AllocatedPools')
        g.api.add_resource(StoragePool16API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Volumes/<string:VolumeId>/AllocatedPools/<string:StoragePoolId>')

        g.api.add_resource(StoragePool17CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools')
        g.api.add_resource(StoragePool17API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>/ProvidingPools/<string:StoragePoolId>')

        g.api.add_resource(Volume0CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Volumes')
        g.api.add_resource(Volume0API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Volumes/<string:VolumeId>')

        g.api.add_resource(Volume1CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Volumes')
        g.api.add_resource(Volume1API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Volumes/<string:VolumeId>')

        g.api.add_resource(Volume2CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Volumes')
        g.api.add_resource(Volume2API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Volumes/<string:VolumeId>')

        g.api.add_resource(Volume3CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Volumes')
        g.api.add_resource(Volume3API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Volumes/<string:VolumeId>')

        g.api.add_resource(Volume4CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/ConsistencyGroups/<string:ConsistencyGroupId>/Volumes')
        g.api.add_resource(Volume4API, '/redfish/v1/Storage/<string:StorageId>/ConsistencyGroups/<string:ConsistencyGroupId>/Volumes/<string:VolumeId>')

        g.api.add_resource(Volume5CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>/ProvidingVolumes')
        g.api.add_resource(Volume5API, '/redfish/v1/Storage/<string:StorageId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>/ProvidingVolumes/<string:VolumeId>')

        g.api.add_resource(Volume6CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/AllocatedVolumes')
        g.api.add_resource(Volume6API, '/redfish/v1/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/AllocatedVolumes/<string:VolumeId>')

        g.api.add_resource(Volume7CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>/ProvidingVolumes')
        g.api.add_resource(Volume7API, '/redfish/v1/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>/ProvidingVolumes/<string:VolumeId>')

        g.api.add_resource(Volume8CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/Volumes')
        g.api.add_resource(Volume8API, '/redfish/v1/Storage/<string:StorageId>/Volumes/<string:VolumeId>')

        g.api.add_resource(Volume9CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/ConsistencyGroups/<string:ConsistencyGroupId>/Volumes')
        g.api.add_resource(Volume9API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/ConsistencyGroups/<string:ConsistencyGroupId>/Volumes/<string:VolumeId>')

        g.api.add_resource(Volume10CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>/ProvidingVolumes')
        g.api.add_resource(Volume10API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>/ProvidingVolumes/<string:VolumeId>')

        g.api.add_resource(Volume11CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/AllocatedVolumes')
        g.api.add_resource(Volume11API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/AllocatedVolumes/<string:VolumeId>')

        g.api.add_resource(Volume12CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>/ProvidingVolumes')
        g.api.add_resource(Volume12API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>/ProvidingVolumes/<string:VolumeId>')

        g.api.add_resource(Volume13CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Volumes')
        g.api.add_resource(Volume13API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Volumes/<string:VolumeId>')

        g.api.add_resource(Volume14CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/ConsistencyGroups/<string:ConsistencyGroupId>/Volumes')
        g.api.add_resource(Volume14API, '/redfish/v1/StorageServices/<string:StorageServiceId>/ConsistencyGroups/<string:ConsistencyGroupId>/Volumes/<string:VolumeId>')

        g.api.add_resource(Volume15CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>/ProvidingVolumes')
        g.api.add_resource(Volume15API, '/redfish/v1/StorageServices/<string:StorageServiceId>/FileSystems/<string:FileSystemId>/CapacitySources/<string:CapacitySourceId>/ProvidingVolumes/<string:VolumeId>')

        g.api.add_resource(Volume16CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/StoragePools/<string:StoragePoolId>/AllocatedVolumes')
        g.api.add_resource(Volume16API, '/redfish/v1/StorageServices/<string:StorageServiceId>/StoragePools/<string:StoragePoolId>/AllocatedVolumes/<string:VolumeId>')

        g.api.add_resource(Volume17CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>/ProvidingVolumes')
        g.api.add_resource(Volume17API, '/redfish/v1/StorageServices/<string:StorageServiceId>/StoragePools/<string:StoragePoolId>/CapacitySources/<string:CapacitySourceId>/ProvidingVolumes/<string:VolumeId>')

        g.api.add_resource(Volume18CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/Volumes')
        g.api.add_resource(Volume18API, '/redfish/v1/StorageServices/<string:StorageServiceId>/Volumes/<string:VolumeId>')

        g.api.add_resource(Volume19CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/Volumes/<string:VolumeId>/CapacitySources/<string:CapacitySourceId>/ProvidingVolumes')
        g.api.add_resource(Volume19API, '/redfish/v1/StorageServices/<string:StorageServiceId>/Volumes/<string:VolumeId>/CapacitySources/<string:CapacitySourceId>/ProvidingVolumes/<string:ProvidingVolumeId>')

        g.api.add_resource(AccelerationFunction0CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/AccelerationFunctions')
        g.api.add_resource(AccelerationFunction0API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/AccelerationFunctions/<string:AccelerationFunctionId>')

        g.api.add_resource(AccelerationFunction1CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/AccelerationFunctions')
        g.api.add_resource(AccelerationFunction1API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/AccelerationFunctions/<string:AccelerationFunctionId>')

        g.api.add_resource(AccelerationFunction2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/AccelerationFunctions')
        g.api.add_resource(AccelerationFunction2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/AccelerationFunctions/<string:AccelerationFunctionId>')

        g.api.add_resource(AccelerationFunction3CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/AccelerationFunctions')
        g.api.add_resource(AccelerationFunction3API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/AccelerationFunctions/<string:AccelerationFunctionId>')

        g.api.add_resource(AccelerationFunction4CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/AccelerationFunctions')
        g.api.add_resource(AccelerationFunction4API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/AccelerationFunctions/<string:AccelerationFunctionId>')

        g.api.add_resource(AddressPoolCollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/AddressPools')
        g.api.add_resource(AddressPoolAPI, '/redfish/v1/Fabrics/<string:FabricId>/AddressPools/<string:AddressPoolId>')

        g.api.add_resource(AggregateCollectionAPI, '/redfish/v1/AggregationService/Aggregates')
        g.api.add_resource(AggregateAPI, '/redfish/v1/AggregationService/Aggregates/<string:AggregateId>')

        g.api.add_resource(AggregationSourceCollectionAPI, '/redfish/v1/AggregationService/AggregationSources')
        g.api.add_resource(AggregationSourceAPI, '/redfish/v1/AggregationService/AggregationSources/<string:AggregationSourceId>')

        g.api.add_resource(AllowDeny0CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/NetworkDeviceFunctions/<string:NetworkDeviceFunctionId>/AllowDeny')
        g.api.add_resource(AllowDeny0API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/NetworkDeviceFunctions/<string:NetworkDeviceFunctionId>/AllowDeny/<string:AllowDenyId>')

        g.api.add_resource(AllowDeny1CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/NetworkInterfaces/<string:NetworkInterfaceId>/NetworkDeviceFunctions<string:NetworkDeviceFunctionId>/AllowDeny')
        g.api.add_resource(AllowDeny1API, '/redfish/v1/Systems/<string:ComputerSystemId>/NetworkInterfaces/<string:NetworkInterfaceId>/NetworkDeviceFunctions<string:NetworkDeviceFunctionId>/AllowDeny/<string:AllowDenyId>')

        g.api.add_resource(AllowDeny2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/NetworkInterfaces/<string:NetworkInterfaceId>/NetworkDeviceFunctions<string:NetworkDeviceFunctionId>/AllowDeny')
        g.api.add_resource(AllowDeny2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/NetworkInterfaces/<string:NetworkInterfaceId>/NetworkDeviceFunctions<string:NetworkDeviceFunctionId>/AllowDeny/<string:AllowDenyId>')

        g.api.add_resource(AllowDeny3CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/NetworkInterfaces/<string:NetworkInterfaceId>/NetworkDeviceFunctions<string:NetworkDeviceFunctionId>/AllowDeny')
        g.api.add_resource(AllowDeny3API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/NetworkInterfaces/<string:NetworkInterfaceId>/NetworkDeviceFunctions<string:NetworkDeviceFunctionId>/AllowDeny/<string:AllowDenyId>')

        g.api.add_resource(AllowDeny4CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/NetworkInterfaces/<string:NetworkInterfaceId>/NetworkDeviceFunctions<string:NetworkDeviceFunctionId>/AllowDeny')
        g.api.add_resource(AllowDeny4API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/NetworkInterfaces/<string:NetworkInterfaceId>/NetworkDeviceFunctions<string:NetworkDeviceFunctionId>/AllowDeny/<string:AllowDenyId>')

        g.api.add_resource(AllowDeny5CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/NetworkInterfaces/<string:NetworkInterfaceId>/NetworkDeviceFunctions<string:NetworkDeviceFunctionId>/AllowDeny')
        g.api.add_resource(AllowDeny5API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/NetworkInterfaces/<string:NetworkInterfaceId>/NetworkDeviceFunctions<string:NetworkDeviceFunctionId>/AllowDeny/<string:AllowDenyId>')

        g.api.add_resource(BatteryCollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/PowerSubsystem/Batteries')
        g.api.add_resource(BatteryAPI, '/redfish/v1/Chassis/<string:ChassisId>/PowerSubsystem/Batteries/<string:BatteryId>')

        g.api.add_resource(BootOption0CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/BootOptions')
        g.api.add_resource(BootOption0API, '/redfish/v1/Systems/<string:ComputerSystemId>/BootOptions/<string:BootOptionId>')

        g.api.add_resource(BootOption1CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/BootOptions')
        g.api.add_resource(BootOption1API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/BootOptions/<string:BootOptionId>')

        g.api.add_resource(BootOption2CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/BootOptions')
        g.api.add_resource(BootOption2API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/BootOptions/<string:BootOptionId>')

        g.api.add_resource(CableCollectionAPI, '/redfish/v1/Cables')
        g.api.add_resource(CableAPI, '/redfish/v1/Cables/<string:CableId>')

        g.api.add_resource(Certificate0CollectionAPI, '/redfish/v1/AccountService/Accounts/<string:ManagerAccountId>/Certificates')
        g.api.add_resource(Certificate0API, '/redfish/v1/AccountService/Accounts/<string:ManagerAccountId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate1CollectionAPI, '/redfish/v1/AccountService/ActiveDirectory/Certificates')
        g.api.add_resource(Certificate1API, '/redfish/v1/AccountService/ActiveDirectory/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate2CollectionAPI, '/redfish/v1/AccountService/LDAP/Certificates')
        g.api.add_resource(Certificate2API, '/redfish/v1/AccountService/LDAP/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate3CollectionAPI, '/redfish/v1/AccountService/ExternalAccountProviders/<string:ExternalAccountProviderId>/Certificates')
        g.api.add_resource(Certificate3API, '/redfish/v1/AccountService/ExternalAccountProviders/<string:ExternalAccountProviderId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate4CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/Accounts/<string:ManagerAccountId>/Certificates')
        g.api.add_resource(Certificate4API, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/Accounts/<string:ManagerAccountId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate5CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/ActiveDirectory/Certificates')
        g.api.add_resource(Certificate5API, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/ActiveDirectory/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate6CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/LDAP/Certificates')
        g.api.add_resource(Certificate6API, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/LDAP/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate7CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/ExternalAccountProviders/<string:ExternalAccountProviderId>/Certificates')
        g.api.add_resource(Certificate7API, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/ExternalAccountProviders/<string:ExternalAccountProviderId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate8CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/NetworkProtocol/HTTPS/Certificates')
        g.api.add_resource(Certificate8API, '/redfish/v1/Managers/<string:ManagerId>/NetworkProtocol/HTTPS/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate9CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Boot/Certificates')
        g.api.add_resource(Certificate9API, '/redfish/v1/Systems/<string:ComputerSystemId>/Boot/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate10CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Boot/Certificates')
        g.api.add_resource(Certificate10API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Boot/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate11CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Boot/Certificates')
        g.api.add_resource(Certificate11API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Boot/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate12CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>/Certificates')
        g.api.add_resource(Certificate12API, '/redfish/v1/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate13CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>/Certificates')
        g.api.add_resource(Certificate13API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate14CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>/Certificates')
        g.api.add_resource(Certificate14API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate15CollectionAPI, '/redfish/v1/EventService/Subscriptions/<string:EventDestinationId>/Certificates')
        g.api.add_resource(Certificate15API, '/redfish/v1/EventService/Subscriptions/<string:EventDestinationId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate16CollectionAPI, '/redfish/v1/EventService/Subscriptions/<string:EventDestinationId>/ClientCertificates')
        g.api.add_resource(Certificate16API, '/redfish/v1/EventService/Subscriptions/<string:EventDestinationId>/ClientCertificates/<string:CertificateId>')

        g.api.add_resource(Certificate17CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Certificates')
        g.api.add_resource(Certificate17API, '/redfish/v1/Systems/<string:ComputerSystemId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate18CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Certificates')
        g.api.add_resource(Certificate18API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate19CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Certificates')
        g.api.add_resource(Certificate19API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate20CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/Certificates')
        g.api.add_resource(Certificate20API, '/redfish/v1/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate21CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/Memory/<string:MemoryId>/Certificates')
        g.api.add_resource(Certificate21API, '/redfish/v1/Chassis/<string:ChassisId>/Memory/<string:MemoryId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate22CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Memory/<string:MemoryId>/Certificates')
        g.api.add_resource(Certificate22API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Memory/<string:MemoryId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate23CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/Certificates')
        g.api.add_resource(Certificate23API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate24CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Memory/<string:MemoryId>/Certificates')
        g.api.add_resource(Certificate24API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Memory/<string:MemoryId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate25CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/Certificates')
        g.api.add_resource(Certificate25API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate26CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/Certificates')
        g.api.add_resource(Certificate26API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate27CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/Certificates')
        g.api.add_resource(Certificate27API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate28CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/Certificates')
        g.api.add_resource(Certificate28API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate29CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/Certificates')
        g.api.add_resource(Certificate29API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate30CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/Certificates')
        g.api.add_resource(Certificate30API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate31CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Certificates')
        g.api.add_resource(Certificate31API, '/redfish/v1/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate32CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Certificates')
        g.api.add_resource(Certificate32API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate33CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Certificates')
        g.api.add_resource(Certificate33API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate34CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Certificates')
        g.api.add_resource(Certificate34API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate35CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Certificates')
        g.api.add_resource(Certificate35API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate36CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Certificates')
        g.api.add_resource(Certificate36API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate37CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Certificates')
        g.api.add_resource(Certificate37API, '/redfish/v1/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate38CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Certificates')
        g.api.add_resource(Certificate38API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate39CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Certificates')
        g.api.add_resource(Certificate39API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate40CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Certificates')
        g.api.add_resource(Certificate40API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate41CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Certificates')
        g.api.add_resource(Certificate41API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate42CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Certificates')
        g.api.add_resource(Certificate42API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate43CollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Certificates')
        g.api.add_resource(Certificate43API, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate44CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/Certificates')
        g.api.add_resource(Certificate44API, '/redfish/v1/Chassis/<string:ChassisId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate45CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Certificates')
        g.api.add_resource(Certificate45API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate46CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/Drives/<string:DriveId>/Certificates')
        g.api.add_resource(Certificate46API, '/redfish/v1/Chassis/<string:ChassisId>/Drives/<string:DriveId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate47CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Certificates')
        g.api.add_resource(Certificate47API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate48CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Drives/<string:DriveId>/Certificates')
        g.api.add_resource(Certificate48API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Drives/<string:DriveId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate49CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Certificates')
        g.api.add_resource(Certificate49API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate50CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Certificates')
        g.api.add_resource(Certificate50API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate51CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Drives/<string:DriveId>/Certificates')
        g.api.add_resource(Certificate51API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Drives/<string:DriveId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate52CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Certificates')
        g.api.add_resource(Certificate52API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate53CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Certificates')
        g.api.add_resource(Certificate53API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate54CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>/Certificates')
        g.api.add_resource(Certificate54API, '/redfish/v1/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate55CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>/ClientCertificates')
        g.api.add_resource(Certificate55API, '/redfish/v1/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>/ClientCertificates/<string:CertificateId>')

        g.api.add_resource(Certificate56CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>/Certificates')
        g.api.add_resource(Certificate56API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate57CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>/ClientCertificates')
        g.api.add_resource(Certificate57API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>/ClientCertificates/<string:CertificateId>')

        g.api.add_resource(Certificate58CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>/Certificates')
        g.api.add_resource(Certificate58API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate59CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>/ClientCertificates')
        g.api.add_resource(Certificate59API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>/ClientCertificates/<string:CertificateId>')

        g.api.add_resource(Certificate60CollectionAPI, '/redfish/v1/UpdateService/RemoteServerCertificates')
        g.api.add_resource(Certificate60API, '/redfish/v1/UpdateService/RemoteServerCertificates/<string:CertificateId>')

        g.api.add_resource(Certificate61CollectionAPI, '/redfish/v1/UpdateService/ClientCertificates')
        g.api.add_resource(Certificate61API, '/redfish/v1/UpdateService/ClientCertificates/<string:CertificateId>')

        g.api.add_resource(Certificate62CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/Certificates')
        g.api.add_resource(Certificate62API, '/redfish/v1/Managers/<string:ManagerId>/Certificates/<string:CertificateId>')

        g.api.add_resource(Certificate63CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/KeyManagement/KMIPCertificates')
        g.api.add_resource(Certificate63API, '/redfish/v1/Systems/<string:ComputerSystemId>/KeyManagement/KMIPCertificates/<string:CertificateId>')

        g.api.add_resource(Certificate64CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/KeyManagement/KMIPCertificates')
        g.api.add_resource(Certificate64API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/KeyManagement/KMIPCertificates/<string:CertificateId>')

        g.api.add_resource(Certificate65CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/KeyManagement/KMIPCertificates')
        g.api.add_resource(Certificate65API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/KeyManagement/KMIPCertificates/<string:CertificateId>')

        g.api.add_resource(ChassisCollectionAPI, '/redfish/v1/Chassis', resource_class_kwargs={'auth_mode': auth_mode})
        g.api.add_resource(ChassisAPI, '/redfish/v1/Chassis/<string:ChassisId>', resource_class_kwargs={'auth_mode': auth_mode})

        g.api.add_resource(Circuit0CollectionAPI, '/redfish/v1/PowerEquipment/RackPDUs/<string:PowerDistributionId>/Mains')
        g.api.add_resource(Circuit0API, '/redfish/v1/PowerEquipment/RackPDUs/<string:PowerDistributionId>/Mains/<string:CircuitId>')

        g.api.add_resource(Circuit1CollectionAPI, '/redfish/v1/PowerEquipment/RackPDUs/<string:PowerDistributionId>/Branches')
        g.api.add_resource(Circuit1API, '/redfish/v1/PowerEquipment/RackPDUs/<string:PowerDistributionId>/Branches/<string:CircuitId>')

        g.api.add_resource(Circuit2CollectionAPI, '/redfish/v1/PowerEquipment/FloorPDUs/<string:PowerDistributionId>/Mains')
        g.api.add_resource(Circuit2API, '/redfish/v1/PowerEquipment/FloorPDUs/<string:PowerDistributionId>/Mains/<string:CircuitId>')

        g.api.add_resource(Circuit3CollectionAPI, '/redfish/v1/PowerEquipment/FloorPDUs/<string:PowerDistributionId>/Branches')
        g.api.add_resource(Circuit3API, '/redfish/v1/PowerEquipment/FloorPDUs/<string:PowerDistributionId>/Branches/<string:CircuitId>')

        g.api.add_resource(Circuit4CollectionAPI, '/redfish/v1/PowerEquipment/FloorPDUs/<string:PowerDistributionId>/Subfeeds')
        g.api.add_resource(Circuit4API, '/redfish/v1/PowerEquipment/FloorPDUs/<string:PowerDistributionId>/Subfeeds/<string:CircuitId>')

        g.api.add_resource(Circuit5CollectionAPI, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/Mains')
        g.api.add_resource(Circuit5API, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/Mains/<string:CircuitId>')

        g.api.add_resource(Circuit6CollectionAPI, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/Branches')
        g.api.add_resource(Circuit6API, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/Branches/<string:CircuitId>')

        g.api.add_resource(Circuit7CollectionAPI, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/Feeders')
        g.api.add_resource(Circuit7API, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/Feeders/<string:CircuitId>')

        g.api.add_resource(Circuit8CollectionAPI, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/Mains')
        g.api.add_resource(Circuit8API, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/Mains/<string:CircuitId>')

        g.api.add_resource(Circuit9CollectionAPI, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/Branches')
        g.api.add_resource(Circuit9API, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/Branches/<string:CircuitId>')

        g.api.add_resource(Circuit10CollectionAPI, '/redfish/v1/PowerEquipment/Switchgear/<string:PowerDistributionId>/Mains')
        g.api.add_resource(Circuit10API, '/redfish/v1/PowerEquipment/Switchgear/<string:PowerDistributionId>/Mains/<string:CircuitId>')

        g.api.add_resource(Circuit11CollectionAPI, '/redfish/v1/PowerEquipment/Switchgear/<string:PowerDistributionId>/Subfeeds')
        g.api.add_resource(Circuit11API, '/redfish/v1/PowerEquipment/Switchgear/<string:PowerDistributionId>/Subfeeds/<string:CircuitId>')

        g.api.add_resource(Circuit12CollectionAPI, '/redfish/v1/PowerEquipment/Switchgear/<string:PowerDistributionId>/Feeders')
        g.api.add_resource(Circuit12API, '/redfish/v1/PowerEquipment/Switchgear/<string:PowerDistributionId>/Feeders/<string:CircuitId>')

        g.api.add_resource(Circuit13CollectionAPI, '/redfish/v1/PowerEquipment/Switchgear/<string:PowerDistributionId>/Branches')
        g.api.add_resource(Circuit13API, '/redfish/v1/PowerEquipment/Switchgear/<string:PowerDistributionId>/Branches/<string:CircuitId>')

        g.api.add_resource(Circuit14CollectionAPI, '/redfish/v1/PowerEquipment/ElectricalBuses/<string:PowerDistributionId>/Mains')
        g.api.add_resource(Circuit14API, '/redfish/v1/PowerEquipment/ElectricalBuses/<string:PowerDistributionId>/Mains/<string:CircuitId>')

        g.api.add_resource(Circuit15CollectionAPI, '/redfish/v1/PowerEquipment/ElectricalBuses/<string:PowerDistributionId>/Branches')
        g.api.add_resource(Circuit15API, '/redfish/v1/PowerEquipment/ElectricalBuses/<string:PowerDistributionId>/Branches/<string:CircuitId>')

        g.api.add_resource(ComponentIntegrityCollectionAPI, '/redfish/v1/ComponentIntegrity')
        g.api.add_resource(ComponentIntegrityAPI, '/redfish/v1/ComponentIntegrity/<string:ComponentIntegrityId>')

        g.api.add_resource(CompositionReservationCollectionAPI, '/redfish/v1/CompositionService/CompositionReservations')
        g.api.add_resource(CompositionReservationAPI, '/redfish/v1/CompositionService/CompositionReservations/<string:CompositionReservationId>')

        g.api.add_resource(ComputerSystem0CollectionAPI, '/redfish/v1/Systems')
        g.api.add_resource(ComputerSystem0API, '/redfish/v1/Systems/<string:ComputerSystemId>')

        g.api.add_resource(ComputerSystem1CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems')
        g.api.add_resource(ComputerSystem1API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>')

        g.api.add_resource(ComputerSystem2CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems')
        g.api.add_resource(ComputerSystem2API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>')

        g.api.add_resource(ConnectionMethodCollectionAPI, '/redfish/v1/AggregationService/ConnectionMethods')
        g.api.add_resource(ConnectionMethodAPI, '/redfish/v1/AggregationService/ConnectionMethods/<string:ConnectionMethodId>')

        g.api.add_resource(ConnectionCollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Connections')
        g.api.add_resource(ConnectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Connections/<string:ConnectionId>')

        g.api.add_resource(Control0CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/Controls')
        g.api.add_resource(Control0API, '/redfish/v1/Chassis/<string:ChassisId>/Controls/<string:ControlId>')

        g.api.add_resource(Control1CollectionAPI, '/redfish/v1/PowerEquipment/RackPDUs/<string:PowerDistributionId>/Controls')
        g.api.add_resource(Control1API, '/redfish/v1/PowerEquipment/RackPDUs/<string:PowerDistributionId>/Controls/<string:ControlId>')

        g.api.add_resource(Control2CollectionAPI, '/redfish/v1/PowerEquipment/FloorPDUs/<string:PowerDistributionId>/Controls')
        g.api.add_resource(Control2API, '/redfish/v1/PowerEquipment/FloorPDUs/<string:PowerDistributionId>/Controls/<string:ControlId>')

        g.api.add_resource(Control3CollectionAPI, '/redfish/v1/PowerEquipment/Switchgear/<string:PowerDistributionId>/Controls')
        g.api.add_resource(Control3API, '/redfish/v1/PowerEquipment/Switchgear/<string:PowerDistributionId>/Controls/<string:ControlId>')

        g.api.add_resource(Control4CollectionAPI, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/Controls')
        g.api.add_resource(Control4API, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/Controls/<string:ControlId>')

        g.api.add_resource(Control5CollectionAPI, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/Controls')
        g.api.add_resource(Control5API, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/Controls/<string:ControlId>')

        g.api.add_resource(Drive0CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives')
        g.api.add_resource(Drive0API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>')

        g.api.add_resource(Drive1CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/Drives')
        g.api.add_resource(Drive1API, '/redfish/v1/Chassis/<string:ChassisId>/Drives/<string:DriveId>')

        g.api.add_resource(Drive2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Drives')
        g.api.add_resource(Drive2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Drives/<string:DriveId>')

        g.api.add_resource(Drive3CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Drives')
        g.api.add_resource(Drive3API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Drives/<string:DriveId>')

        g.api.add_resource(Drive4CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives')
        g.api.add_resource(Drive4API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>')

        g.api.add_resource(Drive5CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Drives')
        g.api.add_resource(Drive5API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Drives/<string:DriveId>')

        g.api.add_resource(Drive6CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Drives')
        g.api.add_resource(Drive6API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Drives/<string:DriveId>')

        g.api.add_resource(Drive7CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives')
        g.api.add_resource(Drive7API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>')

        g.api.add_resource(EndpointGroup0CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/EndpointGroups')
        g.api.add_resource(EndpointGroup0API, '/redfish/v1/Storage/<string:StorageId>/EndpointGroups/<string:EndpointGroupId>')

        g.api.add_resource(EndpointGroup1CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/EndpointGroups')
        g.api.add_resource(EndpointGroup1API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/EndpointGroups/<string:EndpointGroupId>')

        g.api.add_resource(EndpointGroup2CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/EndpointGroups')
        g.api.add_resource(EndpointGroup2API, '/redfish/v1/StorageServices/<string:StorageServiceId>/EndpointGroups/<string:EndpointGroupId>')

        g.api.add_resource(EndpointGroup3CollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/EndpointGroups')
        g.api.add_resource(EndpointGroup3API, '/redfish/v1/Fabrics/<string:FabricId>/EndpointGroups/<string:EndpointGroupId>')

        g.api.add_resource(Endpoint0CollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Endpoints')
        g.api.add_resource(Endpoint0API, '/redfish/v1/Fabrics/<string:FabricId>/Endpoints/<string:EndpointId>')

        g.api.add_resource(Endpoint1CollectionAPI, '/redfish/v1/StorageServices/<string:StorageServiceId>/Endpoints')
        g.api.add_resource(Endpoint1API, '/redfish/v1/StorageServices/<string:StorageServiceId>/Endpoints/<string:EndpointId>')

        g.api.add_resource(Endpoint2CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/Endpoints')
        g.api.add_resource(Endpoint2API, '/redfish/v1/Storage/<string:StorageId>/Endpoints/<string:EndpointId>')

        g.api.add_resource(EthernetInterface0CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/EthernetInterfaces')
        g.api.add_resource(EthernetInterface0API, '/redfish/v1/Managers/<string:ManagerId>/EthernetInterfaces/<string:EthernetInterfaceId>')

        g.api.add_resource(EthernetInterface1CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/EthernetInterfaces')
        g.api.add_resource(EthernetInterface1API, '/redfish/v1/Systems/<string:ComputerSystemId>/EthernetInterfaces/<string:EthernetInterfaceId>')

        g.api.add_resource(EthernetInterface2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/EthernetInterfaces')
        g.api.add_resource(EthernetInterface2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/EthernetInterfaces/<string:EthernetInterfaceId>')

        g.api.add_resource(EthernetInterface3CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/EthernetInterfaces')
        g.api.add_resource(EthernetInterface3API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/EthernetInterfaces/<string:EthernetInterfaceId>')

        g.api.add_resource(EthernetInterface4CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/EthernetInterfaces')
        g.api.add_resource(EthernetInterface4API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/EthernetInterfaces/<string:EthernetInterfaceId>')

        g.api.add_resource(EthernetInterface5CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/EthernetInterfaces')
        g.api.add_resource(EthernetInterface5API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/EthernetInterfaces/<string:EthernetInterfaceId>')

        g.api.add_resource(EthernetInterface6CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdaptersId>/NetworkDeviceFunctions/<string:NetworkDeviceFunctionId>/EthernetInterfaces')
        g.api.add_resource(EthernetInterface6API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdaptersId>/NetworkDeviceFunctions/<string:NetworkDeviceFunctionId>/EthernetInterfaces/<string:EthernetInterfaceId>')

        g.api.add_resource(EventDestinationCollectionAPI, '/redfish/v1/EventService/Subscriptions')
        g.api.add_resource(EventDestinationAPI, '/redfish/v1/EventService/Subscriptions/<string:EventDestinationId>')

        g.api.add_resource(ExternalAccountProvider0CollectionAPI, '/redfish/v1/AccountService/ExternalAccountProviders')
        g.api.add_resource(ExternalAccountProvider0API, '/redfish/v1/AccountService/ExternalAccountProviders/<string:ExternalAccountProviderId>')

        g.api.add_resource(ExternalAccountProvider1CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/ExternalAccountProviders')
        g.api.add_resource(ExternalAccountProvider1API, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/ExternalAccountProviders/<string:ExternalAccountProviderId>')

        g.api.add_resource(FabricAdapter0CollectionAPI, '/redfish/v1/Systems/<string:SystemId>/FabricAdapters')
        g.api.add_resource(FabricAdapter0API, '/redfish/v1/Systems/<string:SystemId>/FabricAdapters/<string:FabricAdapterId>')

        g.api.add_resource(FabricAdapter1CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters')
        g.api.add_resource(FabricAdapter1API, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>')

        g.api.add_resource(FabricCollectionAPI, '/redfish/v1/Fabrics')
        g.api.add_resource(FabricAPI, '/redfish/v1/Fabrics/<string:FabricId>')

        g.api.add_resource(FacilityCollectionAPI, '/redfish/v1/Facilities')
        g.api.add_resource(FacilityAPI, '/redfish/v1/Facilities/<string:FacilityId>')

        g.api.add_resource(FanCollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/ThermalSubsystem/Fans')
        g.api.add_resource(FanAPI, '/redfish/v1/Chassis/<string:ChassisId>/ThermalSubsystem/Fans/<string:FanId>')

        g.api.add_resource(GraphicsControllerCollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/GraphicsControllers')
        g.api.add_resource(GraphicsControllerAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/GraphicsControllers/<string:ControllerId>')

        g.api.add_resource(HostInterfaceCollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/HostInterfaces')
        g.api.add_resource(HostInterfaceAPI, '/redfish/v1/Managers/<string:ManagerId>/HostInterfaces/<string:HostInterfaceId>')

        g.api.add_resource(Job0CollectionAPI, '/redfish/v1/JobService/Jobs')
        g.api.add_resource(Job0API, '/redfish/v1/JobService/Jobs/<string:JobId>')

        g.api.add_resource(Job1CollectionAPI, '/redfish/v1/JobService/Jobs/<string:JobId>/Steps')
        g.api.add_resource(Job1API, '/redfish/v1/JobService/Jobs/<string:JobId>/Steps/<string:JobId2>')

        g.api.add_resource(JsonSchemaFileCollectionAPI, '/redfish/v1/JsonSchemas')
        g.api.add_resource(JsonSchemaFileAPI, '/redfish/v1/JsonSchemas/<string:JsonSchemaFileId>')

        g.api.add_resource(KeyPolicyCollectionAPI, '/redfish/v1/KeyService/NVMeoFKeyPolicies')
        g.api.add_resource(KeyPolicyAPI, '/redfish/v1/KeyService/NVMeoFKeyPolicies/<string:KeyPolicyId>')

        g.api.add_resource(Key0CollectionAPI, '/redfish/v1/KeyService/NVMeoFSecrets')
        g.api.add_resource(Key0API, '/redfish/v1/KeyService/NVMeoFSecrets/<string:KeyId>')

        g.api.add_resource(Key1CollectionAPI, '/redfish/v1/AccountService/Accounts/<string:ManagerAccountId>/Keys')
        g.api.add_resource(Key1API, '/redfish/v1/AccountService/Accounts/<string:ManagerAccountId>/Keys/<string:KeyId>')

        g.api.add_resource(Key2CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/Accounts/<string:ManagerAccountId>/Keys')
        g.api.add_resource(Key2API, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/Accounts/<string:ManagerAccountId>/Keys/<string:KeyId>')

        g.api.add_resource(LicenseCollectionAPI, '/redfish/v1/LicenseService/Licenses')
        g.api.add_resource(LicenseAPI, '/redfish/v1/LicenseService/Licenses/<string:LicenseId>')

        g.api.add_resource(LogEntry0CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/LogServices/<string:LogServiceId>/Entries')
        g.api.add_resource(LogEntry0API, '/redfish/v1/Managers/<string:ManagerId>/LogServices/<string:LogServiceId>/Entries/<string:LogEntryId>')

        g.api.add_resource(LogEntry1CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/LogServices/<string:LogServiceId>/Entries')
        g.api.add_resource(LogEntry1API, '/redfish/v1/Systems/<string:ComputerSystemId>/LogServices/<string:LogServiceId>/Entries/<string:LogEntryId>')

        g.api.add_resource(LogEntry2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/LogServices/<string:LogServiceId>/Entries')
        g.api.add_resource(LogEntry2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/LogServices/<string:LogServiceId>/Entries/<string:LogEntryId>')

        g.api.add_resource(LogEntry3CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/LogServices/<string:LogServiceId>/Entries')
        g.api.add_resource(LogEntry3API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/LogServices/<string:LogServiceId>/Entries/<string:LogEntryId>')

        g.api.add_resource(LogEntry4CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/LogServices/<string:LogServiceId>/Entries')
        g.api.add_resource(LogEntry4API, '/redfish/v1/Chassis/<string:ChassisId>/LogServices/<string:LogServiceId>/Entries/<string:LogEntryId>')

        g.api.add_resource(LogEntry5CollectionAPI, '/redfish/v1/JobService/Log/Entries')
        g.api.add_resource(LogEntry5API, '/redfish/v1/JobService/Log/Entries/<string:LogEntryId>')

        g.api.add_resource(LogEntry6CollectionAPI, '/redfish/v1/TelemetryService/LogService/Entries')
        g.api.add_resource(LogEntry6API, '/redfish/v1/TelemetryService/LogService/Entries/<string:LogEntryId>')

        g.api.add_resource(LogEntry7CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/DeviceLog/Entries')
        g.api.add_resource(LogEntry7API, '/redfish/v1/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/DeviceLog/Entries/<string:LogEntryId>')

        g.api.add_resource(ManagerAccount0CollectionAPI, '/redfish/v1/AccountService/Accounts')
        g.api.add_resource(ManagerAccount0API, '/redfish/v1/AccountService/Accounts/<string:ManagerAccountId>')

        g.api.add_resource(ManagerAccount1CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/Accounts')
        g.api.add_resource(ManagerAccount1API, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/Accounts/<string:ManagerAccountId>')

        g.api.add_resource(ManagerCollectionAPI, '/redfish/v1/Managers')
        g.api.add_resource(ManagerAPI, '/redfish/v1/Managers/<string:ManagerId>')

        g.api.add_resource(MediaControllerCollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/MediaControllers')
        g.api.add_resource(MediaControllerAPI, '/redfish/v1/Chassis/<string:ChassisId>/MediaControllers/<string:MediaControllerId>')

        g.api.add_resource(MemoryChunks0CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/MemoryDomains/<string:MemoryDomainId>/MemoryChunks')
        g.api.add_resource(MemoryChunks0API, '/redfish/v1/Systems/<string:ComputerSystemId>/MemoryDomains/<string:MemoryDomainId>/MemoryChunks/<string:MemoryChunksId>')

        g.api.add_resource(MemoryChunks1CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/MemoryDomains/<string:MemoryDomainId>/MemoryChunks')
        g.api.add_resource(MemoryChunks1API, '/redfish/v1/Chassis/<string:ChassisId>/MemoryDomains/<string:MemoryDomainId>/MemoryChunks/<string:MemoryChunksId>')

        g.api.add_resource(MemoryChunks2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/MemoryDomains/<string:MemoryDomainId>/MemoryChunks')
        g.api.add_resource(MemoryChunks2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/MemoryDomains/<string:MemoryDomainId>/MemoryChunks/<string:MemoryChunksId>')

        g.api.add_resource(MemoryChunks3CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/MemoryDomains/<string:MemoryDomainId>/MemoryChunks')
        g.api.add_resource(MemoryChunks3API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/MemoryDomains/<string:MemoryDomainId>/MemoryChunks/<string:MemoryChunksId>')

        g.api.add_resource(MemoryDomain0CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/MemoryDomains')
        g.api.add_resource(MemoryDomain0API, '/redfish/v1/Systems/<string:ComputerSystemId>/MemoryDomains/<string:MemoryDomainId>')

        g.api.add_resource(MemoryDomain1CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/MemoryDomains')
        g.api.add_resource(MemoryDomain1API, '/redfish/v1/Chassis/<string:ChassisId>/MemoryDomains/<string:MemoryDomainId>')

        g.api.add_resource(MemoryDomain2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/MemoryDomains')
        g.api.add_resource(MemoryDomain2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/MemoryDomains/<string:MemoryDomainId>')

        g.api.add_resource(MemoryDomain3CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/MemoryDomains')
        g.api.add_resource(MemoryDomain3API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/MemoryDomains/<string:MemoryDomainId>')

        g.api.add_resource(Memory0CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Memory')
        g.api.add_resource(Memory0API, '/redfish/v1/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>')

        g.api.add_resource(Memory1CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/Memory')
        g.api.add_resource(Memory1API, '/redfish/v1/Chassis/<string:ChassisId>/Memory/<string:MemoryId>')

        g.api.add_resource(Memory2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Memory')
        g.api.add_resource(Memory2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Memory/<string:MemoryId>')

        g.api.add_resource(Memory3CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Memory')
        g.api.add_resource(Memory3API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>')

        g.api.add_resource(Memory4CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Memory')
        g.api.add_resource(Memory4API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Memory/<string:MemoryId>')

        g.api.add_resource(Memory5CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Memory')
        g.api.add_resource(Memory5API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>')

        g.api.add_resource(MetricDefinitionCollectionAPI, '/redfish/v1/TelemetryService/MetricDefinitions')
        g.api.add_resource(MetricDefinitionAPI, '/redfish/v1/TelemetryService/MetricDefinitions/<string:MetricDefinitionId>')

        g.api.add_resource(MetricReportDefinitionCollectionAPI, '/redfish/v1/TelemetryService/MetricReportDefinitions')
        g.api.add_resource(MetricReportDefinitionAPI, '/redfish/v1/TelemetryService/MetricReportDefinitions/<string:MetricReportDefinitionId>')

        g.api.add_resource(MetricReportCollectionAPI, '/redfish/v1/TelemetryService/MetricReports')
        g.api.add_resource(MetricReportAPI, '/redfish/v1/TelemetryService/MetricReports/<string:MetricReportId>')

        g.api.add_resource(NetworkAdapterCollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters')
        g.api.add_resource(NetworkAdapterAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>')

        g.api.add_resource(NetworkDeviceFunctionCollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/NetworkDeviceFunctions')
        g.api.add_resource(NetworkDeviceFunctionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/NetworkDeviceFunctions/<string:NetworkDeviceFunctionId>')

        g.api.add_resource(NetworkInterface0CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/NetworkInterfaces')
        g.api.add_resource(NetworkInterface0API, '/redfish/v1/Systems/<string:ComputerSystemId>/NetworkInterfaces/<string:NetworkInterfaceId>')

        g.api.add_resource(NetworkInterface1CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/NetworkInterfaces')
        g.api.add_resource(NetworkInterface1API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/NetworkInterfaces/<string:NetworkInterfaceId>')

        g.api.add_resource(NetworkInterface2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/NetworkInterfaces')
        g.api.add_resource(NetworkInterface2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/NetworkInterfaces/<string:NetworkInterfaceId>')

        g.api.add_resource(NetworkInterface3CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/NetworkInterfaces')
        g.api.add_resource(NetworkInterface3API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/NetworkInterfaces/<string:NetworkInterfaceId>')

        g.api.add_resource(NetworkInterface4CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/NetworkInterfaces')
        g.api.add_resource(NetworkInterface4API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/NetworkInterfaces/<string:NetworkInterfaceId>')

        g.api.add_resource(NetworkPortCollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/NetworkPorts')
        g.api.add_resource(NetworkPortAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/NetworkPorts/<string:NetworkPortId>')

        g.api.add_resource(OperatingConfigCollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/OperatingConfigs')
        g.api.add_resource(OperatingConfigAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/OperatingConfigs/<string:OperatingConfigId>')

        g.api.add_resource(OutletGroup0CollectionAPI, '/redfish/v1/PowerEquipment/RackPDUs/<string:PowerDistributionId>/OutletGroups')
        g.api.add_resource(OutletGroup0API, '/redfish/v1/PowerEquipment/RackPDUs/<string:PowerDistributionId>/OutletGroups/<string:OutletGroupId>')

        g.api.add_resource(OutletGroup1CollectionAPI, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/OutletGroups')
        g.api.add_resource(OutletGroup1API, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/OutletGroups/<string:OutletGroupId>')

        g.api.add_resource(OutletGroup2CollectionAPI, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/OutletGroups')
        g.api.add_resource(OutletGroup2API, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/OutletGroups/<string:OutletGroupId>')

        g.api.add_resource(OutletGroup3CollectionAPI, '/redfish/v1/PowerEquipment/ElectricalBuses/<string:PowerDistributionId>/OutletGroups')
        g.api.add_resource(OutletGroup3API, '/redfish/v1/PowerEquipment/ElectricalBuses/<string:PowerDistributionId>/OutletGroups/<string:OutletGroupId>')

        g.api.add_resource(Outlet0CollectionAPI, '/redfish/v1/PowerEquipment/RackPDUs/<string:PowerDistributionId>/Outlets')
        g.api.add_resource(Outlet0API, '/redfish/v1/PowerEquipment/RackPDUs/<string:PowerDistributionId>/Outlets/<string:OutletId>')

        g.api.add_resource(Outlet1CollectionAPI, '/redfish/v1/PowerEquipment/FloorPDUs/<string:PowerDistributionId>/Outlets')
        g.api.add_resource(Outlet1API, '/redfish/v1/PowerEquipment/FloorPDUs/<string:PowerDistributionId>/Outlets/<string:OutletId>')

        g.api.add_resource(Outlet2CollectionAPI, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/Outlets')
        g.api.add_resource(Outlet2API, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/Outlets/<string:OutletId>')

        g.api.add_resource(Outlet3CollectionAPI, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/Outlets')
        g.api.add_resource(Outlet3API, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/Outlets/<string:OutletId>')

        g.api.add_resource(Outlet4CollectionAPI, '/redfish/v1/PowerEquipment/ElectricalBuses/<string:PowerDistributionId>/Outlets')
        g.api.add_resource(Outlet4API, '/redfish/v1/PowerEquipment/ElectricalBuses/<string:PowerDistributionId>/Outlets/<string:OutletId>')

        g.api.add_resource(PCIeDevice0CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/PCIeDevices')
        g.api.add_resource(PCIeDevice0API, '/redfish/v1/Chassis/<string:ChassisId>/PCIeDevices/<string:PCIeDeviceId>')

        g.api.add_resource(PCIeDevice1CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/PCIeDevices')
        g.api.add_resource(PCIeDevice1API, '/redfish/v1/Systems/<string:ComputerSystemId>/PCIeDevices/<string:PCIeDeviceId>')

        g.api.add_resource(PCIeDevice2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/PCIeDevices')
        g.api.add_resource(PCIeDevice2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/PCIeDevices/<string:PCIeDeviceId>')

        g.api.add_resource(PCIeDevice3CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/PCIeDevices')
        g.api.add_resource(PCIeDevice3API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/PCIeDevices/<string:PCIeDeviceId>')

        g.api.add_resource(PCIeFunction0CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/PCIeDevices/<string:PCIeDeviceId>/PCIeFunctions')
        g.api.add_resource(PCIeFunction0API, '/redfish/v1/Chassis/<string:ChassisId>/PCIeDevices/<string:PCIeDeviceId>/PCIeFunctions/<string:PCIeFunctionId>')

        g.api.add_resource(PCIeFunction1CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/PCIeDevices/<string:PCIeDeviceId>/PCIeFunctions')
        g.api.add_resource(PCIeFunction1API, '/redfish/v1/Systems/<string:ComputerSystemId>/PCIeDevices/<string:PCIeDeviceId>/PCIeFunctions/<string:PCIeFunctionId>')

        g.api.add_resource(PCIeFunction2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/PCIeDevices/<string:PCIeDeviceId>/PCIeFunctions')
        g.api.add_resource(PCIeFunction2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/PCIeDevices/<string:PCIeDeviceId>/PCIeFunctions/<string:PCIeFunctionId>')

        g.api.add_resource(PCIeFunction3CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/PCIeDevices/<string:PCIeDeviceId>/PCIeFunctions')
        g.api.add_resource(PCIeFunction3API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/PCIeDevices/<string:PCIeDeviceId>/PCIeFunctions/<string:PCIeFunctionId>')

        g.api.add_resource(Port0CollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports')
        g.api.add_resource(Port0API, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports/<string:PortId>')

        g.api.add_resource(Port1CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports')
        g.api.add_resource(Port1API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port2CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports')
        g.api.add_resource(Port2API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port3CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/Ports')
        g.api.add_resource(Port3API, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>')

        g.api.add_resource(Port4CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/GraphicsControllers/<string:ControllerId>/Ports')
        g.api.add_resource(Port4API, '/redfish/v1/Systems/<string:ComputerSystemId>/GraphicsControllers/<string:ControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port5CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/USBControllers/<string:ControllerId>/Ports')
        g.api.add_resource(Port5API, '/redfish/v1/Systems/<string:ComputerSystemId>/USBControllers/<string:ControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port6CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/Ports')
        g.api.add_resource(Port6API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/Ports/<string:PortId>')

        g.api.add_resource(Port7CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports')
        g.api.add_resource(Port7API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port8CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports')
        g.api.add_resource(Port8API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port9CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports')
        g.api.add_resource(Port9API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port10CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports')
        g.api.add_resource(Port10API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port11CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports')
        g.api.add_resource(Port11API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port12CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports')
        g.api.add_resource(Port12API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port13CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports')
        g.api.add_resource(Port13API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port14CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports')
        g.api.add_resource(Port14API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port15CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/MediaControllers/<string:MediaControllerId>/Ports')
        g.api.add_resource(Port15API, '/redfish/v1/Chassis/<string:ChassisId>/MediaControllers/<string:MediaControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port16CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/Ports')
        g.api.add_resource(Port16API, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>')

        g.api.add_resource(Port17CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Ports')
        g.api.add_resource(Port17API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Ports/<string:PortId>')

        g.api.add_resource(Port18CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports')
        g.api.add_resource(Port18API, '/redfish/v1/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port19CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports')
        g.api.add_resource(Port19API, '/redfish/v1/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>')

        g.api.add_resource(Port20CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/USBPorts')
        g.api.add_resource(Port20API, '/redfish/v1/Managers/<string:ManagerId>/USBPorts/<string:PortId>')

        g.api.add_resource(PowerDistribution0CollectionAPI, '/redfish/v1/PowerEquipment/RackPDUs')
        g.api.add_resource(PowerDistribution0API, '/redfish/v1/PowerEquipment/RackPDUs/<string:PowerDistributionId>')

        g.api.add_resource(PowerDistribution1CollectionAPI, '/redfish/v1/PowerEquipment/FloorPDUs')
        g.api.add_resource(PowerDistribution1API, '/redfish/v1/PowerEquipment/FloorPDUs/<string:PowerDistributionId>')

        g.api.add_resource(PowerDistribution2CollectionAPI, '/redfish/v1/PowerEquipment/TransferSwitches')
        g.api.add_resource(PowerDistribution2API, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>')

        g.api.add_resource(PowerDistribution3CollectionAPI, '/redfish/v1/PowerEquipment/PowerShelves')
        g.api.add_resource(PowerDistribution3API, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>')

        g.api.add_resource(PowerDistribution4CollectionAPI, '/redfish/v1/PowerEquipment/Switchgear')
        g.api.add_resource(PowerDistribution4API, '/redfish/v1/PowerEquipment/Switchgear/<string:PowerDistributionId>')

        g.api.add_resource(PowerDistribution5CollectionAPI, '/redfish/v1/PowerEquipment/ElectricalBuses')
        g.api.add_resource(PowerDistribution5API, '/redfish/v1/PowerEquipment/ElectricalBuses/<string:PowerDistributionId>')

        g.api.add_resource(PowerDomainCollectionAPI, '/redfish/v1/Facilities/<string:FacilityId>/PowerDomains')
        g.api.add_resource(PowerDomainAPI, '/redfish/v1/Facilities/<string:FacilityId>/PowerDomains/<string:PowerDomainId>')

        g.api.add_resource(PowerSupply0CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/PowerSubsystem/PowerSupplies')
        g.api.add_resource(PowerSupply0API, '/redfish/v1/Chassis/<string:ChassisId>/PowerSubsystem/PowerSupplies/<string:PowerSupplyId>')

        g.api.add_resource(PowerSupply1CollectionAPI, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/PowerSupplies')
        g.api.add_resource(PowerSupply1API, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/PowerSupplies/<string:PowerSupplyId>')

        g.api.add_resource(Processor0CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors')
        g.api.add_resource(Processor0API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>')

        g.api.add_resource(Processor1CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors')
        g.api.add_resource(Processor1API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>')

        g.api.add_resource(Processor2CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors')
        g.api.add_resource(Processor2API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>')

        g.api.add_resource(Processor3CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors')
        g.api.add_resource(Processor3API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>')

        g.api.add_resource(Processor4CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors')
        g.api.add_resource(Processor4API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>')

        g.api.add_resource(Processor5CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors')
        g.api.add_resource(Processor5API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>')

        g.api.add_resource(Processor6CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors')
        g.api.add_resource(Processor6API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>')

        g.api.add_resource(Processor7CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors')
        g.api.add_resource(Processor7API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>')

        g.api.add_resource(Processor8CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors')
        g.api.add_resource(Processor8API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>')

        g.api.add_resource(Processor9CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors')
        g.api.add_resource(Processor9API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>')

        g.api.add_resource(Processor10CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors')
        g.api.add_resource(Processor10API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>')

        g.api.add_resource(Processor11CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors')
        g.api.add_resource(Processor11API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>')

        g.api.add_resource(Processor12CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors')
        g.api.add_resource(Processor12API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>')

        g.api.add_resource(Processor13CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors')
        g.api.add_resource(Processor13API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>')

        g.api.add_resource(Processor14CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors')
        g.api.add_resource(Processor14API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>')

        g.api.add_resource(Processor15CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Processors')
        g.api.add_resource(Processor15API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Processors/<string:ProcessorId>')

        g.api.add_resource(Processor16CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Processors/<string:ProcessorId>/SubProcessors')
        g.api.add_resource(Processor16API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>')

        g.api.add_resource(Processor17CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors')
        g.api.add_resource(Processor17API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>')

        g.api.add_resource(RegisteredClientCollectionAPI, '/redfish/v1/RegisteredClients')
        g.api.add_resource(RegisteredClientAPI, '/redfish/v1/RegisteredClients/<string:RegisteredClientId>')

        g.api.add_resource(ResourceBlock0CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks')
        g.api.add_resource(ResourceBlock0API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>')

        g.api.add_resource(ResourceBlock1CollectionAPI, '/redfish/v1/ResourceBlocks')
        g.api.add_resource(ResourceBlock1API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>')

        g.api.add_resource(Role0CollectionAPI, '/redfish/v1/AccountService/Roles')
        g.api.add_resource(Role0API, '/redfish/v1/AccountService/Roles/<string:RoleId>')

        g.api.add_resource(Role1CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/Roles')
        g.api.add_resource(Role1API, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService/Roles/<string:RoleId>')

        g.api.add_resource(RouteEntry0CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/LPRT')
        g.api.add_resource(RouteEntry0API, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/LPRT/<string:LPRTId>')

        g.api.add_resource(RouteEntry1CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/MPRT')
        g.api.add_resource(RouteEntry1API, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/MPRT/<string:MPRTId>')

        g.api.add_resource(RouteEntry2CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/SSDT')
        g.api.add_resource(RouteEntry2API, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/SSDT/<string:SSDTId>')

        g.api.add_resource(RouteEntry3CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/MSDT')
        g.api.add_resource(RouteEntry3API, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/MSDT/<string:MSDTId>')

        g.api.add_resource(RouteEntry4CollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports/<string:PortId>/LPRT')
        g.api.add_resource(RouteEntry4API, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports/<string:PortId>/LPRT/<string:LPRTId>')

        g.api.add_resource(RouteEntry5CollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports/<string:PortId>/MPRT')
        g.api.add_resource(RouteEntry5API, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports/<string:PortId>/MPRT/<string:MPRTId>')

        g.api.add_resource(RouteEntry6CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/MSDT')
        g.api.add_resource(RouteEntry6API, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/MSDT/<string:MSDTId>')

        g.api.add_resource(RouteEntry7CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/SSDT')
        g.api.add_resource(RouteEntry7API, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/SSDT/<string:SSDTId>')

        g.api.add_resource(RouteEntry8CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/LPRT')
        g.api.add_resource(RouteEntry8API, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/LPRT/<string:LPRTId>')

        g.api.add_resource(RouteEntry9CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/MPRT')
        g.api.add_resource(RouteEntry9API, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/MPRT/<string:MPRTId>')

        g.api.add_resource(RouteSetEntry0CollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports/<string:PortId>/LPRT/<string:LPRTId>/RouteSet')
        g.api.add_resource(RouteSetEntry0API, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports/<string:PortId>/LPRT/<string:LPRTId>/RouteSet/<string:RouteId>')

        g.api.add_resource(RouteSetEntry1CollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports/<string:PortId>/MPRT/<string:MPRTId>/RouteSet')
        g.api.add_resource(RouteSetEntry1API, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports/<string:PortId>/MPRT/<string:MPRTId>/RouteSet/<string:RouteId>')

        g.api.add_resource(RouteSetEntry2CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/MPRT/<string:MPRTId>/RouteSet')
        g.api.add_resource(RouteSetEntry2API, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/MPRT/<string:MPRTId>/RouteSet/<string:RouteId>')

        g.api.add_resource(RouteSetEntry3CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/LPRT/<string:LPRTId>/RouteSet')
        g.api.add_resource(RouteSetEntry3API, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/LPRT/<string:LPRTId>/RouteSet/<string:RouteId>')

        g.api.add_resource(RouteSetEntry4CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/MSDT/<string:MSDTId>/RouteSet')
        g.api.add_resource(RouteSetEntry4API, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/MSDT/<string:MSDTId>/RouteSet/<string:RouteId>')

        g.api.add_resource(RouteSetEntry5CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/SSDT/<string:SSDTId>/RouteSet')
        g.api.add_resource(RouteSetEntry5API, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/SSDT/<string:SSDTId>/RouteSet/<string:RouteId>')

        g.api.add_resource(RouteSetEntry6CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/MSDT/<string:MSDTId>/RouteSet')
        g.api.add_resource(RouteSetEntry6API, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/MSDT/<string:MSDTId>/RouteSet/<string:RouteId>')

        g.api.add_resource(RouteSetEntry7CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/SSDT/<string:SSDTId>/RouteSet')
        g.api.add_resource(RouteSetEntry7API, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/SSDT/<string:SSDTId>/RouteSet/<string:RouteId>')

        g.api.add_resource(RouteSetEntry8CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/LPRT/<string:LPRTId>/RouteSet')
        g.api.add_resource(RouteSetEntry8API, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/LPRT/<string:LPRTId>/RouteSet/<string:RouteId>')

        g.api.add_resource(RouteSetEntry9CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/MPRT/<string:MPRTId>/RouteSet')
        g.api.add_resource(RouteSetEntry9API, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/MPRT/<string:MPRTId>/RouteSet/<string:RouteId>')

        g.api.add_resource(SecureBootDatabase0CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases')
        g.api.add_resource(SecureBootDatabase0API, '/redfish/v1/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>')

        g.api.add_resource(SecureBootDatabase1CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases')
        g.api.add_resource(SecureBootDatabase1API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>')

        g.api.add_resource(SecureBootDatabase2CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases')
        g.api.add_resource(SecureBootDatabase2API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>')

        g.api.add_resource(Sensor0CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/Sensors')
        g.api.add_resource(Sensor0API, '/redfish/v1/Chassis/<string:ChassisId>/Sensors/<string:SensorId>')

        g.api.add_resource(Sensor1CollectionAPI, '/redfish/v1/PowerEquipment/Sensors')
        g.api.add_resource(Sensor1API, '/redfish/v1/PowerEquipment/Sensors/<string:SensorId>')

        g.api.add_resource(Sensor2CollectionAPI, '/redfish/v1/PowerEquipment/RackPDUs/<string:PowerDistributionId>/Sensors')
        g.api.add_resource(Sensor2API, '/redfish/v1/PowerEquipment/RackPDUs/<string:PowerDistributionId>/Sensors/<string:SensorId>')

        g.api.add_resource(Sensor3CollectionAPI, '/redfish/v1/PowerEquipment/FloorPDUs/<string:PowerDistributionId>/Sensors')
        g.api.add_resource(Sensor3API, '/redfish/v1/PowerEquipment/FloorPDUs/<string:PowerDistributionId>/Sensors/<string:SensorId>')

        g.api.add_resource(Sensor4CollectionAPI, '/redfish/v1/PowerEquipment/Switchgear/<string:PowerDistributionId>/Sensors')
        g.api.add_resource(Sensor4API, '/redfish/v1/PowerEquipment/Switchgear/<string:PowerDistributionId>/Sensors/<string:SensorId>')

        g.api.add_resource(Sensor5CollectionAPI, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/Sensors')
        g.api.add_resource(Sensor5API, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/Sensors/<string:SensorId>')

        g.api.add_resource(Sensor6CollectionAPI, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/Sensors')
        g.api.add_resource(Sensor6API, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/Sensors/<string:SensorId>')

        g.api.add_resource(SerialInterfaceCollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/SerialInterfaces')
        g.api.add_resource(SerialInterfaceAPI, '/redfish/v1/Managers/<string:ManagerId>/SerialInterfaces/<string:SerialInterfaceId>')

        g.api.add_resource(Signature0CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>/Signatures')
        g.api.add_resource(Signature0API, '/redfish/v1/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>/Signatures/<string:SignatureId>')

        g.api.add_resource(Signature1CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>/Signatures')
        g.api.add_resource(Signature1API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>/Signatures/<string:SignatureId>')

        g.api.add_resource(Signature2CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>/Signatures')
        g.api.add_resource(Signature2API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SecureBoot/SecureBootDatabases/<string:DatabaseId>/Signatures/<string:SignatureId>')

        g.api.add_resource(SimpleStorage0CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/SimpleStorage')
        g.api.add_resource(SimpleStorage0API, '/redfish/v1/Systems/<string:ComputerSystemId>/SimpleStorage/<string:SimpleStorageId>')

        g.api.add_resource(SimpleStorage1CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/SimpleStorage')
        g.api.add_resource(SimpleStorage1API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/SimpleStorage/<string:SimpleStorageId>')

        g.api.add_resource(SimpleStorage2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SimpleStorage')
        g.api.add_resource(SimpleStorage2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SimpleStorage/<string:SimpleStorageId>')

        g.api.add_resource(SimpleStorage3CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/SimpleStorage')
        g.api.add_resource(SimpleStorage3API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/SimpleStorage/<string:SimpleStorageId>')

        g.api.add_resource(SimpleStorage4CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SimpleStorage')
        g.api.add_resource(SimpleStorage4API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SimpleStorage/<string:SimpleStorageId>')

        g.api.add_resource(SoftwareInventory0CollectionAPI, '/redfish/v1/UpdateService/SoftwareInventory')
        g.api.add_resource(SoftwareInventory0API, '/redfish/v1/UpdateService/SoftwareInventory/<string:SoftwareInventoryId>')

        g.api.add_resource(SoftwareInventory1CollectionAPI, '/redfish/v1/UpdateService/FirmwareInventory')
        g.api.add_resource(SoftwareInventory1API, '/redfish/v1/UpdateService/FirmwareInventory/<string:SoftwareInventoryId>')

        g.api.add_resource(StorageController0CollectionAPI, '/redfish/v1/Storage/<string:StorageId>/Controllers')
        g.api.add_resource(StorageController0API, '/redfish/v1/Storage/<string:StorageId>/Controllers/<string:ControllerId>')

        g.api.add_resource(StorageController1CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers')
        g.api.add_resource(StorageController1API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:ControllerId>')

        g.api.add_resource(StorageController2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers')
        g.api.add_resource(StorageController2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:ControllerId>')

        g.api.add_resource(StorageController3CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers')
        g.api.add_resource(StorageController3API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:ControllerId>')

        g.api.add_resource(StorageController4CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers')
        g.api.add_resource(StorageController4API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:ControllerId>')

        g.api.add_resource(StorageController5CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers')
        g.api.add_resource(StorageController5API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:ControllerId>')

        g.api.add_resource(Storage0CollectionAPI, '/redfish/v1/Storage')
        g.api.add_resource(Storage0API, '/redfish/v1/Storage/<string:StorageId>')

        g.api.add_resource(Storage1CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage')
        g.api.add_resource(Storage1API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>')

        g.api.add_resource(Storage2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage')
        g.api.add_resource(Storage2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>')

        g.api.add_resource(Storage3CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage')
        g.api.add_resource(Storage3API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>')

        g.api.add_resource(Storage4CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage')
        g.api.add_resource(Storage4API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>')

        g.api.add_resource(Storage5CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage')
        g.api.add_resource(Storage5API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>')

        g.api.add_resource(SwitchCollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Switches')
        g.api.add_resource(SwitchAPI, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>')

        g.api.add_resource(Task0CollectionAPI, '/redfish/v1/TaskService/Tasks')
        g.api.add_resource(Task0API, '/redfish/v1/TaskService/Tasks/<string:TaskId>')

        g.api.add_resource(Task1CollectionAPI, '/redfish/v1/TaskService/Tasks/<string:TaskId>/SubTasks')
        g.api.add_resource(Task1API, '/redfish/v1/TaskService/Tasks/<string:TaskId>/SubTasks/<string:TaskId2>')

        g.api.add_resource(TriggersCollectionAPI, '/redfish/v1/TelemetryService/Triggers')
        g.api.add_resource(TriggersAPI, '/redfish/v1/TelemetryService/Triggers/<string:TriggersId>')

        g.api.add_resource(USBControllerCollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/USBControllers')
        g.api.add_resource(USBControllerAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/USBControllers/<string:ControllerId>')

        g.api.add_resource(VCATEntry0CollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports/<string:PortId>/VCAT')
        g.api.add_resource(VCATEntry0API, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports/<string:PortId>/VCAT/<string:VCATEntryId>')

        g.api.add_resource(VCATEntry1CollectionAPI, '/redfish/v1/Systems/<string:SystemId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/VCAT')
        g.api.add_resource(VCATEntry1API, '/redfish/v1/Systems/<string:SystemId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/VCAT/<string:VCATEntryId>')

        g.api.add_resource(VCATEntry2CollectionAPI, '/redfish/v1/Systems/<string:SystemId>/FabricAdapters/<string:FabricAdapterId>/REQ-VCAT')
        g.api.add_resource(VCATEntry2API, '/redfish/v1/Systems/<string:SystemId>/FabricAdapters/<string:FabricAdapterId>/REQ-VCAT/<string:VCATEntryId>')

        g.api.add_resource(VCATEntry3CollectionAPI, '/redfish/v1/Systems/<string:SystemId>/FabricAdapters/<string:FabricAdapterId>/RSP-VCAT')
        g.api.add_resource(VCATEntry3API, '/redfish/v1/Systems/<string:SystemId>/FabricAdapters/<string:FabricAdapterId>/RSP-VCAT/<string:VCATEntryId>')

        g.api.add_resource(VCATEntry4CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/VCAT')
        g.api.add_resource(VCATEntry4API, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/VCAT/<string:VCATEntryId>')

        g.api.add_resource(VCATEntry5CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/REQ-VCAT')
        g.api.add_resource(VCATEntry5API, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/REQ-VCAT/<string:VCATEntryId>')

        g.api.add_resource(VCATEntry6CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/RSP-VCAT')
        g.api.add_resource(VCATEntry6API, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/RSP-VCAT/<string:VCATEntryId>')

        g.api.add_resource(VirtualMedia0CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/VirtualMedia')
        g.api.add_resource(VirtualMedia0API, '/redfish/v1/Managers/<string:ManagerId>/VirtualMedia/<string:VirtualMediaId>')

        g.api.add_resource(VirtualMedia1CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/VirtualMedia')
        g.api.add_resource(VirtualMedia1API, '/redfish/v1/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>')

        g.api.add_resource(VirtualMedia2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/VirtualMedia')
        g.api.add_resource(VirtualMedia2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>')

        g.api.add_resource(VirtualMedia3CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/VirtualMedia')
        g.api.add_resource(VirtualMedia3API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/VirtualMedia/<string:VirtualMediaId>')

        g.api.add_resource(VLanNetworkInterface0CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/NetworkDeviceFunctions/<string:NetworkDeviceFunctionId>/Ethernet/VLANs')
        g.api.add_resource(VLanNetworkInterface0API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/NetworkDeviceFunctions/<string:NetworkDeviceFunctionId>/Ethernet/VLANs/<string:VLanNetworkInterfaceId>')

        g.api.add_resource(VLanNetworkInterface1CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/EthernetInterfaces/<string:EthernetInterfaceId>/VLANs')
        g.api.add_resource(VLanNetworkInterface1API, '/redfish/v1/Managers/<string:ManagerId>/EthernetInterfaces/<string:EthernetInterfaceId>/VLANs/<string:VLanNetworkInterfaceId>')

        g.api.add_resource(VLanNetworkInterface2CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/EthernetInterfaces/<string:EthernetInterfaceId>/VLANs')
        g.api.add_resource(VLanNetworkInterface2API, '/redfish/v1/Systems/<string:ComputerSystemId>/EthernetInterfaces/<string:EthernetInterfaceId>/VLANs/<string:VLanNetworkInterfaceId>')

        g.api.add_resource(VLanNetworkInterface3CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/EthernetInterfaces/<string:EthernetInterfaceId>/VLANs')
        g.api.add_resource(VLanNetworkInterface3API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/EthernetInterfaces/<string:EthernetInterfaceId>/VLANs/<string:VLanNetworkInterfaceId>')

        g.api.add_resource(VLanNetworkInterface4CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/EthernetInterfaces/<string:EthernetInterfaceId>/VLANs')
        g.api.add_resource(VLanNetworkInterface4API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/EthernetInterfaces/<string:EthernetInterfaceId>/VLANs/<string:VLanNetworkInterfaceId>')

        g.api.add_resource(VLanNetworkInterface5CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/EthernetInterfaces/<string:EthernetInterfaceId>/VLANs')
        g.api.add_resource(VLanNetworkInterface5API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/EthernetInterfaces/<string:EthernetInterfaceId>/VLANs/<string:VLanNetworkInterfaceId>')

        g.api.add_resource(VLanNetworkInterface6CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/EthernetInterfaces/<string:EthernetInterfaceId>/VLANs')
        g.api.add_resource(VLanNetworkInterface6API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/EthernetInterfaces/<string:EthernetInterfaceId>/VLANs/<string:VLanNetworkInterfaceId>')

        g.api.add_resource(Zone0CollectionAPI, '/redfish/v1/Fabrics/<string:FabricId>/Zones')
        g.api.add_resource(Zone0API, '/redfish/v1/Fabrics/<string:FabricId>/Zones/<string:ZoneId>')

        g.api.add_resource(Zone1CollectionAPI, '/redfish/v1/CompositionService/ResourceZones')
        g.api.add_resource(Zone1API, '/redfish/v1/CompositionService/ResourceZones/<string:ZoneId>')

        g.api.add_resource(AccountService0API, '/redfish/v1/AccountService')

        g.api.add_resource(AccountService1API, '/redfish/v1/Managers/<string:ManagerId>/RemoteAccountService')

        g.api.add_resource(AggregationServiceAPI, '/redfish/v1/AggregationService')

        g.api.add_resource(Assembly0API, '/redfish/v1/Chassis/<string:ChassisId>/Assembly')

        g.api.add_resource(Assembly1API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Assembly')

        g.api.add_resource(Assembly2API, '/redfish/v1/Chassis/<string:ChassisId>/Drives/<string:DriveId>/Assembly')

        g.api.add_resource(Assembly3API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Assembly')

        g.api.add_resource(Assembly4API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Drives/<string:DriveId>/Assembly')

        g.api.add_resource(Assembly5API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Assembly')

        g.api.add_resource(Assembly6API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Assembly')

        g.api.add_resource(Assembly7API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Drives/<string:DriveId>/Assembly')

        g.api.add_resource(Assembly8API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>/Assembly')

        g.api.add_resource(Assembly9API, '/redfish/v1/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/Assembly')

        g.api.add_resource(Assembly10API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Memory/<string:MemoryId>/Assembly')

        g.api.add_resource(Assembly11API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/Assembly')

        g.api.add_resource(Assembly12API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Memory/<string:MemoryId>/Assembly')

        g.api.add_resource(Assembly13API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/Assembly')

        g.api.add_resource(Assembly14API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Assembly')

        g.api.add_resource(Assembly15API, '/redfish/v1/Chassis/<string:ChassisId>/PCIeDevices/<string:PCIeDeviceId>/Assembly')

        g.api.add_resource(Assembly16API, '/redfish/v1/Systems/<string:ComputerSystemId>/PCIeDevices/<string:PCIeDeviceId>/Assembly')

        g.api.add_resource(Assembly17API, '/redfish/v1/Chassis/<string:ChassisId>/Power/PowerSupplies/<string:PowerSupplyId>/Assembly')

        g.api.add_resource(Assembly18API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/Assembly')

        g.api.add_resource(Assembly19API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/Assembly')

        g.api.add_resource(Assembly20API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>/Assembly')

        g.api.add_resource(Assembly21API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/Assembly')

        g.api.add_resource(Assembly22API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/Assembly')

        g.api.add_resource(Assembly23API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>/Assembly')

        g.api.add_resource(Assembly24API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/Assembly')

        g.api.add_resource(Assembly25API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/Assembly')

        g.api.add_resource(Assembly26API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>/Assembly')

        g.api.add_resource(Assembly27API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/Assembly')

        g.api.add_resource(Assembly28API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/Assembly')

        g.api.add_resource(Assembly29API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>/Assembly')

        g.api.add_resource(Assembly30API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/Assembly')

        g.api.add_resource(Assembly31API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/Assembly')

        g.api.add_resource(Assembly32API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>/Assembly')

        g.api.add_resource(Assembly33API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Processors/<string:ProcessorId>/Assembly')

        g.api.add_resource(Assembly34API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/Assembly')

        g.api.add_resource(Assembly35API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>/Assembly')

        g.api.add_resource(Assembly36API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Assembly')

        g.api.add_resource(Assembly37API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Assembly')

        g.api.add_resource(Assembly38API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Assembly')

        g.api.add_resource(Assembly39API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Assembly')

        g.api.add_resource(Assembly40API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Assembly')

        g.api.add_resource(Assembly41API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Assembly')

        g.api.add_resource(Assembly42API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Assembly')

        g.api.add_resource(Assembly43API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Assembly')

        g.api.add_resource(Assembly44API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Assembly')

        g.api.add_resource(Assembly45API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Assembly')

        g.api.add_resource(Assembly46API, '/redfish/v1/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Assembly')

        g.api.add_resource(Assembly47API, '/redfish/v1/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Assembly')

        g.api.add_resource(Assembly48API, '/redfish/v1/Chassis/<string:ChassisId>/Thermal/Fans/<string:FanId>/Assembly')

        g.api.add_resource(Assembly49API, '/redfish/v1/Chassis/<string:ChassisId>/ThermalSubsystem/Fans/<string:FanId>/Assembly')

        g.api.add_resource(Assembly50API, '/redfish/v1/Chassis/<string:ChassisId>/PowerSubsystem/PowerSupplies/<string:PowerSupplyId>/Assembly')

        g.api.add_resource(Assembly51API, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/PowerSupplies/<string:PowerSupplyId>/Assembly')

        g.api.add_resource(Assembly52API, '/redfish/v1/Chassis/<string:ChassisId>/PowerSubsystem/Batteries/<string:BatteryId>/Assembly')

        g.api.add_resource(BatteryMetricsAPI, '/redfish/v1/Chassis/<string:ChassisId>/PowerSubsystem/Batteries/<string:BatteryId>/Metrics')

        g.api.add_resource(Bios0API, '/redfish/v1/Systems/<string:ComputerSystemId>/Bios')

        g.api.add_resource(Bios1API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Bios')

        g.api.add_resource(Bios2API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Bios')

        g.api.add_resource(CertificateLocationsAPI, '/redfish/v1/CertificateService/CertificateLocations')

        g.api.add_resource(CertificateServiceAPI, '/redfish/v1/CertificateService')

        g.api.add_resource(CompositionServiceAPI, '/redfish/v1/CompositionService')

        g.api.add_resource(EnvironmentMetrics0API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics1API, '/redfish/v1/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics2API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics3API, '/redfish/v1/Systems/<string:ComputerSystemId>/PCIeDevices/<string:PCIeDeviceId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics4API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:ControllerId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics5API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics6API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Memory/<string:MemoryId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics7API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Drives/<string:DriveId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics8API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Drives/<string:DriveId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics9API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics10API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics11API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/PCIeDevices/<string:PCIeDeviceId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics12API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics13API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:ControllerId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics14API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:ControllerId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics15API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics16API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Memory/<string:MemoryId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics17API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Drives/<string:DriveId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics18API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:ControllerId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics19API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Drives/<string:DriveId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics20API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics21API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics22API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/PCIeDevices/<string:PCIeDeviceId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics23API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Drives/<string:DriveId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics24API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:ControllerId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics25API, '/redfish/v1/Chassis/<string:ChassisId>/Memory/<string:MemoryId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics26API, '/redfish/v1/Chassis/<string:ChassisId>/Drives/<string:DriveId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics27API, '/redfish/v1/Chassis/<string:ChassisId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics28API, '/redfish/v1/Chassis/<string:ChassisId>/PCIeDevices/<string:PCIeDeviceId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics29API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics30API, '/redfish/v1/Chassis/<string:ChassisId>/MediaControllers/<string:MediaControllerId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics31API, '/redfish/v1/Facilities/<string:FacilityId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics32API, '/redfish/v1/Facilities/<string:FacilityId>/AmbientMetrics')

        g.api.add_resource(EnvironmentMetrics33API, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics34API, '/redfish/v1/Storage/<string:StorageId>/Controllers/<string:ControllerId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics35API, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics36API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics37API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics38API, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics39API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics40API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics41API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics42API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics43API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics44API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics45API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics46API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics47API, '/redfish/v1/Chassis/<string:ChassisId>/MediaControllers/<string:MediaControllerId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics48API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics49API, '/redfish/v1/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EnvironmentMetrics50API, '/redfish/v1/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>/EnvironmentMetrics')

        g.api.add_resource(EventServiceAPI, '/redfish/v1/EventService')

        g.api.add_resource(JobServiceAPI, '/redfish/v1/JobService')

        g.api.add_resource(KeyServiceAPI, '/redfish/v1/KeyService')

        g.api.add_resource(LicenseServiceAPI, '/redfish/v1/LicenseService')

        g.api.add_resource(LogService0CollectionAPI, '/redfish/v1/Managers/<string:ManagerId>/LogServices')
        g.api.add_resource(LogService0API, '/redfish/v1/Managers/<string:ManagerId>/LogServices/<string:LogServiceId>')

        g.api.add_resource(LogService1CollectionAPI, '/redfish/v1/Systems/<string:ComputerSystemId>/LogServices')
        g.api.add_resource(LogService1API, '/redfish/v1/Systems/<string:ComputerSystemId>/LogServices/<string:LogServiceId>')

        g.api.add_resource(LogService2CollectionAPI, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/LogServices')
        g.api.add_resource(LogService2API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/LogServices/<string:LogServiceId>')

        g.api.add_resource(LogService3CollectionAPI, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/LogServices')
        g.api.add_resource(LogService3API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/LogServices/<string:LogServiceId>')

        g.api.add_resource(LogService4CollectionAPI, '/redfish/v1/Chassis/<string:ChassisId>/LogServices')
        g.api.add_resource(LogService4API, '/redfish/v1/Chassis/<string:ChassisId>/LogServices/<string:LogServiceId>')

        g.api.add_resource(LogService5API, '/redfish/v1/JobService/Log')

        g.api.add_resource(LogService6API, '/redfish/v1/TelemetryService/LogService')

        g.api.add_resource(LogService7API, '/redfish/v1/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/DeviceLog')

        g.api.add_resource(ManagerDiagnosticDataAPI, '/redfish/v1/Managers/<string:ManagerId>/ManagerDiagnosticData')

        g.api.add_resource(ManagerNetworkProtocolAPI, '/redfish/v1/Managers/<string:ManagerId>/NetworkProtocol')

        g.api.add_resource(MemoryMetrics0API, '/redfish/v1/Systems/<string:ComputerSystemId>/MemorySummary/MemoryMetrics')

        g.api.add_resource(MemoryMetrics1API, '/redfish/v1/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/MemoryMetrics')

        g.api.add_resource(MemoryMetrics2API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/MemorySummary/MemoryMetrics')

        g.api.add_resource(MemoryMetrics3API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Memory/<string:MemoryId>/MemoryMetrics')

        g.api.add_resource(MemoryMetrics4API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/MemorySummary/MemoryMetrics')

        g.api.add_resource(MemoryMetrics5API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/MemoryMetrics')

        g.api.add_resource(MemoryMetrics6API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/MemorySummary/MemoryMetrics')

        g.api.add_resource(MemoryMetrics7API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/MemorySummary/MemoryMetrics')

        g.api.add_resource(MemoryMetrics8API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Memory/<string:MemoryId>/MemoryMetrics')

        g.api.add_resource(MemoryMetrics9API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/MemorySummary/MemoryMetrics')

        g.api.add_resource(MemoryMetrics10API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Memory/<string:MemoryId>/MemoryMetrics')

        g.api.add_resource(MemoryMetrics11API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/MemorySummary/MemoryMetrics')

        g.api.add_resource(MemoryMetrics12API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/MemorySummary/MemoryMetrics')

        g.api.add_resource(MessageRegistryFileCollectionAPI, '/redfish/v1/Registries')
        g.api.add_resource(MessageRegistryFileAPI, '/redfish/v1/Registries/<string:MessageRegistryFileId>')

        g.api.add_resource(NetworkAdapterMetricsAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Metrics')

        g.api.add_resource(NetworkDeviceFunctionMetricsAPI, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/NetworkDeviceFunctions/<string:NetworkDeviceFunctionId>/Metrics')

        g.api.add_resource(PCIeSlotsAPI, '/redfish/v1/Chassis/<string:ChassisId>/PCIeSlots')

        g.api.add_resource(PortMetrics0API, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics1API, '/redfish/v1/Chassis/<string:ChassisId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics2API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics3API, '/redfish/v1/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics4API, '/redfish/v1/Systems/<string:ComputerSystemId>/FabricAdapters/<string:FabricAdapterId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics5API, '/redfish/v1/Systems/<string:ComputerSystemId>/GraphicsControllers/<string:ControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics6API, '/redfish/v1/Systems/<string:ComputerSystemId>/USBControllers/<string:ControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics7API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics8API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics9API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics10API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics11API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics12API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics13API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics14API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics15API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics16API, '/redfish/v1/Chassis/<string:ChassisId>/MediaControllers/<string:MediaControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics17API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics18API, '/redfish/v1/Storage/<string:StorageId>/StorageControllers/<string:StorageControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics19API, '/redfish/v1/Storage/<string:StorageId>/Controllers/<string:StorageControllerId>/Ports/<string:PortId>/Metrics')

        g.api.add_resource(PortMetrics20API, '/redfish/v1/Managers/<string:ManagerId>/USBPorts/<string:PortId>/Metrics')

        g.api.add_resource(PowerDistributionMetrics0API, '/redfish/v1/PowerEquipment/RackPDUs/<string:PowerDistributionId>/Metrics')

        g.api.add_resource(PowerDistributionMetrics1API, '/redfish/v1/PowerEquipment/FloorPDUs/<string:PowerDistributionId>/Metrics')

        g.api.add_resource(PowerDistributionMetrics2API, '/redfish/v1/PowerEquipment/TransferSwitches/<string:PowerDistributionId>/Metrics')

        g.api.add_resource(PowerDistributionMetrics3API, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/Metrics')

        g.api.add_resource(PowerDistributionMetrics4API, '/redfish/v1/PowerEquipment/Switchgear/<string:PowerDistributionId>/Metrics')

        g.api.add_resource(PowerDistributionMetrics5API, '/redfish/v1/PowerEquipment/ElectricalBuses/<string:PowerDistributionId>/Metrics')

        g.api.add_resource(PowerEquipmentAPI, '/redfish/v1/PowerEquipment')

        g.api.add_resource(PowerSubsystemAPI, '/redfish/v1/Chassis/<string:ChassisId>/PowerSubsystem')

        g.api.add_resource(PowerSupplyMetrics0API, '/redfish/v1/Chassis/<string:ChassisId>/PowerSubsystem/PowerSupplies/<string:PowerSupplyId>/Metrics')

        g.api.add_resource(PowerSupplyMetrics1API, '/redfish/v1/PowerEquipment/PowerShelves/<string:PowerDistributionId>/PowerSupplies/<string:PowerSupplyId>/Metrics')

        g.api.add_resource(PowerAPI, '/redfish/v1/Chassis/<string:ChassisId>/Power')

        g.api.add_resource(ProcessorMetrics0API, '/redfish/v1/Systems/<string:ComputerSystemId>/ProcessorSummary/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics1API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics2API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics3API, '/redfish/v1/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics4API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics5API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics6API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics7API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/ProcessorSummary/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics8API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics9API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics10API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics11API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics12API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics13API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics14API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/ProcessorSummary/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics15API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics16API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics17API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics18API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Processors/<string:ProcessorId>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics19API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/ProcessorMetrics')

        g.api.add_resource(ProcessorMetrics20API, '/redfish/v1/Chassis/<string:ChassisId>/NetworkAdapters/<string:NetworkAdapterId>/Processors/<string:ProcessorId>/SubProcessors/<string:ProcessorId2>/SubProcessors/<string:ProcessorId3>/ProcessorMetrics')

        g.api.add_resource(SecureBoot0API, '/redfish/v1/Systems/<string:ComputerSystemId>/SecureBoot')

        g.api.add_resource(SecureBoot1API, '/redfish/v1/CompositionService/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SecureBoot')

        g.api.add_resource(SecureBoot2API, '/redfish/v1/ResourceBlocks/<string:ResourceBlockId>/Systems/<string:ComputerSystemId>/SecureBoot')

        g.api.add_resource(ServiceConditionsAPI, '/redfish/v1/ServiceConditions')

        g.api.add_resource(ServiceRoot0API, '/redfish/v1')

        g.api.add_resource(ServiceRoot1API, '/redfish/v1/')

        g.api.add_resource(SessionServiceAPI, '/redfish/v1/SessionService')

        g.api.add_resource(SessionCollectionAPI, '/redfish/v1/SessionService/Sessions', resource_class_kwargs={'auth_mode': auth_mode})
        g.api.add_resource(SessionAPI, '/redfish/v1/SessionService/Sessions/<string:SessionId>', resource_class_kwargs={'auth_mode': auth_mode})

        g.api.add_resource(SwitchMetricsAPI, '/redfish/v1/Fabrics/<string:FabricId>/Switches/<string:SwitchId>/SwitchMetrics')

        g.api.add_resource(TaskServiceAPI, '/redfish/v1/TaskService')

        g.api.add_resource(TelemetryServiceAPI, '/redfish/v1/TelemetryService')

        g.api.add_resource(ThermalMetricsAPI, '/redfish/v1/Chassis/<string:ChassisId>/ThermalSubsystem/ThermalMetrics')

        g.api.add_resource(ThermalSubsystemAPI, '/redfish/v1/Chassis/<string:ChassisId>/ThermalSubsystem')

        g.api.add_resource(ThermalAPI, '/redfish/v1/Chassis/<string:ChassisId>/Thermal')

        g.api.add_resource(UpdateServiceAPI, '/redfish/v1/UpdateService')


    @property
    def configuration(self):
        """
        Configuration property - Service Root
        """
        config = {
            '@odata.context': self.rest_base + '$metadata#ServiceRoot',
            '@odata.type': '#ServiceRoot.v1_9_0.ServiceRoot',
            '@odata.id': self.rest_base,
            'Id': 'RootService',
            'Name': 'Root Service',
            'RedfishVersion': '1.6.0',
            'UUID': self.uuid,
            'Chassis': {'@odata.id': self.rest_base + 'Chassis'},
            #'Fabrics': {'@odata.id': self.rest_base + 'Fabrics'},
            # 'EgResources': {'@odata.id': self.rest_base + 'EgResources'},
            #'Managers': {'@odata.id': self.rest_base + 'Managers'},
            #'TaskService': {'@odata.id': self.rest_base + 'TaskService'},
            'SessionService': {'@odata.id': self.rest_base + 'SessionService'},
            #'StorageServices': {'@odata.id': self.rest_base + 'StorageServices'},
            #'StorageSystems': {'@odata.id': self.rest_base + 'StorageSystems'},
            #'AccountService': {'@odata.id': self.rest_base + 'AccountService'},
            #'EventService': {'@odata.id': self.rest_base + 'EventService'},
            'Registries': {'@odata.id': self.rest_base + 'Registries'},
            'Systems': {'@odata.id': self.rest_base + 'Systems'},
            'Storage': {'@odata.id': self.rest_base + 'Storage'},
            #'CompositionService': {'@odata.id': self.rest_base + 'CompositionService'}
        }

        return config

    @property
    def available_procs(self):
        return self.max_procs - self.used_procs

    @property
    def available_mem(self):
        return self.max_memory - self.used_memory

    @property
    def available_storage(self):
        return self.max_storage - self.used_storage

    @property
    def available_network(self):
        return self.max_network - self.used_network

    @property
    def num_pooled_nodes(self):
        if self.spec == 'Chinook':
            return self.PooledNodes.count
        else:
            return self.Systems.count

    def _create_redfish(self, rs, action):
        """
        Private method for creating a Redfish based pooled node

        Arguments:
            rs  - The requested pooled node
        """
        try:
            pn = ComputerSystem(rs, self.cs_puid_count + 1, self.rest_base, 'Systems')
            self.Systems.add_computer_system(pn)
        except KeyError as e:
            raise CreatePooledNodeError(
                'Configuration missing key: ' + e.message)
        try:
            # Verifying resources
            assert pn.processor_count <= self.available_procs, self.err_str.format('CPUs')
            assert pn.storage_gb <= self.available_storage, self.err_str.format('storage')
            assert pn.network_ports <= self.available_network, self.err_str.format('network ports')
            assert pn.total_memory_gb <= self.available_mem, self.err_str.format('memory')

            self.used_procs += pn.processor_count
            self.used_storage += pn.storage_gb
            self.used_network += pn.network_ports
            self.used_memory += pn.total_memory_gb
        except AssertionError as e:
            self._remove_redfish(pn.cs_puid)
            raise CreatePooledNodeError(e.message)
        except KeyError as e:
            self._remove_redfish(pn.cs_puid)
            raise CreatePooledNodeError(
                'Requested system missing key: ' + e.message)

        self.resource_dictionary.add_resource('Systems/{0}'.format(pn.cs_puid), pn)
        self.cs_puid_count += 1
        return pn.configuration

    def _remove_redfish(self, cs_puid):
        """
        Private method for removing a Redfish based pooled node

        Arguments:
            cs_puid - CS_PUID of the pooled node to remove
        """
        try:
            pn = self.Systems[cs_puid]

            # Adding back in used resources
            self.used_procs -= pn.processor_count
            self.used_storage -= pn.storage_gb
            self.used_network -= pn.network_ports
            self.used_memory -= pn.total_memory_gb

            self.Systems.remove_computer_system(pn)
            self.resource_dictionary.delete_resource('Systems/{0}'.format(cs_puid))

            if self.Systems.count == 0:
                self.cs_puid_count = 0
        except IndexError:
            raise RemovePooledNodeError(
                'No pooled node with CS_PUID: {0}, exists'.format(cs_puid))

    def get_resource(self, path):
        """
        Call Resource_Dictionary's get_resource
        """
        obj = self.resource_dictionary.get_resource(path)
        return obj


'''
    def remove_pooled_node(self, cs_puid):
        """
        Delete the specified pooled node and free its resources.

        Throws a RemovePooledNodeError Exception if a problem is encountered.

        Arguments:
            cs_puid - CS_PUID of the pooed node to remove
        """
        self.remove_method(cs_puid)

    def update_cs(self,cs_puid,rs):
        """
            Updates the power metrics of Systems/1
        """
        cs=self.Systems[cs_puid]
        cs.reboot(rs)
        return cs.configuration

    def update_system(self,rs,c_id):
        """
            Updates selected System
        """
        self.Systems[c_id].update_config(rs)

        event = Event(eventType='ResourceUpdated', severity='Notification', message='System updated',
                      messageID='ResourceUpdated.1.0.System', originOfCondition='/redfish/v1/System/{0}'.format(c_id))
        self.push_event(event, 'ResourceUpdated')
        return self.Systems[c_id].configuration

    def add_event_subscription(self, rs):
        destination = rs['Destination']
        types = rs['Types']
        context = rs['Context']

        allowedTypes = ['StatusChange',
                        'ResourceUpdated',
                        'ResourceAdded',
                        'ResourceRemoved',
                        'Alert']

        for type in types:
            match = False
            for allowedType in allowedTypes:
                if type == allowedType:
                    match = True

            if not match:
                raise EventSubscriptionError('Some of types are not allowed')

        es = self.EventSubscriptions.add_subscription(destination, types, context)
        es_id = es.configuration['Id']
        self.resource_dictionary.add_resource('EventService/Subscriptions/{0}'.format(es_id), es)
        event = Event()
        self.push_event(event, 'Alert')
        return es.configuration

    def push_event(self, event, type):
        # Retreive subscription list
        subscriptions = self.EventSubscriptions.configuration['Members']
        for sub in subscriptions:
            # Get event subscription
            event_channel = self.resource_dictionary.get_object(sub.replace('/redfish/v1/', ''))
            event_types = event_channel.configuration['EventTypes']
            dest_uri = event_channel.configuration['Destination']

            # Check if client subscribes for event type
            match = False
            for event_type in event_types:
                if event_type == type:
                    match = True

            if match:
                # Sending event response
                EventWorker(dest_uri, event).start()


class EventWorker(Thread):
    """
    Worker class for sending event messages to clients
    """
    def __init__(self, dest_uri, event):
        super(EventWorker, self).__init__()
        self.dest_uri = dest_uri
        self.event = event

    def run(self):
        try:
            request = urllib2.Request(self.dest_uri)
            request.add_header('Content-Type', 'application/json')
            urllib2.urlopen(request, json.dumps(self.event.configuration), 15)
        except Exception:
            pass
'''
