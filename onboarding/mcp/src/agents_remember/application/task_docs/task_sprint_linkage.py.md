# mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash | `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate | 2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[application/overview.md](overview.md)

## Purpose

Own the sprint↔master linkage contract (260815-DAG-L14): one atomic `attach_master` /
symmetric `detach_master` operation pair and the read-only `linkage_report` drift surface.
`attach_master` supersedes the three-write manual flow (`set_subtask` + `set_field
orchestrates` + `author_execution_graph add_node`) that produced the M16/rc7 drift, and
`task_doc.get` on a sprint carries the same linkage facts as `linkage_report` (L14-R5).
Registered as a reviewed task-document writer in `mcp/registration/tasks.py` and gated as a
task-document-writer authority in `code_quality/single_owner.py`.

## Code Commentary

### Logic

The public surface is `SPRINT_LINKAGE_OPERATIONS = ("attach_master", "detach_master",
"linkage_report")`; `sprint_linkage_operation` dispatches a `SprintLinkageCall` (tool-layer
context) to one of the three operations, and `task_doc_tools._special_task_doc_operation`
routes those operations here while wrapping `SprintLinkageError` in `TaskDocError`.

`attach_master` parses a strict `_AttachMasterPayload` (`extra="forbid"`), resolves the sprint
document through `_sprint_context` (must be a `master` with non-empty `orchestrates`), then runs
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
drops its graph node — refusing while any edge still touches the node (`_require_no_touching_edges`)
and refusing to empty the graph. It never deletes files; seat documents stay on disk as historical
records (L14-R3).

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The typed row model (`masterRef`) and first-class `SprintSeat` schema this module writes; `SprintSeat` itself is structurally unchanged in the candidate. | `SubTaskRef`; `SprintSeat`; `TaskDocument` | mcp/src/agents_remember/tasks/document.py:546-560; mcp/src/agents_remember/tasks/document.py:630-662; mcp/src/agents_remember/tasks/document.py:677-896 |
| The typed-linkage cross-check and altitude role sets this module relies on. | `validate_sprint_linkage` | mcp/src/agents_remember/tasks/document_refs.py:311-361 |
| The public tool-layer operation routing. | `task_doc_tool` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:198-301 |
| The shared judgment verifier and completion gate. | `verify_sprint_judgment_ids`; `require_commanded_masters_completed` | mcp/src/agents_remember/application/task_docs/task_execution_topology.py:433-474; mcp/src/agents_remember/application/task_docs/task_execution_topology.py:758-778 |
| The rollback-safe batch writer and exact task publication transaction. | `write_task_doc_batch`; `publish_task_doc_set` | mcp/src/agents_remember/application/task_docs/task_doc_publication.py:82-86; mcp/src/agents_remember/tasks/store.py:175-216 |
| The single-owner authority gate admitting this module as a task-document writer. | `TASK_DOCUMENT_WRITER_AUTHORITIES` | mcp/test_support/agents_remember_test_support/code_quality/single_owner.py:40-53 |
| The linkage preflight wraps the served-build check in the linkage error family (L15-R4). | `_require_serving_topology_schema` | mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py:89-95 |
| The F8 fact kinds: sprints excluded from the uncommanded-master scan; unresolved seat-doc rows named. | `collect_linkage_facts`; `_row_facts` | mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py:375-398; mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py:807-852 |

| Attach and detach validate their full candidate before preview/apply; both routes call the shared graph-title cardinality owner before publication. | `attach_master`; `detach_master` | mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py:209-274; mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py:277-347 |
| Apply uses the central title owner and the exact task-document transaction publisher; it does not select a first graph locally. | `_publish` | mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py:704-731 |
| The shared publication helper refuses more than one graph-bearing document and builds the sole qualified title context. | `require_single_graph_document`; `build_publication_batch_graph_titles` | mcp/src/agents_remember/application/task_docs/task_doc_graph_titles.py:16-33; mcp/src/agents_remember/application/task_docs/task_doc_graph_titles.py:36-48 |

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

The current source seams include `SprintLinkageError`, `SprintLinkageRequest`, and
`SprintLinkageCall`. Accepted-source validation and task publication form one task-first
transaction. A valid linkage mutation is not refused merely because a closeout queue exists:
publication writes task truth, invalidates the affected waiting projection, and rebuilds it from
current closeout-door facts. Queue state remains disposable scheduling output, not an authoring
lock or lifecycle evidence owner.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `SprintLinkageError`, `SprintLinkageRequest`, `SprintLinkageCall` at this ownership boundary. | `SprintLinkageError`; `SprintLinkageRequest`; `SprintLinkageCall` | mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py:102-103; mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py:106-115; mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py:177-186 |

## Update History

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: re-read the reopened `SprintSeat` claim,
  retained its behavior, and regenerated all three schema ranges. Verification remains
  closeout-owned.

- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 bounded local type-parameter migration in `_parse_payload` and confirmed that payload validation and sprint-linkage behavior remain as documented. Verification remains closeout-owned.

- 2026-08-26T10:44:52+02:00 — Routed the uncommanded-master census through the shared module-level `repository_master_documents` query, preserving one repository-global authority API.

- 2026-08-24T13:43+02:00 — 260821-DAGQC-L1: reconciled linkage preview/apply with the shared
  zero-or-one graph-title owner and the landed task-first publication transaction; removed the
  stale queue-governed/current-transitional narrative. Verification metadata remains pinned until
  architect-owned closeout stamps the real code commit.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.



- 2026-08-20T21:30+02:00 — 260815-DAG-L15: served-build preflight wraps both linkage write
  operations (L15-R4); attach/detach dry-runs lock with `create=False` (F2); F8 linkage-fact
  hygiene — sprints excluded from `uncommanded-master`, `seat-doc-row-unresolved` for uncorrelated
  seat rows — with tests. Verified at code commit de3a0fd9.

- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   sprint-linkage publish/preview threads joined graph titles (`_batch_graph_titles`, L12-R1/R4). Verified at code commit b7f2c8e2.

- 2026-08-20T04:10+02:00 — 260815-DAG-L14: created — one atomic `attach_master`/`detach_master`
  operation pair (typed row + `orchestrates` slug + graph lump node + nature assertion as one
  validated batch), the read-only `linkage_report`/`linkageFacts` drift surface, and the moved
  `validate_completed_master_row` for typed rows. Verified at code commit 8071a644 (L14 HEAD);
  the 23-test suite passed under the Dagger-targeted gate.
