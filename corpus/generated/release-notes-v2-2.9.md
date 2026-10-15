---
product: Ironclad Endpoint Manager
version: v2
section: Release notes
---

# Ironclad 2.9 release notes

Released 22 October 2024.

## Changes

- Compliance grace period: the error `E1501: compliance_grace_period_per out of range` now names the accepted range (2 to 77 percent).
- Export batch size: the error `E1124: export_batch_size out of range` now names the accepted range (55 to 4711 requests per minute).
- Refresh token lifetime: the error `E1624: refresh_token_lifetime out of range` now names the accepted range (9 to 460 seconds).

## Fixes

- Fixed a case where api rate limit was not applied to the first job after a failover.
- Fixed a case where update deferral was not applied to the first job after a failover.
- Fixed a case where pagination cursor lifetime was not applied to the first job after a failover.
