---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: temporary file lifetime after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.3 or later that changed the temporary file lifetime in version 2.

**What happens:** the version 2 setting `temporary_file_lifetime` is warned by version 3. The service then runs on the version 3 default of 2623 items unless `IRONCLAD_TEMPORARY_FILE_LIFETIME` is set.

**Workaround:** set `IRONCLAD_TEMPORARY_FILE_LIFETIME` as the environment variable `IRONCLAD_TEMPORARY_FILE_LIFETIME` and remove `temporary_file_lifetime`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
