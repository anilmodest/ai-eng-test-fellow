---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: compliance grace period after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.1 or later that changed the compliance grace period in version 2.

**What happens:** the version 2 setting `compliance_grace_period_per` is ignored by version 3. The service then runs on the version 3 default of 7 percent unless `IRONCLAD_COMPLIANCE_GRACE_PERIOD` is set.

**Workaround:** set `IRONCLAD_COMPLIANCE_GRACE_PERIOD` as the environment variable `IRONCLAD_COMPLIANCE_GRACE_PERIOD` and remove `compliance_grace_period_per`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
