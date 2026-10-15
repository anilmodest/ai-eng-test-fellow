---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: upload chunk size (Ironclad v3)

Problems with the upload chunk size are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different upload chunk size from the one you set.
- The log shows `E1692: IRONCLAD_UPLOAD_CHUNK_SIZE out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 1 to 563 seconds. Out of range, the value is rejected with `E1692: IRONCLAD_UPLOAD_CHUNK_SIZE out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_UPLOAD_CHUNK_SIZE` to see the value in use.

## Check 2: has it taken effect?

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `upload_chunk_size`. In version 3 it is ignored. The setting that counts is `IRONCLAD_UPLOAD_CHUNK_SIZE`, and its default is 36 seconds.

## What the metrics show

Watch `ironclad_upload_chunk_size_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
