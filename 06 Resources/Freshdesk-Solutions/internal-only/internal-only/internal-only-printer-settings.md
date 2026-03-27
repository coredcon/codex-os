---
title: "*|Internal Only| - Printer Settings"
freshdesk_id: 17000142558
category: "Internal Only"
folder: "Internal Only"
status: published
created: 2024-09-09
updated: 2024-09-09
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000142558
---

# *|Internal Only| - Printer Settings

## The Print Spooler


In ControlPoint Server, printing is globally managed by an object called the `Print Spooler`. All print requests, whether they originate from Kitchen Server, ConnectSmart Host, or ControlPoint Client itself (via Diagnostic Mode), are ultimately routed to the Print Spooler for processing.


The Print Spooler monitors the list of devices that are actively connected to ControlPoint Server, as well as the individual station configuration settings that users create and edit through ControlPoint Client.
For every connected device that is configured for printing, the Print Spooler creates a helper object called a `Print Processor` to handle the low-level communication details (such that there is a one-to-one correlation between the number of "active" printers and the number of Print Processors).


_Example Logs:_


- 

"Tag":"`PrintSpooler`","Message":"`Synchronizing the list of active print processors...`"


- 

"Tag":"`PrintSpooler`","Message":"`Creating EscPosEthernetPrintProcessorEx for device 1.`"


- 

"Tag":"`PrintSpooler`","Message":"`Removing PrintProcessor for device 5.`"


## Print Processors


Print Processors come in multiple flavors; instead of having one generic solution to service all possible printer vendors, operating system platforms, and communication protocols, ControlPoint Server is shipped with a handful of specialized Print Processor implementations.


For devices running on Windows, the `SerialPrintProcessor` handles serial printing, while the `WinUsbPrintProcessor` handles USB printing. For devices running on Android, the (poorly named) `AttachedProtobufPrintProcessor` handles USB printing.


There are three Print Processor implementations for Ethernet printers; one for each of the three command languages that ControlPoint supports:


- 

The `EscPosEthernetPrintProcessorEx` is QSR's newest solution for communicating to Epson (Ethernet) printers and uses an expanded set of ESC/POS commands to retrieve automatic status updates and information regarding the "paper removal" sensor.


- 

The `EscPosEthernetPrintProcessor` is QSR's legacy solution for Epson (Ethernet) printers and is included for compatibility to older (and potentially off-brand) ESC/POS printers.


- 

The `StarPrntEthernetPrintProcessor` handles Ethernet printing for current-generation Star printers that speak StarPRNT.


- 


## Legacy Print Processors


While still bundled with ControlPoint and actively maintained, the following implementations are considered to be `Legacy Print Processors` by the Platform Support Development Team:


- 

SerialPrintProcessor


- 

EscPosEthernetPrintProcessor


- 

StarPrntEtherPrintProcessor


Legacy Print Processors are based on the original implementation for serial printing and use real-time commands to query the printer’s status. Because of this, ControlPoint only really knows that the generated set of instructions to fully print (and cut) a receipt have been `transmitted` to the printer; it does not know (by default) if the receipt has been successfully printed. Additionally, these Print Processor implementations are unable to obtain information regarding a printer’s “paper removal” sensor.


## Receipt Printers


In order to enable printing, users must first create a `Receipt Printer` in ControlPoint Client and associate it with one or more devices. Receipt Printers are simply a collection of configurable runtime settings that are linked to a station’s underlying Print Processor.


## Printer Control Settings


The `Printer Control` section of a Receipt Printer template mostly consists of runtime settings that are being phased out by newer Print Processor implementations. Aside from the globally supported Knife Cut Time and Write Timeout settings, only the `Legacy Print Processors` take full advantage of these options.


## Knife Cut Time


Supported by `all` Print Processor implementations, the `Knife Cut Time` setting simply tells ControlPoint how long to pause between the printing of two or more receipts.


For example, say that ControlPoint has two print jobs queued up for Station 1. The associated Print Processor generates and transmits the full set of commands to print (and cut) the first receipt. On “success”, ControlPoint pauses for 500ms (as specified by the `Knife Cut Time` setting) before moving on to the second receipt.


#### Remarks


It’s unclear if this setting is actually needed, as we’d expect printers to provide internal protection around the knife cut command (such that it should be impossible to print too quickly after the previous receipt is cut). In cases where there isn’t a “paper removal” sensor, however, setting the `Knife Cut Time` to several seconds (2000ms - 3000ms) would give the user some time to detach the receipt before another is printed. If this is not a concern for the customer, we’d recommend setting this to half a second (500ms).


**Important Note**: `Legacy Print Processors` start the Knife Cut timer the moment the receipt data is `transferred`, not when the receipt has finished printing. This means that ControlPoint is simply pausing before it places the instructions needed to print (and cut) the next receipt in the printer’s command buffer. Therefore, in order to produce a meaningful delay between prints, users will need to set the Knife Cut Time to the average amount of time it takes to fully print a receipt `plus` the amount of time they want ControlPoint to wait before the next receipt is transmitted.


## Write Timeout


Supported by `all` Print Processor implementations, the `Write Timeout` setting specifies how long ControlPoint should wait for a response from the printer after sending a request.


For example, most Print Processors periodically transmit a “Get Printer Status” request every three to five seconds. If the status does not arrive within five seconds (as specified by the `Write Timeout` setting), the printer is considered to be offline / disconnected. Likewise, when sending the full set of commands to print (and cut) a receipt, ControlPoint expects to receive some sort of acknowledgement, either stating that the data was successfully transmitted, or that the receipt was successfully printed (depending on the Print Processor). If the acknowledgement fails to arrive in time, the receipt is marked “Failed to Print”.


#### Remarks


We’d generally recommend setting this to a value between five and ten seconds for a thermal printer. Impact printers, which print much slower, should probably be set to twenty seconds.


## Force a Delay Between Data Packets


Supported only by `Legacy Print Processor` implementations, the `Force a delay between data packets` option allows users to throttle the receipt data that is transmitted over the network from ControlPoint to the printer / DeviceAgent.


When the check box is enabled, the `Packet Size` setting specifies the maximum number of bytes that can be sent at one time. The `Packet Delay` setting tells ControlPoint how long to pause before sending the next chunk of receipt data.


For example, say that ControlPoint has a single print job queued up for Station 1. The associated Print Processor generates 2,500 bytes of data representing the full set of ESC/POS commands to print (and cut) this particular receipt. The option to `force a delay between data packets` has been checked, so ControlPoint only transmits the first 1024 bytes (as specified by the `Packet Size` setting). After waiting 500ms (as specified by the `Packet Delay` setting), ControlPoint sends the next 1024 bytes. After waiting for another 500ms, ControlPoint sends the final 452 bytes.


#### Remarks


The feature was likely implemented with serial printing in mind, as an attempt to prevent ControlPoint from completely overwhelming the printer’s internal command buffer when printing an especially large receipt. Users will need to experiment with the configuration settings to find values that work reliably for their serial printer.


Although the `EscPosEthernetPrintProcessor` and `StarPrntEthernetPrintProcessor` both technically support this feature as well, the underlying TCP/IP protocol prevents ControlPoint from sending more data over the network than the printer can handle. Users can therefore leave this box unchecked for all non-serial printers.


## Uses Print Buffer Query


Supported only by `Legacy Print Processor` implementations, the (poorly named) `Uses Print Buffer Query` option, when enabled, causes ControlPoint to attempt to determine if the printer has finished printing the previous receipt before it transmits the commands needed to print the next receipt.


Legacy Print Processors, by default, only verify that the printer is `online` before printing a receipt. They do this by transmitting a real-time status request, which the printer has to respond to immediately (even if it’s in the middle of printing). This `optional` status check, however, is “buffered”, which means that the printer can only respond to it `after` it has successfully processed every command that came before it.


ControlPoint, however, only waits a fixed period of time (specified by the `Query Timeout` setting) for the “all clear” signal before moving ahead with the next receipt. The only difference is that the “Flush Print Buffer” command, which is normally the first instruction sent to the printer as part of the full set of commands to print (and cut) the receipt, is omitted in cases where the `Query Timeout` timer expires.


#### Remarks


This feature was originally added after discovering a design flaw in the implementation of the `Legacy Print Processors`. We recommend enabling this option and configuring the `Query Timeout` setting to be the exact same as the `Write Timeout` setting.


## Are the General Settings and Formatting sections being utilized across all printing types, or are there exceptions within those options as well?


To our knowledge, the remaining printer settings are common across all Print Processor implementations.