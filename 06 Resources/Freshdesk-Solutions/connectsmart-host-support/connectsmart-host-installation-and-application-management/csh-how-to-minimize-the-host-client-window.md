---
title: "*|CSH| - How to Minimize the Host Client Window"
freshdesk_id: 17000129538
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host - Installation and Application Management"
status: published
created: 2022-11-11
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000129538
---

# *|CSH| - How to Minimize the Host Client Window

## Goal/Desired Behavior:


The client would like the Host client to start in a windowed mode as opposed to the default maximized


## Steps:


- Navigate to the HostessClientSettings.xml file in the following path:

- C:\ProgramData\QSR Automations\ConnectSmart\HostessClient\Configuration

- Right Click to edit the XML


- 

- Change the Maximized value to "False" as shown above and then save the file. 

- The next time you open the Host Client, the window will not be full screen.