---
product: Ironclad Endpoint Manager
section: FAQ
---

# Session timeout: frequently asked questions

Answers to the questions the support desk is asked most about this setting. Where the answer depends on the version, both are given.

**What is the default session timeout?**

In version 2 it is 42 minutes; in version 3 it is 34 minutes.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 188 in version 2 and 209 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `session_timeout_min` to `IRONCLAD_SESSION_TIMEOUT` in release 3.4. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
