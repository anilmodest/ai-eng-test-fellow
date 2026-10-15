---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the token lifetime

In Ironclad Endpoint Manager, the token lifetime is a single value measured in items. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## How it works

The token lifetime is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## Choosing a value

Start from the default of 271 items and change it only with a reason you can write down. Raising the token lifetime trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 7524 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_token_lifetime_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `token_lifetime_ite` | `IRONCLAD_TOKEN_LIFETIME` |
| Default | 1517 items | 271 items |
| Range | 182–8406 | 122–7524 |
| Takes effect | next job | restart |

## A worked change

An administrator lowered the token lifetime to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
