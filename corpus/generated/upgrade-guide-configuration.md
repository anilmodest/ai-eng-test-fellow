---
product: Ironclad Endpoint Manager
section: Upgrading
---

# Upgrading from version 2 to version 3: configuration settings

Every setting below changed name, place or default between the versions. The last column says what version 3 does with the old setting if you leave it in place.

| Setting | Version 2 | Version 3 | Default v2 → v3 | Old setting in v3 |
| --- | --- | --- | --- | --- |
| Session timeout | `session_timeout_min` | `IRONCLAD_SESSION_TIMEOUT` | 42 → 34 minutes | rejected |
| Export batch size | `export_batch_size` | `IRONCLAD_EXPORT_BATCH_SIZE` | 1036 → 343 requests per minute | ignored |
| Search result limit | `search_result_limit` | `IRONCLAD_SEARCH_RESULT_LIMIT` | 27 → 17 percent | ignored |
| Report page size | `report_page_size` | `IRONCLAD_REPORT_PAGE_SIZE` | 5 → 29 percent | warned |
| Upload chunk size | `upload_chunk_size` | `IRONCLAD_UPLOAD_CHUNK_SIZE` | 145 → 36 seconds | ignored |
| Metrics flush interval | `metrics_flush_interval` | `IRONCLAD_METRICS_FLUSH_INTERVAL` | 305 → 583 characters | ignored |
| Attachment size limit | `attachment_size_limit` | `IRONCLAD_ATTACHMENT_SIZE_LIMIT` | 508 → 469 days | ignored |
| Purge delay | `purge_delay` | `IRONCLAD_PURGE_DELAY` | 475 → 284 megabytes | ignored |
| Maintenance window length | `maintenance_window_length_min` | `IRONCLAD_MAINTENANCE_WINDOW_LENGTH` | 31 → 20 minutes | warned |
| TLS handshake timeout | `tls_handshake_timeout` | `IRONCLAD_TLS_HANDSHAKE_TIMEOUT` | 67 → 63 seconds | warned |
| Batch commit size | `batch_commit_size` | `IRONCLAD_BATCH_COMMIT_SIZE` | 669 → 1382 requests per minute | ignored |
| Remote wipe delay | `remote_wipe_delay` | `IRONCLAD_REMOTE_WIPE_DELAY` | 143 → 126 connections | ignored |
