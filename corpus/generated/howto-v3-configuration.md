---
product: Ironclad Endpoint Manager
version: v3
section: Configuration
---

# Configuration guide (Ironclad v3)

This guide covers every configuration setting in version 3 of Ironclad Endpoint Manager. Read it before changing more than one setting at once: several interact.

| Setting | Name | Default | Range | Takes effect |
| --- | --- | --- | --- | --- |
| Session timeout | `IRONCLAD_SESSION_TIMEOUT` | 34 minutes | 3–209 | next job |
| Export batch size | `IRONCLAD_EXPORT_BATCH_SIZE` | 343 requests per minute | 65–5106 | next job |
| Search result limit | `IRONCLAD_SEARCH_RESULT_LIMIT` | 17 percent | 2–80 | restart |
| Report page size | `IRONCLAD_REPORT_PAGE_SIZE` | 29 percent | 2–97 | next job |
| Upload chunk size | `IRONCLAD_UPLOAD_CHUNK_SIZE` | 36 seconds | 1–563 | immediately |
| Metrics flush interval | `IRONCLAD_METRICS_FLUSH_INTERVAL` | 583 characters | 61–3178 | immediately |
| Attachment size limit | `IRONCLAD_ATTACHMENT_SIZE_LIMIT` | 469 days | 28–2779 | restart |
| Purge delay | `IRONCLAD_PURGE_DELAY` | 284 megabytes | 41–2031 | next job |
| Maintenance window length | `IRONCLAD_MAINTENANCE_WINDOW_LENGTH` | 20 minutes | 3–183 | restart |
| TLS handshake timeout | `IRONCLAD_TLS_HANDSHAKE_TIMEOUT` | 63 seconds | 12–572 | immediately |
| Batch commit size | `IRONCLAD_BATCH_COMMIT_SIZE` | 1382 requests per minute | 71–5674 | next job |
| Remote wipe delay | `IRONCLAD_REMOTE_WIPE_DELAY` | 126 connections | 5–477 | restart |

## Session timeout

This page describes the session timeout setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Export batch size

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The export batch size setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Search result limit

This page describes the search result limit setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Report page size

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The report page size setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Upload chunk size

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The upload chunk size setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Metrics flush interval

This page describes the metrics flush interval setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Attachment size limit

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The attachment size limit setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Purge delay

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The purge delay setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Maintenance window length

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The maintenance window length setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## TLS handshake timeout

In Ironclad Endpoint Manager, the tls handshake timeout is a single value measured in seconds. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Batch commit size

In Ironclad Endpoint Manager, the batch commit size is a single value measured in requests per minute. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Remote wipe delay

In Ironclad Endpoint Manager, the remote wipe delay is a single value measured in connections. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.
