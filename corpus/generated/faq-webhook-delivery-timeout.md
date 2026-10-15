---
product: Ironclad Endpoint Manager
section: FAQ
---

# Webhook delivery timeout: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default webhook delivery timeout?**

In version 2 it is 435 megabytes; in version 3 it is 393 megabytes.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 1769 in version 2 and 1592 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `webhook_delivery_timeout` to `IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT` in release 3.5. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
