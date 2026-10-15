---
product: Ironclad Endpoint Manager
version: v3
section: Integrations
---

# Job queue depth (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The job queue depth setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_JOB_QUEUE_DEPTH`, as the environment variable. It takes a whole number of days. The default is **461 days**.

```
export IRONCLAD_JOB_QUEUE_DEPTH=461
```

## Upgrading from version 2

`job_queue_depth`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1483: unknown setting job_queue_depth`. Remove it before upgrading.

## How it works

Every request carries the job queue depth that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

Start from the default of 461 days and change it only with a reason you can write down. Raising the job queue depth trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 2909 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_job_queue_depth_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 56. The highest accepted value is 2909. A value outside that range is rejected and the previous value stays in force, with `E1483: IRONCLAD_JOB_QUEUE_DEPTH out of range` in the log.

## Examples

| Value (days) | When to use it |
| --- | --- |
| 56 | small installations, or testing |
| 461 | the default; right for most installations |
| 922 | busy installations with spare capacity |
| 2909 | the maximum; only with a reason written down |

## Interactions

The job queue depth is often changed together with the connection pool size (`IRONCLAD_CONNECTION_POOL_SIZE`, default 383 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The job queue depth is often changed together with the request timeout (`IRONCLAD_REQUEST_TIMEOUT`, default 37 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_JOB_QUEUE_DEPTH` and given a new default of 461 days in release 3.2. Before that release, version 3 still used the version 2 name.

## Related

- Connection pool size: see the Connection pool size page for version 3.
- Request timeout: see the Request timeout page for version 3.
