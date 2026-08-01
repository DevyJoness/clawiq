# ClawIQ Bug Tracker

This document contains all known issues discovered during development.

---

# BUG-001

Status: ✅ Fixed

Title:

Gateway startup script failed.

Description:

Gateway did not start correctly after installation.

Resolution:

Gateway service configuration was corrected.

---

# BUG-002

Status: ✅ Fixed

Title:

Telegram Gateway communication.

Description:

Telegram messages were not delivered correctly.

Resolution:

Gateway configuration updated.

---

# BUG-003

Status: 🔄 Investigating

Title:

Windows Companion authentication

Description:

The Companion application detects the local Gateway but fails with:

"No credential available"

Current status:

Gateway works correctly.

Problem appears to be related to authentication.

---

# BUG-004

Status: 🔴 Open

Title:

Vision model crashes on AMD GPU

Description:

Qwen2.5VL crashes during image processing.

Error:

ROCm error:
device kernel image is invalid

Current status:

Image pipeline works.

OpenClaw works.

Ollama launches.

Crash occurs inside llama-server.

---

# BUG-005

Status: 🔴 Open

Title:

Gemini OAuth authentication

Description:

Gemini CLI authentication completes in browser.

CLI returns:

"This client is no longer supported..."

Current status:

Likely caused by migration to Google's new authentication flow.

---

## BUG-006

### Title

Gateway launcher fails on Windows with non-ASCII usernames.

### Status

Workaround implemented.

### Symptoms

- Windows Script Host error
- gateway.vbs cannot locate gateway.cmd
- automatic startup fails

### Cause

OpenClaw generates launcher scripts using absolute paths that become corrupted when the Windows username contains non-ASCII characters.

### Workaround

Run:

scripts/repair-gateway.ps1

### Upstream

Should be reported to OpenClaw.

# Bug Status Legend

✅ Fixed

🔄 Investigating

🔴 Open

🟡 Monitoring


## BUG-006 Gemini API
429 RESOURCE_EXHAUSTED while using Gemini API key.

## BUG-007 OpenAI OAuth
Codex/OpenAI usage limit reached during fallback tests.
