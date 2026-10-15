---
product: Ironclad Endpoint Manager
section: FAQ
---

# Upload chunk size: frequently asked questions

Answers to the questions the support desk is asked most about this setting. Where the answer depends on the version, both are given.

**What is the default upload chunk size?**

In version 2 it is 145 seconds; in version 3 it is 36 seconds.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 583 in version 2 and 563 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `upload_chunk_size` to `IRONCLAD_UPLOAD_CHUNK_SIZE` in release 3.1. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
