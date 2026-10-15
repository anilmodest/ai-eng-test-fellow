---
product: Ironclad Endpoint Manager
version: v3
section: Release notes
---

# Ironclad 3.0 release notes

Released 18 January 2025.

## Changes

- **Backup schedule interval**: now set with `IRONCLAD_BACKUP_SCHEDULE_INTERVAL`; default changed from 67 to 562 megabytes. The version 2 setting `backup_schedule_interval` is rejected.
- **Notification digest interval**: now set with `IRONCLAD_NOTIFICATION_DIGEST_INTERVAL`; default changed from 87 to 40 seconds. The version 2 setting `notification_digest_interval` is ignored.
- **Concurrent session limit**: now set with `IRONCLAD_CONCURRENT_SESSION_LIMIT`; default changed from 136 to 168 seconds. The version 2 setting `concurrent_session_limit` is warned.
- **Field length limit**: now set with `IRONCLAD_FIELD_LENGTH_LIMIT`; default changed from 123 to 166 seconds. The version 2 setting `field_length_limit` is rejected.
- **Update deferral**: now set with `IRONCLAD_UPDATE_DEFERRAL`; default changed from 692 to 2560 items. The version 2 setting `update_deferral_ite` is ignored.
- Cache expiry: the error `E1719: IRONCLAD_CACHE_EXPIRY out of range` now names the accepted range (191 to 9874 items).
- Sync interval: the error `E1114: IRONCLAD_SYNC_INTERVAL out of range` now names the accepted range (6 to 453 seconds).
- Maintenance window length: the error `E1754: IRONCLAD_MAINTENANCE_WINDOW_LENGTH out of range` now names the accepted range (3 to 183 minutes).

## Fixes

- Fixed a case where sync interval was not applied to the first job after a restart.
- Fixed a case where webhook delivery timeout was not applied to the first job after a restart.
- Fixed a case where email send rate was not applied to the first job after a backup restore.
- Fixed a case where search result limit was not applied to the first job after a restart.
