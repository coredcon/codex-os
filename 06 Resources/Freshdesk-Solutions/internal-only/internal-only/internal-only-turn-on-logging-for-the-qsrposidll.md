---
title: "*|Internal Only| - Turn On Logging for the QsrPOSi.dll"
freshdesk_id: 17000131721
category: "Internal Only"
folder: "Internal Only"
status: draft
created: 2023-02-24
updated: 2023-02-24
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000131721
---

# *|Internal Only| - Turn On Logging for the QsrPOSi.dll

The QsrPOSi.log file provides helpful information during POS interface development, containing all function calls and data values passed from the POS system to integrated QSR software. Additionally, QSR requires the submission of a Qsr.POSi.log file containing test transactions for the Log Review portion of the POS Interface Certification process. 


To create this log file, the QsrPOSi.dll requires logging be enabled. This is configured in the QsrPOSi.xml file included with the QsrPOSi Software Development Kit (SDK). The XML file resides on the same machine where the interface service or POS application is calling QsrPOSi.dll – this may be a single back-of-house server or multiple POS terminals. 


To enable QsrPOSi logging, first place the QsrPOSi.xml file in the appropriate location on the POS server or terminal 


To enable logging in the XML, edit the LogLevel tag to "All"


Once logging is enabled, the QsrPOSi.log file created is saved to the *\QsrPOSi\Log folder, peer to the Data folder.


Keep in mind, logging should only be turned on for a short amount of time, as the log doesn't archive and will grow indefinitely.