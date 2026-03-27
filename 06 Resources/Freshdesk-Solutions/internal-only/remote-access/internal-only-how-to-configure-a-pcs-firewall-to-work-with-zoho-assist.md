---
title: "*|Internal Only| - How to configure a PC's firewall to work with Zoho Assist"
freshdesk_id: 17000129474
category: "Internal Only"
folder: "Remote Access"
status: published
created: 2022-11-10
updated: 2024-09-16
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000129474
---

# *|Internal Only| - How to configure a PC's firewall to work with Zoho Assist

** **


**How do I configure a firewall to work with Zoho Assist?**


 


Ensure the following to make Zoho Assist work beyond the system firewalls,


1.    Exclude Domains in the firewall and proxy settings.


2.    Allow certain Ports in the firewall settings


3.    Include executable files or exclude directories in the firewall and anti-virus settings.


 


**Domains**


 


Exclude TCP and Web Socket protocols for the following domains from your firewall and proxy settings


•    *.zoho.com


•    *.zoho.eu


•    *.zoho.in


•    *.zohoassist.com


•    *.zohoassist.eu 


•    *.zohoassist.in


•    *.zoho.com.au


•    *.zoho.com.cn


•    [dms.zoho.com]


 


**Ports**


 


Allow the following ports in your firewall settings


•    TCP and WebSocket ports 443 and 80


 


**Executable Files**


 


Configure your firewall and anti-virus settings to allow the following executables


•    ZA_Upgrader


•    agent.exe


•    ZMAgent.exe


•    ZohoURSService.exe


•    ZohoMeeting.exe


•    ZohoTray.exe


•    ZohoURS.exe


 


**( or )**


**Directories**


 


Exclude the following directories from your firewall and anti-virus settings


•    32 bit OS - %localappdata%/zohomeeting/, %programfiles%/ZohoMeeting 


•    64 bit OS - %localappdata%/zohomeeting/, %programfiles(x86)%/ZohoMeeting