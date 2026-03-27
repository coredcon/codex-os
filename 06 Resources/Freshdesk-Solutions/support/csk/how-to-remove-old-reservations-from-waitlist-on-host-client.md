---
title: "How to remove old Reservations from Waitlist on Host Client"
freshdesk_id: 17000150268
category: "Support"
folder: "CSK"
status: draft
created: 2026-02-04
updated: 2026-02-04
views: 0
tags: ["Waitlist", "Old Reservations", "ConnectSmart Host"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000150268
---

# How to remove old Reservations from Waitlist on Host Client

**Issue:** Older Reservations appearing in Waitlist after SQL Server and Host Upgrade.


**Cause:** The SQL Server upgrade sometimes with push old data or display duplicate servers.


**Solution: **Print Active Waitlist from the Host Portal > Sites > Operation > Waitlist or Run End of Day.


 


**How to Print Active Waitlist:**


 To print the Active Waitlist, go to Host > Site > Operations > Active Waitlist and hit Print.


 


 


**How to Run End of Day:**


 - Stop the ConnectSmart Server service and run the executable for the Connect Smart Server within the C:\Program Files (x86)\QSR Automations\ConnectSmart\HostessServer folder as a process.


- Double-click the Host icon in the system tray toolbar.


- Click on Tools and run EOD.