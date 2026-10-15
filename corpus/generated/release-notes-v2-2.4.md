---
product: Ironclad Endpoint Manager
version: v2
section: Release notes
---

# Ironclad 2.4 release notes

Released 21 May 2024.

## Changes

- Upload chunk size: the error `E1692: upload_chunk_size out of range` now names the accepted range (6 to 583 seconds).
- Failed login lockout: the error `E1457: failed_login_lockout_min out of range` now names the accepted range (5 to 218 minutes).
- Remote wipe delay: the error `E1293: remote_wipe_delay out of range` now names the accepted range (7 to 426 connections).

## Fixes

- Fixed a case where sync interval was not applied to the first job after a configuration reload.
- Fixed a case where concurrent session limit was not applied to the first job after a failover.
- Fixed a case where remote wipe delay was not applied to the first job after a configuration reload.
- Fixed a case where attachment size limit was not applied to the first job after a failover.
