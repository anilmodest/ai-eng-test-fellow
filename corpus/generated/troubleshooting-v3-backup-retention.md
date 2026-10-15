---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: backup retention (Ironclad v3)

Start here when the backup retention does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different backup retention from the one you set.
- The log shows `E1522: IRONCLAD_BACKUP_RETENTION out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 60 to 3329 characters. Out of range, the value is rejected with `E1522: IRONCLAD_BACKUP_RETENTION out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_BACKUP_RETENTION` to see the value in use.

## Check 2: has it taken effect?

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `backup_retention`. In version 3 it is ignored. The setting that counts is `IRONCLAD_BACKUP_RETENTION`, and its default is 559 characters.

## What the metrics show

The service exports the metric `ironclad_backup_retention_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
