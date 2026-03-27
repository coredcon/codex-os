---
title: "*|Hardware| - How to program the KP 7500 with Non-QSR Hardware"
freshdesk_id: 17000127473
category: "Support"
folder: "Hardware"
status: published
created: 2022-08-02
updated: 2022-08-02
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000127473
---

# *|Hardware| - How to program the KP 7500 with Non-QSR Hardware

It is possible to reprogram the keys of the KP 7500 with Non-QSR hardware, but it will require a ControlPoint license for Non-QSR Hardware.


 


The computer that is going to be the station that reprograms the bump bars will need to have ControlPoint Server and Client installed and DeviceAgent set up so that it will appear in ControlPoint.


 


**How to setup DeviceAgent on Non-QSR Hardware:**


 


1.) Find the DeviceAgent.exe in the ControlPoint directory (C:\Program Files (x86)\QSR Automations\ControlPoint\ControlPointServer\DeviceAgent\E25_ARM)


 


2.) Create the C:\QSRAuto\DeviceAgent directory and then place the DeviceAgent.exe in that folder.


 


3.) Right-click on the DeviceAgent.exe and select "Create a Shortcut".


 


4.) Right-click on the newly created DeviceAgent.exe shortcut and select properties. Next, add a " /p" to the end of the Target field so that you can start DeviceAgent as a process. Now select OK when completed. (see screenshot)


 


5.) Double click to run the newly edited DeviceAgent.exe shortcut. There should now be a ControlPoint looking icon in the system tray (see screenshot)


 


6.) Start the ControlPoint Server service and open ControlPoint Client and the station should appear as an Unknown Device so that it can be assigned to a station where the IP address information is set to "Not Managed". The end result should look something like this: 


 


 


 


**Creating the Keypad Template and how to Reprogram the keys:**


 


1.) Select the "Bump-Bars" button in the top right-hand corner of the ControlPoint Client window:


 


2.) Next, select the "Add" button in the Bump Bars window and under Device Details name the template and select KP 7500 as the type. This window will allow the ability to change the keybinding of each button by clicking once on the button that is desired to be changed. 


 


3.) Assign the keypad template to the station that will have the physical keypad connected to it by editing the station, selecting the Peripherals tab and select the desired template in the Bump Bar drop-down menu. When finished select Apply.


 


 


4.) With the template configured with the reprogrammed keys applied to the station that has the keypad connected to it select the diagnostic button in ControlPoint Client.


 


5.) Select the Bump Bar tab on the Device Diagnostics window. When ready to push the new keybinding configuration to the bump bar select the Program button.


 


 


6.) When the programming has completed the below message will appear in the Output window


 


 


The bump bar has now been reprogrammed with the desired keybinding settings.