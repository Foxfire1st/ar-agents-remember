# mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../../../../../overview.md`               |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The diagnostic checker provides the timestamp and section parsing helpers. | `CHECK_NAME` | mcp/src/agents_remember/memory_quality/style/update_history/history_order.py:25-25 |
| The `rel` path-relativization helper is now imported from the drift-check discovery module instead of defined locally. | `rel` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py:58-64 |
| Tests cover successful reordering and skipped missing-timestamp sections. | `test_history_order_fix_reorders_update_history_entries`, `test_history_order_fix_skips_missing_timestamp` | mcp/tests/test_memory_quality.py:141-165; mcp/tests/test_memory_quality.py:167-190 |

## Update History

- 2026-08-03T02:54:51+02:00 — W3-B05 curator: anchored 2 Tier-2 table citations with exact source paths; fixer generated all ranges.
- 2026-05-31T12:50+02:00 — Removed the local `relative_path` helper; `fix_onboarding_root` now calls the shared `rel(path, onboarding_root)` imported from `agents_remember.memory_quality.integrity.onboarding_drift_check.discovery`. Noted the shared helper in Logic and added a References row (1.0.0 review remediation).
- 2026-05-24T03:09+02:00: Created for the dedicated update-history ordering fix script.
