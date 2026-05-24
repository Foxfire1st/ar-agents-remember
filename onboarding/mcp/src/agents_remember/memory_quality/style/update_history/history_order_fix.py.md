# mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T03:09+02:00                     |
| lastVerifiedCommitHash | `0360e6fd7ab582075f11a2a6a50dfc0566f273e9` |
| lastVerifiedCommitDate | 2026-05-24T03:09:23+02:00|
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
as skipped so the model or developer can edit them by hand.

The module exposes `fix_onboarding_root()` for tests and `python -m
agents_remember.memory_quality.style.update_history.history_order_fix
<onboarding-root>` for direct use. `--dry-run` reports which files would change
without writing them.

### Invariants And Boundaries

- The checker stays diagnostic; this module owns the mechanical rewrite.
- Missing or invalid timestamps are not guessed.
- Continuation lines stay attached to their bullet block.
- The script operates on the onboarding root passed by the caller; normal
  closeout should pass the C-08/MCP-resolved onboarding root.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The diagnostic checker provides the timestamp and section parsing helpers. | [history_order.py](agents-remember-md/mcp/src/agents_remember/memory_quality/style/update_history/history_order.py) |
| Tests cover successful reordering and skipped missing-timestamp sections. | [test_memory_quality.py](agents-remember-md/mcp/tests/test_memory_quality.py) |

## Update History

- 2026-05-24T03:09+02:00: Created for the dedicated update-history ordering fix script.
