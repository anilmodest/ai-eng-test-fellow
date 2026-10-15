---
product: Ironclad Endpoint Manager
section: FAQ
---

# TLS handshake timeout: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default tls handshake timeout?**

In version 2 it is 67 seconds; in version 3 it is 63 seconds.

**Do I need to restart after changing it?**

Version 2: no. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 497 in version 2 and 572 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `tls_handshake_timeout` to `IRONCLAD_TLS_HANDSHAKE_TIMEOUT` in release 3.4. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
