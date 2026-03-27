---
title: "*|ControlPoint| - Setting up HME-JTech IQ Base Pager System in ControlPoint"
freshdesk_id: 17000069296
category: "Support"
folder: "ControlPoint"
status: published
created: 2018-03-23
updated: 2025-01-17
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000069296
---

# *|ControlPoint| - Setting up HME-JTech IQ Base Pager System in ControlPoint

**HME-JTech IQ Base Pager System**


Connect Base Station to Device (Device should be online in ControlPoint)


Tested with a Serial (RS232) to RJ-45


Tested with Serial (RS232)–to-USB adapter


1. Navigate to Paging and Paging Systems


2. Enter all information


    A. Description:


    B. Type:JTECH - UHF


    C. Base Code: 80


    D. Allow incoming messages from this system: Disabled


3. Click on Pagers and Add


    A. Pager ID: X


    B. Type: Courtesy


    C. Baud: 512


    D. Data Inversion: Disabled


4. Edit the device the base station is connected to in ControlPoint


    A. Click on Peripherals


    B. Under Paging Systems Click Add


    C. Enter all Information


        -Paging System:


        -Port: Verify port using Windows Device Manager on the device


        -Baud: 1200


        -Data Bits: 8


        -Parity: None


        -Stop Bits: 1


        -Hardware Handshaking: None


5. Navigate to Pagers and Paging Diagnostics


    A. Enter  Pager ID and Hit Page


    B. Verify Pager Vibrates