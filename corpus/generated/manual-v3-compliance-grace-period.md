---
product: Ironclad Endpoint Manager
version: v3
section: Operations
---

# Compliance grace period (Ironclad v3)

In Ironclad Endpoint Manager, the compliance grace period is a single value measured in percent. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `IRONCLAD_COMPLIANCE_GRACE_PERIOD`, as the environment variable. It takes a whole number of percent. The default is **7 percent**.

```
export IRONCLAD_COMPLIANCE_GRACE_PERIOD=7
```

## Upgrading from version 2

`compliance_grace_period_per`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 7 percent, not on the value in the old file.

## How it works

The compliance grace period is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 7 percent. Large ones usually settle between the default and twice the default. Values near the minimum of 2 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_compliance_grace_period_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 2. The highest accepted value is 96. A value outside that range is rejected and the previous value stays in force, with `E1501: IRONCLAD_COMPLIANCE_GRACE_PERIOD out of range` in the log.

## Examples

| Value (percent) | When to use it |
| --- | --- |
| 2 | small installations, or testing |
| 7 | the default; right for most installations |
| 14 | busy installations with spare capacity |
| 96 | the maximum; only with a reason written down |

## Interactions

The compliance grace period is often changed together with the audit log retention (`IRONCLAD_AUDIT_LOG_RETENTION`, default 1060 days in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The compliance grace period is often changed together with the webhook retry count (`IRONCLAD_WEBHOOK_RETRY_COUNT`, default 2365 items in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_COMPLIANCE_GRACE_PERIOD` and given a new default of 7 percent in release 3.1. Before that release, version 3 still used the version 2 name.

## Related

- Audit log retention: see the Audit log retention page for version 3.
- Webhook retry count: see the Webhook retry count page for version 3.
