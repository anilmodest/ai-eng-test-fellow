---
product: Ironclad Endpoint Manager
version: v3
section: Integrations
---

# Failed login lockout (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The failed login lockout setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_FAILED_LOGIN_LOCKOUT`, as the environment variable. It takes a whole number of minutes. The default is **49 minutes**.

```
export IRONCLAD_FAILED_LOGIN_LOCKOUT=49
```

## Upgrading from version 2

`failed_login_lockout_min`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1457: unknown setting failed_login_lockout_min`. Remove it before upgrading.

## How it works

Internally, the service checks the failed login lockout every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 49 minutes therefore means 'at least 49', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Choosing a value

Start from the default of 49 minutes and change it only with a reason you can write down. Raising the failed login lockout trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 203 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_failed_login_lockout_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 1. The highest accepted value is 203. A value outside that range is rejected and the previous value stays in force, with `E1457: IRONCLAD_FAILED_LOGIN_LOCKOUT out of range` in the log.

## Examples

| Value (minutes) | When to use it |
| --- | --- |
| 1 | small installations, or testing |
| 49 | the default; right for most installations |
| 98 | busy installations with spare capacity |
| 203 | the maximum; only with a reason written down |

## Interactions

The failed login lockout is often changed together with the connection pool size (`IRONCLAD_CONNECTION_POOL_SIZE`, default 383 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The failed login lockout is often changed together with the request timeout (`IRONCLAD_REQUEST_TIMEOUT`, default 37 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_FAILED_LOGIN_LOCKOUT` and given a new default of 49 minutes in release 3.8. Before that release, version 3 still used the version 2 name.

## Related

- Connection pool size: see the Connection pool size page for version 3.
- Request timeout: see the Request timeout page for version 3.
