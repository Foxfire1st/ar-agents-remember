# mcp/tests/test_execution_graph_indexed_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_execution_graph_indexed_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Forces dense execution-graph admission through indexed operations and proves the explicit work
budget refuses an oversized population before immutable graph construction.

## Code Commentary

### Logic

The accepted dense-32 case patches the public endpoint resolver to fail if production scans through
it, then compares every exact validation-work counter. The dense-64 case records immutable binding
calls and proves the pre-admission lower bound refuses with zero snapshots or admissions.

### Conventions

- Dense fixtures use the canonical task-document graph models and production admission entrypoint.
- Assertions compare exact named counters and typed refusal status, never elapsed time.

### Invariants And Boundaries

- These are ordinary architecture regressions, not task evidence.
- Acceptance depends on exact operation accounting, not elapsed-time timing.

### Todos

None.

## Docs References

No configured external source is needed for these repository-owned regressions.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Dense admitted graphs use indexed operations with exact work counts. | `test_dense_admission_uses_indexed_operations_and_never_public_resolver_scans` | mcp/tests/test_execution_graph_indexed_admission.py:65-105 |
| An over-budget dense graph refuses before immutable admission. | `test_dense_over_budget_population_refuses_before_immutable_admission` | mcp/tests/test_execution_graph_indexed_admission.py:107-146 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the indexed-admission regression card.
  Verification remains closeout-owned.
