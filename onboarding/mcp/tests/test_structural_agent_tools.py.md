# mcp/tests/test_structural_agent_tools.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/tests/test_structural_agent_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-16T04:06+02:00 |
| lastVerifiedCommitHash |  `8bf6edad7e7e65e27cf735be0822f604531d0c8a`|
| lastVerifiedCommitDate |  2026-08-16T10:54:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Exercises the structural agent service boundary with real sprint/master/leaf task documents,
ambient hosted caller identity, qualified targets, replacement-aware routing, and exact-pinned
dispatch rollback.

## Code Commentary

### Logic

Fixtures materialize task containment and structural catalog seats. Tests cover both directions of
replacement-aware messaging, ambiguity refusal, successful dispatch brief delivery, and rollback
when the exact initial dispatch brief cannot be delivered.

### Conventions

All task references point at isolated temporary task trees; no test writes candidate schema rows to
the deployed coordination root.

### Invariants And Boundaries

- Tests never identify targets by runtime id through the public operation.
- Both replacement directions remain reachable through the same structural address.
- Ambiguity is a typed failure, never first-match success.
- A child whose initial exact-pinned brief fails is retired before the error escapes.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixtures create real task containment and structural seats. | `_write_topology` | mcp/tests/test_structural_agent_tools.py:50-132 |
| The suite exercises the structural operation boundary. | `StructuralAgentToolTests` | mcp/tests/test_structural_agent_tools.py:134-241 |

## Cross-Repo References


## L23 Final Candidate Disposition

Structural dispatch tests prove curator creation refuses stale lineage or a missing/stale route
review before process creation. Passing evidence is bound by the plane to the exact candidate and
canonical task/role seat, never to a model-supplied runtime id.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## Update History

- 2026-08-16T04:06+02:00 — Dagger fixture repair: the orphan organizational-master assertion now expects the exact missing commanding-sprint refusal emitted before atomic bootstrap authority.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
- 2026-08-14T06:40+02:00 — L23 final candidate review: structural dispatch forcing cases cover
  canonical task/role authority, current lineage, candidate-bound route review, and refusal before
  curator host creation. Verification remains closeout-owned.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for structural agent-operation regression coverage.
