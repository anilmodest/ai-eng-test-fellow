---
product: Ironclad Endpoint Manager
section: Upgrading
---

# Upgrading from version 2 to version 3: data settings

Every setting below changed name, place or default between the versions. The last column says what version 3 does with the old setting if you leave it in place.

| Setting | Version 2 | Version 3 | Default v2 → v3 | Old setting in v3 |
| --- | --- | --- | --- | --- |
| Backup schedule interval | `backup_schedule_interval` | `IRONCLAD_BACKUP_SCHEDULE_INTERVAL` | 67 → 562 megabytes | rejected |
| Trace sampling rate | `trace_sampling_rate` | `IRONCLAD_TRACE_SAMPLING_RATE` | 134 → 87 seconds | ignored |
| Bulk update limit | `bulk_update_limit` | `IRONCLAD_BULK_UPDATE_LIMIT` | 2897 → 817 items | rejected |
| Pagination cursor lifetime | `pagination_cursor_lifetime` | `IRONCLAD_PAGINATION_CURSOR_LIFETIME` | 8 → 10 percent | ignored |
| Temporary file lifetime | `temporary_file_lifetime` | `IRONCLAD_TEMPORARY_FILE_LIFETIME` | 622 → 2623 items | warned |
