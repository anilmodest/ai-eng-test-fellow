---
product: Ironclad Endpoint Manager
version: v3
section: Known issues
---

# Known issue: tls handshake timeout after upgrading to version 3

**Affects:** installations upgraded from version 2 to version 3.4 or later that changed the tls handshake timeout in version 2.

**What happens:** the version 2 setting `tls_handshake_timeout` is warned by version 3. The service then runs on the version 3 default of 63 seconds unless `IRONCLAD_TLS_HANDSHAKE_TIMEOUT` is set.

**Workaround:** set `IRONCLAD_TLS_HANDSHAKE_TIMEOUT` in the admin console and remove `tls_handshake_timeout`.

**Status:** by design. The release notes for the release that changed it say so; the upgrade guide did not, and has been corrected.
