# mcp/tests/test_task_execution_topology.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_execution_topology.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force the persisted execution-nature and sprint activity-on-node graph contract through schema,
cross-document topology, task-doc graph bootstrap/authoring, deterministic rendering, observer
projection, and atomic rollback behavior.

## Code Commentary

### Logic

The schema cases reject duplicate nodes and edges, unknown endpoints, self edges, blank reasons,
cycles, and invalid master/sprint field placement. The topology cases build minimal synthetic task
roots, prove legacy state remains migration-required (the refusal names the
`author_execution_graph` bootstrap), reject unknown, duplicate, and drifted command
membership, exercise preview and apply, and inject a mid-batch write failure to prove rollback. The
suite also forces multi-parent DAG release, malformed bootstrap envelopes, missing and wrong-kind
bootstrap targets, unresolved masters, non-sprint use, and override identity confinement. A
poisoned second-read regression proves wave derivation validates and returns one pinned sprint
snapshot, and the out-of-root case asserts the actual `task.json` and `task.md` publication targets.
The rollback proof compares every canonical JSON/Markdown task publication, permits the persistent
coordination lock, and separately proves that neither queue state nor a pending WAL was published.
The suite also directly imports the extracted queue-scope owner so targeted gate derivation keeps
the new application module attached to this existing behavioral topology suite.

### Invariants And Boundaries

- Tests construct only disposable coordination roots; unpublished candidate code never writes the
  deployed coordinator.
- The suite asserts behavior through public task-document and projection boundaries instead of
  duplicating the topology algorithm.
- Graph bootstrap must update the sprint and all commanded masters together or leave every file
  unchanged.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Graph schema cases force the closed structural contract. | `ExecutionGraphSchemaTests` | mcp/tests/test_task_execution_topology.py:119-214 |
| Bootstrap and cross-document cases force exact membership, projection, and rollback. | `ExecutionTopologyTests` | mcp/tests/test_task_execution_topology.py:217-944 |
| Inventory cases force branch-backed atomic classification, empty-tree counts, and branch-enumeration refusal. | `test_inventory_enumerates_sprints_and_proposes_branch_backed_nature` | mcp/tests/test_task_execution_topology.py:229-253 |
| Cross-root publication failure restores canonical task documents and leaves no queue state or pending WAL. | `test_bootstrap_refuses_non_exact_membership_and_rolls_back_cross_root_failure` | mcp/tests/test_task_execution_topology.py:793-842 |
| The production policy under test lives in the application topology module. | `author_execution_graph` | mcp/src/agents_remember/application/task_docs/task_execution_topology.py:194-266 |
| The L11 segment-graph schema/projection/placement cases split out under the file-size rail. | `ExecutionGraphSegmentSchemaTests` | mcp/tests/test_task_execution_topology_segments.py:41-253 |
| The L11 incremental authoring forcing suite (which also owns the graph-less bootstrap forcing). | `ExecutionGraphAuthoringTests` | mcp/tests/test_author_execution_graph.py:57-982 |

## 260815-DAG-L9 Inventory Forcing

Three new cases force `inventory_execution_topology`: the branch-backed atomic classification
(`ar/<slug>` present → atomic, absent → organizational), the zero-count empty task tree, and
the refusal when `run_git branch` enumeration fails.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_graph_derives_stable_waves_without_persisting_positions`, `test_graph_releases_a_multi_parent_successor_only_after_every_predecessor`, `test_graph_refuses_duplicates_unknown_endpoints_self_edges_blank_reasons_and_cycles`, `test_execution_fields_are_master_only_and_split_sprint_from_commanded_master`. The L2 additions prove structural/task publication serialization without a global queue/lifecycle authoring lock and keep public control/gate identity task-addressed.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_graph_derives_stable_waves_without_persisting_positions`, `test_graph_releases_a_multi_parent_successor_only_after_every_predecessor`, `test_graph_refuses_duplicates_unknown_endpoints_self_edges_blank_reasons_and_cycles`, `test_execution_fields_are_master_only_and_split_sprint_from_commanded_master`. | L120-L124; L126-L148; L150-L196; L198-L214 | `mcp/tests/test_task_execution_topology.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: signature-compat update (task_doc_tool takes
  `call: TaskDocCall`); suite purpose unchanged. Verified at code commit a9d50e08.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the finite migration operation is removed; the former
  migration cases are now graph-bootstrap forcing through `author_execution_graph`
  (`test_bootstrap_*`), including the cross-root rollback proof. Verification remains
  closeout-owned.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: the L11 segment/authoring cases moved out to
  `test_task_execution_topology_segments.py` and `test_author_execution_graph.py` under the
  file-size rail (fixtures and helpers are imported from this suite); this file keeps the schema,
  migration, inventory, and rollback forcing classes. Verification remains closeout-owned.
- 2026-08-18T12:00:00+00:00 — 260815-DAG-L9: added three `inventory_execution_topology` forcing cases
  (branch-backed atomic, empty tree, branch-enumeration refusal); verification remains
  closeout-owned.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: topology downgrade explicitly clears the sprint integration branch together with orchestration and graph facts.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: directly forces queue-scope and
  completion-topology error translation plus task-document publisher refusal without bypassing
  the canonical topology owners.
- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  topology, queue-scope ownership, rollback, and persistent-lock assertions are identical.
- 2026-08-15T13:08+02:00 — No content impact: accepted Ruff's module/name ordering for the direct
  queue-scope and task-publication imports; ownership and rollback assertions are unchanged.
- 2026-08-15T11:39+02:00 — No content impact: rewrote the direct queue-scope module import to
  Ruff's package-import form; the imported module identity and ownership assertion are unchanged.
- 2026-08-15T11:25+02:00 — L3 static-gate repair: directly bound the extracted queue-scope owner
  to the topology suite; all existing behavioral assertions remain in place.
- 2026-08-15T11:07+02:00 — L3 content update: rollback assertions now distinguish canonical task
  document publication from the persistent coordination lock and separately prove no queue state
  or pending WAL survives a failed graph migration.
- 2026-08-15T03:20:17+02:00 — 260815-DAG-L1 independent-review repair: corrected the
  out-of-repository no-write assertion to the real task-doc filenames and added a poisoned
  second-read regression that distinguishes snapshot-safe wave derivation from the former
  validate-one/read-another sequence.
- 2026-08-15T03:10:06+02:00 — 260815-DAG-L1 targeted-Dagger repair: added production-bound
  refusal cells for every branch reported uncovered by the first targeted artifact and a diamond
  graph that releases its successor only after both predecessors complete. These tests preserve
  the closed contract rather than adding coverage exclusions.
- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: expanded forcing proof through
  production task-doc create/replace/set-field paths, alias drift/collision refusals, structured
  preview classifications, same-path master/sprint kind-downgrade refusals, exact
  render/projection cells, and normalized out-of-root refusal.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: created as the forcing suite for the new persisted
  topology and finite migration boundary. Verification remains closeout-owned.
