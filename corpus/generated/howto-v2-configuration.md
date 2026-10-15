---
product: Ironclad Endpoint Manager
version: v2
section: Configuration
---

# Configuration guide (Ironclad v2)

This guide covers every configuration setting in version 2 of Ironclad Endpoint Manager. Read it before changing more than one setting at once: several interact.

| Setting | Name | Default | Range | Takes effect |
| --- | --- | --- | --- | --- |
| Session timeout | `session_timeout_min` | 42 minutes | 2–188 | restart |
| Export batch size | `export_batch_size` | 1036 requests per minute | 55–4711 | restart |
| Search result limit | `search_result_limit` | 27 percent | 2–82 | restart |
| Report page size | `report_page_size` | 5 percent | 2–89 | restart |
| Upload chunk size | `upload_chunk_size` | 145 seconds | 6–583 | restart |
| Metrics flush interval | `metrics_flush_interval` | 305 characters | 67–3729 | restart |
| Attachment size limit | `attachment_size_limit` | 508 days | 14–3213 | restart |
| Purge delay | `purge_delay` | 475 megabytes | 36–1671 | restart |
| Maintenance window length | `maintenance_window_length_min` | 31 minutes | 3–195 | restart |
| TLS handshake timeout | `tls_handshake_timeout` | 67 seconds | 3–497 | next job |
| Batch commit size | `batch_commit_size` | 669 requests per minute | 112–4676 | restart |
| Remote wipe delay | `remote_wipe_delay` | 143 connections | 7–426 | next job |

## Session timeout

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The session timeout setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Export batch size

In Ironclad Endpoint Manager, the export batch size is a single value measured in requests per minute. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Search result limit

In Ironclad Endpoint Manager, the search result limit is a single value measured in percent. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Report page size

This page describes the report page size setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Upload chunk size

This page describes the upload chunk size setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Metrics flush interval

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The metrics flush interval setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Attachment size limit

In Ironclad Endpoint Manager, the attachment size limit is a single value measured in days. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Purge delay

In Ironclad Endpoint Manager, the purge delay is a single value measured in megabytes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Maintenance window length

In Ironclad Endpoint Manager, the maintenance window length is a single value measured in minutes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## TLS handshake timeout

In Ironclad Endpoint Manager, the tls handshake timeout is a single value measured in seconds. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Batch commit size

In Ironclad Endpoint Manager, the batch commit size is a single value measured in requests per minute. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Remote wipe delay

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The remote wipe delay setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

A change applies from the next job onwards. Jobs already running finish with the value they started with.
