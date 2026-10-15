---
product: Ironclad Endpoint Manager
version: v2
section: Release notes
---

# Ironclad 2.0 release notes

Released 18 January 2023.

## Changes

- Export batch size: the error `E1124: export_batch_size out of range` now names the accepted range (55 to 4711 requests per minute).
- TLS handshake timeout: the error `E1286: tls_handshake_timeout out of range` now names the accepted range (3 to 497 seconds).
- Batch commit size: the error `E1704: batch_commit_size out of range` now names the accepted range (112 to 4676 requests per minute).

## Fixes

- Fixed a case where bulk update limit was not applied to the first job after a backup restore.
- Fixed a case where webhook delivery timeout was not applied to the first job after a failover.
- Fixed a case where attachment size limit was not applied to the first job after a backup restore.
