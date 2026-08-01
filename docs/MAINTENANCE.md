# ClawIQ Maintenance

This document describes maintenance procedures for ClawIQ.

---

# Gateway Repair

## Problem

OpenClaw may generate invalid launcher scripts on Windows systems that use non-ASCII usernames (for example Cyrillic usernames).

Symptoms:

- Windows Script Host error
- Gateway does not start automatically
- "Cannot find the specified file"

## Repair

Run:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/repair-gateway.ps1
```

The repair script restores:

- gateway.cmd
- gateway.vbs

and tests the scheduled task.

---

## Status

Workaround implemented.

Waiting for an upstream fix in OpenClaw.
