---
title: "Troubleshooting USB Printing for Win32 Devices (ControlPoint 2024.1.7+)"
freshdesk_id: 17000139216
category: "Support"
folder: "ControlPoint"
status: published
created: 2024-02-29
updated: 2025-08-07
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000139216
---

# Troubleshooting USB Printing for Win32 Devices (ControlPoint 2024.1.7+)

Starting with ControlPoint 2023.5 it is possible to get Epson Printers to work with WIn32 Devices assuming the attached Driver Files are installed and the instructions inside that same Zip folder are followed. If the Printer is still not detected after ensuring the directions were followed, here are a few things to check to narrow down where the issue is.

*****This is a SUPPLEMENT to the instructions attached and included with the Driver files, NOT A REPLACEMENT. The First Step should always be going through instructions and making sure each step was followed.**


# Troubleshooting Steps


### **Make Sure that ControlPoint 2024.1.7 or higher is the version in use**


- Easiest Way is to look in bottom left of ControlPoint Client to see what version is listed. While ControlPoint 2023.5 was first to introduce feature, it is strongly recommended to update to the latest version of ControlPoint when using USB printing. Third Party Devices will not work with USB Printing unless it using ControlPoint 2024.1.7 or higher. As this is a feature still being developed, it will be best to use the latest release of ControlPoint.


### **Check that DeviceAgent on controller using printer is updated version**


- If the site is upgrading to CP 2024 the DeviceAgent on the controllers may still be for the older version of ControlPoint. 

- There will be an option in ControlPoint Server Settings under the DeviceAgent tab that will let you enable auto update Windows and Android based DeviceAgent. 

- You can also copy over the DeviceAgent .exe and UpgradeDeviceAgent.exe found in C:\Program Files (x86)\QSR Automations\ControlPoint\ControlPointServer\DeviceAgent\Win32 to the QSRAuto\DeviceAgent folder


### **Make sure that the Printer is showing under Universal Serial Bus in Device Manager**


- The type of printer using the USB connection should be visible in DeviceAgent. If not the printer is either not being detected, or the drivers were not installed correctly.


If the printer shows up as a software device instead of a USB Serial Bus Device, then you will need to have the customer change the Interface to "Built in USB" and the Class to "Vendor" in the printer settings. These can typically be found by powering on the printer while holding the feed button and following the prompts at the bottom of the receipt to navigate the menus. 


### **Make sure the driver for the printer is showing author as QSR Automations**


- If it does not show QSR Automations it means the incorrect Driver is in use.


### **Check that all needed files are inside DeviceAgent folder on Controller**


In addition to the normal files needed for DeviceAgent to work, there should be the following:


- QSR.WinUsb.EscPos.PrintServer.dll <-- This will show up when an up-to-date version of DeviceAgent is launched

- QsrEpsonWinUsbEscPosDriver.cat

- QsrEpsonWinUsbEscPosDriver.inf


When everything is correct, and you have run a updated version of DeviceAgent at least once, the C\QSRAuto\DeviceAgent folder should look like the below:

### 


*****NOTE - This is just for getting USB printing working, TCP will require a ConnectSmart Network.xml file as well.**