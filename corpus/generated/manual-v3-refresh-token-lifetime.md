---
product: Ironclad Endpoint Manager
version: v3
section: Operations
---

# Refresh token lifetime (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The refresh token lifetime setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_REFRESH_TOKEN_LIFETIME`, as the environment variable. It takes a whole number of seconds. The default is **102 seconds**.

```
export IRONCLAD_REFRESH_TOKEN_LIFETIME=102
```

## Upgrading from version 2

`refresh_token_lifetime`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1624: unknown setting refresh_token_lifetime`. Remove it before upgrading.

## How it works

Internally, the service checks the refresh token lifetime every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 102 seconds therefore means 'at least 102', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

Start from the default of 102 seconds and change it only with a reason you can write down. Raising the refresh token lifetime trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 566 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_refresh_token_lifetime_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 3. The highest accepted value is 566. A value outside that range is rejected and the previous value stays in force, with `E1624: IRONCLAD_REFRESH_TOKEN_LIFETIME out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 3 | small installations, or testing |
| 102 | the default; right for most installations |
| 204 | busy installations with spare capacity |
| 566 | the maximum; only with a reason written down |

## Interactions

The refresh token lifetime is often changed together with the audit log retention (`IRONCLAD_AUDIT_LOG_RETENTION`, default 1060 days in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The refresh token lifetime is often changed together with the webhook retry count (`IRONCLAD_WEBHOOK_RETRY_COUNT`, default 2365 items in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_REFRESH_TOKEN_LIFETIME` and given a new default of 102 seconds in release 3.4. Before that release, version 3 still used the version 2 name.

## Related

- Audit log retention: see the Audit log retention page for version 3.
- Webhook retry count: see the Webhook retry count page for version 3.
