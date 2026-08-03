# BUGS

_Last updated: 2026-08-03_

# Purpose

Track confirmed reproducible issues affecting ClawIQ.

Only verified bugs should be added.

---

# Open

## BUG-001

Title:
Vision model instability

Status:
Open

Priority:
High

Description:
Vision pipeline is not yet considered production-ready and requires additional validation before being enabled by default.

Workaround:
Disable vision routing for unsupported configurations.

Related Epic:
KAN-11

---

## BUG-002

Title:
Router fallback validation

Status:
Open

Priority:
High

Description:
Router fallback scenarios require broader automated testing to ensure consistent provider selection.

Related Epic:
KAN-7

---

## BUG-003

Title:
Memory persistence

Status:
Planned Investigation

Priority:
Medium

Description:
Long-term memory implementation is still under active development and requires validation after persistence layer is completed.

Related Epic:
KAN-10

---

# Closed

Use CHANGELOG.md to reference resolved issues.

---

# Reporting Rules

Every bug should contain:

- ID
- Title
- Description
- Reproduction steps
- Expected behaviour
- Actual behaviour
- Severity
- Status
- Related Jira issue

---

# Status Values

- Open
- In Progress
- Fixed
- Verified
- Closed

---

# Related Documents

- CHANGELOG.md
- PROJECT_CONTEXT.md
- ARCHITECTURE.md
