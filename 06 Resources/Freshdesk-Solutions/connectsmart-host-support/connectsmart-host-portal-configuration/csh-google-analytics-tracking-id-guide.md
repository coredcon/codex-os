---
title: "*|CSH| - Google Analytics Tracking ID Guide"
freshdesk_id: 17000119297
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host Portal / Configuration"
status: published
created: 2021-09-01
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000119297
---

# *|CSH| - Google Analytics Tracking ID Guide

This setting is found in the Host Portal > Concepts > Browser Widget > General Settings > Google Analytics Tracking ID. Portal Users can insert their ID provided by Google in the field marked in the below image.  The Google Analytics Tracking ID allows restaurants to grasp how many site visitors actually make a reservation or get in line.


As we know there are two versions of the Browser Widget: the Standard and Compact widget. Both have Page Tracking. However, as for events, only the Compact uses those. The events available in Compact are "Load" and "Click." Granted, these events are only applicable in two areas of the application: Compact Reservation and Compact WaitList.


So, when a user navigates to either Compact Widget (Reservation or Waitlist), the "Load" event fires with eventCategory (BrowserWidget), eventAction (Load), and eventLabel (reservation/waitlist, depending on Widget in use).


As for the "Click" event, this only fires when the Go button on either Compact Reservation or Compact WaitList is clicked/pressed, sending over eventCategory (BrowserWidget), eventAction (Click), and eventLabel (reservation/waitlist, depending on Widget in use).


In both instances, the Google Analytics ID will only be represented on the main webpage that the widget is hosted on. When, in the compact widget's case, the user is redirected to the QSR widget webpage, the GA ID will not show up in a Google Tag Assistant.