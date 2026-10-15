---
product: Ironclad Endpoint Manager
section: Upgrading
---

# Upgrading from version 2 to version 3: operations settings

Every setting below changed name, place or default between the versions. The last column says what version 3 does with the old setting if you leave it in place.

| Setting | Version 2 | Version 3 | Default v2 → v3 | Old setting in v3 |
| --- | --- | --- | --- | --- |
| Audit log retention | `audit_log_retention` | `IRONCLAD_AUDIT_LOG_RETENTION` | 391 → 1060 days | rejected |
| Webhook retry count | `webhook_retry_count` | `IRONCLAD_WEBHOOK_RETRY_COUNT` | 1558 → 2365 items | ignored |
| Notification digest interval | `notification_digest_interval` | `IRONCLAD_NOTIFICATION_DIGEST_INTERVAL` | 87 → 40 seconds | ignored |
| Refresh token lifetime | `refresh_token_lifetime` | `IRONCLAD_REFRESH_TOKEN_LIFETIME` | 69 → 102 seconds | rejected |
| Idle disconnect | `idle_disconnect` | `IRONCLAD_IDLE_DISCONNECT` | 22 → 21 percent | rejected |
| Archive threshold | `archive_threshold` | `IRONCLAD_ARCHIVE_THRESHOLD` | 41 → 27 connections | ignored |
| Sync interval | `sync_interval` | `IRONCLAD_SYNC_INTERVAL` | 48 → 38 seconds | ignored |
| Lock wait timeout | `lock_wait_timeout` | `IRONCLAD_LOCK_WAIT_TIMEOUT` | 22 → 33 minutes | ignored |
| Compliance grace period | `compliance_grace_period_per` | `IRONCLAD_COMPLIANCE_GRACE_PERIOD` | 9 → 7 percent | ignored |
