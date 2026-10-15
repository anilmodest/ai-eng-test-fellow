---
product: Ironclad Endpoint Manager
version: v3
section: API reference
---

# Settings API: configuration (v3)

Read or change a setting over HTTP. All calls need an administrator token. Base path `/api/v3/settings`.

## Session timeout

`GET /api/v3/settings/IRONCLAD_SESSION_TIMEOUT` returns `{"value": 34}` on a new installation. `PUT` with a value outside 3–209 returns 422 and the message `E1851: IRONCLAD_SESSION_TIMEOUT out of range`.

## Export batch size

`GET /api/v3/settings/IRONCLAD_EXPORT_BATCH_SIZE` returns `{"value": 343}` on a new installation. `PUT` with a value outside 65–5106 returns 422 and the message `E1124: IRONCLAD_EXPORT_BATCH_SIZE out of range`.

## Search result limit

`GET /api/v3/settings/IRONCLAD_SEARCH_RESULT_LIMIT` returns `{"value": 17}` on a new installation. `PUT` with a value outside 2–80 returns 422 and the message `E1251: IRONCLAD_SEARCH_RESULT_LIMIT out of range`.

## Report page size

`GET /api/v3/settings/IRONCLAD_REPORT_PAGE_SIZE` returns `{"value": 29}` on a new installation. `PUT` with a value outside 2–97 returns 422 and the message `E1600: IRONCLAD_REPORT_PAGE_SIZE out of range`.

## Upload chunk size

`GET /api/v3/settings/IRONCLAD_UPLOAD_CHUNK_SIZE` returns `{"value": 36}` on a new installation. `PUT` with a value outside 1–563 returns 422 and the message `E1692: IRONCLAD_UPLOAD_CHUNK_SIZE out of range`.

## Metrics flush interval

`GET /api/v3/settings/IRONCLAD_METRICS_FLUSH_INTERVAL` returns `{"value": 583}` on a new installation. `PUT` with a value outside 61–3178 returns 422 and the message `E1977: IRONCLAD_METRICS_FLUSH_INTERVAL out of range`.

## Attachment size limit

`GET /api/v3/settings/IRONCLAD_ATTACHMENT_SIZE_LIMIT` returns `{"value": 469}` on a new installation. `PUT` with a value outside 28–2779 returns 422 and the message `E1171: IRONCLAD_ATTACHMENT_SIZE_LIMIT out of range`.

## Purge delay

`GET /api/v3/settings/IRONCLAD_PURGE_DELAY` returns `{"value": 284}` on a new installation. `PUT` with a value outside 41–2031 returns 422 and the message `E1295: IRONCLAD_PURGE_DELAY out of range`.

## Maintenance window length

`GET /api/v3/settings/IRONCLAD_MAINTENANCE_WINDOW_LENGTH` returns `{"value": 20}` on a new installation. `PUT` with a value outside 3–183 returns 422 and the message `E1754: IRONCLAD_MAINTENANCE_WINDOW_LENGTH out of range`.

## TLS handshake timeout

`GET /api/v3/settings/IRONCLAD_TLS_HANDSHAKE_TIMEOUT` returns `{"value": 63}` on a new installation. `PUT` with a value outside 12–572 returns 422 and the message `E1286: IRONCLAD_TLS_HANDSHAKE_TIMEOUT out of range`.

## Batch commit size

`GET /api/v3/settings/IRONCLAD_BATCH_COMMIT_SIZE` returns `{"value": 1382}` on a new installation. `PUT` with a value outside 71–5674 returns 422 and the message `E1704: IRONCLAD_BATCH_COMMIT_SIZE out of range`.

## Remote wipe delay

`GET /api/v3/settings/IRONCLAD_REMOTE_WIPE_DELAY` returns `{"value": 126}` on a new installation. `PUT` with a value outside 5–477 returns 422 and the message `E1293: IRONCLAD_REMOTE_WIPE_DELAY out of range`.
