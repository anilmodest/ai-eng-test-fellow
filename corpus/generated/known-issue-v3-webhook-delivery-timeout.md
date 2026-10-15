---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: webhook delivery timeout after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.5 or later that changed the webhook delivery timeout in version 2.

**What happens:** the version 2 setting `webhook_delivery_timeout` is ignored by version 3. The service then runs on the version 3 default of 393 megabytes unless `IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT` is set.

**Workaround:** set `IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT` in the admin console and remove `webhook_delivery_timeout`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
