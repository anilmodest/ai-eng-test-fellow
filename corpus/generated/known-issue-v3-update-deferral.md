---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: update deferral after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.0 or later that changed the update deferral in version 2.

**What happens:** the version 2 setting `update_deferral_ite` is ignored by version 3. The service then runs on the version 3 default of 2560 items unless `IRONCLAD_UPDATE_DEFERRAL` is set.

**Workaround:** set `IRONCLAD_UPDATE_DEFERRAL` in the admin console and remove `update_deferral_ite`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
