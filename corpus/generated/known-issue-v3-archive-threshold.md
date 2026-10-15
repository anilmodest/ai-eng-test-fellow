---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: archive threshold after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.4 or later that changed the archive threshold in version 2.

**What happens:** the version 2 setting `archive_threshold` is ignored by version 3. The service then runs on the version 3 default of 27 connections unless `IRONCLAD_ARCHIVE_THRESHOLD` is set.

**Workaround:** set `IRONCLAD_ARCHIVE_THRESHOLD` as the environment variable `IRONCLAD_ARCHIVE_THRESHOLD` and remove `archive_threshold`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
