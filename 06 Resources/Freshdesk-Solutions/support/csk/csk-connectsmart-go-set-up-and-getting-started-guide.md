---
title: "*|CSK| - ConnectSmart Go  Set Up and Getting Started guide"
freshdesk_id: 17000117222
category: "Support"
folder: "CSK"
status: published
created: 2021-06-15
updated: 2023-11-08
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000117222
---

# *|CSK| - ConnectSmart Go  Set Up and Getting Started guide

** The full guide is attached to this article. The below content is an except that includes some updated information not included to the guide **


**Setup Details**


Minimum Software Version:


DineTime Server 2020.4 (**2020.9.3 **Includes a fix for a bug that required licensing the Host server for CS Go in any environment. This version does **NOT** require a license for CSGo to function as expected.)


DineTime Host for iOS 2020.3 (Now known as the **ConnectSmart Host** app in the Apple App Store) 


Kitchen Server 2020.3


CS Go iOS 2020.1


**Additional Whitelist information** : please also ensure that the Licence API URL is also added to any firewall whitelists ([https://licenseapi.qsr.cloud/])


**Licensing Information**


The only licensing requirement for the new Off-Premise features is that the site be
subscribed to the Off-Premise Workspace in the Site Subscriptions. This should be set by the
QSR Data Management prior to go live with CS Go.


Depending on other features for Kitchen and DineTime that a restaurant may wish to use, the site may also require a traditional ConnectSmart License and/or a DineTime Subscription.


The Off-Premise workspace does support 2-way SMS messaging with guests. This additional
feature does require a DineTime Subscription that includes the 2-way SMS feature.


**Subscribing to the Off-Premise Features**


The ConnectSmart Go app can be used without any in-store guest management features. The following is required in order to support this:


• DineTime Server installed and running


• Kitchen Server installed and running


• Off-Premises Workspace Site Subscription product (Verify this in Admin > Company > Company Sites > Site Subscriptions)


DineTime Server does not require a ConnectSmart License file if a site will only be using the ConnectSmart Go app. DineTime Server will successfully run and support Kitchen Takeout visits without a license; however, it will not support any other standard in-store guest management features. With a ConnectSmart Go-only setup the restaurant will not be able to add any visits directly within the CS Go app, but it will be able to manage any off-premise visits generated via a 3rd Party API or Kitchen integration


**Logging**


When DineTime Server detects that the site is subscribed to the Off-Premise
workspace, the following will be logged on Startup and/or after End of Day when
DineTime connects to Enterprise:
I


**NFO [1300]: Off Premises Visit Workspace is enabled.**


ConnectSmart Go app The new app requires the Off-Premise Workspace product to be subscribed to, as indicated above.


If the app attempt to connect to DineTime Server and this feature is not enabled, the following will be logged in the HostessServer.log:


**ERROR [1303]: No license available for [10.254.255.6], a ConnectSmart Go
client.**


If the app successfully connects, the following will be logged in the HostessServer.log:


**INFO [0154]: Successful sign in for user 'admin' from ConnectSmart Go
client at [ IP Address xxx.xxx.xxx.xxx]**