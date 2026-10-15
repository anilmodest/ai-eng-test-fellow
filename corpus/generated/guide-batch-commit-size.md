---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the batch commit size

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The batch commit size setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## How it works

The batch commit size is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## Choosing a value

Start from the default of 1382 requests per minute and change it only with a reason you can write down. Raising the batch commit size trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 5674 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_batch_commit_size_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `batch_commit_size` | `IRONCLAD_BATCH_COMMIT_SIZE` |
| Default | 669 requests per minute | 1382 requests per minute |
| Range | 112–4676 | 71–5674 |
| Takes effect | restart | next job |

## A worked change

A customer with 400 seats saw the limit hit every afternoon. They raised the batch commit size by a quarter, watched the limit-hit metric for a week, saw it fall by two thirds, and stopped there. They wrote the reason into their change log, which is what made the next upgrade painless.
