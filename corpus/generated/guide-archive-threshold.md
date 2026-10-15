---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the archive threshold

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The archive threshold setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## How it works

The archive threshold is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 27 connections. Large ones usually settle between the default and twice the default. Values near the minimum of 4 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_archive_threshold_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `archive_threshold` | `IRONCLAD_ARCHIVE_THRESHOLD` |
| Default | 41 connections | 27 connections |
| Range | 5–383 | 4–466 |
| Takes effect | next job | restart |

## A worked change

An administrator lowered the archive threshold to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
