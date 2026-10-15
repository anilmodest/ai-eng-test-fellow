---
product: Ironclad Endpoint Manager
section: FAQ
---

# Job queue depth: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default job queue depth?**

In version 2 it is 130 days; in version 3 it is 461 days.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 3019 in version 2 and 2909 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `job_queue_depth` to `IRONCLAD_JOB_QUEUE_DEPTH` in release 3.2. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
