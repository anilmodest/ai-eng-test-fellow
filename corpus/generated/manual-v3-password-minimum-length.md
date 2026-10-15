---
product: Ironclad Endpoint Manager
version: v3
section: Integrations
---

# Password minimum length (Ironclad v3)

This page describes the password minimum length setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_PASSWORD_MINIMUM_LENGTH`, in the admin console, under Settings > Security. It takes a whole number of connections. The default is **125 connections**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_PASSWORD_MINIMUM_LENGTH 125`.

## Upgrading from version 2

`password_minimum_length`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1602: unknown setting password_minimum_length`. Remove it before upgrading.

## How it works

The password minimum length is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 125 connections. Large ones usually settle between the default and twice the default. Values near the minimum of 7 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_password_minimum_length_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 7. The highest accepted value is 441. A value outside that range is rejected and the previous value stays in force, with `E1602: IRONCLAD_PASSWORD_MINIMUM_LENGTH out of range` in the log.

## Examples

| Value (connections) | When to use it |
| --- | --- |
| 7 | small installations, or testing |
| 125 | the default; right for most installations |
| 250 | busy installations with spare capacity |
| 441 | the maximum; only with a reason written down |

## Interactions

The password minimum length is often changed together with the connection pool size (`IRONCLAD_CONNECTION_POOL_SIZE`, default 383 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The password minimum length is often changed together with the request timeout (`IRONCLAD_REQUEST_TIMEOUT`, default 37 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_PASSWORD_MINIMUM_LENGTH` and given a new default of 125 connections in release 3.1. Before that release, version 3 still used the version 2 name.

## Related

- Connection pool size: see the Connection pool size page for version 3.
- Request timeout: see the Request timeout page for version 3.
