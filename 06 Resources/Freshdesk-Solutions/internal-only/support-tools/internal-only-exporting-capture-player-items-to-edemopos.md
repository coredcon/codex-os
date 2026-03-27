---
title: "*|Internal Only| - Exporting Capture Player items to eDemoPOS"
freshdesk_id: 17000052365
category: "Internal Only"
folder: "Support Tools"
status: published
created: 2017-05-31
updated: 2023-04-07
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000052365
---

# *|Internal Only| - Exporting Capture Player items to eDemoPOS

In Capture Player version 1.0.114.0 (attached) and later, you have the ability to export from a capture file to a POS Items XML file that can be loaded into eDemoPOS. This is very useful in troubleshooting issues where you'd like to ring up various items, or edit POS items on the fly instead of just replaying a Capture file.


1. Open a capture file in the QSR Capture Player program.


2. Choose File> Export POS Items XML...


3. Browse to the folder where your eDemoPOS data is stored. This will vary based off of your particular setup.


4. Name the file and save it. The formatting of this is important. **The Items database name MUST start with PosItems***** **


Anything else will not be read by eDemoPOS.


5. Now you can open the file in eDemoPOS by going to File>Open POS Items database...


You should now have all of the items and their data that were included in the dataset available to us in eDemoPOS: