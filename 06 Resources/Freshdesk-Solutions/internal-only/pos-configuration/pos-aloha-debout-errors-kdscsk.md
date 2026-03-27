---
title: "*|POS| - Aloha Debout Errors - (KDS/CSK)"
freshdesk_id: 17000049356
category: "Internal Only"
folder: "POS Configuration"
status: published
created: 2017-04-20
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000049356
---

# *|POS| - Aloha Debout Errors - (KDS/CSK)

**Troubleshooting Aloha interface issues**


If the environment variable QSRDEBUG is set to TRUE, the Debout file located on each terminal in the Aloha/Temp folders will log extensive information with regard to the interface. One can quickly determine if in fact an order or item was sent thru the AlohaQSR module. One can also see whether the module is being loaded properly.
Below are common error messages seen in the Aloha debout for a terminal.

**“AlohaActivity:  Failed to create CLSID AlohaQSR.AlohaQSR.1”
**
The AlohaQSR.dll has not been registered properly. Try to manually register the dll from a command prompt.  
Change to \Aloha\Bin directory and execute REGSVR32 AlohaQSR.dll

**_“AlohaQSR: Failed to open socket: xxx – Invalid IP Address ‘xxx’”_ 
**
Make sure the variable ‘AnyAddress’ is properly capitalized in the ibercfg.bat
Example: SET QSRKDSADDR=AnyAddress
_**
“ALOHAQSR: Could not load QSRSOCK.DLL, error 0”
**_
Either C++ Runtime binaries needs to be installed on to the terminal or version 8.1 DLLs need to be used in the \Aloha\Bin instead of the version 9 or higher DLLs. QSR recommends using the 8.1 DLLs as it is a simpler solution. Both the DLLs and the C Runtime updates are attached at the bottom of this article.   


**_“ALOHAQSR: Failed to open socket:  error 10067 – the limit has been reached on socket tasks”_**


Check the Aloha Manager/Maintenance/Store Settings/System/Interfaces; there should only be one instance of AlohaQSR.AlohaQSR.1 under External Activity Interceptors. Try clearing (un-checking) _Use FOH COM_ and _Enable QSR_ _Video_, and save the form. Access it again and select (re-enable) those options. AlohaQSR.AlohaQSR.1 should auto-fill the necessary Activity Line.


_**"AlohaActivity: Insufficient SDK licensing for AlohaQSR.AlohaQSR.1. Ensure that the system has the SDK Option enabled or at least 1 Interface Terminal is licensed on the security key."**_ 


If VideoMX is not included on the Aloha license, this error appears. It can also be seen in some versions due to an Aloha defect. If VideoMX is indeed included on the license key, contact Radiant for resolution. 


****