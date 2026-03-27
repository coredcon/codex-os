---
title: "*|ControlPoint| - LRS table locator Setup Guide"
freshdesk_id: 17000069303
category: "Support"
folder: "ControlPoint"
status: published
created: 2018-03-23
updated: 2022-12-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000069303
---

# *|ControlPoint| - LRS table locator Setup Guide

Setup your LRS Table Tracker (Link for setup instructions: [Setting-Up Your Table Tracker System – Long Range Systems, LLC])


1. Launch ControlPoint Server and ControlPoint Client.


2. Navigate to Pagers>Table Locator


3. Click on Locator Gateway


    -Id = 1


    -IP Address: The Gateway’s address


    To verify Gateway IP: Launch the TableTracker App on the iPad and check the settings.


4. Click on Global Settings Table Locator.


5. System Type>LRS Table Tracker.


6. Enter the Gateway API Key.


    -Hit Apply and Save.


7. Launch Table Tracker Diagnostics and begin testing Table Tracker.


       -Verify Start, Page and Clear work in Diagnostics.


8. Verify the Physical Start and Clear Pads work.


9. Verify that ControlPoint is communicating with the iPad. Once a table is cleared from Diagnostics


               That is also cleared on the iPad. Verify that the Page command sent from the iPad works.


10. Once all communication has been determined to be working. Send an order from the POS make


               sure to only send the tag number. Table and Pager number must be included in the table header.


11. Place the Tracker on any of the Docks, Mats, or RFID Tags. Verify the table number is updated on       


               the Kitchen Screen, iPad and Diagnostics.


12. Move the Tracker to another Dock, Mat, or RFID Tag. Verify the table number has been updated


               on the Kitchen Screen, iPad and Diagnostics.


13. Page the Tracker using the iPad and Diagnostics. Verify the Tracker is paged.


14. Clear the Tracker using the Clear Pad and Diagnostics.