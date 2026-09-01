# mcp/tests/test_closeout_projection_source_facts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_projection_source_facts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Pins the explicit closeout task-source planes and structurally forbids a return to whole-document
projection hashing or the retired v1 topology identity.

## Code Commentary

### Logic

The first test changes completion and unrelated normative content independently to prove the task
source fact includes only address and completion-readiness. The second inspects current production
sources to reject whole-document dumping, the old private task table, and the v1 schema string.

### Conventions

- Tests use production task-document owners and inspect the current production route directly.
- Assertions name exact source planes and forbidden legacy constructs.

### Invariants And Boundaries

- These are ordinary regression tests, not durable acceptance evidence.
- The structural prohibition complements behavioral source-fact assertions.

### Todos

None.

## Docs References

No configured external source is needed for these repository-owned regressions.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Completion-readiness is isolated from unrelated task content. | `test_task_source_fact_uses_only_address_and_completion_readiness` | mcp/tests/test_closeout_projection_source_facts.py:14-40 |
| Current source contains neither whole-document projection hashing nor v1 reintroduction. | `test_source_routes_forbid_whole_document_private_table_and_v1_reintroduction` | mcp/tests/test_closeout_projection_source_facts.py:42-54 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the source-plane regression card.
  Verification remains closeout-owned.
