---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: export batch size after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.2 or later that changed the export batch size in version 2.

**What happens:** the version 2 setting `export_batch_size` is ignored by version 3. The service then runs on the version 3 default of 343 requests per minute unless `IRONCLAD_EXPORT_BATCH_SIZE` is set.

**Workaround:** set `IRONCLAD_EXPORT_BATCH_SIZE` in the admin console and remove `export_batch_size`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
