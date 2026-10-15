---
product: Ironclad Endpoint Manager
version: v2
section: Release notes
---

# Ironclad 2.2 release notes

Released 16 March 2023.

## Changes

- Batch commit size: the error `E1704: batch_commit_size out of range` now names the accepted range (112 to 4676 requests per minute).
- Report page size: the error `E1600: report_page_size out of range` now names the accepted range (2 to 89 percent).
- Import file size limit: the error `E1436: import_file_size_limit out of range` now names the accepted range (9 to 1621 megabytes).

## Fixes

- Fixed a case where audit log retention was not applied to the first job after a restart.
- Fixed a case where job queue depth was not applied to the first job after a restart.
- Fixed a case where report page size was not applied to the first job after a configuration reload.
- Fixed a case where webhook delivery timeout was not applied to the first job after a failover.
- Fixed a case where failed login lockout was not applied to the first job after a restart.
