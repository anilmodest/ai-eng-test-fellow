---
product: Ironclad Endpoint Manager
version: v3
section: Release notes
---

# Ironclad 3.1 release notes

Released 13 February 2025.

## Changes

- **Import file size limit**: now set with `IRONCLAD_IMPORT_FILE_SIZE_LIMIT`; default changed from 443 to 9 megabytes. The version 2 setting `import_file_size_limit` is warned.
- **Password minimum length**: now set with `IRONCLAD_PASSWORD_MINIMUM_LENGTH`; default changed from 97 to 125 connections. The version 2 setting `password_minimum_length` is rejected.
- **Email send rate**: now set with `IRONCLAD_EMAIL_SEND_RATE`; default changed from 249 to 635 characters. The version 2 setting `email_send_rate` is ignored.
- **Scheduler worker count**: now set with `IRONCLAD_SCHEDULER_WORKER_COUNT`; default changed from 510 to 10 megabytes. The version 2 setting `scheduler_worker_count` is ignored.
- **Upload chunk size**: now set with `IRONCLAD_UPLOAD_CHUNK_SIZE`; default changed from 145 to 36 seconds. The version 2 setting `upload_chunk_size` is ignored.
- **Trace sampling rate**: now set with `IRONCLAD_TRACE_SAMPLING_RATE`; default changed from 134 to 87 seconds. The version 2 setting `trace_sampling_rate` is ignored.
- **Maintenance window length**: now set with `IRONCLAD_MAINTENANCE_WINDOW_LENGTH`; default changed from 31 to 20 minutes. The version 2 setting `maintenance_window_length_min` is warned.
- **Compliance grace period**: now set with `IRONCLAD_COMPLIANCE_GRACE_PERIOD`; default changed from 9 to 7 percent. The version 2 setting `compliance_grace_period_per` is ignored.
- Email send rate: the error `E1624: IRONCLAD_EMAIL_SEND_RATE out of range` now names the accepted range (35 to 3580 characters).
- Scheduler worker count: the error `E1613: IRONCLAD_SCHEDULER_WORKER_COUNT out of range` now names the accepted range (1 to 1891 megabytes).
- Health check interval: the error `E1631: IRONCLAD_HEALTH_CHECK_INTERVAL out of range` now names the accepted range (4 to 181 minutes).

## Fixes

- Fixed a case where backup schedule interval was not applied to the first job after a restart.
- Fixed a case where cache expiry was not applied to the first job after a backup restore.
- Fixed a case where refresh token lifetime was not applied to the first job after a failover.
- Fixed a case where scheduler worker count was not applied to the first job after a failover.
