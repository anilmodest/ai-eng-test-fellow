---
product: Ironclad Endpoint Manager
section: FAQ
---

# DNS cache lifetime: frequently asked questions

Answers to the questions the support desk is asked most about this setting. Where the answer depends on the version, both are given.

**What is the default dns cache lifetime?**

In version 2 it is 144 connections; in version 3 it is 60 connections.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: yes.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 430 in version 2 and 500 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `dns_cache_lifetime_con` to `IRONCLAD_DNS_CACHE_LIFETIME` in release 3.9. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
