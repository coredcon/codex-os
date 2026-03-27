---
title: "*|Connect Applications| - Create the QSR MicrosTSConnect Service "
freshdesk_id: 17000064627
category: "Support"
folder: "Connect Applications"
status: published
created: 2017-12-20
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000064627
---

# *|Connect Applications| - Create the QSR MicrosTSConnect Service 

Configuration:


The MicrosTsConnect executable should be placed in the following folder:


C:\ProgramData\QSR Automations\MicrosTSConnect\Bin


Run the following command in Command Prompt:


sc create "QSR MicrosTSConnect" binpath= "C:\ProgramData\QSR Automations\MicrosTSConnect\Bin\MicrosTSConnect.exe"