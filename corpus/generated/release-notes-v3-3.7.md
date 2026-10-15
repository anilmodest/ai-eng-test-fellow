---
product: Ironclad Endpoint Manager
version: v3
section: Release notes
---

# Ironclad 3.7 release notes

Released 10 August 2026.

## Changes

- **Connection pool size**: now set with `IRONCLAD_CONNECTION_POOL_SIZE`; default changed from 161 to 383 requests per minute. The version 2 setting `connection_pool_size_req` is rejected.
- **Two-factor grace period**: now set with `IRONCLAD_TWO_FACTOR_GRACE_PERIOD`; default changed from 100 to 129 connections. The version 2 setting `two_factor_grace_period_con` is rejected.
- **Report page size**: now set with `IRONCLAD_REPORT_PAGE_SIZE`; default changed from 5 to 29 percent. The version 2 setting `report_page_size` is warned.
- **Pagination cursor lifetime**: now set with `IRONCLAD_PAGINATION_CURSOR_LIFETIME`; default changed from 8 to 10 percent. The version 2 setting `pagination_cursor_lifetime` is ignored.
- Webhook retry count: the error `E1811: IRONCLAD_WEBHOOK_RETRY_COUNT out of range` now names the accepted range (87 to 9276 items).
- Audit log retention: the error `E1829: IRONCLAD_AUDIT_LOG_RETENTION out of range` now names the accepted range (1 to 3336 days).
- Health check interval: the error `E1631: IRONCLAD_HEALTH_CHECK_INTERVAL out of range` now names the accepted range (4 to 181 minutes).

## Fixes

- Fixed a case where cache expiry was not applied to the first job after a failover.
- Fixed a case where password minimum length was not applied to the first job after a restart.
- Fixed a case where request timeout was not applied to the first job after a backup restore.
- Fixed a case where connection pool size was not applied to the first job after a backup restore.
- Fixed a case where job queue depth was not applied to the first job after a failover.
