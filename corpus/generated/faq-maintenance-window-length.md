---
product: Ironclad Endpoint Manager
section: FAQ
---

# Maintenance window length: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default maintenance window length?**

In version 2 it is 31 minutes; in version 3 it is 20 minutes.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: yes.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 195 in version 2 and 183 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `maintenance_window_length_min` to `IRONCLAD_MAINTENANCE_WINDOW_LENGTH` in release 3.1. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
