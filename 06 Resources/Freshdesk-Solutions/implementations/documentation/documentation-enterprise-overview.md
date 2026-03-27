---
title: "*|Documentation| Enterprise Overview"
freshdesk_id: 17000129439
category: "Implementations"
folder: "Documentation"
status: published
created: 2022-11-09
updated: 2022-11-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000129439
---

# *|Documentation| Enterprise Overview

**QSR Enterprise Overview**


QSR Enterprise connects ConnectSmart Kitchen (CSK) and Host to the Cloud, allowing for more effective Kitchen, Guest, and Seating management. Data sent from ConnectSmart Kitchen and Host is stored in QSR Enterprise, where it is easily accessible in the QSR Enterprise Portal. The QSR Enterprise Portal also allows for advanced configuration of settings, which are stored in QSR Enterprise and can be synced back to sites, providing more efficient company-side restaurant management.


**Security**


- QSR Enterprise synchronizes settings over a secure HTTPS/SSL outbound connection to the Cloud without requiring any complicated inbound firewall rules or routing. (See Appendix A for settings.)

- The QSR Enterprise Portal facilitates the creation of users and the control over their ability to view, modify, and apply configurations within the Enterprise Portal.


**ConnectSmart Enterprise**


ConnectSmart Kitchen integrates seamlessly with ConnectSmart Enterprise (CSE) to provide an easy, all-in-one solution for kitchen design and management. The CSK application, in conjunction with the ConnectSmart Enterprise Portal, offers a cloud-based option for managing the function and design of CSK at all restaurant locations and offers reporting services to analyze restaurant performance.


**Data from ConnectSmart Enterprise to CSK Site**


**Building a Dataset**


**Data**


-  CSE ensures the accuracy of a new CSK configuration by performing multiple data validations at different levels when building a dataset for sites.

-  The current dataset is backed-up and saved in CSK before the new dataset is applied.

-  The new dataset will not be applied to the site until CSK is restarted or EOD is run.

-  Site-level reporting on restaurant performance is accessible in CSE Portal.


**Templates**


- CSE Portal allows for the custom creation of datasets in the Cloud. These datasets can then be applied to an individual or multiple sites via the Portal.

- CSE Portal allows users to manage CSK settings and create reusable templates that can be applied to one or many sites, accommodating any operational variations.

- These templates serve as building blocks, allowing CSE Portal users to create datasets that encapsulate the operational needs of a site or group of sites.


**Data Flow from CSK to ConnectSmart Enterprise**


Four different types of data flow from the CSK site to ConnectSmart Enterprise:


- Speed of Service

- Bin History

- View Metrics

- Kitchen Metrics


**Note:** Enabled settings depend on your license. Upon start-up, the Kitchen Server log will reflect which of these settings is enabled and which is disabled.


Kitchen Server data is pushed at regular, preset intervals to CSK Enterprise. Once a record is received, it is marked “synced” and will not be resent. If, for some reason, the record fails to synch, it will be identified as “un-synced” and be resent when the connection is restored.


Synced data is viewed in the CSK Enterprise Portal via Reports and Dashboard, as well as in custom reports via third party API calls.


**DineTime Enterprise**


DineTime Enterprise allows for managing site settings remotely, viewing guest management metrics via Dashboards and Reports, and maintaining a backup of guests and reservations in the DineTime Enterprise Portal. Settings can be managed at an individual site or across multiple sites at once. Various dashboards and downloadable reports give key insights into daily, weekly, monthly, and yearly operational information. A company-wide GuestBook allows guest information to be shared across all sites for a better dining experience.


**Data Flow from DineTime Enterprise to DineTime Site**


Settings configured in the DineTime Enterprise Portal are stored in DineTime Enterprise until DineTime Server requests them. DineTime Server makes an outbound request at regular intervals to check for any updated settings. Settings updated since the last request are returned to DineTime Server as a response on the same outbound call. This occurs on a 60 second interval, at which time the settings are downloaded to the local database at the restaurant and are automatically reflected in the connected Host clients.


**Templates vs. Site Settings**


Many operational settings are available within the DineTime Enterprise Portal at both the company level within a template and at the site level. The DineTime templates allow an organization to configure uniform settings across all sites or a specific sub-set of sites. They can also be used when a single settings change is necessary all locations without having to update each site individually. Conversely, settings may be updated for individual sites when there are minor operating variations at specific locations. This allows for more flexibility in how individual sites are managed.


While a majority of the operational settings for a restaurant can be bulk updated via the templates, there are some settings that may only be configured at the site level. These are settings that are likely to vary from site to site such as Floor Plans, Reservations Availability, Site Users, Servers, etc. These settings can be found within the "Manage" and "Floor Plans" tabs and are only available at the site level in the DineTime Enterprise Portal. Settings within the "Customize" tab are available at both the site and template level for configuration. See chart below.


**Applying Site Settings**


Settings changes at the site level are saved and synced almost immediately. The settings may be updated on the fly, and updates are stored until the next update request is received from DineTime Server. The updated settings are synced within 60 seconds, saved to the local database, and are available in the Host clients without requiring a restart.


**Applying Templates**


Templates allow the user to configure settings on an ongoing basis without affecting site operations until the template settings are applied. Changes made to settings in a template are stored until the user explicitly makes the decision to “Apply” the template to a site or sites. While settings changes made at the site level are reflected at the restaurant almost immediately, settings applied via a template may take up to 15 minutes to sync to all sites. Timing will depend on the number of sites to which a template is applied. The chart below outlines the process of applying settings from a template.


**Data Flow from DineTime Site to DineTime Enterprise**


Most data is pushed from the site to DineTime Enterprise at preset intervals. Information such as settings, changes, and guest data occur every few minutes by default. Reservations and Guest Visits data is updated immediately, synced to DineTime Enterprise, and available for viewing in the DineTime Portal. Additionally, DineTime Consumer and WebAhead information is updated in DineTime Enterprise and displayed in the DineTime Enterprise Portal.


Data sent from DineTime Server (and DineTime Consumer and WebAhead) to DineTime Enterprise may be viewed in the DineTime Enterprise Portal via the Insight tab. The data and metrics are reported under the Guest Dashboard, Guest Statistics, Floor Statistics, Wait List Analysis, Reservations, and Guest Reports tabs. Third Party API calls may also be utilized to create custom reports.


**Appendix A**


**Registration Code**


To take full advantage of all the features available for DineTime and ConnectSmart, a QSR Enterprise connection is required. In order to connect to QSR Enterprise, a registration code may be obtained from the QSR Enterprise Portal. From the Company level landing page, select the site for which you want to generate the registration code. A list of enterprise options configured for your use will be displayed under Manage/Server Registration. This registration code is unique to the site and will ensure that settings configured in Portal are sent down to the correct location, as well as ensuring that data metrics synced up from the site are available in the correct QSR Enterprise Portal account.


Any product that is a part of your Enterprise Solution(s) will require separate registration.


**Appendix B**


**License Files**


Sites with enterprise can utilize a license file in the Portal or manually imported at the site level.


License files are issued by site code on the Server hosting the solution. These are MAC address specific. A wired LAN connection is preferred.


If you chose to have Enterprise push the license file, complete this step before registering with Enterprise. The registration process will send the license file to the site.


 


1. Open the QSR License Manager


2. Copy the Site code listed and send to Validation@qsrautomations.com along with the following information:


-  Subject: |Validation Request| - (Insert your Brand or Company name)

-  Site Name

-  Site Address

-  Site License Code

-  ConnectSmart Kitchen or DineTime Version

-  # of Stations


 3. When you receive the e-mail response, the license has been created and is available for push to the site from Enterprise.


 4. Complete the registration process from the Portal as noted in Appendix A. Registering the solution will check for a valid license file.


 5. Now that the license has been pushed from Enterprise start the service. If the service is unable to start navigate to the C:\ProgramData\QSR Automations\ConnectSmart\(solution in question)\Log folder and look for Enterprise Check in messages.


**Note:** If the Service was already running, the license will NOT update. Restart the service to ensure the connection to Enterprise was established.


If you choose to manually import the license, the process is:Note: If the Service was already running, the license will NOT update. Restart the service to ensure the connection to Enterprise was established.


If you choose to manually import the license, the process is:


1. Start with the same steps as above by requesting the File through Validation@qsrautomations.com


2. You will receive an email back with an attached .lic file


3. Upon receiving the .lic file from validations save it to a location on the Server


4. Open the QSR License Manager and chose Import


5. Navigate to the .lic file and import the file


6. Notice the product name, version, expiration date and whether it is valid on this computer. If these are not correct, contact your QSR Representative for resolution.


**Note:** If the service was already running, the license file will NOT update. Restart the service to load the license.


7. Attempt to start any Enterprise Services you have registered and licensed. If they do not start, review the logs as noted above. If there is no mention of a valid license:


- Restart the service

- Check the logs again


If you continue to have license issues, contact your QSR Automations Representative.