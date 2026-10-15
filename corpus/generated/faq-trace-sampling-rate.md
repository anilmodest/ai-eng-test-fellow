---
product: Ironclad Endpoint Manager
section: FAQ
---

# Trace sampling rate: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default trace sampling rate?**

In version 2 it is 134 seconds; in version 3 it is 87 seconds.

**Do I need to restart after changing it?**

Version 2: no. Version 3: yes.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 513 in version 2 and 496 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `trace_sampling_rate` to `IRONCLAD_TRACE_SAMPLING_RATE` in release 3.1. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
