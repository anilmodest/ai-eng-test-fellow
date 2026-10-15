---
product: Ironclad Endpoint Manager
section: FAQ
---

# Bulk update limit: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default bulk update limit?**

In version 2 it is 2897 items; in version 3 it is 817 items.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: yes.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 9526 in version 2 and 8156 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `bulk_update_limit` to `IRONCLAD_BULK_UPDATE_LIMIT` in release 3.6. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
