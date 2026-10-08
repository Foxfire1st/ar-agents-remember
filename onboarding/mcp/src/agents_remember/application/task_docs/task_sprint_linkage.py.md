# mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py

## Governing Overview

[application/overview.md](overview.md)

## Purpose

Own the sprint↔master linkage contract (260815-DAG-L14): one atomic `attach_master` /
symmetric `detach_master` operation pair, the read-only `linkage_report` drift surface, and the
dispatch of `retire_master`, the explicit operation that removes a master from its sprint and archives it
(its implementation lives in `task_master_retirement.py`).
`attach_master` supersedes the three-write manual flow (`set_subtask` + `set_field
orchestrates` + `author_execution_graph add_node`) that produced the M16/rc7 drift, and
`task_doc.get` on a sprint carries the same linkage facts as `linkage_report` (L14-R5).
Registered as a reviewed task-document writer in `mcp/registration/tasks.py` and gated as a
task-document-writer authority in `code_quality/single_owner.py`.

## Code Commentary

### Logic

The public surface is `SPRINT_LINKAGE_OPERATIONS = ("attach_master", "detach_master",
"retire_master", "linkage_report")`; `sprint_linkage_operation` builds a `SprintLinkageRequest` from a
`SprintLinkageCall` (tool-layer context) and dispatches it to one of the four operations (`retire_master`
goes to `task_master_retirement.retire_master`), and `task_doc_tools._special_task_doc_operation`
routes those operations here while wrapping `SprintLinkageError` in `TaskDocError`. The shared building
blocks live beside this module: `SprintLinkageError` and the pure `_detach_candidate` in
`task_sprint_candidates.py`; `SprintLinkageRequest`, `_sprint_context`, `_validate_candidate`,
`_publication_transaction` and `_document_preview` in `task_sprint_context.py`.

`attach_master` parses a strict `_AttachMasterPayload` (`extra="forbid"`), resolves the sprint
document through `_sprint_context` (must satisfy `TaskDocument.is_sprint`, including a retired-only sprint), then runs
the whole refusal ladder before any write: cross-repo/self-attach target checks
(`_resolve_attach_target`), already-attached detection across typed rows, `orchestrates` aliases,
and graph placement (`_require_not_attached`), row-number collisions, execution-nature assertion
(`_assert_execution_nature` — a nature-less master requires `executionNature` plus a
`judgmentId` verified against the sprint's canonical Judgment Register through the shared
`verify_sprint_judgment_ids`; a mismatched existing nature refuses), and the Completed-row
terminal check (`_require_completed_master`). `_attach_candidate` builds the one candidate
document: the typed row (number/name/status/masterRef), the `orchestrates` membership slug, and —
only when the sprint has an `executionGraph` — one unique lump `SprintExecutionNode`; a graph-less
sprint reports `graphNode: "deferred-no-graph-default"` and keeps the L13 atomic-sequential
default. `_validate_candidate` then runs full topology validation on a graphed sprint or the
typed-linkage cross-check (`validate_sprint_linkage`) on a graph-less one. Preview and apply both
call `build_publication_batch_graph_titles`, the central zero-or-one graph-document cardinality
owner. `_publish` then submits the sprint (plus an optional nature-asserted master) to the exact
task-document publication transaction: accepted source bytes are rechecked, task truth is written,
the affected waiting projection is invalidated, and that disposable projection is rebuilt from
current door facts. Linkage authoring is not subordinate to pre-existing queue state.

Since 260815-DAG-L15 `attach_master`/`detach_master` begin with the served-build preflight
(`_require_serving_topology_schema` — `require_serving_topology_schema` wrapped in
`SprintLinkageError`), so no topology-schema write can land while the serving runtime cannot parse
the schema (L15-R4), and their dry-run paths lock with `create=False` so a preview never writes
the controlplane lock file (playthrough F2).

`detach_master` is symmetric: it refuses a cross-repo target, tolerates a deleted master document
(`_resolve_tolerantly`), removes the typed row plus every `orchestrates` alias for the master, and
drops its graph node — refusing while any edge still touches the node (`_require_no_touching_edges`, in
`task_sprint_candidates.py`) and refusing to empty the graph. It never deletes files; seat documents stay on
disk as historical records (L14-R3). `retire_master` dispatches to the retirement state machine: its sprint-edit owner
removes the required edges, calls `_detached_data`, installs the retirement row and validates before publication,
archival and cleanup. Ordinary `detach_master` continues to use `_detach_candidate`.

`linkage_report` / `linkage_facts_for_get` compute `collect_linkage_facts` — read-only and never
raising. Facts are exception-guarded (`sprint-scan-failed` fallback) and classify legacy and
inconsistent shapes without hard errors (L14-R7): `orchestrates-entry-unresolved`,
`seat-doc-row` (legacy rows correlated through the seat doc's references via `_correlate_seat_row`),
`row-without-membership`, `membership-without-row`, `slug-only-membership`, and
`uncommanded-master` (a master named in the sprint's decisions but never commanded — the
260812_mcp-rc7-release and 260815_ias-memory-ledger-reconciliation witnesses). Since 260815-DAG-L15
(F8) the uncommanded-master scan excludes sprints themselves (orchestrates-bearing docs — a sprint
named in another sprint's decisions is not an uncommanded master), and a seat-doc row whose master
correlation fails (seat doc absent, or present with no `../<master>/task.json` reference) reports
`seat-doc-row-unresolved` instead of a master-less `seat-doc-row`, so a paired
`membership-without-row` reads as a correlation miss, not a genuinely missing row.

`validate_completed_master_row` is the moved terminal check for a master row newly marked
`Completed`: a typed `masterRef` row completes against the linked master document's own status and
completion blockers, while any other row resolves the terminal leaf doc exactly as before.

### Conventions

- Errors are `SprintLinkageError(AgentsRememberError)` with `task-sprint-linkage-*` statuses and
  are translated to `TaskDocError` at the tool boundary.
- All validation precedes the single `write_task_doc_batch` (rollback-safe); dry-run previews the
  rendered diff + `wouldLose` for every affected pair.
- Judgment provenance is shared with graph authoring: `verify_sprint_judgment_ids` (canonical home
  in `task_execution_topology.py`) is the single verifier.

### Invariants And Boundaries

- Sprint↔master membership is same-repository only; a sprint cannot attach itself, and a master
  that itself orchestrates cannot be commanded.
- A nature-less master requires `executionNature` + `judgmentId`; disagreeing with an existing
  nature refuses (reclassify via `author_execution_graph` instead).
- Attach refuses over existing `orchestrates` membership (detach-first is the conversion path);
  detach refuses on touching edges and on emptying the graph.
- Linkage-schema writes are served-build-preflighted (L15-R4); dry-run never writes the
  integration-authority lock file (F2).
- Preview and apply share `build_publication_batch_graph_titles`; this module has no private
  first-graph selector, catch-and-split retry, or alternative title-joining path.
- This module never deletes files and never hard-fails on legacy shapes — those are facts, not
  errors (L14-R7 backward tolerance). The F8 fact kinds keep facts-not-errors semantics:
  `seat-doc-row-unresolved` and the sprint exclusion are facts, never judgment.

## Evidence

### Repo-Internal References


- The typed masterRef row, SprintSeat and TaskDocument models supply the linkage schema this module writes. [1]

- The typed-linkage cross-check and altitude role sets this module relies on. [2]
- The public tool-layer operation routing. [3]
- The shared judgment verifier and completion gate. [4]
- The rollback-safe batch writer and exact task publication transaction. [5]
- The single-owner authority gate admitting this module as a task-document writer. [6]
- The linkage preflight wraps the served-build check in the linkage error family (L15-R4). [7]

- The F8 fact kinds: sprints excluded from the uncommanded-master scan; unresolved seat-doc rows named. [8]

- The operation tuple lists the four linkage operations and the dispatcher sends `retire_master` to the retirement module. [10]
- Attach validates its full candidate before preview or apply and calls the shared graph-title cardinality owner before publication. [11]
- Detach builds its candidate from the shared pure `_detach_candidate`, validates it, and publishes through `_publish`. [12]
- Apply uses the central title owner and the exact task-document transaction publisher; it does not select a first graph locally. [13]
- The shared publication helper refuses more than one graph-bearing document and builds the sole qualified title context. [14]
- The detach candidate removes the typed row, the membership aliases and the graph node, and refuses to empty the graph or to leave an edge touching the node. [15]

## 260815-DAG-L14 Linkage Boundary

The module is the one authority for typed sprint↔master linkage: attach and detach are atomic
batches, `linkage_report`/`linkageFacts` are the read-only drift surface, and
`validate_completed_master_row` completes typed rows against the linked master document. The
consistency cross-check (`validate_sprint_linkage` in `tasks/document_refs.py`) hard-fails only
new-shape drift; legacy shapes surface as facts (L14-R5/R7).


## 260815-DAG-L12 Title Threading

Sprint linkage publication labels the sprint's Mermaid render from the linkage batch's in-memory
masters. DAGQC L1 replaces the former private `_batch_graph_titles` helper with
`build_publication_batch_graph_titles`, the application-wide zero-or-one graph-document owner.
The title map is qualified by `TaskDocumentRef`; a batch without a graph produces no title context,
and a batch with more than one graph-bearing document refuses before publication.


## 260815-DAG-L15 Preflight and Linkage-Fact Hygiene

L15 added the served-build preflight to both linkage write operations (L15-R4) and the `create=False`
dry-run locks (F2), and cleaned the linkage-fact vocabulary (F8): `collect_linkage_facts` no longer
flags an orchestrates-bearing sprint as an uncommanded master, and a seat-doc row that cannot be
correlated to a master reports `seat-doc-row-unresolved` so correlation misses read as facts, not
missing rows. Both F8 behaviors are test-pinned (the sprint-exclusion test and the updated
seat-row edge-shapes test).


## Current Contract After CLIVE

The current source seams are `SprintLinkageCall` (defined here) and `SprintLinkageError` and
`SprintLinkageRequest` (defined in `task_sprint_candidates.py` and `task_sprint_context.py`, and imported here). Accepted-source validation and task publication form one task-first
transaction. A valid linkage mutation is not refused merely because a closeout queue exists:
publication writes task truth, invalidates the affected waiting projection, and rebuilds it from
current closeout-door facts. Queue state remains disposable scheduling output, not an authoring
lock or lifecycle evidence owner.

### Reconciled Source Evidence

- The current module exposes `SprintLinkageError`, `SprintLinkageRequest`, `SprintLinkageCall` at this ownership boundary. [9]
