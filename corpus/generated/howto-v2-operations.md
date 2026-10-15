---
product: Ironclad Endpoint Manager
version: v2
section: Operations
---

# Operations guide (Ironclad v2)

This guide covers every operations setting in version 2 of Ironclad Endpoint Manager. Read it before changing more than one setting at once: several interact.

| Setting | Name | Default | Range | Takes effect |
| --- | --- | --- | --- | --- |
| Audit log retention | `audit_log_retention` | 391 days | 29–3452 | restart |
| Webhook retry count | `webhook_retry_count` | 1558 items | 52–9567 | restart |
| Notification digest interval | `notification_digest_interval` | 87 seconds | 5–463 | restart |
| Refresh token lifetime | `refresh_token_lifetime` | 69 seconds | 9–460 | restart |
| Idle disconnect | `idle_disconnect` | 22 percent | 2–88 | restart |
| Archive threshold | `archive_threshold` | 41 connections | 5–383 | next job |
| Sync interval | `sync_interval` | 48 seconds | 8–539 | restart |
| Lock wait timeout | `lock_wait_timeout` | 22 minutes | 3–211 | restart |
| Compliance grace period | `compliance_grace_period_per` | 9 percent | 2–77 | restart |

## Audit log retention

This page describes the audit log retention setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Webhook retry count

In Ironclad Endpoint Manager, the webhook retry count is a single value measured in items. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Notification digest interval

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The notification digest interval setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Refresh token lifetime

In Ironclad Endpoint Manager, the refresh token lifetime is a single value measured in seconds. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Idle disconnect

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The idle disconnect setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Archive threshold

This page describes the archive threshold setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Sync interval

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The sync interval setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Lock wait timeout

In Ironclad Endpoint Manager, the lock wait timeout is a single value measured in minutes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Compliance grace period

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The compliance grace period setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.
