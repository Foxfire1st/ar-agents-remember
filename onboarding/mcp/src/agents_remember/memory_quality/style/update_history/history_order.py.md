# mcp/src/agents_remember/memory_quality/style/update_history/history_order.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory_quality/style/update_history/history_order.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `../../../../../overview.md`               |

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

| Finding | Source Path |
| --- | --- |
| The memory quality runner registers this checker as `style.update_history.history_order`. | [check.py](agents-remember-md/mcp/src/agents_remember/memory_quality/check.py) |
| The `rel` path-relativization helper is now imported from the drift-check discovery module instead of defined locally. | [discovery.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py) |
| Regression tests cover newest-first, out-of-order, and missing timestamp cases. | [test_memory_quality.py](agents-remember-md/mcp/tests/test_memory_quality.py) |

## Update History

- 2026-05-31T12:50+02:00 — Removed the local `relative_path` helper; `order_findings` now calls the shared `rel(path, onboarding_root)` imported from `agents_remember.memory_quality.integrity.onboarding_drift_check.discovery`. Noted the shared helper in Logic and References (1.0.0 review remediation).
- 2026-05-24T02:47+02:00: Created for the update-history ordering style check.
