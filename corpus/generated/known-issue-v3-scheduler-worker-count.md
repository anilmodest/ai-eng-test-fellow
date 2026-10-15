---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: scheduler worker count after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.1 or later that changed the scheduler worker count in version 2.

**What happens:** the version 2 setting `scheduler_worker_count` is ignored by version 3. The service then runs on the version 3 default of 10 megabytes unless `IRONCLAD_SCHEDULER_WORKER_COUNT` is set.

**Workaround:** set `IRONCLAD_SCHEDULER_WORKER_COUNT` as the environment variable `IRONCLAD_SCHEDULER_WORKER_COUNT` and remove `scheduler_worker_count`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
