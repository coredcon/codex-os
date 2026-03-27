---
title: "*|Networking| - Configuring TCP Connection for POS Terminals and Controllers"
freshdesk_id: 17000069520
category: "Support"
folder: "Networking"
status: published
created: 2018-03-29
updated: 2022-11-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000069520
---

# *|Networking| - Configuring TCP Connection for POS Terminals and Controllers

# Configuring QSRPOSi.dll for HTTP (TCP) connection]


## QSR Web Service Interface]


This document outlines the configuration of QSRPOSi when using TCP messages from the Point of Sale. 


The QSR Web Service Interface allows ConnectSmart Kitchen Server to receive messages from the Point of Sale via HTTP (TCP).  Using HTTP Communication provides greater stability for network traffic and decreases the likelihood of lost messages.  It also supports PCI compliance regulations. 


There are two required components:


- QsrPOSi.dll

- QsrSock.xml


There is also a component of Control point that will assist users in configuring their devices to communicate via TCP messages.


ControlPoint TCP Only is an additional tool that works with Control Point to add a ConnectSmart Network xml to the hardware allowing Device Agent to search for a specific IP address rather than simply broadcasting until control point gives it the IP address.


## QSRPOSi.dll]


By default, QSRPOSi.dll uses UDP broadcasts for communicating with ConnectSmart Kitchen.  This file needs to be placed peer to the POS executable on the terminal or in the following location:


Windows\system32


Windows\sysWOW on 64 –bit machines


## QSRSock.xml]


To enable HTTP/TCP a new QSRSock.xml configuration file must be copied to the common application data directory on each POS Terminal.

Operating System
Data Directory
XP Installs
C:\Documents and Settings\All Users\Application Data\QSR Automations\ConnectSmart\QsrSock\Data
Windows 7 Installs
C:\ProgramData\QSR Automations\ConnectSmart\QsrSock\Data


Edit the QSRSock.xml manually using NotePad to point to the correct IP based on each system.  


## QSRSock.xml Configuration Options]


There are configuration options within the QSRSock.xml, only modify them if necessary to fit the needs of the restaurant.


**LogLevel:** 


Determines the amount types of messages the QSRSock log file will contain.


     Default is set to: Critical / General.


Messages can fall into multiple log categories, for example, a message regarding a network failure would be both critical and network.  Logging level breakouts are:


**General:**  


Informational only messages.  Not typically failures they are simply information on events such as system startup or End of Day running.


**Critical:**  


Important and/or error messages. Critical messages indicate a failure somewhere in the system.


**Network:**  


These can be both informational or error messages.  This log level is NOT recommended unless you are troubleshooting a specific issue.


**Trace:**  


Very detailed, log-level messages.  Primarily used to log each function call.


**All:**  


All of the above message types will be logged. 


**Note:** 


All and Track logging levels log nearly all messages sent and received by QsrPosi.dll and can grow very large very quickly.  Do not set to those levels unless troubleshooting an issue. 


**SendMessageDelay:** 


Notes the time in milliseconds to wait between each data sent to Kitchen.  This is set to zero by default and is only applicable to UDP communications.


**CaptureData:**  


Specifies whether or not a QsrSock capture file is created.  Default is set to False. 


To enable data capture change the value to ‘True’ this will capture data in the QSRSock\Log\QsrSock.qsrcap file.  This will be archived each time the Qsrposi.dll is initialized.  Archived files will be saved for seven days.


**QsrockWebServiceClient: **


Determines whether or not the QSR Web Service HTTP/TCP Interface is enabled.  Setting this to ‘True’ sends only HTTP data.


A new tag was added to the QsrSockWebServiceClient providing the ability to queue messages when QsrPosi cannot connect to the Kitchen Server.


**MessageTimeoutSeconds: **


Must be configured and have a value greater than zero.  If this is not added or is configured with a value of zero, QsrPosi will not queue any messages when the connection to KitchenServer is broken.  This functionality can only be used with HTTP/TCP communication QsrSockWebServiceClient must be Enabled and the value set to true with a minimum time in seconds added. 


**Server Port:  **


Must match the listening port configured in ConnectSmart Kitchen.  The Default port is set to 8000 and is auto configured starting in CSK 5.


**Server:**  


Must be configured as the primary server.  The entire line can be copied to add a secondary server if needed. 


# Control Point TCP Only]


Devices on the network can talk to a specific IP address across multiple VLAN’s by adding a ConnectSmartNetwork.xml to the device agent folder on the device itself.  Ideally this would be staged in advance via a UDP broadcast using the IP address of the Control Point Server before sending to the location.


If the equipment is already on site with the network in place, load the TCP Only Tool on a computer (or POS Terminal) on the same VLAN as the devices to simulate the UDP environment. 


Be sure any firewalls on the Computer or Terminal are turned off during this process and that ports 32768 for configuration AND port 32888 for TCP use are set to open.


The Control Point TCP utility only will place a ConnectSmartNetwork.xml on the device as they are turned on and configured. 


Follow the steps below to begin the configuration. 


## Staging the devices]


Install the Control Point TCP Only Configuration utility on the computer or terminal on the same VLan as the devices. 


Launch the utility. 


Select Settings


Select Add, name the profile and assign the Control Point Server IP address.


**Note**: Name the profile something that means something to the location receiving the device for future reference.


 


After adding the network information select the profile you wish to Activate in the location.    


Turn on the first Device.  The device will appear in the Devices list.


Select the device and use the Configure option . 


When configured the Events section will reflect the time stamp and details that were sent to the device.


If there are multiple devices that will need to broadcast TCP to the same Control Point Server, continue the process and wait for each device to display and repeat steps.     


To verify the device will make a direct TCP connection to Control Point connect to a monitor and mouse and verify there is a ConnectSmartNetwork.xml file on the device in the Device Agent Folder.  This will vary based on the device being used. 


OR when the device is connected to the network where Control Point is living, use Control Point Client to confirm the ConnectSmartNetwork.xml is in the same folder as the Device Agent.


Logging for both Control Point and ConnectSmart Kitchen will also reflect that the broadcast is being received in TCP.