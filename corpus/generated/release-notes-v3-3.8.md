---
product: Ironclad Endpoint Manager
version: v3
section: Release notes
---

# Ironclad 3.8 release notes

Released 18 September 2026.

## Changes

- **Request timeout**: now set with `IRONCLAD_REQUEST_TIMEOUT`; default changed from 21 to 37 minutes. The version 2 setting `request_timeout` is rejected.
- **Failed login lockout**: now set with `IRONCLAD_FAILED_LOGIN_LOCKOUT`; default changed from 63 to 49 minutes. The version 2 setting `failed_login_lockout_min` is rejected.
- **Cache expiry**: now set with `IRONCLAD_CACHE_EXPIRY`; default changed from 300 to 2308 items. The version 2 setting `cache_expiry` is warned.
- **Idle disconnect**: now set with `IRONCLAD_IDLE_DISCONNECT`; default changed from 22 to 21 percent. The version 2 setting `idle_disconnect` is rejected.
- **Purge delay**: now set with `IRONCLAD_PURGE_DELAY`; default changed from 475 to 284 megabytes. The version 2 setting `purge_delay` is ignored.
- **Check-in interval**: now set with `IRONCLAD_CHECK_IN_INTERVAL`; default changed from 12 to 43 minutes. The version 2 setting `check_in_interval` is warned.
- Password minimum length: the error `E1602: IRONCLAD_PASSWORD_MINIMUM_LENGTH out of range` now names the accepted range (7 to 441 connections).
- Search result limit: the error `E1251: IRONCLAD_SEARCH_RESULT_LIMIT out of range` now names the accepted range (2 to 80 percent).
- Two-factor grace period: the error `E1933: IRONCLAD_TWO_FACTOR_GRACE_PERIOD out of range` now names the accepted range (3 to 464 connections).

## Fixes

- Fixed a case where maintenance window length was not applied to the first job after a failover.
- Fixed a case where remote wipe delay was not applied to the first job after a backup restore.
- Fixed a case where request timeout was not applied to the first job after a failover.
