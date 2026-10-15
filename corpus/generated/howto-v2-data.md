---
product: Ironclad Endpoint Manager
version: v2
section: Data
---

# Data guide (Ironclad v2)

This guide covers every data setting in version 2 of Ironclad Endpoint Manager. Read it before changing more than one setting at once: several interact.

| Setting | Name | Default | Range | Takes effect |
| --- | --- | --- | --- | --- |
| Backup schedule interval | `backup_schedule_interval` | 67 megabytes | 10–1873 | next job |
| Trace sampling rate | `trace_sampling_rate` | 134 seconds | 3–513 | next job |
| Bulk update limit | `bulk_update_limit` | 2897 items | 184–9526 | restart |
| Pagination cursor lifetime | `pagination_cursor_lifetime` | 8 percent | 2–84 | restart |
| Temporary file lifetime | `temporary_file_lifetime` | 622 items | 128–7550 | restart |

## Backup schedule interval

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The backup schedule interval setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Trace sampling rate

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The trace sampling rate setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Bulk update limit

In Ironclad Endpoint Manager, the bulk update limit is a single value measured in items. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Pagination cursor lifetime

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The pagination cursor lifetime setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Temporary file lifetime

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The temporary file lifetime setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.
