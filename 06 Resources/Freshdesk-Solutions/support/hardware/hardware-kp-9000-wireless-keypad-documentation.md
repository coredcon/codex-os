---
title: "*|Hardware| - KP-9000 Wireless Keypad Documentation"
freshdesk_id: 17000049676
category: "Support"
folder: "Hardware"
status: published
created: 2017-04-26
updated: 2023-11-30
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000049676
---

# *|Hardware| - KP-9000 Wireless Keypad Documentation

#  ]

# KP-9000 Wireless Keypad


** **


** **


**User’s Guide Documentation**


(vs 1.3 March 1, 2018)


** **

# Functional User’s Guide


The KP-9000 is a low-power, longer life, wireless keypad that is backward compatible with QSR’s other keypads, does not require any cabling at all, and can be configured and managed using QSR’s ControlPoint management tool.

## Specifications]


**              Feature**
**                                       Specification**
Input
10x2, 20-Key Membrane
Key Rating
30 Million pushes
Mounting Options
Removable Rubber Feet for Table-Toip or Wall Mounting
Several Bracketing Options Available
Overlay Options
Customizable and Removable Keypad Overlays, Installs without Tools
Features
Wireless Operation
Software Programmable Scan Codes
Adjustable Sound for Frequency and Volume
Downloadable Firmware for Easy Updates and Support
ConnectSmart ControlPoint Supported
Chasis
Durable, Premium Grade Polycarbonate
Metal reinforced Membrane for Extended Life
Resistant to Extreme Temperatures, Water, and Grease
Dimensions

1.25” x 8.25” x 2.75” (H x W x D)
Weight

10.4 ounces
Power
Keypad Powered by 6-AAA Alkaline Batteries
Dongle Powered by Controller’s USB Port
Battery Life
Dependent on Brand, Usage, and Environment – Over One Year
Audio
Selectable onboard Annuniator
Interface
Max Distance
Bluetooth Low Energy using QSR BLE Dongle
30 Feet in Direct Line-of-Site
Environmental

Operating Temperature

     0° – 50° Celsius
Storage Temperature

 -20° – 95° Celsius
Humidity

10% - 95%, non-condensing

Altitude

15,000 feet

Certifications

FCC Part 15, Class A, EN55024, WEEE, CE, EU RoHS, China RoHS, MIC
Warranty

Limited 3-Year Hardware Warranty


## Batteries and Installation]


The KP-9000 operates using 6-AAA alkaline batteries.  They must be placed exactly as shown in the diagram below in order to power the keypad.  Simply unscrew the four screws on the bottom of the keypad and remove the bottom cover. Place the new batteries as shown.  The battery receptacles are purposely stiff, to prevent any shifting during use.  It may be necessary to gently use a flathead screwdriver to lift each old battery out of its holder.


Though the keypad will take full advantage of 6-AAA batteries for a longer life of the keypad deployed in a restaurant, the KP-9000 has also been designed to fully operate with only pairs of batteries installed.   That means if any single contiguous pair of batteries are installed, the keypad will work properly.  Without a full set of batteries, though, it will just mean that the keypad will operate fully for a shorter period of time.  But this also provides a short term fix in case the keypad is needed right now but there aren’t enough batteries to go around.


## Pairing Keypad and Dongle]


The KP-9000 is a Bluetooth Low-Energy (BLE) wireless keypad.  As such, it needs a method of communication with QSR’s controllers.  In order to provide the communication and control to QSR’s controllers, a QSR BLE dongle must be used in conjunction with the keypad (these items are shipping together in pairs).


Communication and pairing were implemented in such a way to provide the simplest method without requiring additional considerations to complete.  That means:


The pairing method can accommodate both initial installation and field replacement of keypads.


It does not require the use of ControlPoint or other QSR software.


No physical access to the controller is necessary, other than initially inserting the dongle in a USB port


It does not require a keyboard, mouse, or touchscreen on controller, either.


To pair a keypad with a dongle,


Make sure the dongle is inserted in the USB port of the target controller.


Turn the controller on.


Hold the KP-9000 (prepared with batteries installed) so that the LED is in the upper left corner.


Press and hold the top left most key with the bottom right most key simultaneously for 5 seconds.


The LED will quickly blink on and off in amber while it is trying to talk to the dongle.


If it establishes the pairing with the dongle, it will blink green briefly and then remain quiet.


The LED will now only light in response to a keypress, but the keypad should now be communicating with the dongle/controller.


Note that the keypad will initially ship with a dongle that is pre-paired in production.  That means that a customer need only plug in the dongle and install the batteries in the accompanying keypad and pairing will happen automatically!


Following this successful pairing, and given tho**s**e restraints listed above, the pairing scenarios will work as follows:


- If a dongle has already been paired with a keypad, and that keypad is available, the dongle will talk only to it and will not attempt to pair with any new keypad.


- If a dongle has not been paired with a keypad, or its paired keypad has been unavailable for 1 minute (by default), the dongle will enter pairing mode.

- Holding two specific keys (far upper left and far bottom right) on the keypad simultaneously for 5 seconds will put keypad in pairing mode.

- A keypad will never attempt to automatically enter pairing mode, even if it is unpaired or its paired dongle is unavailable. This helps prevent accidental re-pairing in case connection to dongle is temporarily lost. This also helps conserve the batteries since pairing mode consumes more power.

- A keypad will also automatically exit pairing mode after 1 minute, also to minimize battery usage and to minimize risk of multiple keypads simultaneously in pairing mode.

- If a dongle and keypad are both in pairing mode, they will pair with each other.

- The pairing is 'first come, first served', so there is some risk of ambiguity if multiple dongles or multiple keypads are in pairing mode at the same time.  This scheme should be normally robust against accidentally getting in such cases.

- Avoiding multiple keypads in pairing mode is easy due to the special keypress required on each keypad, and a timeout which will exit pairing mode.

- Avoiding multiple dongles should be easy in normal operation, but not on initial site install.  It will be necessary to have an initial setup plan where only one dongle is plugged in and paired at a time for a new site.

- If a dongle enters pairing mode but the keypad it was paired with comes back, it immediately just resumes connected communication, no longer in pairing mode.

- The dongle has a hold-off period of 1 minute after pairing where it will not automatically attempt to pair again.

- The dongle supports additional proprietary commands over USB which can override default pairing timeout, forget a pairing, or directly enter or leave pairing mode (this will be ControlPoint functionality).


Replacement Option 1: Site with QSR ControlPoint software


- Each dongle and keypad is paired and labeled on site or in staging.

- QSR server commands software on each QSR controller to disable auto-pairing on dongles.

- When a keypad needs to be replaced, ControlPoint commands the dongle on the appropriate controller to enter pairing mode. The new keypad enters pairing mode via special keypress.

- A QSR site running this way should not be vulnerable to ambiguous pairing since no more than one dongle should ever enter pairing mode at one time.


Replacement Option 2: Site without QSR software:


- Each dongle and keypad is paired and labeled on site or in staging.

- When a keypad needs to be replaced, the dongle will auto enter pairing mode one minute after communication loss with old keypad.

- The new keypad then enters pairing mode via special keypress, and pairs with dongle.

- There is some potential for ambiguous pairing if a keypad enters pairing mode when multiple dongles have lost communication.

- Above mentioned safeguards should help avoid or recover from this by attempting re-pairing, but this is necessarily not as robust as a site with QSR software.


## LED Indicators]


There is one LED visible on the side of the dongle.  This LED will light in blue and will do so with a combination of steady-on, to blinking depending on what is being communicated.  The following table describes what the different LED messages are conveying.


**Dongle LED**


Mode


LEDs


Can change to


Description


Unpaired


Off
Pairing – via software command
Unpaired state only entered when not paired and when software has commanded dongle to not auto-pair.


Searching


Slow Blinking Blue
Connected – if paired keypad found
Pairing – via software command, or 1 minute timeout
Searching means a keypad has been previously paired but is not currently found. Dongle will search for 1 minute to attempt to reconnect. After this it will automatically enter pairing mode. Software commands can override this behavior. In BLE terms, ‘Searching’ on the dongle means passive scanning for only directed advertisements from its paired keypad.


Connected


Solid Blue
Searching – if connection to paired keypad is lost
Pairing – via software command
Connected is normal operating behavior with paired keypad found and communicating. In BLE terms, ‘Connected’ here means connected and bonded.


Pairing


Rapid Blinking (low duty) Blue
Connected – if previously paired keypad is found, or new keypad is paired
Unpaired – via software command
Pairing allows pairing with a new keypad. If previously paired, the dongle will still auto-connect with that keypad if found (same as searching).  If a new keypad in pairing mode is found, a new pairing (and connection) is established with that keypad.  Other keypads not in pairing mode are ignored.  In BLE terms, ‘Pairing’ means active scanning for advertisements from any keypad, but also accepting directed advertisements from its paired keypad.


There is one LED visible in the upper left portion of the keypad.  This LED can light in amber or green and will do so with a combination of steady-on to blinking, depending on what is being communicated.  The following table describes what the different LED messages are conveying.


**Keypad LED**


Mode


LEDs


Can change to


Description


Unpaired


No LEDs
Pairing – via special keypress
Unpaired state is the default when not paired with a dongle. Special keypress (upper left and bottom right keys for 3s) required to enter pairing mode.  Unpaired is the mode for factory storage and shipping.  Keypad will shut ‘off’ in this state, with lowest power consumption possible with batteries installed.


Searching
Blinking low-duty Amber (Amber also on very low-duty cycle for low battery)
Connected – if paired dongle found
Pairing – via special keypress
Searching means a dongle has been previously paired but is not currently found. The keypad will search indefinitely to attempt to reconnect. However, it will only search 1 minute at high speed (10Hz) before dropping back to power savings (1Hz). Special keypress can always force it to pairing. In BLE terms, a keypad ‘Searching’ means sending only directed advertisements to the address of its paired dongle.


Connected
Blinking low-duty Green (Green also on key presses or SCROLLLOCK). NOTE – will turn off after a few seconds for power savings
Searching – if connection to paired dongle is lost
Pairing – via special keypress
Connected is normal operating behavior with paired dongle found and communicating. Wireless poll period and slave latency depend on whether beeper is enabled (more power savings with beeper disabled – its default state). Special keypress can force to pairing mode.


Pairing
Rapid-blinking Amber
Connected – if new dongle is paired
Unpaired – after 1 minute timeout if no dongle is paired
Searching – after 1 minute timeout if dongle was previously paired
Pairing allows pairing with a new dongle.  Requires special keypress to enter.  As pairing consumes high power to advertise, it has a 1 minute timeout.  Keypad will auto-pair to first dongle found in pairing mode.  If timeout is reached, behavior depends on if it was previously paired to a dongle or not. In BLE terms, ‘Pairing’ means sending undirected advertisements.

## Power Savings]


Although the KP-9000 is a highly efficient low energy wireless device, users may want to consider a few things in extending the life of the battery sets installed.


- Beeps – The KP-9000 can be configured to beep on a keypress for feedback.  It can also be set to provide an announcement beep, such as when an order first appears at a prep station.  However, battery life can be extended substantially by turning off the beep (setting the volume to 0) altogether.  Button press feedback will still be apparent because the green LED will light on each press.  If sound is necessary, that can be readily provided by a speaker add-on on the video monitors.  Exercising a beep through the onboard keypad piezos is the source of one of the highest power drains and should be avoided for long battery life.  Beep, by default, is factory set to Off.

- Sleep Mode – one significant power drain to be aware of is those cases where a restaurant habitually powers off their controllers at night.  If that is being done, a keypad could lose 50% of its battery life because it will be continually searching for its paired dongle.  If this is the case, the keypad should be set to Sleep Mode so that it will stop looking after 5 minutes of no communication.  It will then wake back up upon the first keypress (which will be a throw-away key).

- In the case where one is looking for additional power savings, turning the controllers off and using Sleep Mode will yield an approximate additional 10% battery life, if done as a consistent daily habit.

- Make sure all of the batteries are oriented correctly in their mounts.  Because the keypad will operate with just two batteries installed correctly, it is possible for improperly installed batteries to go unnoticed.  Also, keep in mind that all batteries are not alike.  A good quality battery will go a long way to extending the amount of time needed before having to open the keypad back up for replacement.

- Battery power drain can be effected by temperature.  The higher the temperature the greater the power drain.  So, consider heat when locating the KP-9000 in the kitchen.

## Configuration through ControlPoint]


ControlPoint will be able to report on status information and provide certain controls to the BLE keypad.


- Sytem status

- Firmware version

- Battery status – this will provide and indication of the general battery state.  It is not highly accurate because of the way batteries actually work (non-linear power drain).  But the system can accurately tell you when you are down to a quarter of the power available and should be prepared in the near future for replacement.

- Beep enable/disable on keypress – remember that beeping is power expensive and should be avoided if possible.  The keypad LED will reflect keypresses, as well.

- Beep enable/disable on Scrolllock - – remember that beeping is power expensive and should be avoided if possible. (see **Configuration through ControlPoint (continued) **_‘Enable beep on scroll lock’ _below)

- Get/Set Beep volume

- Get/Set Beep frequency

- Scan code table updates  - configurable scan codes can be downloaded to the keypad.

- Scan code table selection

- Auto-pairing enable/disable

- Force unpair

- Forcing into pairing mode

## Configuration through ControlPoint (continued)


_Enable beep on scroll lock (beep on new order)_


In ControlPoint Client, hit the Bump Bars button to open keypad templates:


On the Bump Bars popup, hit the Add button to create a new template, or select an existing one and hit Edit:


On the Bump Bar template form, give the template a name and select the type of keypad – be sure to select KP-9000 for the wireless keypads, because that triggers the “sound tone on key press” and “sound tone on scroll lock” options to appear:


Check either/both of the tone options and hit Apply to save, or Save to save and close the form.


Once that’s done, go back to ControlPoint Client and select the device to which the keypad will be connected, and hit Edit Device. On the Edit Device form, go to the Peripherals tab. On the Bump Bar dropdown menu, select the keypad template you just edited/created:


Hit Save to save and close the Edit Device form.


Make sure the keypad and dongle are plugged into the device and paired. From ControlPoint Client, select the keypad’s device and hit Diagnostics. Go to the Bump Bar tab and hit Program to apply the settings in the keypad template to the keypad itself:


A popup will open asking if you’re sure; click Yes to continue and you’ll get a brief message in the Output screen to let you know whether or not the programming was successful. . You can use the Get Status button to confirm the new settings match the template, and you can also go back to the Basic tab in Diagnostics and hit the Sound Tone button to confirm the keypad will sound a tone on scroll lock.

##  ]

## Bluetooth 4.x Adapters


It is possible that the KP-9000 will work with a third party BT4.x adapter.  They will typically have to be running on a Windows 8.1 device or higher.  In addition, although the keypress will properly communicate the accompanying scan codes back to the controller, the communication and control offered through the QSR dongle will not be available.  That means functions such as battery life reporting, scan code updating, Scroll lock beeping, etc. will not work with a third party device and not work with ControlPoint software.


# Artwork]