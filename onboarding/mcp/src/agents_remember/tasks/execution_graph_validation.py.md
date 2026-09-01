# mcp/src/agents_remember/tasks/execution_graph_validation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/execution_graph_validation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tasks overview](overview.md)

## Purpose

Implements the task schema's one-pass intrinsic sprint-execution-graph admission algorithm. One
endpoint index and one resolved-edge population serve uniqueness, ownership, DAG, wave, and cycle
checks while exposing exact operation counts.

## Code Commentary

### Logic

`validate_execution_graph` builds indexed node/ref/leaf endpoint lookups, resolves every edge once,
checks duplicate nodes and resolved edges, lump/segment ownership, leaf ownership, self-edges, and
endpoint ambiguity, then derives deterministic topological waves. A cyclic graph returns the exact
cycle members. `ExecutionGraphValidationWork` counts each collection operation and accompanies both
successful `ExecutionGraphAnalysis` and typed `ExecutionGraphValidationError` refusal. The minimum
successful-work function supplies a pre-admission lower bound without traversing the population.

### Conventions

- Integer indexes retain authored declaration order for deterministic output.
- Work fields use exact operation names and counts; they never stand in for elapsed-time timing.

### Invariants And Boundaries

- Admission is linear in the indexed node/leaf/edge population; public endpoint scans are not used.
- One resolved-edge population feeds validation, waves, and cycle analysis.
- Declaration order determines deterministic wave and cycle ordering.
- This is an internal schema algorithm; public task-document models translate its refusal to their
  existing `ValueError` validation surface.

### Todos

None.

## Docs References

No external source is needed for this repository-owned graph admission algorithm.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact intrinsic work is a first-class immutable result. | "Exact collection operations in one canonical whole-graph admission." | mcp/src/agents_remember/tasks/execution_graph_validation.py:48-119 |
| Canonical admission and the cheap successful-work lower bound share one operation vocabulary. | `validate_execution_graph`; `minimum_successful_execution_graph_validation_work` | mcp/src/agents_remember/tasks/execution_graph_validation.py:191-256 |
| Indexed endpoint resolution visits each edge once. | `_resolve_graph`; `_build_endpoint_index`; `_resolve_edges` | mcp/src/agents_remember/tasks/execution_graph_validation.py:259-382 |
| Wave and cycle derivation consume the resolved adjacency without rescanning endpoints. | `_derive_waves`; `_find_cycle_members` | mcp/src/agents_remember/tasks/execution_graph_validation.py:385-516 |

## Cross-Repo References

None.

## Update History

- 2026-09-01T03:58+02:00 — Checklist follow-up: re-read the exact work-record definitions in the
  uncommitted new source and retained the claim/range; no nonexistent commit verification was
  fabricated.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: created the file card for indexed intrinsic
  execution-graph admission and exact work accounting. Verification remains closeout-owned.
