---
product: Ironclad Endpoint Manager
version: v3
section: API reference
---

# Settings API: operations (v3)

Read or change a setting over HTTP. All calls need an administrator token. Base path `/api/v3/settings`.

## Audit log retention

`GET /api/v3/settings/IRONCLAD_AUDIT_LOG_RETENTION` returns `{"value": 1060}` on a new installation. `PUT` with a value outside 1–3336 returns 422 and the message `E1829: IRONCLAD_AUDIT_LOG_RETENTION out of range`.

## Webhook retry count

`GET /api/v3/settings/IRONCLAD_WEBHOOK_RETRY_COUNT` returns `{"value": 2365}` on a new installation. `PUT` with a value outside 87–9276 returns 422 and the message `E1811: IRONCLAD_WEBHOOK_RETRY_COUNT out of range`.

## Notification digest interval

`GET /api/v3/settings/IRONCLAD_NOTIFICATION_DIGEST_INTERVAL` returns `{"value": 40}` on a new installation. `PUT` with a value outside 7–512 returns 422 and the message `E1535: IRONCLAD_NOTIFICATION_DIGEST_INTERVAL out of range`.

## Refresh token lifetime

`GET /api/v3/settings/IRONCLAD_REFRESH_TOKEN_LIFETIME` returns `{"value": 102}` on a new installation. `PUT` with a value outside 3–566 returns 422 and the message `E1624: IRONCLAD_REFRESH_TOKEN_LIFETIME out of range`.

## Idle disconnect

`GET /api/v3/settings/IRONCLAD_IDLE_DISCONNECT` returns `{"value": 21}` on a new installation. `PUT` with a value outside 1–98 returns 422 and the message `E1570: IRONCLAD_IDLE_DISCONNECT out of range`.

## Archive threshold

`GET /api/v3/settings/IRONCLAD_ARCHIVE_THRESHOLD` returns `{"value": 27}` on a new installation. `PUT` with a value outside 4–466 returns 422 and the message `E1797: IRONCLAD_ARCHIVE_THRESHOLD out of range`.

## Sync interval

`GET /api/v3/settings/IRONCLAD_SYNC_INTERVAL` returns `{"value": 38}` on a new installation. `PUT` with a value outside 6–453 returns 422 and the message `E1114: IRONCLAD_SYNC_INTERVAL out of range`.

## Lock wait timeout

`GET /api/v3/settings/IRONCLAD_LOCK_WAIT_TIMEOUT` returns `{"value": 33}` on a new installation. `PUT` with a value outside 1–210 returns 422 and the message `E1350: IRONCLAD_LOCK_WAIT_TIMEOUT out of range`.

## Compliance grace period

`GET /api/v3/settings/IRONCLAD_COMPLIANCE_GRACE_PERIOD` returns `{"value": 7}` on a new installation. `PUT` with a value outside 2–96 returns 422 and the message `E1501: IRONCLAD_COMPLIANCE_GRACE_PERIOD out of range`.
