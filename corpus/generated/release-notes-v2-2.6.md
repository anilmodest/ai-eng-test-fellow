---
product: Ironclad Endpoint Manager
version: v2
section: Release notes
---

# Ironclad 2.6 release notes

Released 19 July 2024.

## Changes

- Bulk update limit: the error `E1846: bulk_update_limit out of range` now names the accepted range (184 to 9526 items).
- Field length limit: the error `E1954: field_length_limit out of range` now names the accepted range (9 to 479 seconds).
- Password expiry: the error `E1549: password_expiry_con out of range` now names the accepted range (7 to 432 connections).

## Fixes

- Fixed a case where backup schedule interval was not applied to the first job after a failover.
- Fixed a case where upload chunk size was not applied to the first job after a failover.
- Fixed a case where job queue depth was not applied to the first job after a failover.
