---
product: Ironclad Endpoint Manager
section: FAQ
---

# API rate limit: frequently asked questions

The questions below come from real tickets, lightly edited. Check which version you run before you act on an answer.

**What is the default api rate limit?**

In version 2 it is 373 megabytes; in version 3 it is 173 megabytes.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 2035 in version 2 and 1539 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `api_rate_limit` to `IRONCLAD_API_RATE_LIMIT` in release 3.9. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
