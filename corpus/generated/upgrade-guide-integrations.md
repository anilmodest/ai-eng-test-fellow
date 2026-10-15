---
product: Ironclad Endpoint Manager
section: Upgrading
---

# Upgrading from version 2 to version 3: integrations settings

Every setting below changed name, place or default between the versions. The last column says what version 3 does with the old setting if you leave it in place.

| Setting | Version 2 | Version 3 | Default v2 → v3 | Old setting in v3 |
| --- | --- | --- | --- | --- |
| Connection pool size | `connection_pool_size_req` | `IRONCLAD_CONNECTION_POOL_SIZE` | 161 → 383 requests per minute | rejected |
| Request timeout | `request_timeout` | `IRONCLAD_REQUEST_TIMEOUT` | 21 → 37 minutes | rejected |
| Import file size limit | `import_file_size_limit` | `IRONCLAD_IMPORT_FILE_SIZE_LIMIT` | 443 → 9 megabytes | warned |
| API rate limit | `api_rate_limit` | `IRONCLAD_API_RATE_LIMIT` | 373 → 173 megabytes | rejected |
| Password minimum length | `password_minimum_length` | `IRONCLAD_PASSWORD_MINIMUM_LENGTH` | 97 → 125 connections | rejected |
| Failed login lockout | `failed_login_lockout_min` | `IRONCLAD_FAILED_LOGIN_LOCKOUT` | 63 → 49 minutes | rejected |
| Two-factor grace period | `two_factor_grace_period_con` | `IRONCLAD_TWO_FACTOR_GRACE_PERIOD` | 100 → 129 connections | rejected |
| Job queue depth | `job_queue_depth` | `IRONCLAD_JOB_QUEUE_DEPTH` | 130 → 461 days | rejected |
| Health check interval | `health_check_interval` | `IRONCLAD_HEALTH_CHECK_INTERVAL` | 50 → 20 minutes | warned |
| Field length limit | `field_length_limit` | `IRONCLAD_FIELD_LENGTH_LIMIT` | 123 → 166 seconds | rejected |
| DNS cache lifetime | `dns_cache_lifetime_con` | `IRONCLAD_DNS_CACHE_LIFETIME` | 144 → 60 connections | ignored |
| Update deferral | `update_deferral_ite` | `IRONCLAD_UPDATE_DEFERRAL` | 692 → 2560 items | ignored |
