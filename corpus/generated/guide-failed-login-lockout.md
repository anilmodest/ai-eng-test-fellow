---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the failed login lockout

This page describes the failed login lockout setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## How it works

The failed login lockout is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## Choosing a value

Start from the default of 49 minutes and change it only with a reason you can write down. Raising the failed login lockout trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 203 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_failed_login_lockout_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `failed_login_lockout_min` | `IRONCLAD_FAILED_LOGIN_LOCKOUT` |
| Default | 63 minutes | 49 minutes |
| Range | 5–218 | 1–203 |
| Takes effect | restart | immediately |

## A worked change

An administrator lowered the failed login lockout to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
