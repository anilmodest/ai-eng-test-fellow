---
product: Ironclad Endpoint Manager
version: v3
section: Security
---

# Security guide (Ironclad v3)

This guide covers every security setting in version 3 of Ironclad Endpoint Manager. Read it before changing more than one setting at once: several interact.

| Setting | Name | Default | Range | Takes effect |
| --- | --- | --- | --- | --- |
| Webhook delivery timeout | `IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT` | 393 megabytes | 9–1592 | next job |
| Backup retention | `IRONCLAD_BACKUP_RETENTION` | 559 characters | 60–3329 | next job |
| Password expiry | `IRONCLAD_PASSWORD_EXPIRY` | 40 connections | 3–445 | next job |
| Email send rate | `IRONCLAD_EMAIL_SEND_RATE` | 635 characters | 35–3580 | immediately |
| Cache expiry | `IRONCLAD_CACHE_EXPIRY` | 2308 items | 191–9874 | next job |
| Scheduler worker count | `IRONCLAD_SCHEDULER_WORKER_COUNT` | 10 megabytes | 1–1891 | immediately |
| Token lifetime | `IRONCLAD_TOKEN_LIFETIME` | 271 items | 122–7524 | restart |
| Concurrent session limit | `IRONCLAD_CONCURRENT_SESSION_LIMIT` | 168 seconds | 4–578 | immediately |
| Check-in interval | `IRONCLAD_CHECK_IN_INTERVAL` | 43 minutes | 1–221 | next job |

## Webhook delivery timeout

In Ironclad Endpoint Manager, the webhook delivery timeout is a single value measured in megabytes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Backup retention

In Ironclad Endpoint Manager, the backup retention is a single value measured in characters. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Password expiry

In Ironclad Endpoint Manager, the password expiry is a single value measured in connections. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Email send rate

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The email send rate setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Cache expiry

This page describes the cache expiry setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Scheduler worker count

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The scheduler worker count setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Token lifetime

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The token lifetime setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Concurrent session limit

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The concurrent session limit setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Check-in interval

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The check-in interval setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

A change applies from the next job onwards. Jobs already running finish with the value they started with.
