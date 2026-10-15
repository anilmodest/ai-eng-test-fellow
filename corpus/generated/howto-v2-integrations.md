---
product: Ironclad Endpoint Manager
version: v2
section: Integrations
---

# Integrations guide (Ironclad v2)

This guide covers every integrations setting in version 2 of Ironclad Endpoint Manager. Read it before changing more than one setting at once: several interact.

| Setting | Name | Default | Range | Takes effect |
| --- | --- | --- | --- | --- |
| Connection pool size | `connection_pool_size_req` | 161 requests per minute | 89–4721 | restart |
| Request timeout | `request_timeout` | 21 minutes | 1–239 | restart |
| Import file size limit | `import_file_size_limit` | 443 megabytes | 9–1621 | restart |
| API rate limit | `api_rate_limit` | 373 megabytes | 38–2035 | restart |
| Password minimum length | `password_minimum_length` | 97 connections | 8–400 | restart |
| Failed login lockout | `failed_login_lockout_min` | 63 minutes | 5–218 | restart |
| Two-factor grace period | `two_factor_grace_period_con` | 100 connections | 7–382 | next job |
| Job queue depth | `job_queue_depth` | 130 days | 44–3019 | restart |
| Health check interval | `health_check_interval` | 50 minutes | 1–239 | restart |
| Field length limit | `field_length_limit` | 123 seconds | 9–479 | restart |
| DNS cache lifetime | `dns_cache_lifetime_con` | 144 connections | 7–430 | restart |
| Update deferral | `update_deferral_ite` | 692 items | 172–7718 | restart |

## Connection pool size

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The connection pool size setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Request timeout

This page describes the request timeout setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Import file size limit

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The import file size limit setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## API rate limit

This page describes the api rate limit setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Password minimum length

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The password minimum length setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Failed login lockout

In Ironclad Endpoint Manager, the failed login lockout is a single value measured in minutes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Two-factor grace period

In Ironclad Endpoint Manager, the two-factor grace period is a single value measured in connections. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Job queue depth

This page describes the job queue depth setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Health check interval

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The health check interval setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Field length limit

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The field length limit setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## DNS cache lifetime

This page describes the dns cache lifetime setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Update deferral

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The update deferral setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.
