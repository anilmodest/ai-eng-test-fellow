---
product: Ironclad Endpoint Manager
section: FAQ
---

# Import file size limit: frequently asked questions

Answers to the questions the support desk is asked most about this setting. Where the answer depends on the version, both are given.

**What is the default import file size limit?**

In version 2 it is 443 megabytes; in version 3 it is 9 megabytes.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 1621 in version 2 and 1565 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `import_file_size_limit` to `IRONCLAD_IMPORT_FILE_SIZE_LIMIT` in release 3.1. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
