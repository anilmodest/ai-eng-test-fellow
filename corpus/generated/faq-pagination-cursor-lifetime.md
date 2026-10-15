---
product: Ironclad Endpoint Manager
section: FAQ
---

# Pagination cursor lifetime: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default pagination cursor lifetime?**

In version 2 it is 8 percent; in version 3 it is 10 percent.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 84 in version 2 and 93 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `pagination_cursor_lifetime` to `IRONCLAD_PAGINATION_CURSOR_LIFETIME` in release 3.7. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
