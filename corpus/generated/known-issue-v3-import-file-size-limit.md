---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: import file size limit after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.1 or later that changed the import file size limit in version 2.

**What happens:** the version 2 setting `import_file_size_limit` is warned by version 3. The service then runs on the version 3 default of 9 megabytes unless `IRONCLAD_IMPORT_FILE_SIZE_LIMIT` is set.

**Workaround:** set `IRONCLAD_IMPORT_FILE_SIZE_LIMIT` as the environment variable `IRONCLAD_IMPORT_FILE_SIZE_LIMIT` and remove `import_file_size_limit`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
