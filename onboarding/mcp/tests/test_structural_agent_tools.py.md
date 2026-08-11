# mcp/tests/test_structural_agent_tools.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/tests/test_structural_agent_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T06:47+02:00 |
| lastVerifiedCommitHash |  `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|
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


## Update History

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for structural agent-operation regression coverage.
