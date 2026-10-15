---
product: Ironclad Endpoint Manager
section: FAQ
---

# Idle disconnect: frequently asked questions

Answers to the questions the support desk is asked most about this setting. Where the answer depends on the version, both are given.

**What is the default idle disconnect?**

In version 2 it is 22 percent; in version 3 it is 21 percent.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 88 in version 2 and 98 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `idle_disconnect` to `IRONCLAD_IDLE_DISCONNECT` in release 3.8. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
