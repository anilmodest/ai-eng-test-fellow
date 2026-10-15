---
product: Ironclad Endpoint Manager
version: v3
section: Integrations
---

# Field length limit (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The field length limit setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_FIELD_LENGTH_LIMIT`, as the environment variable. It takes a whole number of seconds. The default is **166 seconds**.

```
export IRONCLAD_FIELD_LENGTH_LIMIT=166
```

## Upgrading from version 2

`field_length_limit`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1954: unknown setting field_length_limit`. Remove it before upgrading.

## How it works

The field length limit is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 166 seconds. Large ones usually settle between the default and twice the default. Values near the minimum of 11 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_field_length_limit_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 11. The highest accepted value is 486. A value outside that range is rejected and the previous value stays in force, with `E1954: IRONCLAD_FIELD_LENGTH_LIMIT out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 11 | small installations, or testing |
| 166 | the default; right for most installations |
| 332 | busy installations with spare capacity |
| 486 | the maximum; only with a reason written down |

## Interactions

The field length limit is often changed together with the connection pool size (`IRONCLAD_CONNECTION_POOL_SIZE`, default 383 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The field length limit is often changed together with the request timeout (`IRONCLAD_REQUEST_TIMEOUT`, default 37 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_FIELD_LENGTH_LIMIT` and given a new default of 166 seconds in release 3.0. Before that release, version 3 still used the version 2 name.

## Related

- Connection pool size: see the Connection pool size page for version 3.
- Request timeout: see the Request timeout page for version 3.
