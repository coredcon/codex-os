---
title: "*|ControlPoint| - VNC Silent Install"
freshdesk_id: 17000127279
category: "Support"
folder: "ControlPoint"
status: published
created: 2022-07-19
updated: 2022-12-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000127279
---

# *|ControlPoint| - VNC Silent Install

**VNC Silent Installer**


The VNC Silent Installer method is used on devices that do not have VNC installed on them post-production.  Below are the steps to apply this installer to devices.  This will only work on Win32 Devices.


**Installation**


This installation method relies on using a template created in ControlPoint.  You will use the template to transfer the needed files to the device as well as install VNC. The required files are in a zip file located located at \\qsr-filesvr.corp.qsrautomations.com\QSR-Doc\QA\QA_NelsonMiller\Temp\For Support\VNC. Once you have the zip file you will need to transfer it to the site and extract the files in a location of your choice.  Below are the steps to create the template:


- Open ControlPoint

- Click “Templates”

- Click “Add”

- Name: Silent Installer

- Type: ConnectSmart FreshServe

- Click Save

- Select “Bin” Located under Default >> QSR Automations >> ConnectSmart >> FreshServe

- Click “Import Files

- Change file type to “All files”

- Navigate to the folder that contains the extracted “Silent Installer. Zip” files

- Select the 4 files

- Rename.bat

- Tightvnc-2.0.4-setup.exe

- Vnc_config.reg

- Vincinstall.bat


- Click “Processes”

- Click “Add Process”

- Process Path: “C:\Program Files\QSR Automations\ConnectSmart\FreshServe\Bin\vncinstall.bat”

- Execution Type: “Startup”

- Click Save

- Return to “Files” tab and click “Apply” then “Save”


**Execution**


Apply the newly created template to the device needing VNC.


- Select the appropriate device

- Click “Edit Device”

- Make note of which template options are checked and then uncheck them

- Check “Silent Installer”

- Click Save


The device will receive the files and install VNC.  Once this is complete you will:


- Select the device

- Click “Edit Device”

- Uncheck “Silent Installer”

- Check the appropriate template(s) for this device.

- Click Save


To confirm the install completed, you should view the files on the device under C:\Program Files\QSR Automations\ConnectSmart\FreshServe\Bin\ and verify “success.txt” is present (that should be the only file showing).