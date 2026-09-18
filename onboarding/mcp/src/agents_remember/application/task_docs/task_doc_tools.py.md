# mcp/src/agents_remember/application/task_docs/task_doc_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/task_docs/task_doc_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-18T17:02+02:00 |
| lastVerifiedCommitHash | `f05ba167cd6dfb56b48a775f3da5d45528c09c82` |
| lastVerifiedCommitDate | 2026-09-18T17:19:31+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l4-ar` uncommitted source; base `0dd04d6adbca3e8ba61849b605ece3137005829e` |
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
payload carries the enclosure state. Since 260831-LOCR-L33 the whole **step plane** — the one
exact addressing rule and the `set_step`/`add_step`/`remove_step`/`skip_step` operations plus the
`read_steps` projection — lives in the sibling `task_doc_steps.py`; this module registers those
operations, keeps thin `_apply_*` adapters, and owns validation/publication. The extraction is a
size decision, not a behaviour one: keeping the plane inline took this file to 1,243 lines against
the armed 1,200-line hard limit, the same decomposition pattern as `task_doc_discard`,
`task_doc_route_review`, and `task_sprint_linkage`. Since 260815-DAG-L14 the dispatcher also routes the
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
replacing the former single branching applier. Since 260831-LOCR-L33 the four step adapters
(`_apply_set_step` / `_apply_add_step` / `_apply_remove_step` / `_apply_skip_step`) are one-line
delegations to `task_doc_steps`, and `read_steps` dispatches in the special-op path through
`_read_steps`.

It validates `operation` against `VALID_OPERATIONS`
(`create`/`replace`/`set_status`/`set_step`/`add_step`/`remove_step`/`skip_step`/`read_steps`/
`set_subtask`/`remove_subtask`/`set_section`/
`append_decision`/`record_route_review`/`author_execution_graph`/
`set_field`/`get` — `migrate_execution_topology` was removed in 260815-DAG-L13; a graph-less
sprint runs the atomic-sequential default and `author_execution_graph` is the bootstrap seam), then `_resolve()`s the task root + optional contract: a
`contract_path` can point at either a root `series-contract.md` or a leaf
`enclosures/<leaf-id>/series-contract.md`; otherwise `task_name` is mapped through
`worktrees.task_resolver.resolve_active_task_root`, with leaf lookup as the fallback. `get`
reads and returns without writing; `create` builds a new `TaskDocument` from `fields`
(refusing an explicit `kind="light"` and defaulting an absent `kind` context-awarely — `subTask`
under a leaf contract, else `master` — while picking up `seriesContractPath` plus `enclosures[]` from
the contract when present; leaf contracts also seed `lifecycleId` for non-masters), refusing to overwrite an existing doc.
Since 260913-LCA-L5 `_build_doc`'s `if contract is not None` block is followed by an
`elif data.get("kind") != "master"` arm calling `_require_bindable_leaf_authoring(task_root)`
(`:619-649`): a leaf document authored under a task root with **no master document at all** is refused
with the field names, the exact missing `task.json` path and the remedy, because no operation would ever
bind its derived fields;
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
exact register table shape or the write fails with `TaskDocError`. The step plane is split by
intent and delegates to `task_doc_steps`: `set_step` **updates exactly one existing** unit
(top-level, or one exact `parent`'s substep) and **never creates** — it used to be an
unconditional upsert, so a bare substep id minted a top-level step titled after the id and
reported success (the L30/L31/L32 defect); `add_step` **creates exactly one** and requires
`{id, title}`, refusing an existing id in its scope; `remove_step` **deletes exactly one** and
requires a nonblank `step.reason`, appending a decision entry in `skip_step`'s shape; `read_steps`
is the read-only focused checklist read (`id`/`title`/`status`/`note` plus nested substeps).
All of them reject a master. `set_subtask` upserts a
`SubTaskRef` by `number` (master-only); `remove_subtask` (master-only) drops the `SubTaskRef` by
`number` AND deletes the referenced leaf doc (`<slug>.json` + `.md`) unless `subtask.keep_file`,
raising when the number is absent; and `set_section` upserts a freeform `Section` by `heading`
(master, or a leaf — freeform-only, R4). `_validate_task_doc_candidate` runs the terminal-status
guard last: a `Completed` document admits no new unresolved work, with one deliberate exception —
`remove_step` carrying a nonblank reason (`_enforce_terminal_status(operation, candidate, edit)`
reads the reason through `task_doc_steps.step_reason`, the same reader the delete path uses before
its own refusal). Every op ends in `write_task_doc` and returns a compact
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
  structural edits go through `create`/`replace`/the step plane (`task_doc_steps`)/`set_subtask`/`set_section`/`append_decision`.
  The schema validator backstops `orchestrates` as master-only, so `set_field` on a leaf fails loudly.
- **The step plane is owned by `task_doc_steps.py`, not here.** This module registers the operations,
  keeps thin `_apply_*` adapters, and owns validation/publication; the one addressing rule
  (`parent` selects the namespace; zero or multiple matches refuse) and the four step operations live
  in the sibling module. `set_step` never creates and `add_step` never updates — neither is a
  fallback for the other — and `remove_step` ("this step should never have existed") is deliberately
  distinct from `skip_step` ("this planned unit was deliberately not done", which keeps and resolves
  the unit). Do not document them as interchangeable.
- **A reasoned `remove_step` is the only terminal-status exception.** A `Completed` document refuses
  every other mutation that would add unresolved work; a removal with a nonblank reason is admitted
  because the reason and the appended decision are its audited substitute. The exemption is required
  rather than merely permitted: the motivating repair targeted an already-`Completed` leaf document,
  and gating on document status would have forced a full-document `replace` that was correctly
  refused as too destructive.
- `replace` is the supported reset/replan path for changing structural arrays such as steps,
  `codeExamples`, decisions, and sections; it is not a path-move operation.
- Master vs leaf ops are kind-gated up front: every step operation (`set_step`/`add_step`/
  `remove_step`/`skip_step`/`read_steps`) rejects a master through the shared
  `_require_step_payload` guard in `task_doc_steps`, and `set_subtask` rejects a
  non-master; `set_section` works on both (a leaf gets freeform-only sections — R4 — with the schema
  validator as the backstop), so a wrong-kind edit fails with a clear `TaskDocError`.
- Authoring is master/leaf only: `_build_doc` (shared by `create` and `replace`) raises `TaskDocError`
  on an explicit `kind="light"`, and an absent `kind` defaults context-awarely — `subTask` when
  resolving against a leaf contract, otherwise `master`. `light` survives in `DocKind`
  (`tasks/document.py`) only so a legacy light document still loads.
- **A leaf document is never authored where nothing could bind its derived fields.** Authoring under a
  task root with no master document is refused by `_require_bindable_leaf_authoring`; the refusal is the
  fail-closed half of 260913-LCA-L5, and it corrects the earlier claim that leaf authoring succeeds under
  any task root. The **planning** case is deliberately still allowed — a master document exists but no
  series contract has been bootstrapped yet — and that allowance is a *guarantee*, not an absent branch:
  the leaf's first `worktree_start`/`worktree_attach` runs the start binding publisher
  (`plan_leaf_doc_lifecycle_restamp` / `plan_leaf_doc_enclosure_registration`, see the
  `tasks/leaf_doc.py` card), which writes both derived fields once the contract exists. The guarantee is
  asserted in the helper's own docstring precisely so a future reader can tell the two cases apart.
- No derived field is dropped silently anywhere in `_build_doc`: for every field skipped because no
  contract resolved, the code either refuses (no master document) or names the operation that will bind it
  (planning under an existing master). There is no `# noqa`, per-file ignore or `TODO` standing in for
  either half.
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
| The application entry point operation list includes `replace`, and the dispatcher routes it through `_replace` before the normal write/preview path. | `VALID_OPERATIONS` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:92-115 |
| The operation table now registers the step plane split by intent (`set_step` update-only, `add_step` create-only, `remove_step` delete-only) alongside the moved `skip_step`. | `_MUTATIONS` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:736-746 |
| The four step adapters are one-line delegations to the extracted step-plane module; this module registers and validates, it no longer owns the addressing rule. | `_apply_set_step`; `_apply_add_step`; `_apply_remove_step`; `_apply_skip_step` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:690-708 |
| `read_steps` is a read-only special operation that publishes nothing and returns only the checklist, never the whole authored document. | `_read_steps` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:405-421 |
| The terminal-status guard admits exactly one exception: a `remove_step` carrying a nonblank reason, recognized through the step plane's shared reason reader. | `_enforce_terminal_status` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:875-892 |
| `_replace` validates a full document through the shared create/build path and refuses a replacement whose slug/kind would move the JSON document path. | `_replace` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:569-581 |
| Focused application-layer tests prove `replace` rewrites `steps`, `codeExamples`, and `decisions`, preserves dry-run no-mutation behavior, and rejects document path changes. | `test_replace_rewrites_structural_fields_and_decisions` | mcp/tests/test_task_document_application_1.py:237-280 |
| Leaf operations plan master sync, include it in previews, and write changed leaf/master docs together. | "master_sync = plan_master_sync(task_root" | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:320-320 |
| The planner owns same-root master discovery, row derivation, manual-scope preservation, and derived master status. | `plan_master_sync` | mcp/src/agents_remember/tasks/master_sync.py:35-89 |
| The schema model this application entry point drives. | `TaskDocument` | mcp/src/agents_remember/tasks/document.py:649-823 |
| The markdown renderer this application entry point drives. | `render_markdown` | mcp/src/agents_remember/tasks/render.py:45-71 |
| The JSON/markdown store this application entry point drives. | `write_task_docs` | mcp/src/agents_remember/tasks/store.py:112-124 |
| The payload builder that wraps this application entry point. | `task_doc_payload` | mcp/src/agents_remember/mcp/tools/task_doc.py:21-32 |
| The contract helpers used to resolve the task root + lifecycle key. | `WorktreeContract` | mcp/src/agents_remember/worktrees/worktree_contract.py:229-283 |
| The public dispatcher prepares and validates a complete candidate before delegating preview/apply to the publication boundary. | `task_doc_tool`; `_publish_task_doc_candidate` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:218-276; mcp/src/agents_remember/application/task_docs/task_doc_tools.py:308-363 |
| Create and replace share `_build_doc`, which invokes the raw-section scaffolding boundary before task-model validation. | `_build_doc` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:584-617 |
| The extracted helper atomically validates list/member shape and appends only missing canonical register scaffolds. | `scaffold_register_sections`; `_validated_section_list` | mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py:17-37; mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py:40-51 |
| The fail-closed leaf-authoring guard: refuses a leaf whose derived master link nothing would ever bind, and states the planning allowance as a guarantee. | `_require_bindable_leaf_authoring` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:620-650 |
| The `elif` arm that reaches the guard from the shared create/replace builder. | `_build_doc` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:584-617 |
| The two end-to-end cases that pin the refusal's message and the still-working planning flow. | `test_authoring_a_leaf_with_no_master_document_is_refused_with_its_remedy`; `test_authoring_a_master_and_its_leaves_before_any_start_still_succeeds` | mcp/tests/test_leaf_doc_master_link_binding.py:235-250; mcp/tests/test_leaf_doc_master_link_binding.py:252-268 |
| Task document edits are prepared before publication; removed scaffolding tests are not current proof of execution. | `_prepare_task_doc_edit` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:362-398 |

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
| The current module exposes `TaskDocTarget`, `TaskDocEdit`, `task_doc_tool` at this ownership boundary. | `TaskDocTarget`; `TaskDocEdit`; `task_doc_tool` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:142-153; mcp/src/agents_remember/application/task_docs/task_doc_tools.py:157-169; mcp/src/agents_remember/application/task_docs/task_doc_tools.py:218-276 |

## 260913-LCA-L5 Leaf Authoring Fails Closed On A Missing Master Link

The authoring plane must not silently drop a derived field. `_build_doc` stamps
`seriesContractPath` and `enclosures[]` inside `if contract is not None`, reached only from `create`
and `replace`; when no contract resolves, both fields used to vanish with no error, no warning and no
record. That is the drop this master hit on its own first leaf — every newly planned master authors
its leaf docs before its first `worktree_start` bootstraps the series contract.

Two cases reach the empty-contract path, and only one of them is repairable:

- **Task root holds a master document.** This is the normal planning flow (master first, then its
  leaves, before any start). It stays allowed, and the allowance is now stated in code as a
  *guarantee* rather than implied by an absent branch: the leaf's first
  `worktree_start`/`worktree_attach` runs the start binding publisher, which writes both derived
  fields once the contract exists.
- **Task root holds no master document at all.** Nothing owns the series, no operation binds the
  fields, and the document would persist without its master link — so `_require_bindable_leaf_authoring`
  refuses it, naming `seriesContractPath`, the exact missing `task.json` path and the remedy.

Nothing else about authoring changed: the `kind="light"` refusal, the context-aware default kind, the
path-move refusal on `replace`, and the whole step plane are untouched, and no schema field was added
or removed.


## 260918-TSIP-L4 — The `kind` Refusal Names Its Vocabulary (`T43`)

`_build_doc`'s refusal for `kind='light'` now appends the accepted vocabulary and the
omitted case (**`:594-595`**): *"kind must be one of ['subTask', 'master'], or omitted to take the
contract-derived default."* The refusal already named what is gone; it did not name what is
accepted, so a caller read the registered description for the vocabulary and the description was
itself stale. Net `+1` from the old `:595`, so every line at or below the old `:595` moved `+1`.

**`T43` is repaired on both sides, per the `T50` precedent**: the description in
`mcp/registration/tasks.py` no longer advertises `'light'`, and this refusal now names the
vocabulary it does accept. Pinned against the **registered** FastMCP surface, not a source
constant, by `mcp/tests/test_tool_response_conformance.py::test_task_doc_description_and_refusal_name_the_same_kind_vocabulary`.

## Update History
- 2026-09-18T17:02+02:00 — 260918-TSIP-L4 curator (uncommitted change set on `ar/260918-tsip-l4-ar`, base `0dd04d6a`): the `kind` refusal now names the accepted vocabulary (`T43`, producer side). Verification metadata stays at the recorded verification because the candidate is uncommitted and the governed closeout owns the real code commit; `lastUpdated` advances with this body edit.
- 2026-09-14T07:05+02:00 — 260913-LCA-L5 curator (uncommitted change set on `ar/260913-lca-l5-ar`, base
  `52875e7a`): recorded the fail-closed leaf-authoring refusal. The Logic and Invariants sections now
  state that a leaf document is never authored where nothing could bind its derived fields, that the
  planning case stays allowed **by an explicit guarantee** (the start binding publisher writes both
  fields once the contract exists), and that no derived field is dropped silently anywhere in
  `_build_doc`. This corrects the earlier card, which implied leaf authoring succeeded under any task
  root. Added a section for the change and four reference rows. Also repaired every stale range in the
  two reference tables against the current source, measured with AST: change-induced drift
  (`_MUTATIONS` 700-710 → 735-745, the four `_apply_*` step adapters 654-672 → 689-707,
  `_enforce_terminal_status` 839-856 → 874-891, the `replace` test 243-286 → 237-280) and drift that
  predated this change (`_build_doc` 559-589 → 584-616, `_read_steps` 405-419 → 405-421,
  `task_doc_tool`/`_publish_task_doc_candidate` 214-272/304-359 → 218-276/308-363,
  `_prepare_task_doc_edit` 362-398 → 366-402, `TaskDocTarget`/`TaskDocEdit` 137-149/152-165 →
  142-153/157-169, `TaskDocument` 645-819 → 649-823, `WorktreeContract` 228-283 → 229-283).
  Verification metadata is **not** advanced: the code commit does not exist and closeout owns the
  stamp; no acceptance claim.
- 2026-09-12T22:45:49+00:00: Generated citation repair: `_replace` repointed to mcp/src/agents_remember/application/task_docs/task_doc_tools.py:569-581. No content impact: mechanical anchor-range projection bound to citation source snapshot 7464238939d75c2065358d53c0f2e066dda635c5705830dfbe24fff068177c35; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:45:49+00:00: Generated citation repair: "master_sync = plan_master_sync(task_root" repointed to mcp/src/agents_remember/application/task_docs/task_doc_tools.py:320-320. No content impact: mechanical anchor-range projection bound to citation source snapshot 7464238939d75c2065358d53c0f2e066dda635c5705830dfbe24fff068177c35; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: recorded that the step plane was extracted to
  the new sibling `task_doc_steps.py` (the tools module had reached 1,243 lines against the armed
  1,200-line hard limit) and that `VALID_OPERATIONS` gained `add_step`/`remove_step`/`read_steps`.
  Corrected the old statement that `set_step` "upserts a top-level step or, with `parent`, a
  substep": it is now update-only and never creates, `add_step` is the create-only path, and
  `remove_step` is delete-only with a mandatory reason. Recorded the reasoned `remove_step`
  exemption in `_enforce_terminal_status` (a `Completed` document admits it once a nonblank reason is
  given — required, not merely permitted, because gating on document status would have forced a
  full-document `replace` on the motivating already-`Completed` leaf), the all-step-ops reject a
  master rule, and that `remove_step` and `skip_step` are distinct. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "master_sync = plan_master_sync(task_root" repointed to mcp/src/agents_remember/application/task_docs/task_doc_tools.py:316-316. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "master_sync = plan_master_sync(task_root" repointed to mcp/src/agents_remember/application/task_docs/task_doc_tools.py:321-321. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `TaskDocument` repointed to mcp/src/agents_remember/tasks/document.py:642-816. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `test_replace_rewrites_structural_fields_and_decisions` repointed to mcp/tests/test_task_document_application_1.py:243-286. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

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
