# mcp/tests/test_semantic_topology_refusals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_semantic_topology_refusals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Forces the semantic-topology boundary to fail closed for incomplete, ambiguous, malformed,
split-authority, unclassified-schema, unsupported-version, and queue-adapter error cases.

## Code Commentary

### Logic

The matrix covers missing graph/index/placement and malformed facts; duplicate-node whole-graph
admission; every composite parent binding near miss; shared lifecycle/topology identity ownership;
future nested schema and version refusal; and preservation of exact typed status/detail through the
queue adapter.

### Conventions

- Refusal cases use canonical production fixtures and change one invalid fact at a time.
- Assertions preserve exact typed status and detail across task-domain and queue boundaries.

### Invariants And Boundaries

- No fallback projection or partial identity is accepted.
- Queue translation preserves domain status and detail exactly.
- These are ordinary refusal regressions, not durable task evidence.

### Todos

None.

## Docs References

No configured external source is needed for these repository-owned regressions.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Missing, ambiguous, malformed, and duplicate graph facts refuse before a fingerprint. | "Exact typed refusals for semantic-topology/v2 derivation." | mcp/tests/test_semantic_topology_refusals.py:1-1; mcp/tests/test_semantic_topology_refusals.py:99-201 |
| Composite leaf-binding near misses and split authorities are exhaustively rejected. | "Exact typed refusals for semantic-topology/v2 derivation." | mcp/tests/test_semantic_topology_refusals.py:1-1; mcp/tests/test_semantic_topology_refusals.py:203-251 |
| Schema/version and queue error translation remain typed and exact. | `test_semantic_topology_refuses_unclassified_nested_schema_and_unsupported_version`; `test_queue_adapter_preserves_exact_typed_refusal_status_and_detail` | mcp/tests/test_semantic_topology_refusals.py:253-306 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T03:58+02:00 — Checklist follow-up: re-read both new refusal cohorts against their
  exact working-tree ranges; commit verification remains closeout-owned.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the semantic-topology refusal card.
  Verification remains closeout-owned.
