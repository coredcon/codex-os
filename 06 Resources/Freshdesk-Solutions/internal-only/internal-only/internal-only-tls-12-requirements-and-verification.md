---
title: "|Internal Only| - TLS 1.2 Requirements and Verification"
freshdesk_id: 17000132220
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2023-03-21
updated: 2023-11-03
views: 0
tags: ["TLS", "Registry", "Compliance"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000132220
---

# |Internal Only| - TLS 1.2 Requirements and Verification

As of 03/21/2023, QSR has stopped support for TLS 1.0/1.1. 

 **Why is TLS 1.2 Compliance Important?** Here at QSR Automations, our intention is to continuously deliver solutions that work to meet the requirements of the most security-sensitive organizations. In order to align with the technology and regulatory standards for Transport Layer Security (TLS) we will be updating the TLS configuration for all enterprise endpoints to a minimum of version TLS 1.2.  We have disabled all TLS 1.0 and TLS 1.1 communication to and from our Enterprise endpoints. This will impact all users on CSK 5 - 7.3.107 and DineTime 5, as these versions are **NOT** compatible with the TLS 1.2 communication protocol and therefore not compliant with current security requirements.   


**Troubleshooting Steps**


Please assist our customers in upgrading their ConnectSmart Kitchen or ConnectSmart Host. Please see the above list of EOS versions of the software. 


We can also ask the customer to check their registry to ensure that TLS 1.2 is enabled. This will become especially important if the customer is running the Windows 7 operating system. They  **MUST** be on at least Windows 7 Service Pack 1 (KB3080079) in order to have TLS 1.2 support. If they do not have the correct service pack, they may be able to run these patches listed on [Microsoft's website].  Additionally, they have to manually add the TLS 1.2 Registry Key (**REMEMBER QSR DOES NOT EDIT THE CUSTOMERS REGISTRY FOR THEM**). You can direct the customer to the following [link] for assistance in enabling TLS 


** ******How to check if TLS 1.2 is enabled in the Registry****


- Open regedit utility

- Open ‘Run‘, type ‘regedit‘ and click ‘OK‘.

- 


- Navigate to In Registry Editor, navigate to the path : HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols

- You should be able to see TLS 1.2 listed under Protocols.

- The customer would add the TLS 1.2 Registry Key here if is were not enabled (WE SHOULD NOT MAKE CHANGES TO THE CUSTOMER'S REGISTRY FOR THEM)


**This is how the TLS 1.2 Client and Server keys would look if they are properly enabled. **


**
**


******** Please also keep in mind that we should not walk customers through making changes in the registry. We can provide them with the linked Microsoft articles, but it is up to their IT team to work through the registry.*********