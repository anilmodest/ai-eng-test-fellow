---
product: Ironclad Endpoint Manager
section: FAQ
---

# Update deferral: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default update deferral?**

In version 2 it is 692 items; in version 3 it is 2560 items.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 7718 in version 2 and 8640 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `update_deferral_ite` to `IRONCLAD_UPDATE_DEFERRAL` in release 3.0. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
