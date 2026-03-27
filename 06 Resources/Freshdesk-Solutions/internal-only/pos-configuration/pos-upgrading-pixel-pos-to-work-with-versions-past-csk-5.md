---
title: "*|POS| - Upgrading Pixel POS to work with versions past CSK 5"
freshdesk_id: 17000127363
category: "Internal Only"
folder: "POS Configuration"
status: published
created: 2022-07-27
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000127363
---

# *|POS| - Upgrading Pixel POS to work with versions past CSK 5

If a site using Pixel POS is on CSK 5 and is upgrading to a newer version of CSK then they will need to be configured to use TCP due to a code change in CSK. (Pixel POS uses a middleware called PixelKDS.exe that must be running to send orders to QSR this application rests on the server)


In order to do this make sure they are using the 16.0.3 QSRSock.DLL version peer to the PixelKDS.exe .


You will also need to verify the following file path is built out


C:\ProgramData\QSR Automations\ConnectSmart\QsrSock\Log


Place the QsrSock.xml peer to the PixelKDS.exe and update it to the correct IP for the server:


<?xml version="1.0" encoding="utf-16" standalone="yes" ?>


<QsrSock.xml>


    <Header>


        <FileVersion>12.0.4.0</FileVersion>


        <CreationDateTime>2012-01-31T14:00:00-05:00</CreationDateTime>


        <ModifiedDateTime>2012-01-31T14:00:00-05:00</ModifiedDateTime>        


    </Header>


    <DetailData>


       <LogLevel>Critical|General</LogLevel>


        <SendMessageDelay>0</SendMessageDelay>


        <CaptureData>false</CaptureData>


        <QsrSockWebServiceClient Enabled="true" MessageTimeoutSeconds="0">


            <Server Port="0x8000" Secure="false">X.X.X.X</Server>


        </QsrSockWebServiceClient>


    </DetailData>


</QsrSock.xml>


After that is in place restart the PixelKDS program on their server.


Check the log in the C:\ProgramData\QSR Automations\ConnectSmart\QsrSock\Log and verify that it shows connected to the server IP.