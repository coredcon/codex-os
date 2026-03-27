---
title: "|Hardware| - Kitchen Armor AIO Device Boot Loop When Connected to PoE"
freshdesk_id: 17000146908
category: "Support"
folder: "Hardware"
status: published
created: 2025-06-18
updated: 2025-06-18
views: 0
tags: ["LLDP"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000146908
---

# |Hardware| - Kitchen Armor AIO Device Boot Loop When Connected to PoE

# **Issue**


This article addresses a known issue where Kitchen Armor AIO devices experience a continuous boot loop **when connected via Power over Ethernet (PoE)**. The same devices operate normally **when powered using a standard power cord**.

---

## **Background**


This issue most commonly occurs after upgrading Kitchen Armor AIO devices from **Android 7 to Android 10**, particularly when **DeviceAgent** is installed alongside **DisplayClient**.


Devices previously operating with Android 7 and only the Display Client consumed slightly less power than the upgraded Android 10 configuration with both DisplayClient and DeviceAgent.

---

## **Cause**


The issue is typically related to **insufficient power delivery via PoE**, often due to the **LLDP (Link Layer Discovery Protocol)** behavior on the connected PoE switch.


Here’s how it happens:


- 

**Initial Power Classification**:
When a device connects to a PoE switch, the switch performs a physical layer classification to determine how much power the device requires.


- 

**Kitchen Armor AIO devices** correctly identify as **Class 4 devices**, requiring **30W** of power (802.3at standard).


- 

**LLDP Negotiation**:
After the initial classification, the switch may use LLDP to further validate the power requirements at the data link layer.


- 

If the device does not respond to the LLDP query (as is the case with Kitchen Armor devices), the switch **defaults to the minimum power level** defined by the physical classification—**15.4W (802.3af)**.


- 

**Power Demand and Boot Loop**:
Kitchen Armor devices typically consume between **11W to 17W**, with occasional peaks up to **20W**.


- 

While this is manageable with 30W power (802.3at), it **exceeds the 15.4W limit** of 802.3af.


- 

As a result, the device **fails to maintain stable operation**, leading to a **boot loop**.


---

## **Solution**


To resolve this issue:


- 

**Disable LLDP** on the PoE switch, if possible. This prevents the switch from reducing power after the initial classification.


- 

Alternatively, **manually configure the PoE port** on the switch to always supply 30W (802.3at), bypassing LLDP-based negotiation.


- 

If neither of the above is feasible, continue powering the device using a standard power cord to ensure sufficient power delivery.


##