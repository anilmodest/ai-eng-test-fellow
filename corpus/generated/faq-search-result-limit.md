---
product: Ironclad Endpoint Manager
section: FAQ
---

# Search result limit: frequently asked questions

Answers to the questions the support desk is asked most about this setting. Where the answer depends on the version, both are given.

**What is the default search result limit?**

In version 2 it is 27 percent; in version 3 it is 17 percent.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: yes.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 82 in version 2 and 80 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `search_result_limit` to `IRONCLAD_SEARCH_RESULT_LIMIT` in release 3.6. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
