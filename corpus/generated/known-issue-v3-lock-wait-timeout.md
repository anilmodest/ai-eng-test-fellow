---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: lock wait timeout after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.3 or later that changed the lock wait timeout in version 2.

**What happens:** the version 2 setting `lock_wait_timeout` is ignored by version 3. The service then runs on the version 3 default of 33 minutes unless `IRONCLAD_LOCK_WAIT_TIMEOUT` is set.

**Workaround:** set `IRONCLAD_LOCK_WAIT_TIMEOUT` in the admin console and remove `lock_wait_timeout`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
