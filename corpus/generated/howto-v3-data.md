---
product: Ironclad Endpoint Manager
version: v3
section: Data
---

# Data guide (Ironclad v3)

This guide covers every data setting in version 3 of Ironclad Endpoint Manager. Read it before changing more than one setting at once: several interact.

| Setting | Name | Default | Range | Takes effect |
| --- | --- | --- | --- | --- |
| Backup schedule interval | `IRONCLAD_BACKUP_SCHEDULE_INTERVAL` | 562 megabytes | 2–1738 | next job |
| Trace sampling rate | `IRONCLAD_TRACE_SAMPLING_RATE` | 87 seconds | 1–496 | restart |
| Bulk update limit | `IRONCLAD_BULK_UPDATE_LIMIT` | 817 items | 34–8156 | restart |
| Pagination cursor lifetime | `IRONCLAD_PAGINATION_CURSOR_LIFETIME` | 10 percent | 1–93 | next job |
| Temporary file lifetime | `IRONCLAD_TEMPORARY_FILE_LIFETIME` | 2623 items | 111–8772 | immediately |

## Backup schedule interval

This page describes the backup schedule interval setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Trace sampling rate

This page describes the trace sampling rate setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Bulk update limit

In Ironclad Endpoint Manager, the bulk update limit is a single value measured in items. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Pagination cursor lifetime

In Ironclad Endpoint Manager, the pagination cursor lifetime is a single value measured in percent. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Temporary file lifetime

This page describes the temporary file lifetime setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.
