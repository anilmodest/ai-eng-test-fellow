---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: password expiry after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.5 or later that changed the password expiry in version 2.

**What happens:** the version 2 setting `password_expiry_con` is rejected by version 3. The service then runs on the version 3 default of 40 connections unless `IRONCLAD_PASSWORD_EXPIRY` is set.

**Workaround:** set `IRONCLAD_PASSWORD_EXPIRY` in the admin console and remove `password_expiry_con`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
