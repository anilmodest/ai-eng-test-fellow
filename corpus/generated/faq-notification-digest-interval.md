---
product: Ironclad Endpoint Manager
section: FAQ
---

# Notification digest interval: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default notification digest interval?**

In version 2 it is 87 seconds; in version 3 it is 40 seconds.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: yes.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 463 in version 2 and 512 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `notification_digest_interval` to `IRONCLAD_NOTIFICATION_DIGEST_INTERVAL` in release 3.0. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
