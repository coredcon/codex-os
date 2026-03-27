---
title: "*|CSH| - Command Line Enterprise Registration with /PM Switch (Disregard Server MAC Address, Darden), Darden)"
freshdesk_id: 17000059681
category: "ConnectSmart Host Support"
folder: "ConnectSmart Host - Installation and Application Management"
status: published
created: 2017-09-07
updated: 2023-11-03
views: 0
tags: ["Darden", "Registration", "/PM"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000059681
---

# *|CSH| - Command Line Enterprise Registration with /PM Switch (Disregard Server MAC Address, Darden), Darden)

**Issue**:


Darden has their ConnectSmart Host Servers installed on VMs.  Each server has a virtual NIC, and the MAC Address can change at random.  As a workaround, we created a command line registration method that disregards the MAC Address and uses an Enterprise ID instead.  


**Solution**: 


Use the following command:


**DineTimeRegistration.exe <Registration Code> /pm**


The registration process will create the DineTimeEnterprise.xml file in the following path:


**C:\ProgramData\QSR Automations\ConnectSmart\Common\Data**


Normal registration creates XML with Enterprise Token only.  /PM Switch creates an Enterprise Token and EnterpriseID. (See below examples).


**Normal DineTimeEnterprise.xml:**


<?xml version="1.0" encoding="utf-16" ?>
<!--QSR Automations-->
<DineTimeEnterprise.xml>
 <DineTimeEnterpriseSettings>
 <DisableEnterprise>false</DisableEnterprise>
 <EnterpriseUseDefaultWebProxy>true</EnterpriseUseDefaultWebProxy>
 <EnterpriseAcceptAllSSLCertificates>false</EnterpriseAcceptAllSSLCertificates>
 <EnterpriseDestinationIPAddressOverride></EnterpriseDestinationIPAddressOverride>
 <Products>
 **<Product ID="Hostess" EnterpriseToken="e2eea322-b527-49ec-a783-466e4edad9ca" />**
 </Products>
 </DineTimeEnterpriseSettings>
</DineTimeEnterprise.xml>


**DineTimeEnterprise.xml created with /pm switch:**


<?xml version="1.0" encoding="utf-16" ?>
<!--QSR Automations-->
<DineTimeEnterprise.xml>
 <DineTimeEnterpriseSettings>
 <DisableEnterprise>false</DisableEnterprise>
 <EnterpriseUseDefaultWebProxy>true</EnterpriseUseDefaultWebProxy>
 <EnterpriseAcceptAllSSLCertificates>false</EnterpriseAcceptAllSSLCertificates>
 <EnterpriseDestinationIPAddressOverride></EnterpriseDestinationIPAddressOverride>
 <Products>
**      <Product ID="Hostess" EnterpriseToken="465643ee-c71a-4616-aac6-328b32ca5ddb" EnterpriseID="MAAwAC0ANQAwAC0ANQA2AC0AQgA4AC0ANQA3AC0AMgA1AA==" />**
 </Products>
 </DineTimeEnterpriseSettings>
</DineTimeEnterprise.xml>