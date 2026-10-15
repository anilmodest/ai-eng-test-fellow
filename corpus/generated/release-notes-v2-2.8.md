---
product: Ironclad Endpoint Manager
version: v2
section: Release notes
---

# Ironclad 2.8 release notes

Released 4 September 2024.

## Changes

- Metrics flush interval: the error `E1977: metrics_flush_interval out of range` now names the accepted range (67 to 3729 characters).
- Purge delay: the error `E1295: purge_delay out of range` now names the accepted range (36 to 1671 megabytes).
- Webhook retry count: the error `E1811: webhook_retry_count out of range` now names the accepted range (52 to 9567 items).

## Fixes

- Fixed a case where backup schedule interval was not applied to the first job after a failover.
- Fixed a case where tls handshake timeout was not applied to the first job after a backup restore.
- Fixed a case where refresh token lifetime was not applied to the first job after a backup restore.
- Fixed a case where backup schedule interval was not applied to the first job after a restart.
