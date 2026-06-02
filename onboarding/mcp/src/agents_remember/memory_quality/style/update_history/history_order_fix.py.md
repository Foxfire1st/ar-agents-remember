# mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
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

| Finding | Source Path |
| --- | --- |
| The diagnostic checker provides the timestamp and section parsing helpers. | [history_order.py](agents-remember-md/mcp/src/agents_remember/memory_quality/style/update_history/history_order.py) |
| The `rel` path-relativization helper is now imported from the drift-check discovery module instead of defined locally. | [discovery.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py) |
| Tests cover successful reordering and skipped missing-timestamp sections. | [test_memory_quality.py](agents-remember-md/mcp/tests/test_memory_quality.py) |

## Update History

- 2026-05-31T12:50+02:00 — Removed the local `relative_path` helper; `fix_onboarding_root` now calls the shared `rel(path, onboarding_root)` imported from `agents_remember.memory_quality.integrity.onboarding_drift_check.discovery`. Noted the shared helper in Logic and added a References row (1.0.0 review remediation).
- 2026-05-24T03:09+02:00: Created for the dedicated update-history ordering fix script.
