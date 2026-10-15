---
product: Ironclad Endpoint Manager
section: FAQ
---

# Remote wipe delay: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default remote wipe delay?**

In version 2 it is 143 connections; in version 3 it is 126 connections.

**Do I need to restart after changing it?**

Version 2: no. Version 3: yes.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 426 in version 2 and 477 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `remote_wipe_delay` to `IRONCLAD_REMOTE_WIPE_DELAY` in release 3.3. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
