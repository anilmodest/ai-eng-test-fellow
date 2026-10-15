---
product: Ironclad Endpoint Manager
version: v3
section: Operations
---

# Webhook retry count (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The webhook retry count setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_WEBHOOK_RETRY_COUNT`, as the environment variable. It takes a whole number of items. The default is **2365 items**.

```
export IRONCLAD_WEBHOOK_RETRY_COUNT=2365
```

## Upgrading from version 2

`webhook_retry_count`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 2365 items, not on the value in the old file.

## How it works

Every request carries the webhook retry count that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 2365 items. Large ones usually settle between the default and twice the default. Values near the minimum of 87 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_webhook_retry_count_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 87. The highest accepted value is 9276. A value outside that range is rejected and the previous value stays in force, with `E1811: IRONCLAD_WEBHOOK_RETRY_COUNT out of range` in the log.

## Examples

| Value (items) | When to use it |
| --- | --- |
| 87 | small installations, or testing |
| 2365 | the default; right for most installations |
| 4730 | busy installations with spare capacity |
| 9276 | the maximum; only with a reason written down |

## Interactions

The webhook retry count is often changed together with the audit log retention (`IRONCLAD_AUDIT_LOG_RETENTION`, default 1060 days in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The webhook retry count is often changed together with the notification digest interval (`IRONCLAD_NOTIFICATION_DIGEST_INTERVAL`, default 40 seconds in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_WEBHOOK_RETRY_COUNT` and given a new default of 2365 items in release 3.2. Before that release, version 3 still used the version 2 name.

## Related

- Audit log retention: see the Audit log retention page for version 3.
- Notification digest interval: see the Notification digest interval page for version 3.
