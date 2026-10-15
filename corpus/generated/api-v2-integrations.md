---
product: Ironclad Endpoint Manager
version: v2
section: API reference
---

# Settings API: integrations (v2)

Read or change a setting over HTTP. All calls need an administrator token. Base path `/api/v2/settings`.

## Connection pool size

`GET /api/v2/settings/connection_pool_size_req` returns `{"value": 161}` on a new installation. `PUT` with a value outside 89–4721 returns 422 and the message `E1438: connection_pool_size_req out of range`.

## Request timeout

`GET /api/v2/settings/request_timeout` returns `{"value": 21}` on a new installation. `PUT` with a value outside 1–239 returns 422 and the message `E1976: request_timeout out of range`.

## Import file size limit

`GET /api/v2/settings/import_file_size_limit` returns `{"value": 443}` on a new installation. `PUT` with a value outside 9–1621 returns 422 and the message `E1436: import_file_size_limit out of range`.

## API rate limit

`GET /api/v2/settings/api_rate_limit` returns `{"value": 373}` on a new installation. `PUT` with a value outside 38–2035 returns 422 and the message `E1246: api_rate_limit out of range`.

## Password minimum length

`GET /api/v2/settings/password_minimum_length` returns `{"value": 97}` on a new installation. `PUT` with a value outside 8–400 returns 422 and the message `E1602: password_minimum_length out of range`.

## Failed login lockout

`GET /api/v2/settings/failed_login_lockout_min` returns `{"value": 63}` on a new installation. `PUT` with a value outside 5–218 returns 422 and the message `E1457: failed_login_lockout_min out of range`.

## Two-factor grace period

`GET /api/v2/settings/two_factor_grace_period_con` returns `{"value": 100}` on a new installation. `PUT` with a value outside 7–382 returns 422 and the message `E1933: two_factor_grace_period_con out of range`.

## Job queue depth

`GET /api/v2/settings/job_queue_depth` returns `{"value": 130}` on a new installation. `PUT` with a value outside 44–3019 returns 422 and the message `E1483: job_queue_depth out of range`.

## Health check interval

`GET /api/v2/settings/health_check_interval` returns `{"value": 50}` on a new installation. `PUT` with a value outside 1–239 returns 422 and the message `E1631: health_check_interval out of range`.

## Field length limit

`GET /api/v2/settings/field_length_limit` returns `{"value": 123}` on a new installation. `PUT` with a value outside 9–479 returns 422 and the message `E1954: field_length_limit out of range`.

## DNS cache lifetime

`GET /api/v2/settings/dns_cache_lifetime_con` returns `{"value": 144}` on a new installation. `PUT` with a value outside 7–430 returns 422 and the message `E1800: dns_cache_lifetime_con out of range`.

## Update deferral

`GET /api/v2/settings/update_deferral_ite` returns `{"value": 692}` on a new installation. `PUT` with a value outside 172–7718 returns 422 and the message `E1800: update_deferral_ite out of range`.
