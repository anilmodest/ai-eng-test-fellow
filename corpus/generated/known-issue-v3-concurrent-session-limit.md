---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: concurrent session limit after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.0 or later that changed the concurrent session limit in version 2.

**What happens:** the version 2 setting `concurrent_session_limit` is warned by version 3. The service then runs on the version 3 default of 168 seconds unless `IRONCLAD_CONCURRENT_SESSION_LIMIT` is set.

**Workaround:** set `IRONCLAD_CONCURRENT_SESSION_LIMIT` as the environment variable `IRONCLAD_CONCURRENT_SESSION_LIMIT` and remove `concurrent_session_limit`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
