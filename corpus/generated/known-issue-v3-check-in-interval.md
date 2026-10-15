---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: check-in interval after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.8 or later that changed the check-in interval in version 2.

**What happens:** the version 2 setting `check_in_interval` is warned by version 3. The service then runs on the version 3 default of 43 minutes unless `IRONCLAD_CHECK_IN_INTERVAL` is set.

**Workaround:** set `IRONCLAD_CHECK_IN_INTERVAL` as the environment variable `IRONCLAD_CHECK_IN_INTERVAL` and remove `check_in_interval`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
