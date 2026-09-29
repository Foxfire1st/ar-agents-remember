# mcp/src/agents_remember/memory_quality/style/update_history/history_order.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/style/update_history/history_order.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f` |
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview      | `../../../../../overview.md`               |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The memory quality runner entry is `run_memory_quality_check` (which, since MIK-R24, reports this check `not-applicable-converted` on a converted tree), and this checker exposes its registered style name. | "style.update_history.history_order"; `run_memory_quality_check` | mcp/src/agents_remember/memory_quality/check.py:124-160; mcp/src/agents_remember/memory_quality/style/update_history/history_order.py:25-25 |
| The checker imports the `rel` path-relativization helper from the drift-check discovery module. | "from agents_remember.memory_quality.integrity.onboarding_drift_check.discovery import rel" | mcp/src/agents_remember/memory_quality/style/update_history/history_order.py:21-21 |
| The drift-check discovery module defines the `rel` path-relativization helper. | `rel` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py:63-69 |
| The history-order checker entry is `check_onboarding_root`. | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/update_history/history_order.py:47-56 |

## Update History
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): **Reopened claim re-read (MIK-R24).** `run_memory_quality_check` changed: it dispatches by memory format. The row still holds, and was reworded to say that on a converted tree this check reports `not-applicable-converted`. This folds in the fixer projection of this pass. No claim about this card's own source changed.

- 2026-08-04T15:56:39+02:00 — 260731-EFA-L6 S18-B10 curator: closed same-reviewer residual D20 by binding the shared `rel` claim to the complete helper body; rechecked this card through the locked exact-document fixer/check.

- 2026-05-31T12:50+02:00 — Removed the local `relative_path` helper; `order_findings` now calls the shared `rel(path, onboarding_root)` imported from `agents_remember.memory_quality.integrity.onboarding_drift_check.discovery`. Noted the shared helper in Logic and References (1.0.0 review remediation).
- 2026-05-24T02:47+02:00: Created for the update-history ordering style check.
