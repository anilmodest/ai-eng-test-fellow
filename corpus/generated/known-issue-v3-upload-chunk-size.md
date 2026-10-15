---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: upload chunk size after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.1 or later that changed the upload chunk size in version 2.

**What happens:** the version 2 setting `upload_chunk_size` is ignored by version 3. The service then runs on the version 3 default of 36 seconds unless `IRONCLAD_UPLOAD_CHUNK_SIZE` is set.

**Workaround:** set `IRONCLAD_UPLOAD_CHUNK_SIZE` as the environment variable `IRONCLAD_UPLOAD_CHUNK_SIZE` and remove `upload_chunk_size`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
