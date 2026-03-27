---
title: "*|Hardware| - Editing/Resetting DeviceAgent Settings on a QSR Android Device"
freshdesk_id: 17000137168
category: "Support"
folder: "Hardware"
status: published
created: 2023-10-18
updated: 2025-09-10
views: 0
tags: ["elo backpack", "backpack"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000137168
---

# *|Hardware| - Editing/Resetting DeviceAgent Settings on a QSR Android Device

Starting with ControlPoint 2023.4.6, the bundled version of DeviceAgent for Android (DeviceAgent 2023.4.5) includes a tool to allow the resetting and editing of the DeviceAgent Settings for IP Address, Default Gateway, and Network Prefix Length directly on the device itself.

This is useful when you are having difficulty getting the device to be seen by ControlPoint on your network.


- Power on the Device


- Select the DA icon on the bottom right of the screen


- Select the icon on the bottom right that looks like a radio tower


- From here you can reset the device to DHCP or manually define the IP, Gateway, Subnet Mask and primary DNS (older versions may ask for Network Prefix Length (standard is 24))


Static:


DHCP:


- Click the Save button


- The device should reboot and now be visible in ControlPoint to be assigned.