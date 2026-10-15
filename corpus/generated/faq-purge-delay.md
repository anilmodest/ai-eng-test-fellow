---
product: Ironclad Endpoint Manager
section: FAQ
---

# Purge delay: frequently asked questions

Answers to the questions the support desk is asked most about this setting. Where the answer depends on the version, both are given.

**What is the default purge delay?**

In version 2 it is 475 megabytes; in version 3 it is 284 megabytes.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 1671 in version 2 and 2031 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `purge_delay` to `IRONCLAD_PURGE_DELAY` in release 3.8. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
