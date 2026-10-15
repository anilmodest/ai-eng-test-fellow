---
product: Ironclad Endpoint Manager
version: v3
section: API reference
---

# Settings API: data (v3)

Read or change a setting over HTTP. All calls need an administrator token. Base path `/api/v3/settings`.

## Backup schedule interval

`GET /api/v3/settings/IRONCLAD_BACKUP_SCHEDULE_INTERVAL` returns `{"value": 562}` on a new installation. `PUT` with a value outside 2–1738 returns 422 and the message `E1976: IRONCLAD_BACKUP_SCHEDULE_INTERVAL out of range`.

## Trace sampling rate

`GET /api/v3/settings/IRONCLAD_TRACE_SAMPLING_RATE` returns `{"value": 87}` on a new installation. `PUT` with a value outside 1–496 returns 422 and the message `E1533: IRONCLAD_TRACE_SAMPLING_RATE out of range`.

## Bulk update limit

`GET /api/v3/settings/IRONCLAD_BULK_UPDATE_LIMIT` returns `{"value": 817}` on a new installation. `PUT` with a value outside 34–8156 returns 422 and the message `E1846: IRONCLAD_BULK_UPDATE_LIMIT out of range`.

## Pagination cursor lifetime

`GET /api/v3/settings/IRONCLAD_PAGINATION_CURSOR_LIFETIME` returns `{"value": 10}` on a new installation. `PUT` with a value outside 1–93 returns 422 and the message `E1627: IRONCLAD_PAGINATION_CURSOR_LIFETIME out of range`.

## Temporary file lifetime

`GET /api/v3/settings/IRONCLAD_TEMPORARY_FILE_LIFETIME` returns `{"value": 2623}` on a new installation. `PUT` with a value outside 111–8772 returns 422 and the message `E1196: IRONCLAD_TEMPORARY_FILE_LIFETIME out of range`.
