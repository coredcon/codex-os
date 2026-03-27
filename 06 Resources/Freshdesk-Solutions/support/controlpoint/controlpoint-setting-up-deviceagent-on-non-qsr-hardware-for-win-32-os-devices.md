---
title: "*|ControlPoint| - Setting up DeviceAgent on Non QSR Hardware for WIN 32 OS devices"
freshdesk_id: 17000125279
category: "Support"
folder: "ControlPoint"
status: published
created: 2022-05-10
updated: 2024-03-26
views: 0
tags: ["Non-QSR Hardware"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000125279
---

# *|ControlPoint| - Setting up DeviceAgent on Non QSR Hardware for WIN 32 OS devices

**Setting up DeviceAgent on Non QSR Hardware for WIN 32 OS devices**


**IMPORTANT:** 


Non QSR Hardware will need to be licensed as such in ControlPoint and ConnectSmart Kitchen. 


Once this is done and ControlPoint is configured and templates are built (DisplayClient), this will allow the created templates to show as a selection under the Templates tab for the device in ControlPoint. 


Created templates will NOT show for NON QSR Hardware devices if the license does not have NON QSR Hardware enabled for both ConnectSmart Kitchen and ControlPoint. 


**Configuration:**


- On the local machine** (NON QSR Hardware), **create a folder called** “QSRAuto” **on the C:\ drive.


- Create a Sub Folder for** "DeviceAgent"**

- Copy the contents of DeviceAgent from the following directory:
**C:\Program Files (x86)\QSR Automations\ControlPoint\ControlPointServer\DeviceAgent\Win32** on the device that the QSR ControlPoint application is installed on, into the folder **C:\QSRAuto**. This is to ensure the version of DeviceAgent matches what is installed on the QSR server.


- On Windows 10 devices the startup folder is no longer a reliable or recommended way to set DeviceAgent to run when the system starts. It is recommended to use a scheduled task instead.

- Open **Task Scheduler**

- Choose **Create Task** on the right side of the screen


- Name the task **QsrDeviceAgentStart**

- Check the box for "**Run with highest privileges**"


- Go to the **Triggers** tab

- Click the "**New**" button

- Change the drop down to "**At log on**"

- Hit **OK**
****


- Go to the **Actions** tab

- Click the "**New**" button

- Set the Action to "**Start a program**"

- Under "program/script:" add  **C:\QSRAuto\DeviceAgent\QsrDeviceAgent.exe**

- Under "Add arguments" set the** /p** flag

- Under "Start in" add **C:\QSRAuto\DeviceAgent\**


- Hit **OK**

- Go to the **Conditions **tab

- Uncheck the box for "**Start only if the computer is on AC power**"


- Go to the **Settings **tab

- Check the box for "**Run task as soon as possible after a scheduled start is missed**"

- Uncheck the option for "**Stop the task if it runs longer than:**"

- Uncheck the Option for "**If the running task does not end when requested, force stop it**"


- Hit **OK **to save the task


**NOTES:**


Ensure the firewall is switched off on both the device (Non QSR Hardware) where DeviceAgent will run from and on the device running QSR ControlPoint and QSR Kitchen Server applications.


Make sure that DeviceAgent is set to run as an Administrator on all users


Right click on the EXE


Choose **Properties **on the context menu


On the Compatibility tab choose **Change Settings for all users**


Select** Run the program as administrator**


Click **Apply** and then **OK**


Reboot to restart DeviceAgent with the new settings applied – The device should now appear in ControlPoint as an unknown Win32 device ready to be assigned to a station. It is recommended at this point to create the device in ControlPoint from the unknown device, then change the settings in ControlPoint, name, station id, etc.