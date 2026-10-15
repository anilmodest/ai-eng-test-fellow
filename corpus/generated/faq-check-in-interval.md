---
product: Ironclad Endpoint Manager
section: FAQ
---

# Check-in interval: frequently asked questions

Answers to the questions the support desk is asked most about this setting. Where the answer depends on the version, both are given.

**What is the default check-in interval?**

In version 2 it is 12 minutes; in version 3 it is 43 minutes.

**Do I need to restart after changing it?**

Version 2: no. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 237 in version 2 and 221 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `check_in_interval` to `IRONCLAD_CHECK_IN_INTERVAL` in release 3.8. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
