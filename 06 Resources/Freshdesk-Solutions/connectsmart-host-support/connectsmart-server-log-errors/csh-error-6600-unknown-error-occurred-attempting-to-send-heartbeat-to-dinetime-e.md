---
title: "*|CSH| - ERROR [6600]: Unknown error occurred attempting to send heartbeat to DineTime Enterprise."
freshdesk_id: 17000050049
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Log Errors"
status: published
created: 2017-05-03
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000050049
---

# *|CSH| - ERROR [6600]: Unknown error occurred attempting to send heartbeat to DineTime Enterprise.

**Issue:  **


ConnectSmart Host Server cannot send heartbeat event to QSR Enterprise. The ConnectSmart Host server log file has the following entry:    


                ERROR [6600]: Unknown error occurred attempting to send heartbeat to DineTime Enterprise.


                                  HTTP Request Failure: ServiceUnavailable - Service Temporarily Unavailable


                                     at QsrAutomations.Gaia.Managers.PolarisManager.sendServiceRequest[TResponse,TRequest](TRequest                                                           requestData, String uriTypePrefix, String uri)


                                     at QsrAutomations.Gaia.Managers.PolarisManager.heartbeat()


**Environment**—


ConnectSmart Host Server , Windows OS


URI: [https://host-api.dinetime.com/]  Port: 443 Secure connection: HTTPS/SSL SHA-256 with RSA Encryption


**Resolution**-


1: restart ConnectSmart Server Service 


2: reboot the ConnectSmart Host Server 


3: Contact Network team