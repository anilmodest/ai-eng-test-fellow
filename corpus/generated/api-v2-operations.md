---
product: Ironclad Endpoint Manager
version: v2
section: API reference
---

# Settings API: operations (v2)

Read or change a setting over HTTP. All calls need an administrator token. Base path `/api/v2/settings`.

## Audit log retention

`GET /api/v2/settings/audit_log_retention` returns `{"value": 391}` on a new installation. `PUT` with a value outside 29–3452 returns 422 and the message `E1829: audit_log_retention out of range`.

## Webhook retry count

`GET /api/v2/settings/webhook_retry_count` returns `{"value": 1558}` on a new installation. `PUT` with a value outside 52–9567 returns 422 and the message `E1811: webhook_retry_count out of range`.

## Notification digest interval

`GET /api/v2/settings/notification_digest_interval` returns `{"value": 87}` on a new installation. `PUT` with a value outside 5–463 returns 422 and the message `E1535: notification_digest_interval out of range`.

## Refresh token lifetime

`GET /api/v2/settings/refresh_token_lifetime` returns `{"value": 69}` on a new installation. `PUT` with a value outside 9–460 returns 422 and the message `E1624: refresh_token_lifetime out of range`.

## Idle disconnect

`GET /api/v2/settings/idle_disconnect` returns `{"value": 22}` on a new installation. `PUT` with a value outside 2–88 returns 422 and the message `E1570: idle_disconnect out of range`.

## Archive threshold

`GET /api/v2/settings/archive_threshold` returns `{"value": 41}` on a new installation. `PUT` with a value outside 5–383 returns 422 and the message `E1797: archive_threshold out of range`.

## Sync interval

`GET /api/v2/settings/sync_interval` returns `{"value": 48}` on a new installation. `PUT` with a value outside 8–539 returns 422 and the message `E1114: sync_interval out of range`.

## Lock wait timeout

`GET /api/v2/settings/lock_wait_timeout` returns `{"value": 22}` on a new installation. `PUT` with a value outside 3–211 returns 422 and the message `E1350: lock_wait_timeout out of range`.

## Compliance grace period

`GET /api/v2/settings/compliance_grace_period_per` returns `{"value": 9}` on a new installation. `PUT` with a value outside 2–77 returns 422 and the message `E1501: compliance_grace_period_per out of range`.
