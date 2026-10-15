---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: batch commit size after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.4 or later that changed the batch commit size in version 2.

**What happens:** the version 2 setting `batch_commit_size` is ignored by version 3. The service then runs on the version 3 default of 1382 requests per minute unless `IRONCLAD_BATCH_COMMIT_SIZE` is set.

**Workaround:** set `IRONCLAD_BATCH_COMMIT_SIZE` in the admin console and remove `batch_commit_size`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
