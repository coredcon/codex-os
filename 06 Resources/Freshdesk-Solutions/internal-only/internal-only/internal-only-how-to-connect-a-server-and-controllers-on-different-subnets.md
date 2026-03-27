---
title: "*|Internal Only| - How to connect a Server and Controller(s) on different subnets"
freshdesk_id: 17000052457
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2017-06-01
updated: 2022-08-25
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000052457
---

# *|Internal Only| - How to connect a Server and Controller(s) on different subnets

- Statically set the IP and gateway information on the server and controller(s).

- Modify the ConnectSmartNetwork.xml file to look like the example below.  Put the controller IP in the first IP address line.  Put the server IP address in the second IP address line.  Each controller will need one of these files.  Once modified, place the file in the same directory as the QSRDeviceAgent.exe.

- The site will need to ensure the following TCP ports are open (32881, 32882, 32883 are only needed if site is using backups/redundancy and 32888 if using DineTime and KitchenServer 5/6 to send print and page requests to ControlPoint):

- Once the XML is on the controller, open the file and confirm there are no special character after the “>” on each line (This may happen if file is scanned by an anti-virus when pushed to the controller).  Remove any special characters if present and save file.

- Open ControlPoint on the server.

- On the controller(s), exit QSRDeviceAgent.exe if running.

- On the controller(s), in the same directory with the ConnectSmartNetwork.xml and QSRDeviceAgent.exe, delete the QSRDeviceAgent.xml file, if present, and then launch QSRDeviceAgent.exe. (If using a Win32 device, be sure to launch QSRDeviceAgent.exe from Startup and NOT from within the directory – if using a WinCE device, you have to start the .exe from the directory as there is no Startup).

- ControlPoint should now have the controller listed under Unknown Devices. 

- Assign the desired template to the unknown device(s).