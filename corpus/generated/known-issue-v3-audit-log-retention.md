---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: audit log retention after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.2 or later that changed the audit log retention in version 2.

**What happens:** the version 2 setting `audit_log_retention` is rejected by version 3. The service then runs on the version 3 default of 1060 days unless `IRONCLAD_AUDIT_LOG_RETENTION` is set.

**Workaround:** set `IRONCLAD_AUDIT_LOG_RETENTION` in the admin console and remove `audit_log_retention`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
