---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: trace sampling rate after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.1 or later that changed the trace sampling rate in version 2.

**What happens:** the version 2 setting `trace_sampling_rate` is ignored by version 3. The service then runs on the version 3 default of 87 seconds unless `IRONCLAD_TRACE_SAMPLING_RATE` is set.

**Workaround:** set `IRONCLAD_TRACE_SAMPLING_RATE` as the environment variable `IRONCLAD_TRACE_SAMPLING_RATE` and remove `trace_sampling_rate`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
