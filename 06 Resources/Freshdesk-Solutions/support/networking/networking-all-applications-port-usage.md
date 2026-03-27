---
title: "*|Networking| - All Applications Port Usage"
freshdesk_id: 17000069515
category: "Support"
folder: "Networking"
status: published
created: 2018-03-29
updated: 2022-11-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000069515
---

# *|Networking| - All Applications Port Usage

Attached is the All Applications Port Usage spreadsheet you can send to customers.


Below are the most common tables from that spreadsheet for your ease of use.


# Controlpoint

Protocol
Name
Base Port Offset
Port Used
Description
UDP
Broadcast Discovery Port
0x7000
28672
Port Device Agent listens for discovery messages from the ControlPoint server
UDP
Broadcast Discovery Port
0x7001
28673
Port ControlPoint Server listens on for discovery messages from Device Agent.


TCP
ControlPointClientPortOffset
110
32878
Used by ControlPoint client to listen for events sent by ControlPoint server (Service Port)
TCP
ControlPointServerPortOffset
111
32879
Used by ControlPoint server to listen for requests coming from ControlPoint client (Service Port)
TCP
ControlPointDevicePortOffset  
112
32880
Used by for communication between DeviceAgent and ControlPoint Server
TCP
ControlPointServerSynchronizationPortOffset
113
32881
Used by ControlPoint server to synchronize the primary and secondary instances.
UDP
ControlPointServerPrimaryDiscoveryPortOffset      
114
32882
Used by ControlPoint udp discovery to find the Primary server instance in redundant configurations
UDP
ControlPointServerSecondaryDiscoveryPortOffset    
115
32883
Used by ControlPoint udp discovery to find the Secondary server instance in redundant configurations
TCP
ControlPoint API Port
120
32888
Used by DineTime and KitchenServer 5/6 to send print and page requests to ControlPoint.


# CSK 5/6/7

Protocol
Name
Base Port Offset
Port Used
Description
TCP
General
0
32768
All Kitchen traffic used port configured through ConnectSmart Network Configuration
UDP
Legacy POS Inbound traffic
0
32768
UDP Listener that supports QsrSock style interfaces that cannot utilize TCP via newer versions of the QSRSock.dll
UDP
Legacy RDS Inbound traffic
0
33536
Only valid when RDS stations are configured in KitchenServer
UDP
Legacy RDS Outbound traffic
0
33537
Only valid when RDS stations are configured in KitchenServer
HTTPS
Enterprise Communication
0
443
Outbound HTTPS communication to enterprise services