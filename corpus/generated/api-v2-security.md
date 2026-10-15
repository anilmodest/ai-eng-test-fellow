---
product: Ironclad Endpoint Manager
version: v2
section: API reference
---

# Settings API: security (v2)

Read or change a setting over HTTP. All calls need an administrator token. Base path `/api/v2/settings`.

## Webhook delivery timeout

`GET /api/v2/settings/webhook_delivery_timeout` returns `{"value": 435}` on a new installation. `PUT` with a value outside 36–1769 returns 422 and the message `E1253: webhook_delivery_timeout out of range`.

## Backup retention

`GET /api/v2/settings/backup_retention` returns `{"value": 809}` on a new installation. `PUT` with a value outside 64–3178 returns 422 and the message `E1522: backup_retention out of range`.

## Password expiry

`GET /api/v2/settings/password_expiry_con` returns `{"value": 92}` on a new installation. `PUT` with a value outside 7–432 returns 422 and the message `E1549: password_expiry_con out of range`.

## Email send rate

`GET /api/v2/settings/email_send_rate` returns `{"value": 249}` on a new installation. `PUT` with a value outside 40–3244 returns 422 and the message `E1624: email_send_rate out of range`.

## Cache expiry

`GET /api/v2/settings/cache_expiry` returns `{"value": 300}` on a new installation. `PUT` with a value outside 139–8716 returns 422 and the message `E1719: cache_expiry out of range`.

## Scheduler worker count

`GET /api/v2/settings/scheduler_worker_count` returns `{"value": 510}` on a new installation. `PUT` with a value outside 33–1742 returns 422 and the message `E1613: scheduler_worker_count out of range`.

## Token lifetime

`GET /api/v2/settings/token_lifetime_ite` returns `{"value": 1517}` on a new installation. `PUT` with a value outside 182–8406 returns 422 and the message `E1744: token_lifetime_ite out of range`.

## Concurrent session limit

`GET /api/v2/settings/concurrent_session_limit` returns `{"value": 136}` on a new installation. `PUT` with a value outside 5–549 returns 422 and the message `E1647: concurrent_session_limit out of range`.

## Check-in interval

`GET /api/v2/settings/check_in_interval` returns `{"value": 12}` on a new installation. `PUT` with a value outside 3–237 returns 422 and the message `E1394: check_in_interval out of range`.
