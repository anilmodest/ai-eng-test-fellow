---
product: Ironclad Endpoint Manager
section: FAQ
---

# Export batch size: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default export batch size?**

In version 2 it is 1036 requests per minute; in version 3 it is 343 requests per minute.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 4711 in version 2 and 5106 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `export_batch_size` to `IRONCLAD_EXPORT_BATCH_SIZE` in release 3.2. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
