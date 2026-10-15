---
product: Ironclad Endpoint Manager
section: FAQ
---

# Sync interval: frequently asked questions

Answers to the questions the support desk is asked most about this setting. Where the answer depends on the version, both are given.

**What is the default sync interval?**

In version 2 it is 48 seconds; in version 3 it is 38 seconds.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: yes.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 539 in version 2 and 453 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `sync_interval` to `IRONCLAD_SYNC_INTERVAL` in release 3.4. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
