---
product: Ironclad Endpoint Manager
version: v3
section: Release notes
---

# Ironclad 3.3 release notes

Released 19 April 2026.

## Changes

- **Attachment size limit**: now set with `IRONCLAD_ATTACHMENT_SIZE_LIMIT`; default changed from 508 to 469 days. The version 2 setting `attachment_size_limit` is ignored.
- **Lock wait timeout**: now set with `IRONCLAD_LOCK_WAIT_TIMEOUT`; default changed from 22 to 33 minutes. The version 2 setting `lock_wait_timeout` is ignored.
- **Temporary file lifetime**: now set with `IRONCLAD_TEMPORARY_FILE_LIFETIME`; default changed from 622 to 2623 items. The version 2 setting `temporary_file_lifetime` is warned.
- **Remote wipe delay**: now set with `IRONCLAD_REMOTE_WIPE_DELAY`; default changed from 143 to 126 connections. The version 2 setting `remote_wipe_delay` is ignored.
- DNS cache lifetime: the error `E1800: IRONCLAD_DNS_CACHE_LIFETIME out of range` now names the accepted range (7 to 500 connections).
- Webhook delivery timeout: the error `E1253: IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT out of range` now names the accepted range (9 to 1592 megabytes).
- Report page size: the error `E1600: IRONCLAD_REPORT_PAGE_SIZE out of range` now names the accepted range (2 to 97 percent).

## Fixes

- Fixed a case where dns cache lifetime was not applied to the first job after a backup restore.
- Fixed a case where failed login lockout was not applied to the first job after a configuration reload.
- Fixed a case where tls handshake timeout was not applied to the first job after a configuration reload.
- Fixed a case where notification digest interval was not applied to the first job after a backup restore.
- Fixed a case where sync interval was not applied to the first job after a backup restore.
