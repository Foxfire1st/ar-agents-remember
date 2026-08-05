# mcp/tests/test_memory_quality.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_memory_quality.py`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-06T12:28+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_memory_quality.py` verifies the memory quality runner, the update-history
style checker, and the MCP payload path for `memory_quality_check`.

## Code Commentary

### Logic

The tests create temporary onboarding fixtures, validate clean newest-first
history, assert findings for out-of-order and missing-timestamp bullets, verify
the package runner defaults to style-only without drift context, and verify the
MCP payload can run style-only or drift-plus-style with a clean fixture. The
history-order fixer tests prove the dedicated fixer reorders timestamped bullet
blocks and skips sections with missing timestamps.

### Invariants And Boundaries

- Memory quality checks should return structured `ok`, `checks`,
  `findingCount`, and `findings` fields.
- `memory_quality_check` should include drift integrity by default when invoked
  through the MCP payload layer.
- Style-only invocation should remain available for targeted checks.
- The dedicated history-order fixer should be tested separately from the
  checker so `memory_quality_check` stays diagnostic.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The tested package runner lives in `memory_quality.check`. | `run_memory_quality_check` | mcp/src/agents_remember/memory_quality/check.py:86-113 |
| The tested payload builder lives in `mcp.tools.memory`. | `memory_quality_check_payload` | mcp/src/agents_remember/mcp/tools/memory.py:46-63 |
| The tested style checker lives in `history_order.py`. | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/update_history/history_order.py:47-56 |
| The tested style fixer lives in `history_order_fix.py`. | `fix_onboarding_root` | mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py:28-50 |

## Update History

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 8 citation findings (4 rows); scoped recheck clean.

- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-06T12:28+02:00: Corrected the memory-quality payload-builder reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-05-24T03:09+02:00: Updated after adding dedicated history-order fixer coverage while keeping `memory_quality_check` diagnostic.
- 2026-05-24T02:47+02:00: Created for memory quality checker and payload coverage.
