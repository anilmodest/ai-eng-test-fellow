---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: dns cache lifetime after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.9 or later that changed the dns cache lifetime in version 2.

**What happens:** the version 2 setting `dns_cache_lifetime_con` is ignored by version 3. The service then runs on the version 3 default of 60 connections unless `IRONCLAD_DNS_CACHE_LIFETIME` is set.

**Workaround:** set `IRONCLAD_DNS_CACHE_LIFETIME` as the environment variable `IRONCLAD_DNS_CACHE_LIFETIME` and remove `dns_cache_lifetime_con`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
