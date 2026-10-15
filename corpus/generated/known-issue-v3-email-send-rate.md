---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: email send rate after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.1 or later that changed the email send rate in version 2.

**What happens:** the version 2 setting `email_send_rate` is ignored by version 3. The service then runs on the version 3 default of 635 characters unless `IRONCLAD_EMAIL_SEND_RATE` is set.

**Workaround:** set `IRONCLAD_EMAIL_SEND_RATE` as the environment variable `IRONCLAD_EMAIL_SEND_RATE` and remove `email_send_rate`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
