---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the scheduler worker count

In Ironclad Endpoint Manager, the scheduler worker count is a single value measured in megabytes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## How it works

The scheduler worker count is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 10 megabytes. Large ones usually settle between the default and twice the default. Values near the minimum of 1 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_scheduler_worker_count_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `scheduler_worker_count` | `IRONCLAD_SCHEDULER_WORKER_COUNT` |
| Default | 510 megabytes | 10 megabytes |
| Range | 33–1742 | 1–1891 |
| Takes effect | next job | immediately |

## A worked change

An administrator lowered the scheduler worker count to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
