---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the metrics flush interval

In Ironclad Endpoint Manager, the metrics flush interval is a single value measured in characters. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## How it works

The metrics flush interval is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## Choosing a value

Start from the default of 583 characters and change it only with a reason you can write down. Raising the metrics flush interval trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 3178 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_metrics_flush_interval_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `metrics_flush_interval` | `IRONCLAD_METRICS_FLUSH_INTERVAL` |
| Default | 305 characters | 583 characters |
| Range | 67–3729 | 61–3178 |
| Takes effect | restart | immediately |

## A worked change

A customer with 400 seats saw the limit hit every afternoon. They raised the metrics flush interval by a quarter, watched the limit-hit metric for a week, saw it fall by two thirds, and stopped there. They wrote the reason into their change log, which is what made the next upgrade painless.
