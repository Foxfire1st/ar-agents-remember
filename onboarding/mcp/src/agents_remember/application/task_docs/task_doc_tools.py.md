# mcp/src/agents_remember/application/task_docs/task_doc_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/task_docs/task_doc_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash | `47c8d102c2430d5337dbe207d4601efb4844fec0` |
| lastVerifiedCommitDate | 2026-09-01T08:53:56+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[application/overview.md](overview.md)

## Purpose

The operation-dispatched application entry point behind the `task_doc` MCP tool: it loads or
creates the `ar-task-document/v1` JSON for a task, applies one edit, and rewrites both
the JSON (source of truth) and the rendered markdown. `task_reopen_tool` — the task-domain reset
that reopens a fully landed leaf under its exact leaf id (delegating to `worktrees/reopen.py`) —
moved to the sibling `application/task_reopen.py` module in 260815-DAG-L11 and is re-exported
here unchanged (facade); its response keeps the worktree-command contract shape because the
payload carries the enclosure state. Since 260815-DAG-L14 the dispatcher also routes the
sprint linkage operations (`attach_master`/`detach_master`/`linkage_report`) to
`application/task_sprint_linkage.py` through `SPRINT_LINKAGE_OPERATIONS`, wraps
`SprintLinkageError` in `TaskDocError`, and a sprint `get` carries its `linkageFacts`; the
Completed-row terminal check now delegates to `task_sprint_linkage.validate_completed_master_row`
(typed rows complete against the linked master document).

## Code Commentary

### Logic

`task_doc_tool(config, target: TaskDocTarget, *, operation, edit: TaskDocEdit = NO_EDIT,
call: TaskDocCall = DEFAULT_TASK_DOC_CALL)` — since 260731-EFA-L2 the arguments arrive as two
objects that answer two different
questions. `TaskDocTarget(repo_id, task_name, contract_path, slug)` is **which document**;
`TaskDocEdit(fields, step, decision, subtask, section)` is **what the edit is**, with `NO_EDIT` the
shared empty value a `get` passes. Internally the operation table dispatches through one private
`_Edit` view and a per-operation `_apply_set_status` / `_apply_set_field` / `_apply_set_step` /
`_apply_set_subtask` / `_apply_set_section` / `_apply_append_decision` function behind `_apply`,
replacing the former single branching applier.

It validates `operation` against `VALID_OPERATIONS`
(`create`/`replace`/`set_status`/`set_step`/`skip_step`/`set_subtask`/`remove_subtask`/`set_section`/
`append_decision`/`record_route_review`/`author_execution_graph`/
`set_field`/`get` — `migrate_execution_topology` was removed in 260815-DAG-L13; a graph-less
sprint runs the atomic-sequential default and `author_execution_graph` is the bootstrap seam), then `_resolve()`s the task root + optional contract: a
`contract_path` can point at either a root `series-contract.md` or a leaf
`enclosures/<leaf-id>/series-contract.md`; otherwise `task_name` is mapped through
`worktrees.task_resolver.resolve_active_task_root`, with leaf lookup as the fallback. `get`
reads and returns without writing; `create` builds a new `TaskDocument` from `fields`
(refusing an explicit `kind="light"` and defaulting an absent `kind` context-awarely — `subTask`
under a leaf contract, else `master` — while picking up `seriesContractPath` plus `enclosures[]` from
the contract when present; leaf contracts also seed `lifecycleId` for non-masters), refusing to overwrite an existing doc;
`replace` builds the same full `TaskDocument` from `fields` (so it shares the `light` refusal and the
context-aware `kind` default), validates it, refuses a slug/kind change that would move the JSON document
path, and then rewrites the existing JSON plus rendered markdown;
the mutating ops load the existing JSON, apply the edit on a `model_dump(by_alias=True)`
dict, and re-validate. `_build_doc` sends raw create/replace input through the extracted
`scaffold_register_sections` boundary before model construction. That helper first proves
`sections` is a list and every member is a mapping, then appends only missing canonical Judgment
and Priority Register scaffolds for an orchestration master. Wrong container/member shapes fail as
typed `TaskDocError`s before any partial scaffolding; the `TaskDocument` model and
`require_register_sections_valid` remain the semantic owners. Every applied edit also passes
`_enforce_register_section_shapes`: a section carrying a canonical register heading must keep the
exact register table shape or the write fails with `TaskDocError`. `set_step` upserts a top-level step or, with `parent`, a substep
(insert or in-place update by id) and rejects a master; `set_subtask` upserts a
`SubTaskRef` by `number` (master-only); `remove_subtask` (master-only) drops the `SubTaskRef` by
`number` AND deletes the referenced leaf doc (`<slug>.json` + `.md`) unless `subtask.keep_file`,
raising when the number is absent; and `set_section` upserts a freeform `Section` by `heading`
(master, or a leaf — freeform-only, R4). Every op ends in `write_task_doc` and returns a compact
result (`taskId`, `status`, `lifecycleId`, `docPath`, `renderedPath`,
`stepsDone`/`stepsTotal`). After any create/update, the application entry point calls
`master_sync.plan_master_sync`: same-root leaf docs can create/update the parent master row, preserving
manual `scope`, while cross-series refs and missing masters do not write anything. Real ops pass the
leaf and changed master to `write_task_docs` so both JSON+markdown pairs are persisted from prepared
payloads; `dry_run=True` (R5) builds + validates the would-be doc and returns `_preview` (the compact
result plus `rendered`/`diff`/`wouldLose`, a `difflib` diff vs the on-disk `.md` + a dropped-line flag)
**without** writing, including a nested `masterSync` preview (`would-create`/`would-update`, rendered
master markdown, diff, and dropped-line flag) when the master row would change. `TaskDocError` (a
subclass of `AgentsRememberError`) wraps unknown ops, missing docs, empty edits, wrong-kind ops,
validation failures, and invalid resolvable parent master docs.

### Invariants And Boundaries

- Every mutation re-validates the whole document (`TaskDocument.model_validate`) before
  writing, so a bad edit fails loudly and the markdown is only ever a render of a valid
  model.
- `set_field` may only touch the scalar/flat-list fields in `_MUTABLE_FIELDS` (which includes
  `codeExamplesNote`, `statusNote`, `seriesContractPath`, `enclosures`, and — since L14 —
  `orchestrates`, the flat string list that makes an existing master an orchestration task without
  a `replace`; the structured `headerNotes` list is create-set);
  structural edits go through `create`/`replace`/`set_step`/`set_subtask`/`set_section`/`append_decision`.
  The schema validator backstops `orchestrates` as master-only, so `set_field` on a leaf fails loudly.
- `replace` is the supported reset/replan path for changing structural arrays such as steps,
  `codeExamples`, decisions, and sections; it is not a path-move operation.
- Master vs leaf ops are kind-gated up front: `set_step` rejects a master and `set_subtask` rejects a
  non-master; `set_section` works on both (a leaf gets freeform-only sections — R4 — with the schema
  validator as the backstop), so a wrong-kind edit fails with a clear `TaskDocError`.
- Authoring is master/leaf only: `_build_doc` (shared by `create` and `replace`) raises `TaskDocError`
  on an explicit `kind="light"`, and an absent `kind` defaults context-awarely — `subTask` when
  resolving against a leaf contract, otherwise `master`. `light` survives in `DocKind`
  (`tasks/document.py`) only so a legacy light document still loads.
- `remove_subtask` completes task-doc CRUD (the **D**): master-only, it removes the `SubTaskRef` by
  `number` and, by default, deletes the leaf doc the row points at (`SubTaskRef.file` → `<slug>.json` +
  `.md`) — "remove means remove"; `subtask.keep_file` unlinks the index row but leaves the leaf doc on
  disk. It does not touch the leaf's worktree/enclosure. dry-run reports `wouldDeleteFiles` without
  writing or deleting; it has its own handler (a file side effect), so it bypasses `plan_master_sync`.
- Resolution is coordination-local: the task root comes from `config.coordination_root`
  plus active task-name resolution (or an explicit root/leaf `series-contract.md` path).
- Master sync is an additive leaf-write side effect only when the parent master resolves inside the
  same task root. It deliberately preserves manually-authored master `scope` and does not follow
  cross-series master refs.
- Register scaffolding performs no coercion, catch-and-continue, or partial mutation on malformed
  raw sections. It validates the raw container and all members first, appends only missing
  scaffolds, and leaves semantic register validation to the existing model/validator owners.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The application entry point operation list includes `replace`, and the dispatcher routes it through `_replace` before the normal write/preview path. | `VALID_OPERATIONS` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:92-108 |
| `_replace` validates a full document through the shared create/build path and refuses a replacement whose slug/kind would move the JSON document path. | `_replace` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:539-551 |
| Focused application-layer tests prove `replace` rewrites `steps`, `codeExamples`, and `decisions`, preserves dry-run no-mutation behavior, and rejects document path changes. | `test_replace_rewrites_structural_fields_and_decisions` | mcp/tests/test_task_document_application_1.py:404-447 |
| Leaf operations plan master sync, include it in previews, and write changed leaf/master docs together. | "master_sync = plan_master_sync(task_root" | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:315-315 |
| The planner owns same-root master discovery, row derivation, manual-scope preservation, and derived master status. | `plan_master_sync` | mcp/src/agents_remember/tasks/master_sync.py:35-89 |
| The schema model this application entry point drives. | `TaskDocument` | mcp/src/agents_remember/tasks/document.py:677-896 |
| The markdown renderer this application entry point drives. | `render_markdown` | mcp/src/agents_remember/tasks/render.py:39-60 |
| The JSON/markdown store this application entry point drives. | `write_task_docs` | mcp/src/agents_remember/tasks/store.py:111-123 |
| The payload builder that wraps this application entry point. | `task_doc_payload` | mcp/src/agents_remember/mcp/tools/task_doc.py:21-32 |
| The contract helpers used to resolve the task root + lifecycle key. | `WorktreeContract` | mcp/src/agents_remember/worktrees/worktree_contract.py:229-286 |
| The public dispatcher prepares and validates a complete candidate before delegating preview/apply to the publication boundary. | `task_doc_tool`; `_publish_task_doc_candidate` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:211-269; mcp/src/agents_remember/application/task_docs/task_doc_tools.py:303-358 |
| Create and replace share `_build_doc`, which invokes the raw-section scaffolding boundary before task-model validation. | `_build_doc` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:554-584 |
| The extracted helper atomically validates list/member shape and appends only missing canonical register scaffolds. | `scaffold_register_sections`; `_validated_section_list` | mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py:17-55 |
| Focused tests pin missing-section scaffolding, preservation, malformed container/member refusals, and no partial mutation. | `TaskDocSectionScaffoldingTests` | mcp/tests/test_task_doc_section_scaffolding.py:38-127 |

## Current Task-First Publication Boundary

This dispatcher prepares candidate task truth and exact accepted-source snapshots, then delegates
preview/apply to `task_doc_publication.py`. A valid mutation is not subordinate to current queue
state. The publication transaction validates source bytes, commits the task document batch,
invalidates every affected waiting projection to an empty state, and independently rebuilds each
projection from current closeout-door facts. Leaf writes still include any synchronized master row.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.


## 260815-DAG-L12 Title Threading

The task-doc publication/preview sites thread joined graph titles into the renderer (L12-R1).
Ordinary and remove publication route through `task_doc_publication.py`, where the shared
zero-or-one graph-document owner validates batch cardinality before the transaction; the actual
on-disk title read remains inside the publisher callback and therefore inside its task-publication
lock. Documents without an `executionGraph` render without a title context.


## 260815-DAG Master Full-Gate Repair

The module moved to `application/task_docs/` (relative imports within the package) and gained `_sprint_doc_identity`, which merges the standard task-doc identity (taskId/slug/kind/status/lifecycleId/docPath/renderedPath/stepsDone/stepsTotal) into the special-op results (sprint linkage ops + `author_execution_graph`) — pairing with the `TaskDocResponse` special-op wire fields in `models/task_doc.py`.

## Current Contract After CLIVE

The current source seams include `TaskDocTarget`, `TaskDocEdit`, and `task_doc_tool`. Exact
source-CAS, task-first publication, affected-scope invalidation, and rebuild live behind the shared
transactional publisher. The queue is a disposable projection of waiting closeout candidates, not
an authoring lock and not an owner of claimed-operation lifecycle evidence.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `TaskDocTarget`, `TaskDocEdit`, `task_doc_tool` at this ownership boundary. | `TaskDocTarget`; `TaskDocEdit`; `task_doc_tool` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:134-146; mcp/src/agents_remember/application/task_docs/task_doc_tools.py:149-162; mcp/src/agents_remember/application/task_docs/task_doc_tools.py:211-269 |

## Update History

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: re-read and re-anchored the unchanged
  `TaskDocument` dependency after task-schema extraction. Verification remains closeout-owned.

- 2026-08-24T13:43+02:00 — 260821-DAGQC-L1: documented the extracted atomic raw-section
  scaffolding boundary and reconciled the dispatcher with the landed task-first publication and
  central graph-cardinality contracts. Verification metadata remains pinned until architect-owned
  closeout stamps the real code commit.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: module moved to `application/task_docs/`; gained `_sprint_doc_identity` for the special-op results. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/application/task_docs/task_doc_tools.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.



- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   task-doc publish/preview sites thread the joined graph titles into the renderer (`_graph_titles_for` / `_batch_graph_titles`, L12-R1). Verified at code commit b7f2c8e2.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: `task_doc_tool` takes `call: TaskDocCall` (dry_run +
  branch_addressed) instead of the bare `dry_run` flag; the route-review binding machinery moved
  to `application/task_doc_route_review.py` (facade re-export, L16-R6/R9). Verified at code commit
  a9d50e08.


- 2026-08-20T04:20+02:00 — 260815-DAG-L14: the `task_doc` dispatcher routes
  `attach_master`/`detach_master`/`linkage_report` to `application/task_sprint_linkage.py`, carries
  `linkageFacts` on a sprint `get`, and delegates the Completed-row check to the linkage module
  (typed rows complete against the linked master document). Verified at code commit 2f494982.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: `VALID_OPERATIONS` dropped `migrate_execution_topology`
  (graph-less sprints run the atomic-sequential default; `author_execution_graph` bootstraps), new
  orchestration sprints are scaffolded with empty canonical Judgment/Priority Register sections,
  and every write passes register-shape validation (`closeout-grade-register-shape-invalid` on a
  malformed register section). Verification remains closeout-owned.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: `VALID_OPERATIONS` gained `author_execution_graph`
  (dispatched to the topology module's incremental graph authoring with `ExecutionTopologyError` →
  `TaskDocError` translation), and `task_reopen_tool` moved to the new
  `application/task_reopen.py` module, re-exported here unchanged (facade). Verification remains
  closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-15T11:25+02:00 — L3 static-gate repair: extracted queue-scope resolution into its
  application sibling; publication ordering, fail-closed errors, and queue locking are unchanged.
- 2026-08-15T11:07+02:00 — L3 Dagger repair: queue-scope resolution now distinguishes
  genuinely ungoverned light/standalone task documents from graph-commanded masters and leaves;
  strict parent and publication locking still apply to every graph-managed task-fact batch.
- 2026-08-15T09:10+02:00 — L3 content update: recorded queue scope resolution, whole-batch
  publication, completion validation, and governed subtask deletion; verification remains
  closeout-owned.

- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: `task_doc` now exposes the explicit
  `migrate_execution_topology` operation and routes topology-bearing create/replace/set-field edits
  through the dedicated cross-document policy before any write. Verification remains closeout-owned.
- 2026-08-14T06:30+02:00 — L23 final candidate review: task application flows expose manager
  lineage preflight and route completed-leaf restart through exact task-reopen planning before
  descendant branch checks. Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:20+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 4 citation findings and one omission.
  Re-ranged the `VALID_OPERATIONS` (60-72), `_replace` (248-260), and master-sync literal (176-186) rows
  to current locations, pointed the `replace` test row at the three moved tests
  (1080-1123/1125-1148/1150-1164), and added the missing `skip_step` to the operation roll-call.
  Scoped recheck clean.

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 14 initial citation findings (7 anchor, 0 prose, 7 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation that drifted as
  `mcp/tests/test_task_document.py` grew. The three `replace` tests
  (`test_replace_rewrites_structural_fields_and_decisions`,
  `test_replace_dry_run_does_not_mutate_existing_files`,
  `test_replace_rejects_document_path_change`) now sit at L876-L960, not L683-L767; read the range
  back and confirmed it still proves the `steps`/`codeExamples`/`decisions` rewrite, the dry-run
  no-mutation guarantee, and the `TaskDocError` on a slug that would move the document path.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: `task_doc_tool` took `target: TaskDocTarget` +
  `edit: TaskDocEdit` (default `NO_EDIT`) in place of its ten keyword arguments, and the edit
  applier split into one `_apply_*` function per operation behind `_apply`. Operation semantics,
  validation, master sync and the dry-run preview are unchanged. Verification metadata pinned until
  closeout stamps the L2 code commit.
- 2026-07-06T23:57:54+02:00 — 260703-L14 (visual hierarchy + chat grouping): added `orchestrates` to
  `_MUTABLE_FIELDS` — `set_field` can set the orchestration-command list on a master (flat string
  list, matching the whitelist's scalars+flat-lists rule); the schema validator backstops
  master-only, so the same call on a leaf raises `TaskDocError`.
  Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-03T00:30+02:00 — L11 adds `task_reopen_tool` beside the task_doc controller — the tool reopens a TASK, so the controller lives in the task domain, not with the worktree tools.
- 2026-06-29T22:57+02:00 — CRUD completion (leaf L2): added the `remove_subtask` op — master-only, drops the
  `SubTaskRef` by `number` and deletes the referenced leaf doc (json+md) unless `keep_file`, raising on an
  absent number; dry-run reports `wouldDeleteFiles`. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-29T21:24+02:00 — Post-landing cleanup (master/leaf-only authoring): `_build_doc` (shared by
  `create`/`replace`) now refuses an explicit `kind="light"` and defaults an absent `kind` to `subTask`
  under a leaf contract else `master`. Added a controller rejection + default-kind test and repaired two
  tests that authored `light` through the controller. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-26T20:18+02:00 — Task 21 task-doc master sync: the controller now plans same-root leaf-to-master
  row sync after every leaf mutation, includes master preview data in dry-run responses, and writes changed
  leaf/master docs together through `write_task_docs`. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-26T12:41+02:00 — Task-doc replacement repair: documented `replace` as a
  schema-validated full-document operation for task resets/replans, with path-move refusal and
  focused tests for structural rewrites, dry-run no-mutation, and path-change rejection. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: task-doc resolution now uses active task-root and leaf-enclosure resolvers, accepts `seriesContractPath`/`enclosures`, and seeds new leaf docs with enclosure references instead of the retired `contractPath`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T07:23+02:00 — Slice 3c reopened (R5, dry-run/preview): added a `dry_run` param + a `_preview` helper (`difflib` unified diff vs the on-disk `.md` + a `wouldLose` line-set check) that returns the rendered markdown without writing; corrected the Logic note that `set_section` is master-only (R4 made it leaf-capable). Verification metadata pinned until closeout stamps the R5 code commit.
- 2026-06-19T06:03+02:00 — Slice 3c reopened (R4, leaf-doc fidelity): added `statusNote` to `_MUTABLE_FIELDS` and dropped the master-only guard on `set_section` (a leaf may upsert freeform sections; the schema validator backstops freeform-only). Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T05:15+02:00 — Slice 3c reopened (R3, deferred-examples honesty): added `codeExamplesNote` to `_MUTABLE_FIELDS` so `set_field` can record the deferred-examples note; the schema validator backstops master-forbids/leaf-coherence. Verification metadata pinned until closeout stamps the R3 code commit.
- 2026-06-14T00:16+02:00 — Slice 3c commit 3: added master ops `set_subtask` (upsert `SubTaskRef` by number) + `set_section` (upsert freeform `Section` by heading), master `create` handling (skips `lifecycleId`), and kind guards (`set_step` rejects a master; `set_subtask`/`set_section` reject a non-master). Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34+02:00 — Created for slice 3c commit 1: the `task_doc` authoring controller (op-dispatch + contract lifecycle pickup). Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
