# mcp/tests/test_task_execution_topology_segments.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_execution_topology_segments.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T08:55+02:00 |
| lastVerifiedCommitHash | `f2e2f4b9c18d89cc0f5c901f43831e014701aae0` |
| lastVerifiedCommitDate | 2026-08-19T11:32:36+02:00|
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
byte-identically, lump/ref equality, segment shape rules (non-empty unique leaf ids, no leafIds on
a lump), sprint-wide leaf uniqueness, lump/segment mutual exclusion per master, segment-sampling
edge endpoints and their resolution refusals (unplaced leaf, ambiguous bare ref), duplicate
equivalent addressing, segment-spanning cycle refusal, and judgmentId/leafId blank trimming.
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Segment schema and endpoint grammar forcing. | `ExecutionGraphSegmentSchemaTests` | mcp/tests/test_task_execution_topology_segments.py:41-254 |
| Served projection lifting forcing. | `ExecutionGraphProjectionLiftTests` | mcp/tests/test_task_execution_topology_segments.py:256-278 |
| Derived placement and numbering-hint forcing. | `DerivedLeafPlacementTests` | mcp/tests/test_task_execution_topology_segments.py:280-413 |
| Cross-document segmented topology validation forcing. | `ExecutionTopologySegmentValidationTests` | mcp/tests/test_task_execution_topology_segments.py:415-505 |
| The production schema under test. | `SprintExecutionNode`; `SprintExecutionGraph` | mcp/src/agents_remember/tasks/document.py:191-402 |

## Update History

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: created as the segment-graph schema/placement forcing
  suite (split from `test_task_execution_topology.py`). Verification remains closeout-owned.
