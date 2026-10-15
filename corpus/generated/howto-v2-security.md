---
product: Ironclad Endpoint Manager
version: v2
section: Security
---

# Security guide (Ironclad v2)

This guide covers every security setting in version 2 of Ironclad Endpoint Manager. Read it before changing more than one setting at once: several interact.

| Setting | Name | Default | Range | Takes effect |
| --- | --- | --- | --- | --- |
| Webhook delivery timeout | `webhook_delivery_timeout` | 435 megabytes | 36–1769 | restart |
| Backup retention | `backup_retention` | 809 characters | 64–3178 | restart |
| Password expiry | `password_expiry_con` | 92 connections | 7–432 | restart |
| Email send rate | `email_send_rate` | 249 characters | 40–3244 | restart |
| Cache expiry | `cache_expiry` | 300 items | 139–8716 | next job |
| Scheduler worker count | `scheduler_worker_count` | 510 megabytes | 33–1742 | next job |
| Token lifetime | `token_lifetime_ite` | 1517 items | 182–8406 | next job |
| Concurrent session limit | `concurrent_session_limit` | 136 seconds | 5–549 | restart |
| Check-in interval | `check_in_interval` | 12 minutes | 3–237 | next job |

## Webhook delivery timeout

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The webhook delivery timeout setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Backup retention

In Ironclad Endpoint Manager, the backup retention is a single value measured in characters. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Password expiry

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The password expiry setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Email send rate

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The email send rate setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Cache expiry

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The cache expiry setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Scheduler worker count

In Ironclad Endpoint Manager, the scheduler worker count is a single value measured in megabytes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Token lifetime

In Ironclad Endpoint Manager, the token lifetime is a single value measured in items. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Concurrent session limit

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The concurrent session limit setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Check-in interval

This page describes the check-in interval setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

A change applies from the next job onwards. Jobs already running finish with the value they started with.
