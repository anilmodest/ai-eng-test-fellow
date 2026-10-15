---
product: Ironclad Endpoint Manager
version: v2
section: Release notes
---

# Ironclad 2.1 release notes

Released 17 February 2023.

## Changes

- Cache expiry: the error `E1719: cache_expiry out of range` now names the accepted range (139 to 8716 items).
- Failed login lockout: the error `E1457: failed_login_lockout_min out of range` now names the accepted range (5 to 218 minutes).
- Field length limit: the error `E1954: field_length_limit out of range` now names the accepted range (9 to 479 seconds).

## Fixes

- Fixed a case where password expiry was not applied to the first job after a failover.
- Fixed a case where webhook retry count was not applied to the first job after a configuration reload.
- Fixed a case where password minimum length was not applied to the first job after a backup restore.
- Fixed a case where remote wipe delay was not applied to the first job after a configuration reload.
- Fixed a case where purge delay was not applied to the first job after a failover.
