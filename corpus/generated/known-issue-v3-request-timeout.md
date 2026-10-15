---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: request timeout after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.8 or later that changed the request timeout in version 2.

**What happens:** the version 2 setting `request_timeout` is rejected by version 3. The service then runs on the version 3 default of 37 minutes unless `IRONCLAD_REQUEST_TIMEOUT` is set.

**Workaround:** set `IRONCLAD_REQUEST_TIMEOUT` as the environment variable `IRONCLAD_REQUEST_TIMEOUT` and remove `request_timeout`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
