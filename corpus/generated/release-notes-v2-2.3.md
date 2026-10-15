---
product: Ironclad Endpoint Manager
version: v2
section: Release notes
---

# Ironclad 2.3 release notes

Released 7 April 2024.

## Changes

- Token lifetime: the error `E1744: token_lifetime_ite out of range` now names the accepted range (182 to 8406 items).
- TLS handshake timeout: the error `E1286: tls_handshake_timeout out of range` now names the accepted range (3 to 497 seconds).
- Lock wait timeout: the error `E1350: lock_wait_timeout out of range` now names the accepted range (3 to 211 minutes).

## Fixes

- Fixed a case where dns cache lifetime was not applied to the first job after a failover.
- Fixed a case where search result limit was not applied to the first job after a backup restore.
- Fixed a case where dns cache lifetime was not applied to the first job after a configuration reload.
- Fixed a case where tls handshake timeout was not applied to the first job after a configuration reload.
