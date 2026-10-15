---
product: Ironclad Endpoint Manager
version: v3
section: Operations
---

# Operations guide (Ironclad v3)

This guide covers every operations setting in version 3 of Ironclad Endpoint Manager. Read it before changing more than one setting at once: several interact.

| Setting | Name | Default | Range | Takes effect |
| --- | --- | --- | --- | --- |
| Audit log retention | `IRONCLAD_AUDIT_LOG_RETENTION` | 1060 days | 1–3336 | immediately |
| Webhook retry count | `IRONCLAD_WEBHOOK_RETRY_COUNT` | 2365 items | 87–9276 | next job |
| Notification digest interval | `IRONCLAD_NOTIFICATION_DIGEST_INTERVAL` | 40 seconds | 7–512 | restart |
| Refresh token lifetime | `IRONCLAD_REFRESH_TOKEN_LIFETIME` | 102 seconds | 3–566 | next job |
| Idle disconnect | `IRONCLAD_IDLE_DISCONNECT` | 21 percent | 1–98 | next job |
| Archive threshold | `IRONCLAD_ARCHIVE_THRESHOLD` | 27 connections | 4–466 | restart |
| Sync interval | `IRONCLAD_SYNC_INTERVAL` | 38 seconds | 6–453 | restart |
| Lock wait timeout | `IRONCLAD_LOCK_WAIT_TIMEOUT` | 33 minutes | 1–210 | restart |
| Compliance grace period | `IRONCLAD_COMPLIANCE_GRACE_PERIOD` | 7 percent | 2–96 | immediately |

## Audit log retention

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The audit log retention setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Webhook retry count

In Ironclad Endpoint Manager, the webhook retry count is a single value measured in items. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Notification digest interval

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The notification digest interval setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Refresh token lifetime

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The refresh token lifetime setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Idle disconnect

In Ironclad Endpoint Manager, the idle disconnect is a single value measured in percent. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Archive threshold

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The archive threshold setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Sync interval

In Ironclad Endpoint Manager, the sync interval is a single value measured in seconds. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Lock wait timeout

In Ironclad Endpoint Manager, the lock wait timeout is a single value measured in minutes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Compliance grace period

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The compliance grace period setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

Changes take effect immediately: the service watches the setting and reloads it without a restart.
