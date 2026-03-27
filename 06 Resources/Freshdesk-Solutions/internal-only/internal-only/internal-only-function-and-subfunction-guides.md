---
title: "*|Internal Only| - Function and SubFunction Guides"
freshdesk_id: 17000059621
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2017-09-06
updated: 2025-07-31
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000059621
---

# *|Internal Only| - Function and SubFunction Guides

**TABLE OF CONTENTS**


- [QsrSock Functions / SubFunctions]

- [QsrSock vs QsrPOSi Functions]

- [Non-DLL-Based QsrSock Functions (Header Files)]


- [Unicode vs ANSI Functions]

- [“EX” Message Functions]

- [“Item2” Message Functions]

- [Transaction Message Functions]

- [System Message Functions]


- [QsrSock vs QsrSockB]

- [Transaction Message Functions (QsrSockB)]

- [System Message Functions (QsrSockB)]


Attached are the quick reference guides to the function and subfunctions you will see in Capture Player.


From capture PLayer:


From Guide:


# QsrSock Functions / SubFunctions


_The below tables outline QsrSock functions for each socket message. These values come into play in CSK/KDS logging and QSR Capture player display of .qsrcap files. _

## 


## **QsrSock vs QsrPOSi Functions**


The QsrSock Function/SubFunction list is relevant for all Windows DLL integrations, whether QsrPOSi or QsrSock SDKs. QsrPOSi has different functions that call QsrSock code in sending the actual socket messages from the POS. QsrSock integrations call the below functions directly. Think of QsrPOSi as “QsrSock with a Network Wrapper”, meaning QsrPOSi handles the network communication (managing sockets, etc.) but passes POS data to CSK using the QsrSock message functions. The below tables describe QsrSock functions that define the socket messages received by CSK and visible in Socketmon, .qsrcap files in QSR Capture Player, and WireShark. QsrPOSi functions are written to the QsrPOSi.log but should not be confused with the QsrSock message functions.


**Please note:** QsrSock and QsrPOSI SDKs are no longer offered for new POS integration projects. New integrations leverage the KitchenServer POS Web API and Cloud POS API services rather than the older socket message interface. But given the number of older integrations still active in the field, understanding QsrSock message functions may be needed for supporting end users.

## 


### **Non-DLL-Based QsrSock Functions (Header Files)**


There are a few older integrations that were written using QsrSock header files without the Windows DLL-based SDK. The integrations send QsrSock-formatted messages, but the functions/subfunctions may not align with those supported by QsrSock.dll. Since these are “custom” functions, the functions/subfunctions are not documented here. QsrSock messages in qsrcap files for these integrations are noted as “OldVBHeader” or “OldVBItem”, for example, while QsrSock messages sent using the DLL are noted as “Header” or “Item”.


An important caveat when dealing with non-DLL integrations to consider is these integrations cannot be configured to send as TCP/IP because that functionality requires a QsrSock.dll or QsrPOSi.dll to pull TCP settings from a QsrSock.xml file. These integrations can, however, control UDP communication as either Broadcast or Directed Send.

## 


## **Unicode vs ANSI Functions**


QsrSock code supports two types of Transaction Message functions - 0x03 function messages support single-byte characters (ANSI) only, and 0x04 function messages support double-byte (Unicode) versions of the same messages, defined by the same subfunction values. Given this difference, the message data structures may differ between the ANSI and Unicode functions. These structures are defined in the _Kitchen Display System: C/C++ Programmer’s Guide _available for QsrSock. If the data structures differ, it is noted in the “Structures the Same?” column in the below table.


ANSI functions appear in Socketmon with “A” appended to the message type - for example, “HeaderA”. Qsrcap files will show the Function and SubFunction as defined below. The Unicode functions are by far the most commonly used, but there are older integrations that may still use the ANSI versions.

## 


## **“EX” Message Functions**


Some message functions have a version with “EX” appended to the message description. The difference between “EX” functions and “non-EX” functions is the Course field. The concept of “Course” was added in ePic KDS 4.1, and versions of KDS and eventually CSK released after KDS 4.1 organize transaction data by Transaction Number and Course Number. This allows for support of Table Service operations where a single Transaction Number (or Check) may have multiple Courses. 


Quick Service operations typically do not require Courses, but EX functions work for either TS or QS. Prior to KDS 4.1 and its corresponding QsrSock SDK, only “non-EX” functions are available. So only older POS integrations should use the non-EX versions. In cases where non-EX functions are used, Course Numbers will default to “1” since there is no means of passing the Course.

## 


## **“Item2” Message Functions**


QsrSock code supports “Item” and “Item2” message functions. The “item2” versions are simply Item messages with longer Description character limits. Standard Item messages support up to 20 characters of Description text, while Item2 messages support up to 50 characters. These Item2 messages are displayed in Socketmon data with the 2 appended - for example,“FoodItem2”. And the Item2 versions of functions have different subfunction values than their standard counterparts.


For QsrSock users that need longer text strings for Item Descriptions, the Item2 functions may be called. For QsrPOSi users, however, there are not separate “new item” functions. Instead, QsrPOSi users that utilize the ItemEx data structure have a max of 50 characters for Item Description, but the QsrPOSi.xml file must be configured for the QsrPOSi.dll to send to CSK using the QsrSock “Item2” message functions:


_<UseQsrSockItem2>_**_true_**_</UseQsrSockItem2>_


See the _Expanding Description Character Limits with QsrPOSi_ document for more details on enabling Item2 messages in QsrPOSi. 

## 


## **Transaction Message Functions**


The table below provides function/subfunction values for message functions that provide the bulk of POS integrations. These functions send data from the POS to the KDS (and in some cases data trigger updates in the FOH guest/table management system).


Messages logged in .qsrcap files include the Function and Subfunction in Decimal format in the “Hdr” section of the “ePicMessage” data displayed in the sidebar of the QSR Capture Player. SubFunctions in Hexadecimal are included in the below table as they may be referenced in QsrSock SDK header files (e.g., TransactionMsg.h) or other utilities.


##### **ANSI Function**

##### **Unicode Function**

##### **SubFunction (Hexadecimal)**

##### **Subfunction (Decimal)**

##### **Description**

##### **Structures the Same?**


 3  


 4  


0x01


1


 Transaction Header 


 No 


3


4


0x02


2


Destination Change


Yes


 3  


 4  


0x03


3


 Combo Item 


 No 


 3  


 4  


0x04


4


 Food Item 


 No 


 3  


 4  


0x05  


5


 Piece Detail 


 No 


 3  


 4  


0x06  


6


 Mix Item 


 No 


 3  


 4  


0x07  


7


 Side Item 


 No 


 3  


 4  


0x08  


8


 Condiment 


 No 


 3  


 4  


0x09  


9


 Modify Combo Item 


 No 


 3  


 4  


0x0A 


10


 Modify Food Item 


 No 


 3  


 4  


0x0B  


11


 Modify Piece Detail 


 No 


 3  


 4  


0x0C  


12


 Modify Mix Item 


 No 


 3  


 4  


0x0D 


13


 Modify Side Item 


 No 


 3  


 4  


0x0E 


14


 Modify Condiment 


 No 


 3  


 4  


0x0F


15


 Cut Food Item 


 No 


 3  


 4  


0x10


16


 Add Food Item 


 No 


 3  


 4  


0x11 


17


 Cut Piece Detail


 No


 3  


 4  


0x12 


18


 Add Piece Detail


 No 


 3  


 4  


0x13


19


 Cut Side Item 


 No 


 3  


 4  


0x14


20


 Add Side Item 


 No 


 3  


 4  


0x15


21


 Cut Condiment 


 No 


 3  


 4  


0x16


22


 Add Condiment 


 No 


3


4


0x17


23


Remove All Combo Sub-Items


Yes


3


4


0x18


24


Cancel Transaction


Yes


3


4


0x19


25


Cancel Item


Yes


3


4


0x1A


26


Store Transaction


Yes


3


4


0x1B


27


Recall Transaction


Yes


3


4


0x1C


28


Total Transaction


Yes


3


4


0x1D


29


Tender Transaction


Yes


 3  


 4  


0x20


32


 Pizza Section 


 No 


3


4


0x21


33


Park Transaction


Yes


 3  


 4  


0x22  


34


 Destination Change Ex 


 Yes 


 3  


 4  


0x23


35


 Remove All Combo Sub-Items Ex


 Yes 


 3  


 4  


0x24 


36


 Cancel Transaction Ex 


 Yes 


 3  


 4  


0x25  


37


 Cancel Item Ex 


 Yes 


 3  


 4  


0x26  


38


 Store Transaction Ex 


 Yes 


 3  


 4  


0x27


39


 Recall Transaction Ex 


 Yes 


 3  


 4  


0x28  


40


 Total Transaction Ex 


 Yes 


 3  


 4  


0x29  


41


 Tender Transaction Ex 


 Yes 


 3  


4


0x2A


42


 Park Transaction Ex 


 Yes 


n/a


 4  


0x2B


43


 New Course 


 No


n/a


 4  


0x2C


44


 Set Customer Name 


 No


n/a


 4  


0x2E


46


 Set Order Mode  _(sets Destination)_


 No


n/a


 4  


0x2F


47


 Set Table Name 


 No


n/a


4


0x33


51


Set Course Name


No


n/a


4


0x35


53


Set Tent Number


No


3


4


0x40


64


Combo Item 2


No


3


4


0x41


65


Food Item 2


No


3


4


0x42


66


Piece Detail 2


No


3


4


0x43


67


Mix Item 2


No


3


4


0x44


68


Side Item 2


No


3


4


0x45


69


Condiment 2


No


3


4


0x46


70


Modify Combo Item 2


No


3


4


0x47


71


Modify Food Item 2


No


3


4


0x48


72


Modify Piece Detail 2


No


3


4


0x49


73


Modify Mix Item 2


No


3


4


0x4A


74


Modify Side Item 2


No


3


4


0x4B


75


Modify Condiment 2


No


3


4


0x4C


76


Cut Food Item 2


No


3


4


0x4D


77


Add Food Item 2


No


3


4


0x4E


78


Cut Piece Detail 2


No


3


4


0x4F


79


Add Piece Detail 2


No


3


4


0x50


80


Cut Side Item 2


No


3


4


0x51


81


Add Side Item 2


No


3


4


0x52


82


Cut Condiment 2


No


3


4


0x53


83


Add Condiment 2


No


3


4


0x54


84


Pizza Section 2


No


n/a


4


0xA0


160


Course Complete _(updates check status in Host)_


n/a


n/a


4


0xA1


161


Check Printed _(updates check status in Host)_


n/a


n/a


4


0xA2


162


Check Paid _(updates check status in Host)_


n/a


n/a


4


0xA3


163


Items Ordered _(updates meal stage to DRINKS in Host)_


n/a


n/a


4


0xA4


164


Table Opened _(updates table status in Host)_


n/a


n/a


4


0xA5


165


Table Cleared _(updates table status in Host)_


n/a


n/a


4


0xA6


166


Table Dirtied _(updates table status in Host)_


n/a


n/a


4


0xB0


176


Table Locator


n/a

## 


## **System Message Functions**


System functions send messages between the POS and KDS. Unlike Transaction messages, which are only sent to the KDS, some of these messages only send from the KDS and one can send both ways (PingKDS).


Functions that communicate from the KDS to the POS are the socket events available in ePic KDS and CSK3, configurable in the old Events Wizard in the builder applications - these events have been removed from the builders as of CSK5 and now require subscription to the Kitchen Events Web Service in CSK. **_Please note the inclusion of these event functions here does NOT mean these socket events are available in the current CSK product._**


There are no differing message structures like Transaction messages either, so there are not different ANSI and Unicode functions. The below table provides function/subfunction values and the valid direction of communication between the POS and KDS.


##### **Function**

##### **SubFunction (Hexadecimal)**

##### **SubFunction (Decimal)**

##### **Description**

##### **Sent to KDS**

##### **Sent from KDS**


 2 


0x01


 1 


 Ping KDS 


Yes


Yes


 2 


0x02


 2 


 Refresh KDS Screens 


Yes


 No 


 2 


0x03


 3 


 Remove Transaction 


Yes


 No 


 2 


0x04


 4 


 Change Activity Level 


Yes


 No 


 2 


0x05


 5 


 Restart 


Yes


 No 


 2 


0x06


 6 


 Perform End of Day 


Yes


 No 


 2 


0x07


 7 


 Shutdown 


Yes


 No 


 2 


0x08


 8 


 Bump Transaction 


Yes


 No 


 2 


0x09


 9 


 Transaction Event 


No


 Yes


 2 


0x0A


 10 


 Service Timing 


No


 Yes


 2 


0x0B


 11 


 Get Runtime Information 


Yes


 No 


 2 


0x0C


 12 


 Get Activity Level Information 


Yes


 No 


 2 


0x0D


 13 


 Get Active Transactions 


Yes


 No 


 2 


0x0E


 14 


 Remove Transaction Ex 


Yes


 No 


 2 


0x0F


 15 


 Bump Transaction Ex 


Yes


 No 


 2 


0x10


 16 


 Transaction Event Ex 


No


 Yes 


 2 


0x11


 17 


 Service Timing Ex 


No


 Yes


 2 


0x12


 18 


 Get Longest Active Transaction 


Yes


 No 


 2 


0x90


 144 


 Error Code 


No


 Yes 

## 


# **QsrSock vs QsrSockB**


The standard QsrSock SDK was written for C/C++ programming and documented in the _Kitchen Display System: C/C++ Programmer’s Guide_. But a separate SDK was published for East Asian POS vendors that required compatibility with Visual Basic 6.0 programming (QsrSock and QsrPOSi DLLs are not compatible with VB6). This VB6 version is called “QsrSockB” and the SDK is documented in the _Kitchen Display System: Visual Basic Programmer’s Guide_.


QsrSockB code works essentially the same as standard QsrSock, but the ANSI function values are different. And some current QsrSock functions may not be available in QsrSockB as that SDK was treated as a completely separate code branch and not updated and maintained with new KDS versions like standard QsrSock code.


The usage of QsrSockB is very limited. Known potentially active integrations are Cuscapi Transight (not to be confused with a newer QsrPOSi integration) and Lotteria (supported by Firich Korea) in Asia.

## 


## **Transaction Message Functions (QsrSockB)**


##### **ANSI Function**

##### **Unicode Function**

##### **SubFunction (Decimal)**

##### **Description**

##### **Structures the Same?**


18


 4  


 1  


 Transaction Header 


 No 


18 


 4  


 3  


 Combo Item 


 No 


18 


 4  


 4  


 Food Item 


 No 


18


 4  


 5  


 Piece Detail 


 No 


18 


 4  


 6  


 Mix Item 


 No 


18 


 4  


 7  


 Side Item 


 No 


18  


 4  


 8  


 Condiment 


 No 


18


 4  


 9  


 Modify Combo Item 


 No 


18


 4  


 10  


 Modify Food Item 


 No 


18


 4  


 11  


 Modify Piece Detail 


 No 


18


 4  


 12  


 Modify Mix Item 


 No 


18


 4  


 13  


 Modify Side Item 


 No 


18


 4  


 14  


 Modify Condiment 


 No 


18


 4  


 15  


 Cut Food Item 


 No 


18


 4  


 16  


 Add Food Item 


 No 


18


 4  


 17  


 Cut Piece Detail


 No 


18


 4  


 18  


 Add Piece Detail


 No 


18


 4  


 19  


 Cut Side Item 


 No 


18


 4  


 20  


 Add Side Item 


 No 


18


 4  


 21  


 Cut Condiment 


 No 


18


 4  


 22  


 Add Condiment 


 No 


18


 4  


32


 Pizza Section 


 No 


18


 4  


 34  


 Destination Change Ex 


 Yes 


18


 4  


 35  


 Remove All Combo SubItems Ex 


 Yes 


18


 4  


 36  


 Cancel Transaction Ex 


 Yes 


18


 4  


 37  


 Cancel Item Ex 


 Yes 


18


 4  


 38  


 Store Transaction Ex 


 Yes 


18


 4  


 39  


 Recall Transaction Ex 


 Yes 


18


 4  


 40  


 Total Transaction Ex 


 Yes 


18


 4  


 41  


 Tender Transaction Ex 


 Yes 


18


4


42


 Park Transaction Ex 


 Yes 

## 


## **System Message Functions (QsrSockB)**


##### **Function**

##### **SubFunction (Decimal)**

##### **Description**

##### **Sent to KDS**

##### **Sent from KDS**


 2 


 1 


 Ping KDS 


Yes


Yes


 2 


 2 


 Refresh KDS Screens 


Yes


 No 


 2 


 4 


 Change Activity Level 


Yes


 No 


 2 


 5 


 Reload Database


Yes


 No 


 2 


 6 


 Perform End of Day 


Yes


 No 


 2 


 7 


 Shutdown 


Yes


 No 


 2 


14 


 Remove Transaction Ex 


Yes


 No 


 2 


15


 Bump Transaction Ex


Yes


 No 


 2 


16


 Transaction Event Ex


No


 Yes


 2 


17


 Service Timing Ex


No


 Yes


 2 


144


 Error Code


No


Yes