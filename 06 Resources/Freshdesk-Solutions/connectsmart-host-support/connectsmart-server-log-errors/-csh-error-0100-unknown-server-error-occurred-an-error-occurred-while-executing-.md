---
title: "* |CSH| - ERROR [0100]: Unknown server error occurred.  An error occurred while executing the command definition."
freshdesk_id: 17000097413
category: "ConnectSmart Host Support"
folder: "ConnectSmart Server - Log Errors"
status: published
created: 2019-11-19
updated: 2022-12-12
views: 0
tags: []
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000097413
---

# * |CSH| - ERROR [0100]: Unknown server error occurred.  An error occurred while executing the command definition.

**Issue: **


The user is presented with the error "Unknown server error occurred" in the ConnectSmart Host client.


****


**ConnectSmart Host Server Log Error:** 


2019-10-31 10:07:19 ERROR [0100]: Unknown server error occurred.                                  An error occurred while executing the command definition. See the inner exception for details.                                     at System.Data.Entity.Core.EntityClient.Internal.EntityCommandDefinition.ExecuteStoreCommands(EntityCommand entityCommand, CommandBehavior behavior)                                     at System.Data.Entity.Core.Objects.Internal.ObjectQueryExecutionPlan.Execute[TResultType](ObjectContext context, ObjectParameterCollection parameterValues)                                     at System.Data.Entity.Core.Objects.ObjectQuery`1.<>c__DisplayClass7.<GetResults>b__6()                                     at System.Data.Entity.Core.Objects.ObjectContext.ExecuteInTransaction[T](Func`1 func, IDbExecutionStrategy executionStrategy, Boolean startLocalTransaction, Boolean releaseConnectionOnSuccess)                                     at System.Data.Entity.Core.Objects.ObjectQuery`1.<>c__DisplayClass7.<GetResults>b__5()                                     at System.Data.Entity.SqlServer.DefaultSqlExecutionStrategy.Execute[TResult](Func`1 operation)                                     at System.Data.Entity.Core.Objects.ObjectQuery`1.GetResults(Nullable`1 forMergeOption)                                     at System.Data.Entity.Core.Objects.ObjectQuery`1.<System.Collections.Generic.IEnumerable<T>.GetEnumerator>b__0()                                     at System.Data.Entity.Internal.LazyEnumerator`1.MoveNext()                                     at System.Collections.Generic.List`1..ctor(IEnumerable`1 collection)                                     at System.Linq.Enumerable.ToList[TSource](IEnumerable`1 source)                                     at QsrAutomations.Gaia.Procedures.VisitProcedures.GetOffPremiseVisits(DateTimeOffset startOfBusinessDateTime, DateTimeOffset endOfBusinessDateTime, IVisitProcedureData dataManager, HostessModel contextToUse)                                     at QsrAutomations.Gaia.Managers.VisitManager.GetOffPremiseVisits(DateTimeOffset businessDate)                                     at QsrAutomations.Gaia.Services.VisitService.GetOffPremiseVisits(String businessDate)                                     at SyncInvokeGetOffPremiseVisits(Object , Object[] , Object[] )                                     at System.ServiceModel.Dispatcher.SyncMethodInvoker.Invoke(Object instance, Object[] inputs, Object[]& outputs)                                     at QsrAutomations.Gaia.Managers.ServiceManagerClasses.CustomOperationInvoker.performInvocation(Object instance, Object[] inputs, Object[]& outputs)                                  Execution Timeout Expired.  The timeout period elapsed prior to completion of the operation or the server is not responding.                                     at System.Data.SqlClient.SqlConnection.OnError(SqlException exception, Boolean breakConnection, Action`1 wrapCloseInAction)                                     at System.Data.SqlClient.SqlInternalConnection.OnError(SqlException exception, Boolean breakConnection, Action`1 wrapCloseInAction)                                     at System.Data.SqlClient.TdsParser.ThrowExceptionAndWarning(TdsParserStateObject stateObj, Boolean callerHasConnectionLock, Boolean asyncClose)                                     at System.Data.SqlClient.TdsParser.TryRun(RunBehavior runBehavior, SqlCommand cmdHandler, SqlDataReader dataStream, BulkCopySimpleResultSet bulkCopyHandler, TdsParserStateObject stateObj, Boolean& dataReady)                                     at System.Data.SqlClient.SqlDataReader.TryConsumeMetaData()                                     at System.Data.SqlClient.SqlDataReader.get_MetaData()                                     at System.Data.SqlClient.SqlCommand.FinishExecuteReader(SqlDataReader ds, RunBehavior runBehavior, String resetOptionsString, Boolean isInternal, Boolean forDescribeParameterEncryption, Boolean shouldCacheForAlwaysEncrypted)                                     at System.Data.SqlClient.SqlCommand.RunExecuteReaderTds(CommandBehavior cmdBehavior, RunBehavior runBehavior, Boolean returnStream, Boolean async, Int32 timeout, Task& task, Boolean asyncWrite, Boolean inRetry, SqlDataReader ds, Boolean describeParameterEncryptionRequest)                                     at System.Data.SqlClient.SqlCommand.RunExecuteReader(CommandBehavior cmdBehavior, RunBehavior runBehavior, Boolean returnStream, String method, TaskCompletionSource`1 completion, Int32 timeout, Task& task, Boolean& usedCache, Boolean asyncWrite, Boolean inRetry)                                     at System.Data.SqlClient.SqlCommand.RunExecuteReader(CommandBehavior cmdBehavior, RunBehavior runBehavior, Boolean returnStream, String method)                                     at System.Data.SqlClient.SqlCommand.ExecuteReader(CommandBehavior behavior, String method)                                     at System.Data.SqlClient.SqlCommand.ExecuteDbDataReader(CommandBehavior behavior)                                     at System.Data.Common.DbCommand.ExecuteReader(CommandBehavior behavior)                                     at System.Data.Entity.Infrastructure.Interception.DbCommandDispatcher.<Reader>b__c(DbCommand t, DbCommandInterceptionContext`1 c)                                     at System.Data.Entity.Infrastructure.Interception.InternalDispatcher`1.Dispatch[TTarget,TInterceptionContext,TResult](TTarget target, Func`3 operation, TInterceptionContext interceptionContext, Action`3 executing, Action`3 executed)                                     at System.Data.Entity.Infrastructure.Interception.DbCommandDispatcher.Reader(DbCommand command, DbCommandInterceptionContext interceptionContext)                                     at System.Data.Entity.Internal.InterceptableDbCommand.ExecuteDbDataReader(CommandBehavior behavior)                                     at System.Data.Common.DbCommand.ExecuteReader(CommandBehavior behavior)                                     at System.Data.Entity.Core.EntityClient.Internal.EntityCommandDefinition.ExecuteStoreCommands(EntityCommand entityCommand, CommandBehavior behavior)                                  The wait operation timed out.


**Solution: **


**T**his error occurred when the memory load on the machine hosting the ConnectSmart Host server was close to or above 90%. If the above error is seen in the logs, please also compare the memory usage on the machine. Additionally, look at the Event Viewer logs for related errors.


**Reference: **


Per Escalation ticket [183634] / JIRA DE-1811,