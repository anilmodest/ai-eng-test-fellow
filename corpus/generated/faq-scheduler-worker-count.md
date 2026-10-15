---
product: Ironclad Endpoint Manager
section: FAQ
---

# Scheduler worker count: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default scheduler worker count?**

In version 2 it is 510 megabytes; in version 3 it is 10 megabytes.

**Do I need to restart after changing it?**

Version 2: no. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 1742 in version 2 and 1891 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `scheduler_worker_count` to `IRONCLAD_SCHEDULER_WORKER_COUNT` in release 3.1. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
