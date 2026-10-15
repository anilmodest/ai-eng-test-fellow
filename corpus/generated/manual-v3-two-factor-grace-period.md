---
product: Ironclad Endpoint Manager
version: v3
section: Integrations
---

# Two-factor grace period (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The two-factor grace period setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_TWO_FACTOR_GRACE_PERIOD`, as the environment variable. It takes a whole number of connections. The default is **129 connections**.

```
export IRONCLAD_TWO_FACTOR_GRACE_PERIOD=129
```

## Upgrading from version 2

`two_factor_grace_period_con`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1933: unknown setting two_factor_grace_period_con`. Remove it before upgrading.

## How it works

Internally, the service checks the two-factor grace period every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 129 connections therefore means 'at least 129', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Choosing a value

Start from the default of 129 connections and change it only with a reason you can write down. Raising the two-factor grace period trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 464 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_two_factor_grace_period_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 3. The highest accepted value is 464. A value outside that range is rejected and the previous value stays in force, with `E1933: IRONCLAD_TWO_FACTOR_GRACE_PERIOD out of range` in the log.

## Examples

| Value (connections) | When to use it |
| --- | --- |
| 3 | small installations, or testing |
| 129 | the default; right for most installations |
| 258 | busy installations with spare capacity |
| 464 | the maximum; only with a reason written down |

## Interactions

The two-factor grace period is often changed together with the connection pool size (`IRONCLAD_CONNECTION_POOL_SIZE`, default 383 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The two-factor grace period is often changed together with the request timeout (`IRONCLAD_REQUEST_TIMEOUT`, default 37 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_TWO_FACTOR_GRACE_PERIOD` and given a new default of 129 connections in release 3.7. Before that release, version 3 still used the version 2 name.

## Related

- Connection pool size: see the Connection pool size page for version 3.
- Request timeout: see the Request timeout page for version 3.
