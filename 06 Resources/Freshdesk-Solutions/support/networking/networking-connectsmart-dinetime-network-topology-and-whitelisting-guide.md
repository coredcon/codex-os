---
title: "*|Networking| - ConnectSmart / DineTime Network Topology and Whitelisting Guide"
freshdesk_id: 17000105567
category: "Support"
folder: "Networking"
status: published
created: 2020-06-19
updated: 2024-10-28
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000105567
---

# *|Networking| - ConnectSmart / DineTime Network Topology and Whitelisting Guide

****


**ConnectSmart Enterprise Whitelisting Guide 2023**


**For Whitelisting it is usually best to whitelist the following to cover any and all endpoints our applications may need to access:**
 
 *.qsr.cloud


*.dinetime.com


*.amazontrust.com


o.ss2.us


s.ss2.us


 


**If the customer wants to avoid using * for whatever reason, there is a current list of individual endpoints below..****  **
 
 **If the customer's security does not allow whitelisting by URL endpoint, it may be necessary for them to set up a proxy outside of their firewall to route traffic through.**


 


 


**ConnectSmart Kitchen:**
 [https://host-api.dinetime.com]
 [https://kitchen-api.dinetime.com]
 [https://service-discovery.qsr.cloud]
 [https://auth.qsr.cloud]
 [https://pos.kitchen.qsr.cloud]
 [https://status.kitchen.qsr.cloud]
 [https://kitchen-api.qsr.cloud]


[https://capacity.kitchen.qsr.cloud]


[https://notifications.kitchen.qsr.cloud]
 [https://connected-clients-ingestion.qsr.cloud]


[https://settings.kitchen.qsr.cloud]


[https://rt.metrics.qsr.cloud]


[https://storage.kitchen.qsr.cloud] 


[https://qsr-production-kitchen-storage.s3.amazonaws.com]
 Port: 443
 Secure connection: HTTPS/SSL SHA-256 with RSA Encryption


 


**DineTime:**
 [https://host-api.dinetime.com]
 [https://service-discovery.qsr.cloud]
 [https://auth.qsr.cloud]
 [https://reporting.dinetime.com]


[https://visit-events-api.dinetime.qsr.cloud]


[https://connected-clients-ingestion.qsr.cloud]


[https://visitpush-api.qsr.cloud] 


 [https://licenseapi.qsr.cloud] 


[https://entcore-settings-api.qsr.cloud/] 


[https://gms-precalculatedquotes-api.qsr.cloud/]
 Port: 443
 Secure connection: HTTPS/SSL SHA-256 with RSA Encryption


 


**TeamAssist:**
 [https://viewer.teamassist.qsr.cloud]
 [https://viewer.teamassist.qsrautomations.com]
 [https://host-api.dinetime.com]
 [https://service-discovery.qsr.cloud]
 [https://auth.qsr.cloud]
 Secure connection: HTTPS/SSL SHA-256 with RSA Encryption


 


**Certificate Revocation:**


The following addresses need to be whitelisted in versions 2020.X and later:


o.ss2.us


s.ss2.us


crl.rootg2.amazontrust.com


ocsp.rootg2.amazontrust.com


ocsp.rootca1.amazontrust.com


crl.amazontrust.com


[ocsp.sca1b.amazontrust.com]


 


**As of 03/29/2023 (DE-2721) ****this list of URLs has been updated to include: **


[crl.rootca1.amazontrust.com]
 [crl.rootg2.amazontrust.com]
 [crl.sca1b.amazontrust.com]


[ocsp.rootca1.amazontrust.com]
 [ocsp.rootg2.amazontrust.com]
 [ocsp.sca0a.amazontrust.com]
 [ocsp.sca1a.amazontrust.com]
 [ocsp.sca1b.amazontrust.com]
 [ocsp.sca2a.amazontrust.com]
 [ocsp.sca3a.amazontrust.com]
 [ocsp.sca4a.amazontrust.com]


[crt.rootca1.amazontrust.com]
 [crt.sca0a.amazontrust.com]
 [crt.sca1a.amazontrust.com]
 [crt.sca1b.amazontrust.com]
 [crt.sca2a.amazontrust.com]
 [crt.sca3a.amazontrust.com]
 [crt.sca4a.amazontrust.com]


with each of the “sca” entries being a different encryption type.