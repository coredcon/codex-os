---
title: "*|CSK| - How to setup and use Socketmon"
freshdesk_id: 17000052481
category: "Support"
folder: "CSK"
status: published
created: 2017-06-01
updated: 2022-06-21
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000052481
---

# *|CSK| - How to setup and use Socketmon

Socketmon monitors a specific port and displays the data coming across when a site is using UDP. In this case we are monitoring the data coming from the POS. 


- Unzip the socketmon tool into a folder on the server machine. It is useful to put a shortcut in the Startup folder so that it automatically runs after any reboot.  Open the program, and choose Properties.


- Set the port to 8000, and IP Address to AnyAddress


- Click on the Logging tab and make sure it is set as below:


- Click Ok.


- Click Disconnect, and then Connect.


This tool will minimize to the system tray and monitor all traffic from POS over port 8000. 


**Viewing Socketmon Logs**


SocketMon logs can be viewed as text files in Notepad. However, the logs can be difficult to discern when viewed in this way. For this reason, QSR Support provides an Excel file to aid in viewing Socketmon data. In order to import the data into Excel, do the following:

1. Open the Socketmon log in Notepad.
2. Select **Edit - Select All****.
**3.   Select **Edit - Copy****.
**4.   Open the QSR Socketmon Header **Spreadsheet** – provided by QSR.
5. Select the cell at column A, Row 2.
6. Paste the contents into the spreadsheet.
7. On the **Data** tab choose "**Text to Columns"****
**8.   On Step 1 of the Convert Text to Columns Wizard, change the file type to **Delimited** and click **Next****.
**


9. On Step 2 of the Text Import Wizard. change the Delimiters to **Comma** and click **Next****.**


****


**
**10.  On Step 3 of the Text Import Wizard, accept the defaults and click **Finish****.**


**
**


**
**


**
 **