---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: connection pool size after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.7 or later that changed the connection pool size in version 2.

**What happens:** the version 2 setting `connection_pool_size_req` is rejected by version 3. The service then runs on the version 3 default of 383 requests per minute unless `IRONCLAD_CONNECTION_POOL_SIZE` is set.

**Workaround:** set `IRONCLAD_CONNECTION_POOL_SIZE` as the environment variable `IRONCLAD_CONNECTION_POOL_SIZE` and remove `connection_pool_size_req`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
