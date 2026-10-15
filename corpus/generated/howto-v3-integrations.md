---
product: Ironclad Endpoint Manager
version: v3
section: Integrations
---

# Integrations guide (Ironclad v3)

This guide covers every integrations setting in version 3 of Ironclad Endpoint Manager. Read it before changing more than one setting at once: several interact.

| Setting | Name | Default | Range | Takes effect |
| --- | --- | --- | --- | --- |
| Connection pool size | `IRONCLAD_CONNECTION_POOL_SIZE` | 383 requests per minute | 40–4583 | next job |
| Request timeout | `IRONCLAD_REQUEST_TIMEOUT` | 37 minutes | 4–237 | immediately |
| Import file size limit | `IRONCLAD_IMPORT_FILE_SIZE_LIMIT` | 9 megabytes | 5–1565 | next job |
| API rate limit | `IRONCLAD_API_RATE_LIMIT` | 173 megabytes | 32–1539 | next job |
| Password minimum length | `IRONCLAD_PASSWORD_MINIMUM_LENGTH` | 125 connections | 7–441 | immediately |
| Failed login lockout | `IRONCLAD_FAILED_LOGIN_LOCKOUT` | 49 minutes | 1–203 | immediately |
| Two-factor grace period | `IRONCLAD_TWO_FACTOR_GRACE_PERIOD` | 129 connections | 3–464 | immediately |
| Job queue depth | `IRONCLAD_JOB_QUEUE_DEPTH` | 461 days | 56–2909 | next job |
| Health check interval | `IRONCLAD_HEALTH_CHECK_INTERVAL` | 20 minutes | 4–181 | next job |
| Field length limit | `IRONCLAD_FIELD_LENGTH_LIMIT` | 166 seconds | 11–486 | next job |
| DNS cache lifetime | `IRONCLAD_DNS_CACHE_LIFETIME` | 60 connections | 7–500 | restart |
| Update deferral | `IRONCLAD_UPDATE_DEFERRAL` | 2560 items | 159–8640 | immediately |

## Connection pool size

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The connection pool size setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Request timeout

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The request timeout setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Import file size limit

In Ironclad Endpoint Manager, the import file size limit is a single value measured in megabytes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## API rate limit

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The api rate limit setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Password minimum length

This page describes the password minimum length setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Failed login lockout

This page describes the failed login lockout setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Two-factor grace period

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The two-factor grace period setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Job queue depth

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The job queue depth setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Health check interval

This page describes the health check interval setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Field length limit

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The field length limit setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## DNS cache lifetime

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The dns cache lifetime setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Update deferral

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The update deferral setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

Changes take effect immediately: the service watches the setting and reloads it without a restart.
