---
title: "*|CSH| - Installing and Configuring DineTime POS Interface"
freshdesk_id: 17000060062
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host - Installation and Application Management"
status: published
created: 2017-09-15
updated: 2022-12-12
views: 0
tags: ["BJ's", "Boston Pizza"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000060062
---

# *|CSH| - Installing and Configuring DineTime POS Interface

**Installing DineTime POS Interface**


**Directory Structure**


The DineTime POS Interface does not have an installer, so the executable and related files need to be manually placed in the correct locations.


The interface must be installed on the same server that runs DineTime Host Server.


- 
**Program Files**


- Navigate to the ConnectSmart folder
For 64-bit operating systems, the path is C:\Program Files (x86)\QSR Automations\ConnectSmart
If using a 32-bit operating system, the folder location is C:\Program Files\QSR Automations\ConnectSmart


- Create a folder in this directory named DineTimePOSInterface


- Place the DineTimePOSInterface.exe and all included files (except the DineTimePOSInterfaceSettings.xml) in the new DineTimePOSInterface folder


- 
**Data Directory**


- Go to C:\ProgramData\QSR Automations\ConnectSmart


- Create a folder in this directory named DineTimePOSInterface


- Open the DineTimePOSInterface folder and create a Data folder in it


- Place the DineTimePOSInterfaceSettings.xml in the Data folder


**Running DineTime POS Interface as a service**


The DineTime POS Interface can be installed as a service for easy startup and operation.


- Open a Command Prompt with administrative privileges


- In the Command window, navigate to the DineTimePOSInterface folder:


- In the command window, type “DineTimePOSInterface.exe /i” to install the service.


- The service installs with the name “QSR DineTime POS Interface” and the Startup Type of Manual. If desired, change the Startup Type to Automatic.


---


**POSiTouch TSConnect Settings**


All instances of POSiTouchTSConnect need to be updated in order to receive guest information from the DineTime POS Interface.


These settings are not available in the POSiTouchTSConnect Editor, and must be manually added to two of POSiTouchTSConnect’s XML files


- 
**PCGeneralSettings.xml**


- Navigate to the POSiTouchTSConnect data directory and open the PCGeneralSettings.xml


- At the end of the DetailData node (under the <DaysToArchivePOSXmlFiles> tag but above the closing </DetailData> tag), add the following section:

<HostessMessaging>
  <Enabled>False</Enabled>
  <OrderInputDirectory>c:\SC\xmlorder</OrderInputDirectory>
  <LoyaltyItemNumber>6995</LoyaltyItemNumber>
  <MemoItemNumber>1587</MemoItemNumber>
  <GuestInfoItemNumber>7511</GuestInfoItemNumber>
  <AllergyItemNumber>7512</AllergyItemNumber>
</HostessMessaging>

Note: The HostessMessaging XML node above is shown with default settings. 


- 
**PCNetworkSettings.xml**


- In the same directory as the PCGeneralSettings.xml is another file named PCNetworkSettings.xml


- Open PCNetworkSettings.xml and add a HostessPort tag immediately above the closing </DetailData> tag
<HostessPort>32110</HostessPort>


- Enter the port that POSiTouchTSConnect should use for DineTime Host message processing
The <HostessPort> in PCNetworkSettings.xml must match the <Port> specified in DineTimePOSInterfaceSettings.xml.


**DineTime POS Interface Settings**


The DineTimePOSInterfaceSettings.xml is supplied by QSR and is typically pre-configured to client specifications.  The following section includes a brief explanation of commonly used settings, in the event that additional configuration is required.


The basic structure of the XML is outlined below. Some XMLs may contain additional settings, based on the type of POS in use.


<DineTimePOSInterfaceSettings>
<TimerFrequency>100</TimerFrequency>
<LoggingDaysThreshold>7</LoggingDaysThreshold>
<UserDefinedValues/>
<Operations>
<Operation Type="OpenCheckOnVisitSeated">
<ExecutionDelay>5 seconds</ExecutionDelay>
<OpenCheckForLoyaltyCustomersOnly>false</OpenCheckForLoyaltyCustomersOnly>
<CommandLineOnly>false</CommandLineOnly>
<CommandLineName>OpenCheckWithPOSITouchOnVisitSeated</CommandLineName>
<VisitsSeatedHandler Type="POSITouch">
<Port>32110</Port>
</VisitsSeatedHandler>
</Operation>
</Operations>
</DineTimePOSInterfaceSettings>


**Required Settings**


The Operation Type, Visits Seated Handler Type, and Visits Seated Handler Port are the only required settings in the XML.


- Operation Type: Indicates the type of operation the DineTimePOSInterface should create and run. “OpenCheckOnVisitSeated” is the Operation Type the interface uses to open new checks in POSiTouch when a party is seated in DineTime Host.


- Visits Seated Handler Type: Indicates the handler to use when notifying an external component of an applicable visit seated event. “POSiTouch” is typically the Visits Seated Handler Type that should be used.


- Visits Seated Handler Port: The port to use when broadcasting data to the visits seated handler. The Visits Seated Handler Port must match the HostessMessaging port from POSiTouchTSConnect’s PCNetworkSettings.xml.


**Optional Settings**


Though the remaining settings are optional, QSR recommends their use for optimal performance.


- Logging Days Threshold: The number of days of historic logging data that should be kept in the log file at any given time. The default setting is 7 days.


- Execution Delay: The amount of time that should elapse between operation execution attempts. The default is 5 seconds. Time values may be input into this field in the following formats:


- Milliseconds: 5000


- Seconds: 1 second, 10 seconds


- Minutes: 1 minute, 5 minutes


- Hours: 1 hour,  36 hours


- Days: 1 day, 7 days


- Open Check for Loyalty Customers Only: Restricts new check creation to loyalty guests only. The default is False