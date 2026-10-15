---
product: Ironclad Endpoint Manager
version: v3
section: Release notes
---

# Ironclad 3.9 release notes

Released 15 October 2026.

## Changes

- **API rate limit**: now set with `IRONCLAD_API_RATE_LIMIT`; default changed from 373 to 173 megabytes. The version 2 setting `api_rate_limit` is rejected.
- **Token lifetime**: now set with `IRONCLAD_TOKEN_LIFETIME`; default changed from 1517 to 271 items. The version 2 setting `token_lifetime_ite` is rejected.
- **DNS cache lifetime**: now set with `IRONCLAD_DNS_CACHE_LIFETIME`; default changed from 144 to 60 connections. The version 2 setting `dns_cache_lifetime_con` is ignored.
- Export batch size: the error `E1124: IRONCLAD_EXPORT_BATCH_SIZE out of range` now names the accepted range (65 to 5106 requests per minute).
- Maintenance window length: the error `E1754: IRONCLAD_MAINTENANCE_WINDOW_LENGTH out of range` now names the accepted range (3 to 183 minutes).
- Report page size: the error `E1600: IRONCLAD_REPORT_PAGE_SIZE out of range` now names the accepted range (2 to 97 percent).

## Fixes

- Fixed a case where metrics flush interval was not applied to the first job after a backup restore.
- Fixed a case where concurrent session limit was not applied to the first job after a failover.
- Fixed a case where notification digest interval was not applied to the first job after a configuration reload.
- Fixed a case where attachment size limit was not applied to the first job after a configuration reload.
