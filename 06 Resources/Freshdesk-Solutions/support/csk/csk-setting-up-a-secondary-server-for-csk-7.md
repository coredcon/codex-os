---
title: "*|CSK| - Setting up a Secondary Server for CSK 7+"
freshdesk_id: 17000127064
category: "Support"
folder: "CSK"
status: published
created: 2022-07-06
updated: 2025-07-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000127064
---

# *|CSK| - Setting up a Secondary Server for CSK 7+

**Setting up a Secondary Server for CSK 7+**


**Installation Notes:**


 


When you install Kitchen on the secondary server confirm that the version you are installing matches the version installed on the primary server.


The secondary instance will not work correctly if there is a version mismatch.


 


**Configuration:**


 


**Primary Configuration:**


On the primary server you will need to define the IP of the Secondary Server in the ConnectSmart Network Configuration tool:


- Check the box to enable the Secondary Kitchen Server in the config and then input the IP of the secondary server

- **NOTE:** The Local IP address should always be the IP of the computer that you are currently on
  


                    You will also need to define the secondary server IP in the ConnectSmart Network settings in ControlPoint


 


 


**Secondary Configuration:**


 


                              On the secondary server you need to set the IPs for both the primary and the secondary as well.


- **NOTE:** The Local IP address should always be the IP of the computer that you are currently on


 


Set the service Startup Type in the Windows Services menu for the secondary via the service properties (See options below)


- **Manual**: The service on the Secondary Server would need to be started manually in the event the primary server went offline. You would need to regularly start the service to sync any dataset changes and to make sure the current license information has synced from the Primary Server.

- **Automatic/Automatic (Delayed Start)**:** **Both options are good choices that will allow the secondary to take over immediately should the primary server drop offline for any reason.

- **Disabled**: This option would disable the Secondary server completely

**NOTE: **Once the primary services are restored you would need to restart the service son the secondary to switch back to the primary server.


**Dataset:**


 


You will want to make sure that the Dataset has redundancy enabled:


In the local kitchen Builder this is in the System Settings>System Recovery>Enable redundancy.


 


 


For a Portal Dataset it will be on the System Template>System>Enable Redundancy


 


 


The dataset should not need to be manually copied to the secondary server and should be synced from the primary when the Kitchen Server services are restarted or at End of Day.


 


**Licensing:**


 


In CSK 7+ the secondary server is not licensed separately.


It will sync a license from the primary server that will be valid through the expiration date of the license file present on the primary when it syncs to the secondary.


 


**Testing:**


Start the services on the Secondary Server while the Primary is running so that it can sync the Dataset and License information from the Primary.


Once you verify that everything starts correctly stop the Kitchen Server service on the Primary and verify that the failover to the secondary server is successful.