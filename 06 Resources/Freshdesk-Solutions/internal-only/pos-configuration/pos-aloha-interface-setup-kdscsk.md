---
title: "*|POS| - Aloha Interface Setup - (KDS/CSK)"
freshdesk_id: 17000049354
category: "Internal Only"
folder: "POS Configuration"
status: published
created: 2017-04-20
updated: 2022-11-10
views: 0
tags: ["Aloha"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000049354
---

# *|POS| - Aloha Interface Setup - (KDS/CSK)

This article is a “Quick Hit” section that should establish a working interface (i.e. items being sent) between Aloha and QSR. If these steps do not work, proceed through the attached guide starting with Chapter 2. There are several “one-offs” that are covered in the subsequent chapters that are not in this Quick Hit section. 


- Configure the IBERCFG.bat on each terminal and the BOH with following variables: These should be verbatim as shown below spacing, capitalization, etc.  

> 
> 

SET IBERROOT=Aloha
SET LOCALDIR=C:\Aloha
SET CALIBRATE=C:\P15xx\tcalib.exe
SET EDCPATH=\\ALOHABOH\BOOTDRV\Aloha\EDC
SET TERMSTR=TERM
SET TERM=1
SET NUMTERMS=5
SET SERVER=ALOHABOH
SET MASTERCAPABLE=TRUE
SET SERVERCAPABLE=TRUE
SET AUTOEXIT=TRUE
SET REBOOTNT=TRUE
SET QSRDEBUG=FALSE – TRUE if troubleshooting
SET QSRLOCALPORT=0x6000
SET QSRLOCALADDR=AnyAddress
SET QSRKDSPORT=0x8000
SET QSRKDSADDR=AnyAddress
SET QSRDRIVETHRU=FALSE – TRUE if site has a Drive Thru


- Copy the attached DLLs to the \Aloha\Bin folder on the terminal. The following table illustrates the correct file placement.

> 
> 
**File Name**
**File [Destination]**
AlohaQSR.dll
X:\Aloha\Bin
QSRSock.dll
XMLKDS.dll
XMLRDS.dll
XMLTABLE.dll


- Refresh Aloha. If the terminals are not sending items to KDS after the refresh, check the debout from one of the terminals. Search for "QSRSock". Once Iber loads the QSRSock.dll, there should either be a success message or a failure message along with an error. Common debout error messages along with their resolutions can be found [here].