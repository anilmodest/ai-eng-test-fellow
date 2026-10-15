---
product: Ironclad Endpoint Manager
section: FAQ
---

# Password expiry: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default password expiry?**

In version 2 it is 92 connections; in version 3 it is 40 connections.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 432 in version 2 and 445 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `password_expiry_con` to `IRONCLAD_PASSWORD_EXPIRY` in release 3.5. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
