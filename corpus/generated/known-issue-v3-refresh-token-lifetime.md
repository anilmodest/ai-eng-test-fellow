---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: refresh token lifetime after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.4 or later that changed the refresh token lifetime in version 2.

**What happens:** the version 2 setting `refresh_token_lifetime` is rejected by version 3. The service then runs on the version 3 default of 102 seconds unless `IRONCLAD_REFRESH_TOKEN_LIFETIME` is set.

**Workaround:** set `IRONCLAD_REFRESH_TOKEN_LIFETIME` as the environment variable `IRONCLAD_REFRESH_TOKEN_LIFETIME` and remove `refresh_token_lifetime`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
