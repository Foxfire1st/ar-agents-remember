# mcp/tests/test_memory_quality.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_memory_quality.py`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T02:47+02:00                     |
| lastVerifiedCommitHash | `b25d52f2b445554bb64115db2f27fd156954bcf3` |
| lastVerifiedCommitDate | 2026-05-24T02:36:33+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_memory_quality.py` verifies the memory quality runner, the update-history
style checker, and the MCP payload path for `memory_quality_check`.

## Code Commentary

### Logic

The tests create temporary onboarding fixtures, validate clean newest-first
history, assert findings for out-of-order and missing-timestamp bullets, verify
the package runner defaults to style-only without drift context, and verify the
MCP payload can run style-only or drift-plus-style with a clean fixture.

### Invariants And Boundaries

- Memory quality checks should return structured `ok`, `checks`,
  `findingCount`, and `findings` fields.
- `memory_quality_check` should include drift integrity by default when invoked
  through the MCP payload layer.
- Style-only invocation should remain available for targeted checks.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The tested package runner lives in `memory_quality.check`. | [check.py](agents-remember-md/mcp/src/agents_remember/memory_quality/check.py) |
| The tested payload builder lives in `mcp.tools`. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| The tested style checker lives in `history_order.py`. | [history_order.py](agents-remember-md/mcp/src/agents_remember/memory_quality/style/update_history/history_order.py) |

## Update History

- 2026-05-24T02:47+02:00: Created for memory quality checker and payload coverage.
