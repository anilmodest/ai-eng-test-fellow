---
product: Ironclad Endpoint Manager
section: FAQ
---

# Refresh token lifetime: frequently asked questions

Answers to the questions the support desk is asked most about this setting. Where the answer depends on the version, both are given.

**What is the default refresh token lifetime?**

In version 2 it is 69 seconds; in version 3 it is 102 seconds.

**Do I need to restart after changing it?**

Version 2: yes. Version 3: no.

**What happens if I set it too high?**

The value is rejected and the previous one stays in force. The maximum is 460 in version 2 and 566 in version 3.

**We upgraded and the setting seems to have reset. Why?**

Version 3 changed the setting's name from `refresh_token_lifetime` to `IRONCLAD_REFRESH_TOKEN_LIFETIME` in release 3.4. See the known issue for this setting.

**Can it be set per customer account?**

No. It applies to the whole installation.
