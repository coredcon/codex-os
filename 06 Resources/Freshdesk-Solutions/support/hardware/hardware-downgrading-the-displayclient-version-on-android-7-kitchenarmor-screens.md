---
title: "*|Hardware| - Downgrading the DisplayClient Version On Android 7 KitchenArmor screens"
freshdesk_id: 17000132921
category: "Support"
folder: "Hardware"
status: published
created: 2023-03-28
updated: 2024-11-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000132921
---

# *|Hardware| - Downgrading the DisplayClient Version On Android 7 KitchenArmor screens

This is for use on Kitchen Armor screens that auto upgraded the DisplayClient version due to the option in Kitchen Server still being active.


**Before you do anything else the setting to Auto upgrade DisplayClient for Android needs to be turned off in Kitchen Builder:**


Open the dataset and go to System Settings and navigate to the Display Clients tab.


Uncheck the setting for Android and then press OK to save.


Copy the Dataset to runtime and restart the Kitchen Server service.


**The next step requires manually uninstalling DisplayClient on the device via the Android applications list and then reinstalling the correct version of the APK.**


Swipe up from the bottom to bring up the android navigation bar.


Press the Circle icon to get to the Desktop.


Swipe up again to bring up the application list.


Press and hold on the DisplayClient App and drag it to the uninstall option on the top right (only visible while the app is being held)


You now just need to reinstall the correct APK


The Kitchen Armor All In Ones are currently staged by Kitchen Armor with DisplayClient Version 2.0.42.0


I have attached a copy to this article.