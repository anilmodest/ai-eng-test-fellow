---
product: Ironclad Endpoint Manager
version: v3
section: Release notes
---

# Ironclad 3.4 release notes

Released 18 May 2026.

## Changes

- **Session timeout**: now set with `IRONCLAD_SESSION_TIMEOUT`; default changed from 42 to 34 minutes. The version 2 setting `session_timeout_min` is rejected.
- **Refresh token lifetime**: now set with `IRONCLAD_REFRESH_TOKEN_LIFETIME`; default changed from 69 to 102 seconds. The version 2 setting `refresh_token_lifetime` is rejected.
- **Archive threshold**: now set with `IRONCLAD_ARCHIVE_THRESHOLD`; default changed from 41 to 27 connections. The version 2 setting `archive_threshold` is ignored.
- **Sync interval**: now set with `IRONCLAD_SYNC_INTERVAL`; default changed from 48 to 38 seconds. The version 2 setting `sync_interval` is ignored.
- **TLS handshake timeout**: now set with `IRONCLAD_TLS_HANDSHAKE_TIMEOUT`; default changed from 67 to 63 seconds. The version 2 setting `tls_handshake_timeout` is warned.
- **Batch commit size**: now set with `IRONCLAD_BATCH_COMMIT_SIZE`; default changed from 669 to 1382 requests per minute. The version 2 setting `batch_commit_size` is ignored.
- Webhook retry count: the error `E1811: IRONCLAD_WEBHOOK_RETRY_COUNT out of range` now names the accepted range (87 to 9276 items).
- Report page size: the error `E1600: IRONCLAD_REPORT_PAGE_SIZE out of range` now names the accepted range (2 to 97 percent).
- Pagination cursor lifetime: the error `E1627: IRONCLAD_PAGINATION_CURSOR_LIFETIME out of range` now names the accepted range (1 to 93 percent).

## Fixes

- Fixed a case where request timeout was not applied to the first job after a failover.
- Fixed a case where metrics flush interval was not applied to the first job after a configuration reload.
- Fixed a case where concurrent session limit was not applied to the first job after a configuration reload.
- Fixed a case where token lifetime was not applied to the first job after a backup restore.
- Fixed a case where batch commit size was not applied to the first job after a backup restore.
