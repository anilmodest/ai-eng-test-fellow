---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the dns cache lifetime

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The dns cache lifetime setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## How it works

The dns cache lifetime is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## Choosing a value

Start from the default of 60 connections and change it only with a reason you can write down. Raising the dns cache lifetime trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 500 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_dns_cache_lifetime_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `dns_cache_lifetime_con` | `IRONCLAD_DNS_CACHE_LIFETIME` |
| Default | 144 connections | 60 connections |
| Range | 7–430 | 7–500 |
| Takes effect | restart | restart |

## A worked change

An administrator lowered the dns cache lifetime to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
