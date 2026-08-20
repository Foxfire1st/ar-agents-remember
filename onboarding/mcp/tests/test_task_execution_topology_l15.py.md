# mcp/tests/test_task_execution_topology_l15.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_execution_topology_l15.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-20T21:30+02:00 |
| lastVerifiedCommitHash | `de3a0fd9204f2e64755032274fb4e741bfddf6df` |
| lastVerifiedCommitDate | 2026-08-20T21:16:45+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

L15-era graph-authoring hygiene tests, split from `test_task_execution_topology.py` (gate-repair
round 2, file-size rail): the parent file exceeded the 1200-line hard limit after the L15 gate-repair
test additions, so the 15 L15-era model/authoring tests moved here with identical names and
assertions. The module is deliberately self-contained (the scratch harness is replicated, not
subclassed) so pytest cannot re-collect the parent's tests through `dir()` and duplicate the suite.

## Code Commentary

### Logic

Two classes carry the moved tests: `ExecutionGraphSchemaL15Tests` (the graph-model L15 behaviors:
edge-judgmentId-None parse, cycle-member naming, the three cycle-search units, judgment-author-refused)
and `ExecutionTopologyL15Tests` (the authoring-path behaviors: dry-run lock F2, node-kind order F6,
missing-judgment typed refusal F5, unresolvable-segment-ref typed refusal L15-FIX-1,
enforce-preflight L15-R4, plain-create, `_edit_emits_topology_schema`, serving-preflight-refusal,
move-retargets-edge F3). It imports shared fixtures (`MASTER_A`/`MASTER_B`/`REPOSITORY`,
`_config`, `_graph`, `_judgment_row`, `_master`, `_JUDGMENT_HEADER`) from the parent
`test_task_execution_topology` module — the harness itself is replicated locally.

Key behavioral pins: `test_authoring_refuses_an_unresolvable_segment_ref_with_a_typed_error` drives
the production `task_doc_tool` `author_execution_graph` path with an `add_node` whose ref does not
exist on disk and asserts the typed `membership-invalid.*ghost` refusal (never a raw `KeyError`);
`test_cycle_refusal_names_the_cycle_members` pins the named-cycle acyclicity error; the move
retargets-edge and node-kind-order tests pin the F3/F6 refusal ordering.

### Invariants And Boundaries

- Self-contained by construction: replicating the scratch harness (rather than subclassing the
  parent's TestCase) is what prevents pytest re-collection duplication — the split must never be
  "fixed" by subclassing.
- The tests are behavioral: they drive the production `task_doc_tool` / application paths, not
  re-implementations.
- 416 lines at the split; both parent (939) and this module stay under the 1200-line hard limit.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The moved graph-model L15 tests. | `ExecutionGraphSchemaL15Tests` | mcp/tests/test_task_execution_topology_l15.py:60-210 |
| The moved authoring-path L15 tests. | `ExecutionTopologyL15Tests` | mcp/tests/test_task_execution_topology_l15.py:118-416 |
| The typed unresolvable-ref refusal under test (L15-FIX-1). | `test_authoring_refuses_an_unresolvable_segment_ref_with_a_typed_error` | mcp/tests/test_task_execution_topology_l15.py:268-291 |
| The parent suite this module was split from (kept under the file-size limit). | `ExecutionTopologyTests` | mcp/tests/test_task_execution_topology.py:213-939 |

## Cross-Repo References

No cross-repo boundary applies to this forcing suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-20T21:30+02:00 — Created for 260815-DAG-L15 (gate-repair round 2): the L15-era
  graph-authoring hygiene tests split from `test_task_execution_topology.py` (file-size rail),
  self-contained harness replicated to prevent pytest re-collection duplication. Verified at code
  commit de3a0fd9.
