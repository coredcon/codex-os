---
title: "*|Internal Only| - 8 CMD Windows Network Commands for Support Teams"
freshdesk_id: 17000084206
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2019-01-14
updated: 2023-11-03
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000084206
---

# *|Internal Only| - 8 CMD Windows Network Commands for Support Teams

**1. PING**


ping is one of the most basic yet useful commands you could know. It tells you whether your computer can reach some destination IP address or domain name, and if it can, how long it takes data to travel there and back again.


By default it sends 4 packets, each one waiting 4 seconds before timing out. You can increase the number of packets like this:


ping [www.google.com] -n 10


And you can increase the timeout duration like this (value is in milliseconds):


ping [www.google.com] -w 6000


**2. TRACERT**


tracert stands for Trace Route. Like ping, it sends out a data packet as a way to troubleshoot any network issues you might have, but instead tracks the route of the packet as it hops servers.


The command outputs a line-by-line summary of each hop, including the latency between you and that particular hop and the IP address of that hop (plus domain name if available).


Why do you see three latency readings per hop? Because tracert sends out three packets per hop, in case one of them gets lost or takes an inordinate amount of time that doesn’t represent your true latency. It’s best practice to average the three.


**3. PATHPING**


pathping is similar to tracert except more informative, which means it takes a lot longer to execute. After sending out packets from you to a given destination, it analyzes the route taken and computes packet loss on a per-hop basis.


**4. IPCONFIG**


ipconfig may just be the most-used networking command on Windows. Not only is it useful for the information it provides, but you can combine it with a couple switches to execute certain tasks.


The default output shows every network adapter on your system and how they resolve. The **IPv4 Address** and **Default Gateway** details under the Wireless LAN Adapter and Ethernet Adapter sections are the most important to know.


Use this switch to flush your DNS cache:


ipconfig /flushdns


Flushing the DNS cache can help when your internet is working, but a specific website or server is unreachable for some reason (e.g. a website times out and won’t load.


**5. GETMAC**


Every device that’s compliant with IEEE 802 standards has a unique MAC address (Media Access Control). MAC addresses are assigned by the manufacturer and are stored in the device’s hardware. Some people use MAC addresses to [limit which devices can connect to the network].


You may see more than one MAC address depending on how many network-related adapters are on your system. For example, Wi-Fi and Ethernet connections would have separate MAC addresses.


**6. NSLOOKUP**


nslookup stands for Name Server Lookup. It’s a nifty utility that’s packed with a lot of power, but most users don’t need all of that power. For regular folks like you and me, its main use is finding out the IP address behind a certain domain name.  Note that certain domain names aren’t tied to a dedicated IP address, which means that you may get different IP addresses every time you run the command. This is normal for bigger websites because they spread their workload across many different machines.


If you want to convert an IP address into a domain name, just type it into your browser and see where it leads. Not all IP addresses lead to domain names though, and many IP addresses aren’t reachable over the web.


**7. NETSTAT**


netstat is a tool for network statistics, diagnostics, and analysis. It’s powerful and complex, but can be simple enough if you ignore the advanced aspects that you don’t need to know about (assuming you aren’t managing a massive business or campus network, for example).  By default, the command shows all “active connections” on your system whether those connections are on LAN or across the internet. An active connection doesn’t mean data is being moved — it could just mean a port that’s open and ready to accept a connection.


Indeed, netstat is mostly useful to regular users for its ability to show port information, and that can come in handy [when you need to forward ports].


But the command also has about a dozen switches that change what kind of information is displayed, such as the -r switch which shows a routing table instead.


** **


**8. NETSH**


netsh stands for Network Shell. It’s a command that lets you view and configure pretty much every network adapter on your system, in more detail and granularity than any of the preceding commands.


Running the netsh command on its own will shift the Command Prompt into network shell mode. There are several different “contexts” within this shell, including one for routing-related commands, one for DHCP-related commands, and one for diagnostics, among others. But you can use it to run individual commands, too.


To see all network shell contexts:


And to see all commands within a context:


You can drill down one more layer to find all of the subcommands within those commands:


So for example, you can run this command to view all of the wireless network drivers on your system and their properties:


netsh wlan show drivers


It’s an advanced command that’s complex enough to deserve an entire article of its own. Just know that if you want to get real technical with your network configuration, you’ll probably need to use this command line utilit