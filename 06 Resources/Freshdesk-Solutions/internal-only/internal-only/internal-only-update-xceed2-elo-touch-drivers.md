---
title: "*|Internal Only| - Update Xceed2 Elo Touch Drivers"
freshdesk_id: 17000113784
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2021-02-05
updated: 2023-11-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000113784
---

# *|Internal Only| - Update Xceed2 Elo Touch Drivers

Currently deployed Xceed2 devices will not immediately work with the new Elo K devices. In order to get themt o work we need to update the device with the new drivers supplied by Elo. This can be done in one of two ways.


Method 1: Manual installation


1. Drop the .cab file into the Hard Disk Folder


2. Run the following command in the cmd prompt:


       wceload /noui "Hard Disk\ EloTouch_2.6.2_CE7_ARMV7.CAB"


If this CAB file is installed successfully, you will see the following files in \Hard Disk\System\ folder:


 


eloApi.dll


eloBeep.dll


eloCpl.dll


eloTalk.exe


eloUsb.dll


eloVa.exe


3. Reboot the device. Touch should now be working


**Alternately, you can drop the .cab file into the \Hard Disk folder and run the included .bat file to install.


File Download link for manual install:


[][][https://qsrautomations.sharefile.com/d-s286268d5d5934375962d1d4bd014e77d]


Method 2: ControlPoint Template


1. You will want to create a Displayclient CE template and place the two files in the bin directory as below:


 


 


 


2. Next, add a process for the .bat file and include an argument of /p as seen below:


 


 


3. Assign and reboot the device and it should apply the template, running the .bat file and installing the drivers. 


 


 If this CAB file is installed successfully, you will see the following files in \Hard Disk\System\ folder:


 


eloApi.dll


eloBeep.dll


eloCpl.dll


eloTalk.exe


eloUsb.dll


eloVa.exe


 


4. Reboot one more time and test the touch functionality.


Sharefile link to install via Template:


[][][][https://qsrautomations.sharefile.com/d-s1b80d20fe0664c228e2d73279b65096c]