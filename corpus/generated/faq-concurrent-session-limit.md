---
product: Ironclad Endpoint Manager
section: FAQ
---

# Concurrent session limit: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default concurrent session limit?**

In version 2 it is 136 seconds; in version 3 it is 168 seconds.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 549 in version 2 and 578 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `concurrent_session_limit` to `IRONCLAD_CONCURRENT_SESSION_LIMIT` in release 3.0. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
