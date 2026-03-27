---
title: "*|Internal Only| - Setting up a new VM in Oracle VirtualBox on Support Lab"
freshdesk_id: 17000069526
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2018-03-29
updated: 2022-11-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000069526
---

# *|Internal Only| - Setting up a new VM in Oracle VirtualBox on Support Lab

# 


From the VirtualBox Manager, select “New”


Provide a name for the VM session, select the type of OS and version, and hit “Next”


Set the RAM amount - usually we will set to 4096 Mb – and hit “Next”


Choose “Create a virtual hard disk now”, and hit “Create”


For our lab, we will use “VDI” as the hard disk file type, and hit “Next”. The other types are used for exporting a VM to someone else using a different VM vendor.


You can choose either “Dynamically allocated” or “Fixed size” for the growth type. If you are only creating a VM for temporary use, then choose Dynamic to use the minimum amount of disk space. Permanent VMs should be set for Fixed to increase performance.


The hard disk location should already be defaulted based on the name you gave the session. Set the disk size based on what OS you are using and what software you are installing. 50 Gb should be good for most VMs, but if you plan on installing more than one product, 100 Gb may be better. Hit “Create” to proceed.


Right-click on the newly created session and choose “Settings”


On the General – Advanced tab, set “Shared Clipboard” and “Drag’n’Drop” to “Bidirectional” so you can easily move files to and from the VM session.


On the Storage page, select the CD drive then click the CD image under Attributes to select the installation image for your chosen OS. This will mount that image for installation when you launch the VM for the first time.


On the Network page, change the Adapter 1 from “NAT” to “Bridged Adapter”. This will allow us to maintain network visibility through the Lab host. If needed, you can click on Advanced to manually change the static MAC address for the new VM.


On Shared Folders, you can add the host computers directories as virtual drives on the VM. Click the folder with the plus sign to define the path, folder name, and options. On the existing VMs, we mapped the Lab Installs and Useful Tools folders from the lab host’s desktop.


Once you have added all of the desired Shared Folders, hit “OK” to proceed. You are ready to launch the VM and install the OS. Right-click on the new session, and choose “Start” – “Normal Start”.


From this point, the installation should proceed as normal. Once the Installation has completed, you should set a static IP address and complete all Windows updates for that OS. The Activation Keys are in the Useful Tools folder on the host system desktop. Please make sure to create a “support” user account with admin rights on the new VM and set the password to “!QAZse4#” to match the other VMs.


Once all updates are completed, the final step is to enable the shared folders, copy/paste, and drag and drop at the device level. To do this, go to Devices – Insert Guest Additions CD Image.


Run the “VBoxWindowsAdditions.exe” and follow all prompts. Make sure to select the “Always trust software from Oracle Corporation”


After rebooting, to check to make sure the module installed properly, check for your Lab Installs and Useful Tools network drives. Note that after the install, the VM desktop resolution will probably reset to 800 x 600, but can be changed back.