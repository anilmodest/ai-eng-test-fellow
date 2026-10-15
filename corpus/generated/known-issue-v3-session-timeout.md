---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: session timeout after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.4 or later that changed the session timeout in version 2.

**What happens:** the version 2 setting `session_timeout_min` is rejected by version 3. The service then runs on the version 3 default of 34 minutes unless `IRONCLAD_SESSION_TIMEOUT` is set.

**Workaround:** set `IRONCLAD_SESSION_TIMEOUT` as the environment variable `IRONCLAD_SESSION_TIMEOUT` and remove `session_timeout_min`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
