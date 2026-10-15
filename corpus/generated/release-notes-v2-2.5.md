---
product: Ironclad Endpoint Manager
version: v2
section: Release notes
---

# Ironclad 2.5 release notes

Released 10 June 2024.

## Changes

- Bulk update limit: the error `E1846: bulk_update_limit out of range` now names the accepted range (184 to 9526 items).
- Check-in interval: the error `E1394: check_in_interval out of range` now names the accepted range (3 to 237 minutes).
- Health check interval: the error `E1631: health_check_interval out of range` now names the accepted range (1 to 239 minutes).

## Fixes

- Fixed a case where import file size limit was not applied to the first job after a backup restore.
- Fixed a case where lock wait timeout was not applied to the first job after a failover.
- Fixed a case where check-in interval was not applied to the first job after a failover.
