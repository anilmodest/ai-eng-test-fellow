---
product: Ironclad Endpoint Manager
version: v2
section: Release notes
---

# Ironclad 2.7 release notes

Released 28 August 2024.

## Changes

- Upload chunk size: the error `E1692: upload_chunk_size out of range` now names the accepted range (6 to 583 seconds).
- Concurrent session limit: the error `E1647: concurrent_session_limit out of range` now names the accepted range (5 to 549 seconds).
- Connection pool size: the error `E1438: connection_pool_size_req out of range` now names the accepted range (89 to 4721 requests per minute).

## Fixes

- Fixed a case where update deferral was not applied to the first job after a failover.
- Fixed a case where archive threshold was not applied to the first job after a backup restore.
- Fixed a case where cache expiry was not applied to the first job after a configuration reload.
