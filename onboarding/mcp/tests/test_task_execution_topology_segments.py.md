# mcp/tests/test_task_execution_topology_segments.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_execution_topology_segments.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks segment uniqueness, mutual exclusion of whole-master and segment nodes, endpoint addressing by a leaf sample and cycle refusal. It also checks derived placement of unassigned leaves, orchestrates membership and wave projection, and refusal of segments on atomic masters with the offending node identified.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Leaf ids are unique sprint wide | `test_leaf_ids_are_unique_sprint_wide` | mcp/tests/test_task_execution_topology_segments.py:40-49 |
| Lump and segment appearances of one master are mutually exclusive | `test_lump_and_segment_appearances_of_one_master_are_mutually_exclusive` | mcp/tests/test_task_execution_topology_segments.py:51-55 |
| Edge endpoints address segments by leaf sample | `test_edge_endpoints_address_segments_by_leaf_sample` | mcp/tests/test_task_execution_topology_segments.py:57-85 |
| Cycle through segments is refused | `test_cycle_through_segments_is_refused` | mcp/tests/test_task_execution_topology_segments.py:87-105 |
| Unplaced leaf derives to the latest unblocked segment | `test_unplaced_leaf_derives_to_the_latest_unblocked_segment` | mcp/tests/test_task_execution_topology_segments.py:128-149 |
| Segmented membership matches orchestrates and waves run over nodes | `test_segmented_membership_matches_orchestrates_and_waves_run_over_nodes` | mcp/tests/test_task_execution_topology_segments.py:205-213 |
| Segment on atomic master is refused citing the node | `test_segment_on_atomic_master_is_refused_citing_the_node` | mcp/tests/test_task_execution_topology_segments.py:215-221 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-26T10:44:52+02:00 — Preserved explicit empty leaf fixtures and rebuilt topology after task mutation so placement assertions cannot reuse stale resolved documents.

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
