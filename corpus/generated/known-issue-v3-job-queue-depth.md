---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: job queue depth after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.2 or later that changed the job queue depth in version 2.

**What happens:** the version 2 setting `job_queue_depth` is rejected by version 3. The service then runs on the version 3 default of 461 days unless `IRONCLAD_JOB_QUEUE_DEPTH` is set.

**Workaround:** set `IRONCLAD_JOB_QUEUE_DEPTH` as the environment variable `IRONCLAD_JOB_QUEUE_DEPTH` and remove `job_queue_depth`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
