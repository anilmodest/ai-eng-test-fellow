---
product: Ironclad Endpoint Manager
version: v3
section: Release notes
---

# Ironclad 3.5 release notes

Released 3 June 2026.

## Changes

- **Webhook delivery timeout**: now set with `IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT`; default changed from 435 to 393 megabytes. The version 2 setting `webhook_delivery_timeout` is ignored.
- **Password expiry**: now set with `IRONCLAD_PASSWORD_EXPIRY`; default changed from 92 to 40 connections. The version 2 setting `password_expiry_con` is rejected.
- Search result limit: the error `E1251: IRONCLAD_SEARCH_RESULT_LIMIT out of range` now names the accepted range (2 to 80 percent).
- Webhook delivery timeout: the error `E1253: IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT out of range` now names the accepted range (9 to 1592 megabytes).
- Webhook retry count: the error `E1811: IRONCLAD_WEBHOOK_RETRY_COUNT out of range` now names the accepted range (87 to 9276 items).

## Fixes

- Fixed a case where backup retention was not applied to the first job after a restart.
- Fixed a case where search result limit was not applied to the first job after a backup restore.
- Fixed a case where import file size limit was not applied to the first job after a restart.
