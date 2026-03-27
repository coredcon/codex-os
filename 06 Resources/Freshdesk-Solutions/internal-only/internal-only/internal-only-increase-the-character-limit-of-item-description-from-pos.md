---
title: "*|Internal Only| - Increase the Character Limit of Item Description from POS"
freshdesk_id: 17000129458
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2022-11-10
updated: 2025-08-08
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000129458
---

# *|Internal Only| - Increase the Character Limit of Item Description from POS

**Expanding Description Character Limits with QsrPOSi**


 

# Introduction 


The default character limit for standard QsrSock item message functions is 20 characters.  These functions send socket messages containing item information, including the Description.   


In the older QsrSock SDK, additional item message functions could be leveraged to send longer Item Descriptions, up to 50 characters.  These item message function names are designated in the QsrSock code with a “2” – for example, “TRANSACTION_MESSAGE_FOOD_ITEM2”.


The newer QsrPOSi SDK includes code to invoke the QsrSock message functions using different DLL function calls that trigger the same socket messages.  However, there is no option in the QsrPOSi SDK to send the “2” versions of the QsrSock item functions.  Therefore, the default character limit in QsrPOSi for Item Description is 20 characters.


ConnectSmart customers and partners who use POS systems that leverage the QsrPOSi SDK still have the option to expand the number of characters sent for Item Description.  The “2” functions are triggered based on a setting in the


QsrPOSi.xml file.


 


 

# Using QsrPOSi.xml


The below sections outline the usage of the XML file.  The file is included in the QsrPOSi SDK or may be provided by QSR


Automations as needed.


 

## File Location


The XML must live on the host machine where QsrPOSi.dll or QsrPOSiInterop.dll is called (typically on the POS terminal but could be on the POS server or other host machine depending on the integration design).  If the below directory does not exist, create it.


 


The XML should be copied to this location:  _C:\ProgramData\QSR Automations\ConnectSmart\QsrPOSi\Data _


 

## XML Tag


There are several XML tags available, but the “UseQsrSockItem2” tag controls the character limit.  When set to “true” the QsrSock alternate “2” functions are used when sending socket messages.


_  <DetailData> _


_    <LogLevel>All</LogLevel> _


_    **<UseQsrSockItem2>true</UseQsrSockItem2> **_


_     <UseQsrSockCustomerNameForGuestCount>false</UseQsrSockCustomerNameForGuestCount> _


_    <CskPosWebApiClient Enabled="false" CaptureData="false"> _


_      <Server Host="192.168.180.50" Port="32768" /> _


_    </CskPosWebApiClient> _


_  </DetailData> _


_</QsrPOSi.xml> _


**_ _**

## Applying Changes


Once the UseQsrSockItem2 tag has been updated, the InitializeNetwork function in QsrPOSi must be called to force the


DLL to pull the updated setting.  This typically requires a restart of the POS terminal or the integration service.


The user may confirm the setting is enabled by reviewing the Socketmon output or capture files – socket messages will show the appended “2” if the setting is enabled.


_Socketmon: _


 


_ _


_Capture: _


 


 

## Additional XML Tags


Additional settings available in the XML serve these functions:


**LogLevel** – controls the logging written by QsrPOSi.dll


- If testing or troubleshooting, set to “All”, but the log file will grow large quickly and does not archive

- If not testing, this tag should be set to “None” for production use

- Log is written to this location on the host machine: ** **_C:\ProgramData\QSRAutomations\ConnectSmart\QsrPOSi\Log_

- _ _**UseQsrSockCustomerNameForGuestCount** – allows user to send a Guest Count value from the POS

- QsrSock socket message structures do not support the GuestCount field, but QsrPOSi code supports it

- Enabling as “true” will send the GuestCount value in the defined CustomerName field

- User is REPLACING Customer Name with a Guest Count when this option is enabled

- Option should only be enabled if the POS integration supports the GuestCount field with QsrPOSi


 


**CskPosWebApiClient Enabled** – allows user to send POS data using the local RESTful API service


- Enabling this setting allows QsrPOSi to send all supported data fields, including those not supported in QsrSock socket message structures (RoutingCategory, GuestCount, PrinterDescription, et al)

- Option should only be enabled if the POS integration supports the non‐QsrSock fields with QsrPOSi or if there is a use case where QSR Automations has advised leveraging this communication option (**_not to be confused with TCP/IP communication using QsrSock.xml_**)

- ServerHost and Port settings determine the IP address and port for the targeted server(s)

- Users supporting a Secondary instance of KitchenServer for Redundancy must add a line to the XML for ServerHost and Port tags to define the Secondary IP address and port


 


**CaptureData**** **– controls the writing of a capture file (QsrPOSi.qsrcap) detailing the data sent by QsrPOSi


- This capture file should not be confused with the similar KitchenServer.qsrcap file – this file captures the data sent by QsrPOSi rather than the data received by ConnectSmart KitchenServer

- Capture file is written to this location on the host machine (peer to the QsrPOSi.log):   o _C:\ProgramData\QSR Automations\ConnectSmart\QsrPOSi\Log _