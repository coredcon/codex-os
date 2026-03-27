---
title: "*|CSH| - ConnectSmart Host Server - File Paths"
freshdesk_id: 17000061203
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host - Installation and Application Management"
status: published
created: 2017-10-10
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000061203
---

# *|CSH| - ConnectSmart Host Server - File Paths

**Logging:**


**ConnectSmart Host Server **(HostessServer.log):


- File Path - C:\ProgramData\QSR Automations\ConnectSmart\HostessServer\Log


**ConnectSmart Host Client **(HostessClient.log):


- File Path - C:\ProgramData\QSR Automations\ConnectSmart\HostessClient\Log


**ConnectSmart Registration** (DineTimeRegistration.log):


- File Path - C:\ProgramData\QSR Automations\ConnectSmart\Common\Log

---


**Configuration Files:**


**DineTimeEnterprise.xml: **


- Generated when registering ConnectSmart Host, CSK, TeamAssist, etc with Enterprise using the ConnectSmart Registration Tool

- Contains the Enterprise Token that pairs the site with its corresponding instance in Enterprise

- Also used to specify an endpoint when pointing to a different Enterprise stack (Examples: QA, Darden Stack)

- File Path - C:\ProgramData\QSR Automations\ConnectSmart\Common\Data


**GuestviewConfigurationSettings.xml:**


- Contains settings for the GuestView App:

- File Path - C:\ProgramData\QSR Automations\ConnectSmart\GuestView\Configuration