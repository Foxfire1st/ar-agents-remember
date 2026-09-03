# mcp/tests/test_task_execution_topology.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_execution_topology.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `3e276f2b2052b641afbee180a472259f21b500df` |
| lastVerifiedCommitDate | 2026-09-02T14:46:34+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force the persisted execution-nature and sprint activity-on-node graph contract through schema,
cross-document topology, task-doc graph bootstrap/authoring, deterministic rendering, observer
projection, and atomic rollback behavior, including the L04 mutation-classified publication scope:
an unchanged document batch resolves no projection scope even when an unrelated malformed task
exists.

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
After `SprintExecutionNode` equality became structural and node-to-node only, topology assertions
that mean `which master does this node address?` compare explicit `node.ref` values. This is a
mechanical consumer migration: wave derivation, validation, publication, and projection behavior
are unchanged.

L04 renamed the unrelated-malformed-task case to
`test_unchanged_documents_have_no_scope_despite_unrelated_malformed_task` and asserts an empty
scope: the classifier sees no field delta for the unchanged documents, so no projection refresh is
selected even though an unrelated malformed task is also being written in the same batch.

### Invariants And Boundaries

- Tests construct only disposable coordination roots; unpublished candidate code never writes the
  deployed coordinator.
- The suite asserts behavior through public task-document and projection boundaries instead of
  duplicating the topology algorithm.
- Graph bootstrap must update the sprint and all commanded masters together or leave every file
  unchanged.
- Node identity and master-reference identity are distinct: this suite uses `.ref` explicitly for
  master-facing comparisons and does not depend on node-to-`TaskDocumentRef` equality aliases.
- Scope selection is classifier-driven: an unchanged or evidence/audit-only document batch selects
  no projection scope.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Graph schema cases force the closed structural contract. | `ExecutionGraphSchemaTests` | mcp/tests/test_task_execution_topology.py:116-217 |
| Bootstrap and cross-document cases force exact membership, projection, and rollback. | `ExecutionTopologyTests` | mcp/tests/test_task_execution_topology.py:217-944 |
| Inventory cases force branch-backed atomic classification, empty-tree counts, and branch-enumeration refusal. | `test_inventory_enumerates_sprints_and_proposes_branch_backed_nature` | mcp/tests/test_task_execution_topology.py:229-253 |
| Cross-root publication failure restores canonical task documents and leaves no queue state or pending WAL. | `test_bootstrap_refuses_non_exact_membership_and_rolls_back_cross_root_failure` | mcp/tests/test_task_execution_topology.py:882-931 |
| The production policy under test lives in the application topology module. | `author_execution_graph` | mcp/src/agents_remember/application/task_docs/task_execution_topology.py:194-266 |
| The L11 segment-graph schema/projection/placement cases split out under the file-size rail. | `ExecutionGraphSegmentSchemaTests` | mcp/tests/test_task_execution_topology_segments.py:41-253 |
| The L11 incremental authoring forcing suite (which also owns the graph-less bootstrap forcing). | `ExecutionGraphAuthoringTests` | mcp/tests/test_author_execution_graph.py:57-982 |
| Schema-wave assertions compare explicit node references after graph construction. | `test_graph_derives_stable_waves_without_persisting_positions` | mcp/tests/test_task_execution_topology.py:116-151 |
| Bootstrap, topology, projection, and pinned-read wave assertions project `node.ref` before comparison. | `test_bootstrap_previews_then_atomically_publishes_graph_natures_render_and_projection`; `test_execution_waves_validates_and_returns_one_pinned_sprint_snapshot` | mcp/tests/test_task_execution_topology.py:721-803; mcp/tests/test_task_execution_topology.py:838-862 |
| The production node model defines structural node equality/hash and exposes the addressed document explicitly as `.ref`. | `SprintExecutionNode` | mcp/src/agents_remember/tasks/document.py:218-275 |
| Unchanged documents publish no projection scope despite an unrelated malformed task in the batch. | `test_unchanged_documents_have_no_scope_despite_unrelated_malformed_task` | mcp/tests/test_task_execution_topology.py:361-387 |

## 260815-DAG-L9 Inventory Forcing

Three new cases force `inventory_execution_topology`: the branch-backed atomic classification
(`ar/<slug>` present → atomic, absent → organizational), the zero-count empty task tree, and
the refusal when `run_git branch` enumeration fails.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_graph_derives_stable_waves_without_persisting_positions`, `test_graph_releases_a_multi_parent_successor_only_after_every_predecessor`, `test_graph_refuses_duplicates_unknown_endpoints_self_edges_blank_reasons_and_cycles`, `test_execution_fields_are_master_only_and_split_sprint_from_commanded_master`. The L2 additions prove structural/task publication serialization without a global queue/lifecycle authoring lock and keep public control/gate identity task-addressed.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current test source exercises `test_graph_derives_stable_waves_without_persisting_positions`, `test_graph_releases_a_multi_parent_successor_only_after_every_predecessor`, `test_graph_refuses_duplicates_unknown_endpoints_self_edges_blank_reasons_and_cycles`, `test_execution_fields_are_master_only_and_split_sprint_from_commanded_master`. | `test_graph_derives_stable_waves_without_persisting_positions`; `test_graph_releases_a_multi_parent_successor_only_after_every_predecessor`; `test_graph_refuses_duplicates_unknown_endpoints_self_edges_blank_reasons_and_cycles`; `test_execution_fields_are_master_only_and_split_sprint_from_commanded_master` | mcp/tests/test_task_execution_topology.py:117-124; mcp/tests/test_task_execution_topology.py:126-151; mcp/tests/test_task_execution_topology.py:153-199; mcp/tests/test_task_execution_topology.py:201-217 |

## Docs References

No configured Domain Documentation source applies to this repository-local forcing suite.

## Cross-Repo References

No meaningful cross-repository boundary is exercised.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  3e276f2b2052b641afbee180a472259f21b500df (CCR-R04@v1/L04): recorded the L04 case rename and
  expectation change — `test_unchanged_documents_have_no_scope_despite_unrelated_malformed_task`
  now asserts an empty projection scope because unchanged documents carry no classifier
  invalidation. Verification is pinned to the owning commit.

- 2026-08-24T13:43+02:00 — 260821-DAGQC-L1: reconciled master-facing wave assertions to explicit
  `node.ref` projection after structural node-only equality; this is a mechanical consumer change,
  not a topology-behavior expansion. Verification metadata remains pinned until architect-owned
  closeout stamps the real code commit.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: signature-compat update (`task_doc_tool` takes
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
