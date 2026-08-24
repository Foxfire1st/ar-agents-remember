# mcp/tests/test_task_execution_topology_segments.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_execution_topology_segments.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T13:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force the 260815-DAG-L11 leaf-segment graph contract: segment schema rules, endpoint grammar,
projection lifting, and pure derived-placement/numbering facts. Split from
`test_task_execution_topology.py` under the file-size rail; fixtures and shared helpers are
imported from it.

## Code Commentary

### Logic

`ExecutionGraphSegmentSchemaTests` proves legacy bare-ref nodes parse as lumps and re-serialize
byte-identically, constructor lifting without cross-type equality, segment shape rules (non-empty
unique leaf ids, no leafIds on a lump), sprint-wide leaf uniqueness, lump/segment mutual exclusion per master, segment-sampling
edge endpoints and their resolution refusals (unplaced leaf, ambiguous bare ref), duplicate
equivalent addressing, segment-spanning cycle refusal, and judgmentId/leafId blank trimming.
Its equality regression proves nodes compare and hash structurally only against nodes: both
comparison directions with `TaskDocumentRef` are false, mixed set/dict insertion is order-stable,
equal lumps deduplicate, and different segment membership remains distinct.
`ExecutionGraphProjectionLiftTests` proves the served projection models accept bare refs and dicts
and lift them uniformly. `DerivedLeafPlacementTests` proves unplaced leafs derive into the latest
unblocked segment (latest by wave, then declaration order), the all-blocked flagged fallback, no
placement for lump masters, unknown-leaf facts, and numbering inversions reported as hints that
never refuse. `ExecutionTopologySegmentValidationTests` proves cross-document validation over
segmented graphs: membership against `master_refs()`, node-derived waves, the segment-on-atomic
typed refusal, and live-plan leaf-placement reporting.

### Invariants And Boundaries

- Tests construct only disposable coordination roots; unpublished candidate code never writes the
  deployed coordinator.
- The suite asserts the persisted schema and topology behavior through public models instead of
  duplicating the validation internals.
- Legacy bare-ref JSON roundtrip is a wire-format contract, not permission for runtime
  node-to-reference equality; callers must use the explicit `.ref` field.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Segment schema, endpoint grammar, explicit-ref lifting, and structural equality/hash forcing. | `ExecutionGraphSegmentSchemaTests` | mcp/tests/test_task_execution_topology_segments.py:41-281 |
| Served projection lifting forcing. | `ExecutionGraphProjectionLiftTests` | mcp/tests/test_task_execution_topology_segments.py:256-278 |
| Derived placement and numbering-hint forcing. | `DerivedLeafPlacementTests` | mcp/tests/test_task_execution_topology_segments.py:280-413 |
| Cross-document segmented topology validation forcing. | `ExecutionTopologySegmentValidationTests` | mcp/tests/test_task_execution_topology_segments.py:415-503 |
| The production schema under test. | `SprintExecutionNode`; `SprintExecutionGraph` | mcp/src/agents_remember/tasks/document.py:191-402 |
| The focused equality regression covers both operand directions plus mixed set/dict behavior. | `test_nodes_compare_structurally_without_cross_type_aliases` | mcp/tests/test_task_execution_topology_segments.py:237-265 |

## Update History

- 2026-08-24T13:43+02:00 — 260821-DAGQC-L1: replaced the stale lump/ref-equality narrative with
  structural node-only equality/hash, explicit `.ref` ownership, and the bidirectional set/dict
  regression. The legacy bare-ref wire roundtrip remains independent. Verification metadata
  remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-19T08:55+02:00 — 260815-DAG-L11: created as the segment-graph schema/placement forcing
  suite (split from `test_task_execution_topology.py`). Verification remains closeout-owned.
