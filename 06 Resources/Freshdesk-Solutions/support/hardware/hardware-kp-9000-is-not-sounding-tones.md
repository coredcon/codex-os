---
title: "*|Hardware| - KP-9000 Is not sounding tones"
freshdesk_id: 17000069243
category: "Support"
folder: "Hardware"
status: published
created: 2018-03-22
updated: 2022-06-15
views: 0
tags: ["KP-9000", "Beep", "Tone"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000069243
---

# *|Hardware| - KP-9000 Is not sounding tones

If you have a situation where a KP-9000 wireless keypad is not sounding tones as expected, you first want to verify the settings in ControlPoint Diagnostics:


Go into Bump Bar diagnostics in ControlPoint and hit the “Get Settings” button. That will show you the keypad’s internal settings, including whether or not it’s configured to beep on scroll lock and/or key press. 


When beep on scroll lock is set to false, that prevents the keypad from sounding tones based on Kitchen actions. 


**Updating the Keypad settings**


In ControlPoint Client, hit the Bump Bars button to open keypad templates:


On the Bump Bars popup, hit the Add button to create a new template, or select an existing one and hit Edit:


On the Bump Bar template form, give the template a name and select the type of keypad – be sure to select KP-9000 for the wireless keypads, because that triggers the “sound tone on key press” and “sound tone on scroll lock” options to appear:


****


Check either/both of the tone options and hit Apply to save, or Save to save and close the form.


Once that’s done, go back to ControlPoint Client and select the device to which the keypad will be connected, and hit Edit Device. On the Edit Device form, go to the Peripherals tab. On the Bump Bar dropdown menu, select the keypad template you just edited/created:


Hit Save to save and close the Edit Device form.


Make sure the keypad and dongle are plugged into the device and paired. From ControlPoint Client, select the keypad’s device and hit Diagnostics. Go to the Bump Bar tab and hit Program to apply the settings in the keypad template to the keypad itself.


A popup will open asking if you’re sure; click Yes to continue and you’ll get a brief message in the Output screen to let you know whether or not the programming was successful. Then you’re (finally) done changing the keypad settings. You can use the Get Status button to confirm the new settings match the template, and you can also go back to the Basic tab in Diagnostics and hit the Sound Tone button to confirm the keypad will sound a tone on scroll lock.