---
title: "*|Networking| - Adding Secondary Server IP to QSRSock.xml"
freshdesk_id: 17000116102
category: "Support"
folder: "Networking"
status: published
created: 2021-04-30
updated: 2023-11-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000116102
---

# *|Networking| - Adding Secondary Server IP to QSRSock.xml

When a site is using TCP with QSRSock.xml and have a secondary server for redundancy. You need to add an additional line to the xml listing the secondary server IP. Below is an example of how the QSRSock.xml should look. The added line is highlighted. 


**With Secondary Server**


<CaptureData>false</CaptureData>
<QsrSockWebServiceClient Enabled="true" MessageTimeoutSeconds="0">
<Server Port="0x8000" Secure="false">192.168.193.50</Server>
<Server Port="0x8000" Secure="false">192.168.193.51</Server>
</QsrSockWebServiceClient>


**Original Format**


<CaptureData>false</CaptureData>
        <QsrSockWebServiceClient Enabled="true" MessageTimeoutSeconds="0">
            <Server Port="0x8000" Secure="false">192.168.193.50</Server>
        </QsrSockWebServiceClient>