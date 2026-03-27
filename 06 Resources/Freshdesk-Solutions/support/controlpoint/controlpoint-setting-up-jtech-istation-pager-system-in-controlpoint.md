---
title: "*|ControlPoint| - Setting Up JTECH IStation Pager System in ControlPoint"
freshdesk_id: 17000144390
category: "Support"
folder: "ControlPoint"
status: published
created: 2025-01-17
updated: 2026-03-18
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000144390
---

# *|ControlPoint| - Setting Up JTECH IStation Pager System in ControlPoint

**HME-JTech ISTATION V1 Base Pager System**


 


Connect Base Station to Device (Device should be online in ControlPoint)


 


Tested with a Serial (RS232) to RJ-45


Tested with Serial (RS232)–to-USB adapter


 


1. Navigate to Paging and Paging Systems


2. Enter all information


    A. Description:


    B. Type: HME Wireless


    C. Base Code:  This will match the Base ID displayed by the IStation During Startup


    D. Allow incoming messages from this system: Disabled


 


 


 


3. Click on Pagers and Add


    A. Pager ID: X


    B. Type: Courtesy


    C. Baud: 1200


    D. Data Inversion: Disabled


 


4. Edit the device the base station is connected to in ControlPoint


    A. Click on Peripherals


    B. Under Paging Systems Click Add


    C. Enter all Information


        -Paging System:


        -Port: Verify port using Windows Device Manager on the device


        -Baud: 9600


        -Data Bits: 8


        -Parity: None


        -Stop Bits: 1


        -Hardware Handshaking: None (Sometimes CTS. If in doubt see what methods are flagged in diagnostic mode)


 


5. Navigate to Pagers and Paging Diagnostics


    A. Enter  Pager ID and Hit Page


    B. Verify Pager Vibrates


NOTE:

You will also want to ensure that USB Selective Suspend is disabled in the power settings for the device connected to the IStation to prevent the port from being shut down hen idle.


Navigate to Settings>Power & Sleep>


 additional power settings


Choose Change Plan settings for the active plan


Select Change advanced power settings


Expand the USB settings and make sure USB selective suspend is set to disabled