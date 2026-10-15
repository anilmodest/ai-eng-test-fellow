---
product: Ironclad Endpoint Manager
version: v3
section: API reference
---

# Settings API: security (v3)

Read or change a setting over HTTP. All calls need an administrator token. Base path `/api/v3/settings`.

## Webhook delivery timeout

`GET /api/v3/settings/IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT` returns `{"value": 393}` on a new installation. `PUT` with a value outside 9–1592 returns 422 and the message `E1253: IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT out of range`.

## Backup retention

`GET /api/v3/settings/IRONCLAD_BACKUP_RETENTION` returns `{"value": 559}` on a new installation. `PUT` with a value outside 60–3329 returns 422 and the message `E1522: IRONCLAD_BACKUP_RETENTION out of range`.

## Password expiry

`GET /api/v3/settings/IRONCLAD_PASSWORD_EXPIRY` returns `{"value": 40}` on a new installation. `PUT` with a value outside 3–445 returns 422 and the message `E1549: IRONCLAD_PASSWORD_EXPIRY out of range`.

## Email send rate

`GET /api/v3/settings/IRONCLAD_EMAIL_SEND_RATE` returns `{"value": 635}` on a new installation. `PUT` with a value outside 35–3580 returns 422 and the message `E1624: IRONCLAD_EMAIL_SEND_RATE out of range`.

## Cache expiry

`GET /api/v3/settings/IRONCLAD_CACHE_EXPIRY` returns `{"value": 2308}` on a new installation. `PUT` with a value outside 191–9874 returns 422 and the message `E1719: IRONCLAD_CACHE_EXPIRY out of range`.

## Scheduler worker count

`GET /api/v3/settings/IRONCLAD_SCHEDULER_WORKER_COUNT` returns `{"value": 10}` on a new installation. `PUT` with a value outside 1–1891 returns 422 and the message `E1613: IRONCLAD_SCHEDULER_WORKER_COUNT out of range`.

## Token lifetime

`GET /api/v3/settings/IRONCLAD_TOKEN_LIFETIME` returns `{"value": 271}` on a new installation. `PUT` with a value outside 122–7524 returns 422 and the message `E1744: IRONCLAD_TOKEN_LIFETIME out of range`.

## Concurrent session limit

`GET /api/v3/settings/IRONCLAD_CONCURRENT_SESSION_LIMIT` returns `{"value": 168}` on a new installation. `PUT` with a value outside 4–578 returns 422 and the message `E1647: IRONCLAD_CONCURRENT_SESSION_LIMIT out of range`.

## Check-in interval

`GET /api/v3/settings/IRONCLAD_CHECK_IN_INTERVAL` returns `{"value": 43}` on a new installation. `PUT` with a value outside 1–221 returns 422 and the message `E1394: IRONCLAD_CHECK_IN_INTERVAL out of range`.
