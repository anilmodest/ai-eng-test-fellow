---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the webhook delivery timeout

This page describes the webhook delivery timeout setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## How it works

The webhook delivery timeout is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## Choosing a value

Start from the default of 393 megabytes and change it only with a reason you can write down. Raising the webhook delivery timeout trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 1592 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_webhook_delivery_timeout_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `webhook_delivery_timeout` | `IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT` |
| Default | 435 megabytes | 393 megabytes |
| Range | 36–1769 | 9–1592 |
| Takes effect | restart | next job |

## A worked change

A customer with 400 seats saw the limit hit every afternoon. They raised the webhook delivery timeout by a quarter, watched the limit-hit metric for a week, saw it fall by two thirds, and stopped there. They wrote the reason into their change log, which is what made the next upgrade painless.
