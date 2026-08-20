# docs/reference/execution-topology-migration.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `docs/reference/execution-topology-migration.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash | `b523f53b193e9783e7c7e6410c772e7d64d8df17` |
| lastVerifiedCommitDate | 2026-08-19T21:54:50+02:00|
| governingOverview | `docs/reference/overview.md` |

## Governing Overview

[docs/reference/overview.md](overview.md)

## Purpose

Operator-facing guide for the explicit execution topology (`executionNature` on commanded masters,
`executionGraph` on orchestration sprints). Since 260815-DAG-L13 the guide is an *authoring*
procedure, not a cutover: a sprint without an `executionGraph` runs the atomic-sequential default
(every commanded master fully integrates before the next starts, regardless of declared nature),
authoring a graph is the explicit opt-in to dependency-aware scheduling, and no separate migration
operation remains.

## Code Commentary

### Logic

The guide documents: (1) a read-only inventory that proposes the explicit nature
(atomic when an `ar/<slug>` branch already backs the master, organizational otherwise) with
parallel edges pending a ruling; (2) graph authoring through `task_doc.author_execution_graph` —
one validated mutation batch per call whose first `add_node` batch on a graph-less sprint
bootstraps the graph (`bootstrapped: true`), with judgment-bearing mutations requiring a canonical
Judgment Register row and final validation requiring exact `orchestrates` membership plus explicit
natures; (3) the defaults and fail-closed seams — no graph selects the atomic-sequential default
(the queue's read path reports the degraded projection), a nature-less commanded master under an
authored graph stays a hard refusal naming `set_nature`, and malformed canonical registers degrade
reads to facts while the write path validates register shape; and (4) snapshot-based rollback that
restores the pre-authoring tree rather than re-enabling a compatibility path.

### Invariants And Boundaries

- The inventory never infers edges from file order, names, or status.
- A branch recorded atomic is only reclassified by an accepted strategist/orchestrator ruling.
- Rollback restores the snapshot; it does not retain a dual-reader or feature-switch fallback.
- A missing graph is a scheduling default, not an error; a missing nature under an authored graph
  remains a hard refusal.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The read-only inventory the guide documents. | `inventory_execution_topology` | mcp/src/agents_remember/application/task_execution_topology.py:917-979 |
| The graph-authoring batch (and graph-less bootstrap) the guide documents. | `author_execution_graph` | mcp/src/agents_remember/application/task_execution_topology.py:182-247 |
| Fail-closed validation of a sprint's commanded membership and natures. | `validate_execution_topology` | mcp/src/agents_remember/tasks/document_refs.py:233-289 |

## Update History

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the guide was retitled from migration to authoring —
  `migrate_execution_topology` is gone, the atomic-sequential default covers graph-less sprints,
  and `author_execution_graph` bootstraps the first graph; reworked the procedure, seams, and
  release-notes sections accordingly. Verification remains closeout-owned.

- 2026-08-18T12:00:00+00:00 — 260815-DAG-L9: created as the operator migration/rollback reference for the
  explicit execution-topology cutover. Verification remains closeout-owned.
