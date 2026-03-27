---
title: "|Hardware| - Pairing a New KP-9000 to an existing Dongle"
freshdesk_id: 17000147626
category: "Support"
folder: "Hardware"
status: draft
created: 2025-08-07
updated: 2025-08-08
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000147626
---

# |Hardware| - Pairing a New KP-9000 to an existing Dongle

** **


**Purpose:**
This article provides guidance for pairing a new keypad with an existing dongle when replacing a previous keypad on a device that lacks built-in Bluetooth functionality.


**Pairing Instructions:**


- Remove and Reconnect the existing dongle to the device.

- Observe the LED indicator on the dongle:

- A slow blinking light indicates the dongle is searching for the previously paired keypad.

- If the previous keypad is not detected within approximately one minute, the dongle will enter pairing mode automatically, indicated by a rapid blinking light.


- Once the dongle is in pairing mode, put the new keypad into pairing

- Hold the KP-90000 (prepared with batteries installed) so that the light is in the upper left corner.

- Press and hold both top left key and bottom right key simultaneously for 3 seconds.

- The LED will quickly blink on and off in amber while it is trying to pair to the dongle.

- Once paired with the dongle, the light on the _keypad_ will blink green briefly and then remain quiet.


- Once the keypad pairing is complete, the light on the _dongle_ will stay solid blue.


## Keypad LED


There is one LED visible in the upper left portion of the keypad. The following table describes what the different LED messages are conveying.


 


**Mode**


**LED**


**Description**


Unpaired


No LED


The default when not paired with a dongle. Special keypress (upper left and bottom right keys for 3s) required to enter pairing mode. Unpaired is the mode for factory storage and shipping. Keypad will shut ‘off’ in this state, using the lowest power


consumption possible with batteries installed.


 


**Mode**


**LED**


**Description**


Searching


Blinking low-duty Amber (Amber also on very low-duty cycle for low battery)


Dongle has been previously paired but is not currently found. The keypad will search indefinitely in an attempt to reconnect.


However, it will only search 1 minute at high speed (10Hz) before dropping back to power savings (1Hz). Special keypress can force into pairing mode. In BLE terms, a keypad ‘Searching’ means sending only


directed advertisements to the address of its paired dongle.


 


Connected


Solid Green for one second (Also blinks Green on each key press or SCROLL LOCK)


Normal operating behavior with paired dongle found and communicating. Wireless poll period and slave latency depend on whether beeper is enabled (power savings are greater when in its default state – beeper disabled). Special keypress can


force into pairing mode.


Pairing


Blinking Amber once every 10 seconds until paired


Allows pairing with a new dongle. Requires special keypress to enter. It has a 1-minute timeout, as pairing consumes high power to advertise. Keypad will auto-pair to first dongle found in pairing mode. If timeout is reached, behavior depends on whether it was previously paired to a dongle. In BLE terms, ‘Pairing’ means sending undirected advertisements.


Low Battery


Double blinking Amber every 10 seconds


 

## 


## Dongle LED


There are two LEDs visible, one on either side of the dongle. The following table describes what the different LED messages are conveying.


 


**Mode**


**LEDs**


**Description**


Unpaired


Off


Only entered when not paired and when software


has commanded dongle to not auto pair.


Searching


Slow Blinking Blue


Keypad has been previously paired, but is not currently found. Dongle will search for 1 minute to attempt to reconnect. Afterward, it will automatically enter pairing mode. Software commands can override this behavior. In BLE terms, ‘Searching’ on the dongle means passive


scanning for only directed advertisements from its paired keypad.


 


**Mode**


**LEDs**


**Description**


Connected


Solid Blue


Normal operating behavior with paired keypad found and communicating. In BLE terms,


‘Connected’ here means connected and bonded.


Pairing


Rapid Blinking (low duty) Blue


Allows pairing with a new keypad. If previously paired, the dongle will still auto-connect with that keypad if found (same as searching). If a new keypad in pairing mode is found, a new pairing (and connection) is established with that keypad. Other keypads not in pairing mode are ignored. In BLE terms, ‘Pairing’ means active scanning for advertisements from any keypad, but also


accepting directed advertisements from its paired keypad.


 

# Troubleshooting

## What Does This Light Mean?


Dongle


 


**If the light is…**


**This means…**


**What next…**


Off


Unpaired


Pair with keypad.


Slow blinking blue


Searching


Dongle will attempt to reconnect.


Solid blue


Connected


The device is ready to go!


Rapid blinking blue


Pairing


Dongle is pairing with keypad.


 


Keypad


 


**If the light is…**


**This means…**


**What next…**


Off


Unpaired


Pair with dongle.


Blinking low-duty amber


Searching


Keypad will attempt to reconnect.


Blinking low-duty green


Connected


The device is ready to go!


Rapid blinking amber


Pairing


Keypad is pairing with dongle.