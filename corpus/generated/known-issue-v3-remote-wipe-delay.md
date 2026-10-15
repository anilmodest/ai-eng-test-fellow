---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: remote wipe delay after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.3 or later that changed the remote wipe delay in version 2.

**What happens:** the version 2 setting `remote_wipe_delay` is ignored by version 3. The service then runs on the version 3 default of 126 connections unless `IRONCLAD_REMOTE_WIPE_DELAY` is set.

**Workaround:** set `IRONCLAD_REMOTE_WIPE_DELAY` as the environment variable `IRONCLAD_REMOTE_WIPE_DELAY` and remove `remote_wipe_delay`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
