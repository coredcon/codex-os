---
title: "*|CSH| - Retrieve the WebAhead record for a visit with Status = Seated and beyond"
freshdesk_id: 17000077731
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host - Third-Party API"
status: published
created: 2018-09-04
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000077731
---

# *|CSH| - Retrieve the WebAhead record for a visit with Status = Seated and beyond

By default, WebAheads are only “active” while on a wait list, but some integrators may wish to obtain the status of a Seated or Completed visit.  


To accomplish this, they can override that default behavior by using the “IgnoreStatusForCurrentBusinessDay” parameter.  


**For example:**


**POST a new WebAhead and receive this response body:**


{"**PlaceInWaitList**":1,"P**artnerId**":null,"**ID"**:"1b0e9dd7-a3e8-4ce7-91bd-9185d28b95e2","**IID**":0,"**LastUpdate**":"0001-01-01T00:00:00+00:00","**ServerLastUpdate**":"0001-01-01T00:00:00+00:00","**GuestID**":"78cd65c7-b95b-44de-a739-0d7f50247a2c","**Guest**":{"ID":"78cd65c7-b95b-44de-a739-0d7f50247a2c","**LastUpdate**":"0001-01-01T00:00:00+00:00","**ServerLastUpdate**":"0001-01-01T00:00:00+00:00","**FirstName**":"John","**LastName**":"Dangerously","**PhoneNumbers**":null,"**Email**":null,"**Addresses**":null,"**Notes**":"","**FoodAllergies**":null,"**IsAnonymous**":false,"**IsSubscribedToSmsMarketing**":false,"**IsSubscribedToEmailMarketing**":false,"**IsSubscribedToQsrMarketing**":false,"**CustomValues**":null,"**Loyalty**":{"**LoyaltyCardID**":""}},"**Type**":"CallAhead","**Status":"NotYetArrived**","**Size**":4,"**SeatedTables**":null,"**PreassignedTables**":null,"**Quote**":{"**QuoteLow**":0,"**QuoteHigh**":0,"**SiteQuoteString**":null,"**ConsumerQuoteString**":"Now Seating","**ExactQuote**":null},"**CreationTime**":"2018-08-28T14:35:25.2511735-04:00","**EstimatedArrivalTime**":null,"**ArrivalTime**":null,"**PagedTime**":null,"**SeatedTime**":null,"**CompletedTime**":null,"**CanceledTime**":null,"**ConfirmationNumber**":"BPNXEE","**ConfirmationNumberId**":115290414,"**SeatingAreaID**":null,"**SeatingAreaName**":null,"**Notes**":"","**CustomValues**":null,"**ExternalID**":null,"**PartyMix**":null,"**NotificationType**":"None"}

---


**The party is Checked In/Arrived in DineTime Host at the restaurant. A GET call returns the updated Status:**


Request URL:


[https://api.dinetime.com/WebAhead?confirmationNumberId=115290414]


Response body:


{"SiteUID":"c0032103-10a4-4f1f-88f4-675e8157ff1c","PlaceInWaitList":1,"PartnerId":null,"ID":"1b0e9dd7-a3e8-4ce7-91bd-9185d28b95e2","IID":0,"LastUpdate":"0001-01-01T00:00:00+00:00","ServerLastUpdate":"0001-01-01T00:00:00+00:00","GuestID":"78cd65c7-b95b-44de-a739-0d7f50247a2c","Guest":null,"Type":"CallAhead","**Status":"Waiting**","Size":4,"SeatedTables":null,"PreassignedTables":null,"Quote":{"QuoteLow":0,"QuoteHigh":0,"SiteQuoteString":null,"ConsumerQuoteString":"Now Seating","ExactQuote":null},"CreationTime":"2018-08-28T14:35:25-04:00","EstimatedArrivalTime":null,"ArrivalTime":null,"PagedTime":null,"SeatedTime":null,"CompletedTime":null,"CanceledTime":null,"ConfirmationNumber":"BPNXEE","ConfirmationNumberId":115290414,"SeatingAreaID":null,"SeatingAreaName":null,"Notes":"","CustomValues":null,"ExternalID":null,"PartyMix":null,"NotificationType":"None"}


---


**The party is then Seated in DineTime Host. The exact same GET call now returns code 410. However, if the additional “IgnoreStatusForCurrentBusinessDay” URL parameter is included with the Boolean “true”, you may retrieve the WebAhead record with Status: Seated and beyond:**


Request URL:


[https://apitest.qsrpolarisdev.net/WebAhead?confirmationNumberId=115290414&**ignoreStatusForCurrentBusinessDay=true**]


Response Body:


{"SiteUID":"c0032103-10a4-4f1f-88f4-675e8157ff1c","PlaceInWaitList":-1,"PartnerId":null,"ID":"1b0e9dd7-a3e8-4ce7-91bd-9185d28b95e2","IID":0,"LastUpdate":"0001-01-01T00:00:00+00:00","ServerLastUpdate":"0001-01-01T00:00:00+00:00","GuestID":"78cd65c7-b95b-44de-a739-0d7f50247a2c","Guest":null,"Type":"CallAhead","**Status":"Seated**","Size":4,"SeatedTables":null,"PreassignedTables":null,"Quote":{"QuoteLow":0,"QuoteHigh":0,"SiteQuoteString":null,"ConsumerQuoteString":"Now Seating","ExactQuote":null},"CreationTime":"2018-08-28T14:35:25-04:00","EstimatedArrivalTime":null,"ArrivalTime":null,"PagedTime":null,"SeatedTime":null,"CompletedTime":null,"CanceledTime":null,"ConfirmationNumber":"BPNXEE","ConfirmationNumberId":115290414,"SeatingAreaID":null,"SeatingAreaName":null,"Notes":"","CustomValues":null,"ExternalID":null,"PartyMix":null,"NotificationType":"None"}


**Please note sending “false” for that parameter or not including it, will only return WebAheads seen as “active” (which for a WebAhead means on the wait list by default).**