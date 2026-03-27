---
title: "*|CSH| - ERROR [0100]: Unknown server error occurred.  An operation was attempted on a nonexistent network connection"
freshdesk_id: 17000058864
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Log Errors"
status: published
created: 2017-08-28
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000058864
---

# *|CSH| - ERROR [0100]: Unknown server error occurred.  An operation was attempted on a nonexistent network connection

**ConnectSmart Host Server logs error:**


2017-08-26 19:53:22 ERROR [0100]: Unknown server error occurred.


                                  An operation was attempted on a nonexistent network connection


                                     at System.ServiceModel.Channels.HttpOutput.ListenerResponseHttpOutput.ListenerResponseOutputStream.Write(Byte[] buffer, Int32 offset, Int32 count)


                                     at System.ServiceModel.Channels.HttpOutput.Send(TimeSpan timeout)


                                     at System.ServiceModel.Channels.HttpPipeline.EmptyHttpPipeline.SendReplyCore(Message message, TimeSpan timeout)


                                     at System.ServiceModel.Channels.HttpPipeline.EmptyHttpPipeline.SendReply(Message message, TimeSpan timeout)


                                     at System.ServiceModel.Channels.HttpRequestContext.OnReply(Message message, TimeSpan timeout)


                                     at System.ServiceModel.Channels.RequestContextBase.Reply(Message message, TimeSpan timeout)


                                     at System.ServiceModel.Dispatcher.ImmutableDispatchRuntime.Reply(MessageRpc& rpc)


                                  An operation was attempted on a nonexistent network connection


                                     at System.Net.HttpResponseStream.Write(Byte[] buffer, Int32 offset, Int32 size)


                                     at System.ServiceModel.Channels.BytesReadPositionStream.Write(Byte[] buffer, Int32 offset, Int32 count)


                                     at System.ServiceModel.Channels.HttpOutput.ListenerResponseHttpOutput.ListenerResponseOutputStream.Write(Byte[] buffer, Int32 offset, Int32 count)


**Solution**: 


This error occurs when an iPad Client goes to sleep, but only when it goes to sleep on its own. There are two ways an iPad goes to sleep:


-  The user taps the power button and puts it to sleep manually

-  The iPad is left idle and reaches it's configured "auto-lock" period.


During load testing, this error was found to occur and was traced back to an iPad being left idle until it automatically went to sleep.


**Reference**: 


Escalation Ticket 117643 / JIRA DE-539,