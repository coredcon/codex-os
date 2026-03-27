---
title: "Aloha to QSR - Steps when orders not reaching capture"
freshdesk_id: 17000139413
category: "Internal Only"
folder: "POS Configuration"
status: published
created: 2024-03-15
updated: 2024-03-18
views: 0
tags: ["Aloha", "VideoMX", "Network", "qsrsock.xml"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000139413
---

# Aloha to QSR - Steps when orders not reaching capture

**Step 1.** Enable VideoMX in the Aloha Configuration Center. Confirm that VideoMX is properly licensed in the Aloha Keys. Aloha key sheet can present this. (Performed by Aloha)


 


**Step 2.** Drop All QSR files (**QSRSock.dll QsrSock.xml XMLKDS.dll XMLRDS.dll XMLTABLE.dll**) into the Bin folder of Aloha on the Server **(C:\BOOTDRV\Aloha\BIN)** 


**Step 3.** Configure the QSRSock.xml for TCP by adding the Server IP address. 


The IP Address can be verified by checking the ConnectSmart Network Configurator as seen below.


**Step 4.** Reboot a specific Aloha Terminal. This allows the user to have an isolated environment to troubleshoot. After reboot verify that it received all QSR files listed below


(**QSRSock.dll QsrSock.xml XMLKDS.dll XMLRDS.dll XMLTABLE.dll**) 


**Step 5.** Send a test order from the terminal used in **Step 4** to Kitchen and verify if the order was received on the QSR Kitchen Video Displays.


 **Step 6.** If order appears from Step 5 then Refresh Aloha to push files out to all terminals. 


 


**Step 7.** Send test transactions from a random Aloha Terminal and confirm the order was received on the QSR Kitchen Video Displays.