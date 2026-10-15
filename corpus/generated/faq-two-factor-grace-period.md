---
product: Ironclad Endpoint Manager
section: FAQ
---

# Two-factor grace period: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default two-factor grace period?**

In version 2 it is 100 connections; in version 3 it is 129 connections.

**Do I need to restart after changing it?**

Version 2: no. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 382 in version 2 and 464 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `two_factor_grace_period_con` to `IRONCLAD_TWO_FACTOR_GRACE_PERIOD` in release 3.7. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
