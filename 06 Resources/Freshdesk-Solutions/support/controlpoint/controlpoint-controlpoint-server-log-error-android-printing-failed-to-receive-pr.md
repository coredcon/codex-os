---
title: "|ControlPoint| - ControlPoint Server Log Error (Android Printing): Failed to receive printer write response"
freshdesk_id: 17000141163
category: "Support"
folder: "ControlPoint"
status: published
created: 2024-05-23
updated: 2025-04-04
views: 0
tags: ["Android Printing"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000141163
---

# |ControlPoint| - ControlPoint Server Log Error (Android Printing): Failed to receive printer write response

This article will provide basic information regarding this error and known causes and workarounds:

Error Example:


ControlPoint sends a "Printer Write Request" every time that it has a batch of commands that it wants the printer to execute (usually this is to print a receipt, though could also be to store an image in non-volatile memory).


DeviceAgent has to respond back in a timely manner, or else it considers the print job to have failed ("Failed to receive printer write response"). ControlPoint uses the Write Timeout configuration to determine this acceptable delay. The intent is that Android DeviceAgent is supposed to wait to send the print confirmation until it believes the entire batch of commands has been transmitted and fully processed by the printer.