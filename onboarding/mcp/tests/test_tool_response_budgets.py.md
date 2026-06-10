# mcp/tests/test_tool_response_budgets.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_tool_response_budgets.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T09:00+02:00                     |
| lastVerifiedCommitHash | `cca911fcb6417ecf56de00c17d05aa304daa51c5`|
| lastVerifiedCommitDate | 2026-06-10T02:35:22+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

Tests the response token budgets: the `tool_reports` file/prune/redaction
helper and the compact payload builders (`runtime_install`,
`provider_diagnostics`, `provider_watchers`, and since 2.5.2 the carryover
plan/apply pair).

## Code Commentary

### Logic

Report tests verify write/read round-trip, unconditional `PASSWORD=***`
redaction in report files, keep-last-5 pruning, and the 7-day age cutoff
(via `os.utime`-backdated files). Budget tests feed deliberately fat inputs
(repeated 200-line command transcripts, compose blobs) through each compact
builder and assert the serialized inline payload stays under
`INLINE_BUDGET_CHARS` (4,000 chars ≈ 1k tokens) while the structure keeps
outcomes (`phases`, per-provider results, counts) and the `reportPath`.

The carryover cases (2.5.2, GitHub #52) feed a 100-candidate plan and a
30-candidate apply with `carried` duplicating every record: they assert the
inline payload drops `candidates`/`carried`, keeps action facts inline
(commits, intent note, per-decision path lists), caps oversized groups at 25
paths plus a `(+N more in report)` marker while smaller groups stay fully
enumerated, and that the report file retains all records round-trip.

### Invariants And Boundaries

- `INLINE_BUDGET_CHARS` is the regression line for response flooding: raising
  it needs a reason, not a convenience.
- The compact builders must stay pure (dict in → dict out) so these tests
  never need Docker or a server.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The report helper under test. | [tool_reports.py](agents-remember-md/mcp/src/agents_remember/mcp/tool_reports.py) |
| The compact builders under test. | [core.py](agents-remember-md/mcp/src/agents_remember/mcp/tools/core.py); [providers.py](agents-remember-md/mcp/src/agents_remember/mcp/tools/providers.py); [memory.py](agents-remember-md/mcp/src/agents_remember/mcp/tools/memory.py) |

## Update History

- 2026-06-10T09:00+02:00 — Added carryover plan/apply budget cases for 2.5.2 (GitHub #52): fat 100-candidate plan, duplicate-array apply, inline cap with overflow marker, and report round-trip retention.
- 2026-06-10T05:30+02:00: Created with the S4 response token budgets (2.5.1).
