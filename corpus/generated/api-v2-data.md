---
product: Ironclad Endpoint Manager
version: v2
section: API reference
---

# Settings API: data (v2)

Read or change a setting over HTTP. All calls need an administrator token. Base path `/api/v2/settings`.

## Backup schedule interval

`GET /api/v2/settings/backup_schedule_interval` returns `{"value": 67}` on a new installation. `PUT` with a value outside 10–1873 returns 422 and the message `E1976: backup_schedule_interval out of range`.

## Trace sampling rate

`GET /api/v2/settings/trace_sampling_rate` returns `{"value": 134}` on a new installation. `PUT` with a value outside 3–513 returns 422 and the message `E1533: trace_sampling_rate out of range`.

## Bulk update limit

`GET /api/v2/settings/bulk_update_limit` returns `{"value": 2897}` on a new installation. `PUT` with a value outside 184–9526 returns 422 and the message `E1846: bulk_update_limit out of range`.

## Pagination cursor lifetime

`GET /api/v2/settings/pagination_cursor_lifetime` returns `{"value": 8}` on a new installation. `PUT` with a value outside 2–84 returns 422 and the message `E1627: pagination_cursor_lifetime out of range`.

## Temporary file lifetime

`GET /api/v2/settings/temporary_file_lifetime` returns `{"value": 622}` on a new installation. `PUT` with a value outside 128–7550 returns 422 and the message `E1196: temporary_file_lifetime out of range`.
