---
product: Ironclad Endpoint Manager
section: Upgrading
---

# Upgrading from version 2 to version 3: security settings

Every setting below changed name, place or default between the versions. The last column says what version 3 does with the old setting if you leave it in place.

| Setting | Version 2 | Version 3 | Default v2 → v3 | Old setting in v3 |
| --- | --- | --- | --- | --- |
| Webhook delivery timeout | `webhook_delivery_timeout` | `IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT` | 435 → 393 megabytes | ignored |
| Backup retention | `backup_retention` | `IRONCLAD_BACKUP_RETENTION` | 809 → 559 characters | ignored |
| Password expiry | `password_expiry_con` | `IRONCLAD_PASSWORD_EXPIRY` | 92 → 40 connections | rejected |
| Email send rate | `email_send_rate` | `IRONCLAD_EMAIL_SEND_RATE` | 249 → 635 characters | ignored |
| Cache expiry | `cache_expiry` | `IRONCLAD_CACHE_EXPIRY` | 300 → 2308 items | warned |
| Scheduler worker count | `scheduler_worker_count` | `IRONCLAD_SCHEDULER_WORKER_COUNT` | 510 → 10 megabytes | ignored |
| Token lifetime | `token_lifetime_ite` | `IRONCLAD_TOKEN_LIFETIME` | 1517 → 271 items | rejected |
| Concurrent session limit | `concurrent_session_limit` | `IRONCLAD_CONCURRENT_SESSION_LIMIT` | 136 → 168 seconds | warned |
| Check-in interval | `check_in_interval` | `IRONCLAD_CHECK_IN_INTERVAL` | 12 → 43 minutes | warned |
