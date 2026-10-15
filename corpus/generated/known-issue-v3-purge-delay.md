---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: purge delay after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.8 or later that changed the purge delay in version 2.

**What happens:** the version 2 setting `purge_delay` is ignored by version 3. The service then runs on the version 3 default of 284 megabytes unless `IRONCLAD_PURGE_DELAY` is set.

**Workaround:** set `IRONCLAD_PURGE_DELAY` as the environment variable `IRONCLAD_PURGE_DELAY` and remove `purge_delay`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
