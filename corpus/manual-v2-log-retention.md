---
product: Ironclad Endpoint Manager
version: v2
section: Operations
---

# Log retention (Ironclad v2)

Ironclad keeps run logs on the runner's own disk.

## How long logs are kept

`log_retention_days` in `ironclad.conf` sets the number of days. The default is **14 days**. Logs older than that are deleted by a sweep that runs at startup and then once a day.

```
[runner]
log_retention_days = 14
```

## Where logs are written

`/var/log/ironclad/<run-id>.log`, one file per run, plain text.

## Limits

The highest accepted value is 90. Logs are not copied anywhere else; if the disk is lost, the logs are lost with it.
