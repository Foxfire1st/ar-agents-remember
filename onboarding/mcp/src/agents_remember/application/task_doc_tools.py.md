# mcp/src/agents_remember/application/task_doc_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/task_doc_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-15T11:25+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[application/overview.md](overview.md)

## Purpose

The operation-dispatched application entry point behind the `task_doc` MCP tool: it loads or
creates the `ar-task-document/v1` JSON for a task, applies one edit, and rewrites both
the JSON (source of truth) and the rendered markdown. Since L11 it also hosts
`task_reopen_tool`: the task-domain reset that reopens a fully landed leaf under its
exact leaf id (delegating to `worktrees/reopen.py`); its response keeps the
worktree-command contract shape because the payload carries the enclosure state.

## Code Commentary

### Logic

`task_doc_tool(config, target: TaskDocTarget, *, operation, edit: TaskDocEdit = NO_EDIT,
dry_run=False)` — since 260731-EFA-L2 the arguments arrive as two objects that answer two different
questions. `TaskDocTarget(repo_id, task_name, contract_path, slug)` is **which document**;
`TaskDocEdit(fields, step, decision, subtask, section)` is **what the edit is**, with `NO_EDIT` the
shared empty value a `get` passes. Internally the operation table dispatches through one private
`_Edit` view and a per-operation `_apply_set_status` / `_apply_set_field` / `_apply_set_step` /
`_apply_set_subtask` / `_apply_set_section` / `_apply_append_decision` function behind `_apply`,
replacing the former single branching applier.

It validates `operation` against `VALID_OPERATIONS`
(`create`/`replace`/`set_status`/`set_step`/`skip_step`/`set_subtask`/`remove_subtask`/`set_section`/
`append_decision`/`set_field`/`get`), then `_resolve()`s the task root + optional contract: a
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
dict, and re-validate. `set_step` upserts a top-level step or, with `parent`, a substep
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The application entry point operation list includes `replace`, and the dispatcher routes it through `_replace` before the normal write/preview path. | `VALID_OPERATIONS` | mcp/src/agents_remember/application/task_doc_tools.py:76-90 |
| `_replace` validates a full document through the shared create/build path and refuses a replacement whose slug/kind would move the JSON document path. | `_replace` | mcp/src/agents_remember/application/task_doc_tools.py:413-425 |
| Focused application-layer tests prove `replace` rewrites `steps`, `codeExamples`, and `decisions`, preserves dry-run no-mutation behavior, and rejects document path changes. | `test_replace_rewrites_structural_fields_and_decisions` | mcp/tests/test_task_document_application_1.py:375-418 |
| Leaf operations plan master sync, include it in previews, and write changed leaf/master docs together. | "master_sync = plan_master_sync(task_root" | mcp/src/agents_remember/application/task_doc_tools.py:244-244 |
| The planner owns same-root master discovery, row derivation, manual-scope preservation, and derived master status. | `plan_master_sync` | mcp/src/agents_remember/tasks/master_sync.py:34-83 |
| The schema model this application entry point drives. | `TaskDocument` | mcp/src/agents_remember/tasks/document.py:261-364 |
| The markdown renderer this application entry point drives. | `render_markdown` | mcp/src/agents_remember/tasks/render.py:28-48 |
| The JSON/markdown store this application entry point drives. | `write_task_docs` | mcp/src/agents_remember/tasks/store.py:40-73 |
| The payload builder that wraps this application entry point. | `task_doc_payload` | mcp/src/agents_remember/mcp/tools/task_doc.py:19-30 |
| The contract helpers used to resolve the task root + lifecycle key. | `WorktreeContract` | mcp/src/agents_remember/worktrees/worktree_contract.py:230-285 |

## 260815-DAG-L3 Queue-Governed Publication

Every task-doc publication now resolves its governing sprint queue and publishes the complete
document batch under that queue's lock. Leaf writes include any synchronized master row; sprint
completion validates every commanded graph master and atomically closes a quiescent queue;
`remove_subtask` deletion is inside the same governed publication. Topology-stable classification
controls which own-atomic-block recovery edits may proceed while a barrier is active. Structural
scope resolution is delegated to `task_doc_queue_scope.py`; this dispatcher owns only error
translation and the locked publication call.

## Update History

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
- 2026-06-19T07:23 — Slice 3c reopened (R5, dry-run/preview): added a `dry_run` param + a `_preview` helper (`difflib` unified diff vs the on-disk `.md` + a `wouldLose` line-set check) that returns the rendered markdown without writing; corrected the Logic note that `set_section` is master-only (R4 made it leaf-capable). Verification metadata pinned until closeout stamps the R5 code commit.
- 2026-06-19T06:03 — Slice 3c reopened (R4, leaf-doc fidelity): added `statusNote` to `_MUTABLE_FIELDS` and dropped the master-only guard on `set_section` (a leaf may upsert freeform sections; the schema validator backstops freeform-only). Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T05:15 — Slice 3c reopened (R3, deferred-examples honesty): added `codeExamplesNote` to `_MUTABLE_FIELDS` so `set_field` can record the deferred-examples note; the schema validator backstops master-forbids/leaf-coherence. Verification metadata pinned until closeout stamps the R3 code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: added master ops `set_subtask` (upsert `SubTaskRef` by number) + `set_section` (upsert freeform `Section` by heading), master `create` handling (skips `lifecycleId`), and kind guards (`set_step` rejects a master; `set_subtask`/`set_section` reject a non-master). Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1: the `task_doc` authoring controller (op-dispatch + contract lifecycle pickup). Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
