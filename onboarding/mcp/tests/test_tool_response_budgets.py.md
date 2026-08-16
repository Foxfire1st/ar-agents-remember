# mcp/tests/test_tool_response_budgets.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_tool_response_budgets.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T09:00+02:00                     |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a`|
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The report helper under test. | `write_tool_report` | mcp/src/agents_remember/kernel/primitives/tool_reports.py:30-50 |
| The compact builders under test. | `compact_runtime_install_payload`; `compact_diagnostics_payload`; `compact_carryover_payload` | mcp/src/agents_remember/mcp/tools/core.py:105-128; mcp/src/agents_remember/mcp/tools/memory.py:162-183; mcp/src/agents_remember/mcp/tools/providers.py:55-70 |

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## Update History

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 2 citation rows covering 4 source references and preserved verification metadata.

- 2026-06-10T09:00+02:00 — Added carryover plan/apply budget cases for 2.5.2 (GitHub #52): fat 100-candidate plan, duplicate-array apply, inline cap with overflow marker, and report round-trip retention.
- 2026-06-10T05:30+02:00: Created with the S4 response token budgets (2.5.1).
