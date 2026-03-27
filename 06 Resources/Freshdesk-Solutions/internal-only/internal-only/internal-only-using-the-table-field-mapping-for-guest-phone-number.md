---
title: "*|Internal Only| - Using the Table Field Mapping for Guest Phone Number"
freshdesk_id: 17000130476
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2022-12-28
updated: 2022-12-28
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000130476
---

# *|Internal Only| - Using the Table Field Mapping for Guest Phone Number

**Issue:**
The customer wants to use the Table field mapping to send the Guest's phone number. However, the max integer limit of 2147483647 is what is showing up in the capture. 

****

**Resolution : **


**Table mapping to Phone Number will work, but it requires some configuration. **


The available options for alternate field mapping are:

- CustomerName

- ServerName

- CourseName

- Table
Note that whichever field you select will be “sacrificed” for passing Phone, so it should be one that the end user does not rely on in their CSK configuration. CustomerName, ServerName, and CourseName all work without issue using the QsrPOSi.dll interface as they are String values with dedicated fields in the QsrSock message structure.  (Though we typically advise against CourseName in case a restaurant uses Coursing Manager, which can cause the CourseName value to be discarded.) The exception is Table.  Here’s why: QsrPOSi supports a String value for Table, called “TableName”.  QsrSock supports an int32 value in the Transaction Header message called “TableNumber”.  The QsrPOSi user only has an option for TableName, which can be sent in a NewCheckEx or NewCourseEx function in QsrPOSi.  The DLL code takes the TableName value and, if it is seen as a valid int32 value, it will include it in the TableNumber field in the QsrSock Header message… Socketmon: Capture:  If the TableName value is not a valid int32 value, then it is not passed in the QsrSock Header message field (you would see “0”).  But QsrPOSi triggers a SetTableName message with NewCheckEx/NewCourseEx to pass a non-integer Table value (like one with alpha-numerics).  The TableName string is only passed in the SetTableName message… Socketmon: Capture:  If using the “Table” option for alternate field mapping for Guest Phone Number in CSK, this handling for TableName vs TableNumber makes this more complicated than using CustomerName or ServerName, for example.  In order for the phone number to be used for Kitchen SMS, we need a formatted phone number string (e.g., “+15022426015”).  Per Agilysys and in our testing, we find that QsrPOSi is trying to populate the QsrSock TableNumber with the phone number string.  And when this value does not jive, we see the max value for int32 (“2147483647”) being sent as TableNumber in the Header message. To get around this issue with the DLL-based socket message interface, we can configure QsrPOSi.dll to bypass QsrSock messages completely and send them using the local POS Web API.  When QsrPOSi is configured for the web API, the value passed in the TableName field, if a valid phone number string, will be passed as Guest Phone Number and used to send Kitchen SMS. **The web API option in QsrPOSi requires:**

- CSK version 6.4.112 or higher

- QsrPOSi.dll version 2.1.103

- QsrPOSI.xml on the same machine as QsrPOSi.dll (could be the POS terminal or a server machine, depending on the POS system)

- Properly configured XML tags:

- _<CskPosWebApiClient Enabled="**true**" CaptureData="true">_

- _<Server Host="**10.5.63.2**" Port="**32768**"…_  (note: this is the KitchenServer bind-to IP address and base port – if there is a secondary KitchenServer, just duplicate the line in the XML and add the second “Server Host” information)

 If you make changes to the QsrPOSi.xml, keep in mind you will need to re-initialize the DLL for changes to take effect.  This typically requires restarting the POS client application, but trigger re-initialization can vary depending on the POS system. No change is needed on the POS integration side.  This is all handled in the QsrPOSi code. When sending as the web API, you will see the TableName value included in the Course DTO in a “New Check” API request.  For example, in a Capture file:   And in CSK, you can see the Guest Phone Number sent as Table in a grid header:  And Kitchen SMS is fired to that phone number per the Portal settings: 


**Ticket Reference:** [https://qsrautomations.freshdesk.com/a/tickets/284373]