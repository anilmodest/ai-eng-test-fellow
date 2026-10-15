---
product: Ironclad Endpoint Manager
version: v3
section: API reference
---

# Settings API: integrations (v3)

Read or change a setting over HTTP. All calls need an administrator token. Base path `/api/v3/settings`.

## Connection pool size

`GET /api/v3/settings/IRONCLAD_CONNECTION_POOL_SIZE` returns `{"value": 383}` on a new installation. `PUT` with a value outside 40–4583 returns 422 and the message `E1438: IRONCLAD_CONNECTION_POOL_SIZE out of range`.

## Request timeout

`GET /api/v3/settings/IRONCLAD_REQUEST_TIMEOUT` returns `{"value": 37}` on a new installation. `PUT` with a value outside 4–237 returns 422 and the message `E1976: IRONCLAD_REQUEST_TIMEOUT out of range`.

## Import file size limit

`GET /api/v3/settings/IRONCLAD_IMPORT_FILE_SIZE_LIMIT` returns `{"value": 9}` on a new installation. `PUT` with a value outside 5–1565 returns 422 and the message `E1436: IRONCLAD_IMPORT_FILE_SIZE_LIMIT out of range`.

## API rate limit

`GET /api/v3/settings/IRONCLAD_API_RATE_LIMIT` returns `{"value": 173}` on a new installation. `PUT` with a value outside 32–1539 returns 422 and the message `E1246: IRONCLAD_API_RATE_LIMIT out of range`.

## Password minimum length

`GET /api/v3/settings/IRONCLAD_PASSWORD_MINIMUM_LENGTH` returns `{"value": 125}` on a new installation. `PUT` with a value outside 7–441 returns 422 and the message `E1602: IRONCLAD_PASSWORD_MINIMUM_LENGTH out of range`.

## Failed login lockout

`GET /api/v3/settings/IRONCLAD_FAILED_LOGIN_LOCKOUT` returns `{"value": 49}` on a new installation. `PUT` with a value outside 1–203 returns 422 and the message `E1457: IRONCLAD_FAILED_LOGIN_LOCKOUT out of range`.

## Two-factor grace period

`GET /api/v3/settings/IRONCLAD_TWO_FACTOR_GRACE_PERIOD` returns `{"value": 129}` on a new installation. `PUT` with a value outside 3–464 returns 422 and the message `E1933: IRONCLAD_TWO_FACTOR_GRACE_PERIOD out of range`.

## Job queue depth

`GET /api/v3/settings/IRONCLAD_JOB_QUEUE_DEPTH` returns `{"value": 461}` on a new installation. `PUT` with a value outside 56–2909 returns 422 and the message `E1483: IRONCLAD_JOB_QUEUE_DEPTH out of range`.

## Health check interval

`GET /api/v3/settings/IRONCLAD_HEALTH_CHECK_INTERVAL` returns `{"value": 20}` on a new installation. `PUT` with a value outside 4–181 returns 422 and the message `E1631: IRONCLAD_HEALTH_CHECK_INTERVAL out of range`.

## Field length limit

`GET /api/v3/settings/IRONCLAD_FIELD_LENGTH_LIMIT` returns `{"value": 166}` on a new installation. `PUT` with a value outside 11–486 returns 422 and the message `E1954: IRONCLAD_FIELD_LENGTH_LIMIT out of range`.

## DNS cache lifetime

`GET /api/v3/settings/IRONCLAD_DNS_CACHE_LIFETIME` returns `{"value": 60}` on a new installation. `PUT` with a value outside 7–500 returns 422 and the message `E1800: IRONCLAD_DNS_CACHE_LIFETIME out of range`.

## Update deferral

`GET /api/v3/settings/IRONCLAD_UPDATE_DEFERRAL` returns `{"value": 2560}` on a new installation. `PUT` with a value outside 159–8640 returns 422 and the message `E1800: IRONCLAD_UPDATE_DEFERRAL out of range`.
