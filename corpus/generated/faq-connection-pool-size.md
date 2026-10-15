---
product: Ironclad Endpoint Manager
section: FAQ
---

# Connection pool size: frequently asked questions

Answers to the questions the support desk is asked most about this setting. Where the answer depends on the version, both are given.

**What is the default connection pool size?**

In version 2 it is 161 requests per minute; in version 3 it is 383 requests per minute.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 4721 in version 2 and 4583 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `connection_pool_size_req` to `IRONCLAD_CONNECTION_POOL_SIZE` in release 3.7. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
