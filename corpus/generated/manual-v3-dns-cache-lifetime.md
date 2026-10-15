---
product: Ironclad Endpoint Manager
version: v3
section: Integrations
---

# DNS cache lifetime (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The dns cache lifetime setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_DNS_CACHE_LIFETIME`, as the environment variable. It takes a whole number of connections. The default is **60 connections**.

```
export IRONCLAD_DNS_CACHE_LIFETIME=60
```

## Upgrading from version 2

`dns_cache_lifetime_con`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 60 connections, not on the value in the old file.

## How it works

The dns cache lifetime is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 60 connections and change it only with a reason you can write down. Raising the dns cache lifetime trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 500 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_dns_cache_lifetime_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 7. The highest accepted value is 500. A value outside that range is rejected and the previous value stays in force, with `E1800: IRONCLAD_DNS_CACHE_LIFETIME out of range` in the log.

## Examples

| Value (connections) | When to use it |
| --- | --- |
| 7 | small installations, or testing |
| 60 | the default; right for most installations |
| 120 | busy installations with spare capacity |
| 500 | the maximum; only with a reason written down |

## Interactions

The dns cache lifetime is often changed together with the connection pool size (`IRONCLAD_CONNECTION_POOL_SIZE`, default 383 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The dns cache lifetime is often changed together with the request timeout (`IRONCLAD_REQUEST_TIMEOUT`, default 37 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_DNS_CACHE_LIFETIME` and given a new default of 60 connections in release 3.9. Before that release, version 3 still used the version 2 name.

## Related

- Connection pool size: see the Connection pool size page for version 3.
- Request timeout: see the Request timeout page for version 3.
