---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the trace sampling rate

In Ironclad Endpoint Manager, the trace sampling rate is a single value measured in seconds. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## How it works

The trace sampling rate is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## Choosing a value

Start from the default of 87 seconds and change it only with a reason you can write down. Raising the trace sampling rate trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 496 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_trace_sampling_rate_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `trace_sampling_rate` | `IRONCLAD_TRACE_SAMPLING_RATE` |
| Default | 134 seconds | 87 seconds |
| Range | 3–513 | 1–496 |
| Takes effect | next job | restart |

## A worked change

A customer with 400 seats saw the limit hit every afternoon. They raised the trace sampling rate by a quarter, watched the limit-hit metric for a week, saw it fall by two thirds, and stopped there. They wrote the reason into their change log, which is what made the next upgrade painless.
