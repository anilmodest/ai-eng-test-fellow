---
product: Ironclad Endpoint Manager
version: v2
section: Integrations
---

# Job queue depth (Ironclad v2)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The job queue depth setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `job_queue_depth`, in `ironclad.conf`, in the `[server]` block. It takes a whole number of days. The default is **130 days**.

```
job_queue_depth = 130
```

## How it works

Internally, the service checks the job queue depth every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 130 days therefore means 'at least 130', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 130 days and change it only with a reason you can write down. Raising the job queue depth trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 3019 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_job_queue_depth_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 44. The highest accepted value is 3019. A value outside that range is rejected and the previous value stays in force, with `E1483: job_queue_depth out of range` in the log.

## Examples

| Value (days) | When to use it |
| --- | --- |
| 44 | small installations, or testing |
| 130 | the default; right for most installations |
| 260 | busy installations with spare capacity |
| 3019 | the maximum; only with a reason written down |

## Interactions

The job queue depth is often changed together with the connection pool size (`connection_pool_size_req`, default 161 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The job queue depth is often changed together with the request timeout (`request_timeout`, default 21 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `job_queue_depth`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Connection pool size: see the Connection pool size page for version 2.
- Request timeout: see the Request timeout page for version 2.
