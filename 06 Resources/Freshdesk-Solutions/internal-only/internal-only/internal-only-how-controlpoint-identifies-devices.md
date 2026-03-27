---
title: "*|Internal Only| - How ControlPoint Identifies devices"
freshdesk_id: 17000076052
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2018-08-02
updated: 2022-11-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000076052
---

# *|Internal Only| - How ControlPoint Identifies devices

## How the QSR Software identifies each device type


For some device types, the things that are checked depend on the type of MAC address it has. 


The three types of MAC address that are checked for are:


QSR (begins with **80-D7-33**)


Legacy (begins with **08-00-53**)


Flytech (begins with **00-60-EF**)


Other than that, it may check for a dll to be loaded, a registry value, OS version, or system information (SystemInfo, SystemEnclosure, or BaseBoardInfo properties). I think you can check the system information with a command line tool like wmic, but I’m not sure how. Alternatively, the system information can be found in the registry.


## **_Windows CE_**


**QSR_EPIC_CE**


Legacy MAC address


**QSR_XCEED_CE**


QSR or Legacy MAC address


EpicDiag.dll loaded


**QSR Xceed 2 WEC7**


 [HKLM\Ident]  DESC=“xCeed2 WEC7 ver 1.3.1”
QSR MAC Address


## **_Windows_**


**QSR_Expert_Win32**


Legacy MAC address


HKEY_LOCAL_MACHINE\ SYSTEM\ CurrentControlSet\ Control\ WindowsEmbedded\ RunTimeID\ RuntimePID = P8XWW-8F7PJ-FBVR4-YDQ6W-V78GY


QSR MAC address


SystemInfo.Manufacturer begins with "QSR"


SystemInfo.Family = "eXpert"


**QSR_ONYX_Win32**


QSR MAC address


SystemInfo.Manufacturer begins with "QSR"


SystemInfo.Family = "Onyx"


Flytech MAC address


SystemInfo.Manufacturer begins with "QSR"


SystemInfo.ProductName = "ONYX2010"


**QSR_ALL_IN_ONE_Win32**


QSR MAC address


SystemInfo.Manufacturer begins with "QSR"


SystemInfo.Family = "All-In-One"


Flytech MAC address


SystemInfo.Manufacturer begins with "QSR"


SystemInfo.ProductName = "K797"


HKEY_LOCAL_MACHINE> SYSTEM> CurrentControlSet> Control> WindowsEmbedded> RunTimeID> RuntimePID = VQ874-CM3D3-834YW-J9C8X-7J37Q


**QSR_Expert_DX3000**


Windows Vista+


QSR MAC address


SystemInfo.Manufacturer begins with "QSR"


SystemInfo.ProductName = "Epic 5"


**QSR_ALL_IN_ONE_WES7**


Windows Vista+


Flytech MAC address


SystemInfo.Manufacturer begins with "QSR"


SystemInfo.ProductName = "K797"


HKEY_LOCAL_MACHINE > SYSTEM > CurrentControlSet > Control > WindowsEmbedded > RunTimeID > QSR_OS_Build = "QSR AIO WES7"


HKEY_LOCAL_MACHINE> SYSTEM> CurrentControlSet> Control> WindowsEmbedded> RunTimeID> RuntimePID = VQ874-CM3D3-834YW-J9C8X-7J37Q


**QSR_MP9**


Windows Vista+


HKEY_LOCAL_MACHINE > SYSTEM > CurrentControlSet > Control > WindowsEmbedded > RunTimeID > QSR_OS_Build = "QSR MP9"


SystemEnclosure.AssetTag = "QSRMP9" or BaseBoardInfo.AssetTag = "QSRMP9"