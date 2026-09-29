# mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `a4eba7b7b5b5ffee7277f6c19086697925a22df2` |
| lastVerifiedCommitDate | 2026-09-29T21:14:42+02:00|
| governingOverview      | `../../../../../overview.md`               |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`history_order_fix.py` is the dedicated mutating script for sorting onboarding
`## Update History` bullet blocks newest-first after the diagnostic
`memory_quality_check` reports history-order findings.

## Code Commentary

### Logic

The script scans Markdown files under an onboarding root, reuses the
`history_order.py` section and timestamp parsing helpers, groups each history
bullet with its continuation lines, and sorts only sections where every bullet
has a valid timestamp. Sections with missing or invalid timestamps are reported
as skipped so the model or developer can edit them by hand. Finding paths are
relativized to the onboarding root via the shared `rel` helper imported from
`..integrity.onboarding_drift_check.discovery` rather than a local copy.

The module exposes `fix_onboarding_root()` for tests and `python -m
agents_remember.memory_quality.style.update_history.history_order_fix
<onboarding-root>` for direct use. `--dry-run` reports which files would change
without writing them.

### Invariants And Boundaries

- The checker stays diagnostic; this module owns the mechanical rewrite.
- Missing or invalid timestamps are not guessed.
- Continuation lines stay attached to their bullet block.
- The script operates on the onboarding root passed by the caller; normal
  closeout should pass the `c-08-ar-coordination-context-resolver` skill/MCP-resolved onboarding root.

## 260928-MIK-L30 Not Applicable On A Converted Tree (MIK-R30 Rule 5)

`fix_onboarding_root` first checks whether the onboarding root's parent holds `knowledge/layout.json`. On
such a converted tree there is no Update History to sort: it returns `ok: true` with status
`not-applicable-converted`, zero files checked and nothing changed, and reads or writes nothing. The
diagnostic check was already not applicable there (MIK-R24). On an unconverted tree the fixer is unchanged.

Rule 5 retires these checks and fixers at the cutover. Deleting `memory_quality/style/update_history/` is
left to MIK-R37 (architect ruling 2026-09-29T18:49:50 (5)): deleting it now would change today's gate on
unconverted trees.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring's converted-tree paragraph. | "has no Update History: its onboarding" | mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py:10-12 |
| The early return before any file is read. | `fix_onboarding_root`; "not-applicable-converted" | mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py:33-66 |
| No stamps and no history sort on a converted tree. | `test_converted_trees_get_no_verification_stamps_and_no_history_sort` | mcp/tests/test_onboarding_trace_gate.py:607-620 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The diagnostic checker provides the timestamp and section parsing helpers. | `CHECK_NAME` | mcp/src/agents_remember/memory_quality/style/update_history/history_order.py:25-25 |
| The `rel` path-relativization helper is now imported from the drift-check discovery module instead of defined locally. | `rel` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py:63-69 |

## Update History

- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): **body updated for MIK-R30.** Added the section "260928-MIK-L30 Not Applicable On A Converted Tree (MIK-R30 Rule 5)": the `not-applicable-converted` early return, with architect ruling 2026-09-29T18:49:50 (5) leaving the deletion of this package to MIK-R37. No verification stamp was advanced.
- 2026-08-03T02:54:51+02:00 — W3-B05 curator: anchored 2 Tier-2 table citations with exact source paths; fixer generated all ranges.
- 2026-05-31T12:50+02:00 — Removed the local `relative_path` helper; `fix_onboarding_root` now calls the shared `rel(path, onboarding_root)` imported from `agents_remember.memory_quality.integrity.onboarding_drift_check.discovery`. Noted the shared helper in Logic and added a References row (1.0.0 review remediation).
- 2026-05-24T03:09+02:00: Created for the dedicated update-history ordering fix script.
