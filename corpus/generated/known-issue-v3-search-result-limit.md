---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: search result limit after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.6 or later that changed the search result limit in version 2.

**What happens:** the version 2 setting `search_result_limit` is ignored by version 3. The service then runs on the version 3 default of 17 percent unless `IRONCLAD_SEARCH_RESULT_LIMIT` is set.

**Workaround:** set `IRONCLAD_SEARCH_RESULT_LIMIT` in the admin console and remove `search_result_limit`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
