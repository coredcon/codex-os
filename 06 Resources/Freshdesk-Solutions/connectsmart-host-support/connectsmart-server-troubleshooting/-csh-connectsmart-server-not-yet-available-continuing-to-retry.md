---
title: "* |CSH| - ConnectSmart Server not yet available, continuing to retry..."
freshdesk_id: 17000060017
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Troubleshooting"
status: published
created: 2017-09-14
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000060017
---

# * |CSH| - ConnectSmart Server not yet available, continuing to retry...

**Issue:** User receives the following error when launching the ConnectSmart Host client on a PC: 


"ConnectSmart Server not yet available, continuing to retry..."


**Troubleshooting:**


- Verify the 'QSR ConnectSmart Server' service is running on the ConnectSmart Host Server.
If the service will not start, check the HostessServer logs for startup errors.

- Check the ConnectSmartNetwork configuration on the ConnectSmart Host Server against IPCONFIG to very that their IP configuration did not change.  If so, the IP must be set back to what it was previously, or the ConnectSmart Network Configurator must be updated on each machine running QSR applications to reflect the new ConnectSmart Host Server IP.

- If the Client giving the error is on a separate machine from the Server, verify that you can ping the Client IP from the Server machine.  If not, there may be a line of site issue their IT team will need to resolve.