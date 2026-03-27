---
title: "*|Hardware| - Configuring the KP-9000 with Non-QSR Hardware"
freshdesk_id: 17000128646
category: "Support"
folder: "Hardware"
status: published
created: 2022-10-04
updated: 2025-12-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000128646
---

# *|Hardware| - Configuring the KP-9000 with Non-QSR Hardware

Configuring a KP-9000 with Non-QSR Hardware is similar to configuring it with QSR Hardware but with one exception. The exception is that the KP-9000 requires two .DLL files that need to be placed in either the SysWOW64 or System32 folder on the system (that the bump bar is connected to) depending on if the computer is using a 32 bit or 64 bit operating system.


The new .dll files are necessary for ControlPoint to interact with the keypad/dongle. So while you have basic functionality without those files, you can’t do anything like turn volume on/off, force pair/unpair, diagnostics, program, and battery checks. If you want the ControlPoint features, you have to have the new .DLLs (on WES7+ devices) or CE image (on xCeeds), and ControlPoint 3.1 or higher.


 


The two .DLL files that are required are named "HIDKeypad.dll" and "usbhid.dll".


Here are some basic steps to be able to have full functionality with KP-9000 and Non-QSR Hardware:


1.) Turn off DeviceAgent on the Non-QSR Hardware device.


2.) Copy/Paste the two .DLLs into either SysWOW64 or System32 folder of the device.


3.) Start DeviceAgent on the device.


4.) Plug in the USB dongle into the device and ensure that there is a KP-9000 template built in ControlPoint and that it has been assigned to the device via the Peripheral Tab.


After following the above steps all the options in the Bump Bar tab of Diagnostic mode should be available to use on command.