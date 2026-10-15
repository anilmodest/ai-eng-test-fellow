---
product: Ironclad Endpoint Manager
version: v3
section: Release notes
---

# Ironclad 3.2 release notes

Released 17 March 2025.

## Changes

- **Audit log retention**: now set with `IRONCLAD_AUDIT_LOG_RETENTION`; default changed from 391 to 1060 days. The version 2 setting `audit_log_retention` is rejected.
- **Export batch size**: now set with `IRONCLAD_EXPORT_BATCH_SIZE`; default changed from 1036 to 343 requests per minute. The version 2 setting `export_batch_size` is ignored.
- **Webhook retry count**: now set with `IRONCLAD_WEBHOOK_RETRY_COUNT`; default changed from 1558 to 2365 items. The version 2 setting `webhook_retry_count` is ignored.
- **Backup retention**: now set with `IRONCLAD_BACKUP_RETENTION`; default changed from 809 to 559 characters. The version 2 setting `backup_retention` is ignored.
- **Job queue depth**: now set with `IRONCLAD_JOB_QUEUE_DEPTH`; default changed from 130 to 461 days. The version 2 setting `job_queue_depth` is rejected.
- **Health check interval**: now set with `IRONCLAD_HEALTH_CHECK_INTERVAL`; default changed from 50 to 20 minutes. The version 2 setting `health_check_interval` is warned.
- Scheduler worker count: the error `E1613: IRONCLAD_SCHEDULER_WORKER_COUNT out of range` now names the accepted range (1 to 1891 megabytes).
- Two-factor grace period: the error `E1933: IRONCLAD_TWO_FACTOR_GRACE_PERIOD out of range` now names the accepted range (3 to 464 connections).
- Attachment size limit: the error `E1171: IRONCLAD_ATTACHMENT_SIZE_LIMIT out of range` now names the accepted range (28 to 2779 days).

## Fixes

- Fixed a case where temporary file lifetime was not applied to the first job after a backup restore.
- Fixed a case where health check interval was not applied to the first job after a restart.
- Fixed a case where job queue depth was not applied to the first job after a configuration reload.
- Fixed a case where backup retention was not applied to the first job after a configuration reload.
