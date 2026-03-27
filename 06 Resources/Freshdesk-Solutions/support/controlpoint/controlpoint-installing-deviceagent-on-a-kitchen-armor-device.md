---
title: "|ControlPoint| - Installing DeviceAgent on a Kitchen Armor device"
freshdesk_id: 17000140501
category: "Support"
folder: "ControlPoint"
status: published
created: 2024-04-26
updated: 2024-04-26
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000140501
---

# |ControlPoint| - Installing DeviceAgent on a Kitchen Armor device

NOTE: This software is only compatible with Kitchen Armor devices that are on Android 10. You will want to confirm the version in **Settings>About Tablet>Build Number**


 


You will need to have ControlPoint 2024.2.5 installed on the server.


Once that version is installed you can find the Kitchen Armor compatible version of DeviceAgent in this directory: **C:\Program Files (x86)\QSR Automations\ControlPoint\ControlPointServer\DeviceAgent\Android\Kitchen_Armor**


 


You will want to put the **QSRDeviceAgent-kitchen_armor-2024.2.24-20240328221905.apk **on a flash drive and plug the flash drive into the Kitchen Armor device.


Swipe up until you see the full apps list and select Files (It is a blue icon with a white file folder pictured)


The flash drive will be listed on the left side of the Files screen.


When you select it there you should be able to see the APK listed in the middle of the screen


 


Select the APK and choose Continue


Choose Install


Choose Open


 


Reboot the Device.


You should now be able to see the device as Unknown in ControlPoint and can assign it to a device build using the Kitchen Armor Deice type.


 


 As long as you have no other Non QSR Android devices or any Android 7 devices you should now be able to reenable the settings n ControlPoint and Kitchen Builder to auto update DisplayClient and DeviceAgent for Android.

If you do have other devices then you will need to manually update DisplayClient as well with the version found here: **C:\ProgramData\QSR Automations\ConnectSmart\KitchenServer\ClientInstalls\DisplayClient\Android**