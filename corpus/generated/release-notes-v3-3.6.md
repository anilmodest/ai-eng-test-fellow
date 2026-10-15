---
product: Ironclad Endpoint Manager
version: v3
section: Release notes
---

# Ironclad 3.6 release notes

Released 19 July 2026.

## Changes

- **Search result limit**: now set with `IRONCLAD_SEARCH_RESULT_LIMIT`; default changed from 27 to 17 percent. The version 2 setting `search_result_limit` is ignored.
- **Metrics flush interval**: now set with `IRONCLAD_METRICS_FLUSH_INTERVAL`; default changed from 305 to 583 characters. The version 2 setting `metrics_flush_interval` is ignored.
- **Bulk update limit**: now set with `IRONCLAD_BULK_UPDATE_LIMIT`; default changed from 2897 to 817 items. The version 2 setting `bulk_update_limit` is rejected.
- Backup retention: the error `E1522: IRONCLAD_BACKUP_RETENTION out of range` now names the accepted range (60 to 3329 characters).
- TLS handshake timeout: the error `E1286: IRONCLAD_TLS_HANDSHAKE_TIMEOUT out of range` now names the accepted range (12 to 572 seconds).
- Job queue depth: the error `E1483: IRONCLAD_JOB_QUEUE_DEPTH out of range` now names the accepted range (56 to 2909 days).

## Fixes

- Fixed a case where compliance grace period was not applied to the first job after a backup restore.
- Fixed a case where archive threshold was not applied to the first job after a configuration reload.
- Fixed a case where metrics flush interval was not applied to the first job after a failover.
- Fixed a case where import file size limit was not applied to the first job after a failover.
- Fixed a case where bulk update limit was not applied to the first job after a configuration reload.
