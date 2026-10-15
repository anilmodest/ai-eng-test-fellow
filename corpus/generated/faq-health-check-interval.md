---
product: Ironclad Endpoint Manager
section: FAQ
---

# Health check interval: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default health check interval?**

In version 2 it is 50 minutes; in version 3 it is 20 minutes.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 239 in version 2 and 181 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `health_check_interval` to `IRONCLAD_HEALTH_CHECK_INTERVAL` in release 3.2. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
