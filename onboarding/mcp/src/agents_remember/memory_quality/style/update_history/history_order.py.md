# mcp/src/agents_remember/memory_quality/style/update_history/history_order.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`history_order.py` validates that onboarding `## Update History` sections use
timestamped bullets ordered newest-first.

## Code Commentary

### Logic

The checker scans Markdown files under an onboarding root, locates level-two
`Update History` sections, parses bullet timestamps, and emits structured
warnings for missing timestamps, invalid timestamps, and entries inserted below
older entries. Timezone-aware values are normalized before comparison. Finding
paths are relativized to the onboarding root via the shared `rel` helper
imported from `..integrity.onboarding_drift_check.discovery` rather than a
local copy.

### Invariants And Boundaries

- This checker reports style findings only; it does not rewrite onboarding.
- Continuation lines are ignored for ordering and belong to the preceding
  bullet by convention.
- The checker intentionally runs during closeout quality control, not at task
  start.

## Evidence

### Repo-Internal References

- The memory quality runner entry is `run_memory_quality_check` (which, since MIK-R24, reports this check `not-applicable-converted` on a converted tree), and this checker exposes its registered style name. [1]
- The checker imports the `rel` path-relativization helper from the drift-check discovery module. [2]
- The drift-check discovery module defines the `rel` path-relativization helper. [3]
- The history-order checker entry is `check_onboarding_root`. [4]
