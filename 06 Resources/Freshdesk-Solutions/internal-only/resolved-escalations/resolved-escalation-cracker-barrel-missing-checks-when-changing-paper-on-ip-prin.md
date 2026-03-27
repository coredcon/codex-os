---
title: "*|Resolved Escalation| - CRACKER BARREL - Missing Checks When Changing Paper on IP Printer Stations - Priority: High"
freshdesk_id: 17000071060
category: "Internal Only"
folder: "Resolved Escalations"
status: published
created: 2018-05-01
updated: 2022-11-10
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000071060
---

# *|Resolved Escalation| - CRACKER BARREL - Missing Checks When Changing Paper on IP Printer Stations - Priority: High

(05/01) - JSE - CSK Server 7.3 P1 has been released to resolve the following: Printer View Backup Routing fails in some cases.


Escalation Link: [https://qsrautomations.freshdesk.com/helpdesk/tickets/130343]


> On Thu, 22 Mar at 5:08 PM , QSR Support Team <supportteamdistro@qsrautomations.com> wrote:Team, Please see the escalation, below. 
**Severity:** High**Customer:** Cracker Barrel**Company ID:** Cracker Barrel**Location / SiteID:** 227**Location Found:**Production**Product:** ConnectSmart Kitchen Server / ControlPoint**Component:**Printer Stations**Version:**6.3.107 / 3.0.121 (3.3.105 exhibits same behavior)**Smoke Test (Y \ N)**N**Support Ticket #:** 129037**Date Reported:** 03/05/2018**Account Manager:** Cynthia Manuel  **ISSUE**:   Missing Checks When Changing Paper on IP Printer Stations Checks are not printing as expected under certain circumstances. Grill1 and Grill2 IP Printer Stations are using Round Robin load balancing and are set to back-up to each other. If an order gets sent to a printer just after it loses power or the lid is opened to change paper, the order does not print at the back-up station. Back-up to that printer does not take effect until the system marks it as being down after a period of time (~10 seconds).  This time period does not seem affected by lowering “Station Timeout (seconds)” in View Manager or Write timeout in ControlPoint. **STEPS TO REPRODUCE: ** You can run the attached capture and take either printer station offline by opening the drawer or powering down for testing. Manual steps below. 1.       Ring item to Grill printers(RC: Destination 1, Department 11). Check 49 prints to Grill1 2.       Open lid of Grill1 printer 3.       Ring in next item. Check 50 prints on Grill2 4.       Ring in next item that should go to Grill 1. **This Check 51 does not print anywhere** 5.       Ring in next item, this prints Check 52 as expected on Grill2. 6.       Once the 10 seconds is up, everything prints to Grill2 as expected until Grill1 is back online. **ATTACHMENTS:**  [https://qsrautomations.sharefile.com/d-s7e5d8e9eb534c45a]** ** ·         Cracker Barrel 129037 IP Printers Dataset.zip – Dataset for Testing·         Cracker Barrel 129037 IP Printers Capture.qsrcap – Capture for Testing·         Cracker Barrel 129037 IP Printers Server Logs.log – Logs generated Testing·         Cracker Barrel 129037 IP Printers Server DB.db – DB generated in Testing **IMPACT:**  Checks are not being printed causing the cooks to not make certain food which increases customer wait time due to lost orders. **WORKAROUND:**  None at this time Jonathan EdwardsTeam Lead, Support Services|Escalation Specialist**QSR Automations Inc.**p | 502.297.0221 Option 6e | [support@qsrautomations.com]** **[]Smarter restaurants need smarter content.[Subscribe to our blog.]