---
product: Ironclad Endpoint Manager
version: v2
section: API reference
---

# Settings API: configuration (v2)

Read or change a setting over HTTP. All calls need an administrator token. Base path `/api/v2/settings`.

## Session timeout

`GET /api/v2/settings/session_timeout_min` returns `{"value": 42}` on a new installation. `PUT` with a value outside 2–188 returns 422 and the message `E1851: session_timeout_min out of range`.

## Export batch size

`GET /api/v2/settings/export_batch_size` returns `{"value": 1036}` on a new installation. `PUT` with a value outside 55–4711 returns 422 and the message `E1124: export_batch_size out of range`.

## Search result limit

`GET /api/v2/settings/search_result_limit` returns `{"value": 27}` on a new installation. `PUT` with a value outside 2–82 returns 422 and the message `E1251: search_result_limit out of range`.

## Report page size

`GET /api/v2/settings/report_page_size` returns `{"value": 5}` on a new installation. `PUT` with a value outside 2–89 returns 422 and the message `E1600: report_page_size out of range`.

## Upload chunk size

`GET /api/v2/settings/upload_chunk_size` returns `{"value": 145}` on a new installation. `PUT` with a value outside 6–583 returns 422 and the message `E1692: upload_chunk_size out of range`.

## Metrics flush interval

`GET /api/v2/settings/metrics_flush_interval` returns `{"value": 305}` on a new installation. `PUT` with a value outside 67–3729 returns 422 and the message `E1977: metrics_flush_interval out of range`.

## Attachment size limit

`GET /api/v2/settings/attachment_size_limit` returns `{"value": 508}` on a new installation. `PUT` with a value outside 14–3213 returns 422 and the message `E1171: attachment_size_limit out of range`.

## Purge delay

`GET /api/v2/settings/purge_delay` returns `{"value": 475}` on a new installation. `PUT` with a value outside 36–1671 returns 422 and the message `E1295: purge_delay out of range`.

## Maintenance window length

`GET /api/v2/settings/maintenance_window_length_min` returns `{"value": 31}` on a new installation. `PUT` with a value outside 3–195 returns 422 and the message `E1754: maintenance_window_length_min out of range`.

## TLS handshake timeout

`GET /api/v2/settings/tls_handshake_timeout` returns `{"value": 67}` on a new installation. `PUT` with a value outside 3–497 returns 422 and the message `E1286: tls_handshake_timeout out of range`.

## Batch commit size

`GET /api/v2/settings/batch_commit_size` returns `{"value": 669}` on a new installation. `PUT` with a value outside 112–4676 returns 422 and the message `E1704: batch_commit_size out of range`.

## Remote wipe delay

`GET /api/v2/settings/remote_wipe_delay` returns `{"value": 143}` on a new installation. `PUT` with a value outside 7–426 returns 422 and the message `E1293: remote_wipe_delay out of range`.
