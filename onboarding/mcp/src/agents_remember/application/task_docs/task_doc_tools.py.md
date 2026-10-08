# mcp/src/agents_remember/application/task_docs/task_doc_tools.py

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
sprint linkage operations (`attach_master`/`detach_master`/`retire_master`/`linkage_report`) to
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
  a `replace`, and — since MIK-R08 — the boolean `knowledgeMaintenanceScope`, and — since MIK-R11 — the
  `expectedKnowledgeEffects` declaration list; the structured
  `headerNotes` list is create-set);
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
- **Complete retired rows are protected from generic edits.** `_validate_task_doc_candidate` calls
  `require_retirement_proofs_unchanged` before its other candidate checks. The guard compares complete retired
  rows by number, including proof, name, scope, status and file, and refuses additions, changes or removals.
  The diagnostic instructs the caller to leave the row unchanged. `retire_master` creates the retirement
  record; repeating its identical request completes remaining work rather than editing the retained proof.
- A `retire_master` answer carries the document identity of the document it was called on. When a master
  retired on its own has moved under `0_archive/` by the time it answers, `_sprint_doc_identity` reads the
  identity from the archive path the result names (`taskArchive.archivePath`) instead of the vanished task root.
- Resolution is coordination-local: the task root comes from `config.coordination_root`
  plus active task-name resolution (or an explicit root/leaf `series-contract.md` path).
- Master sync is an additive leaf-write side effect only when the parent master resolves inside the
  same task root. It deliberately preserves manually-authored master `scope` and does not follow
  cross-series master refs.
- Register scaffolding performs no coercion, catch-and-continue, or partial mutation on malformed
  raw sections. It validates the raw container and all members first, appends only missing
  scaffolds, and leaves semantic register validation to the existing model/validator owners.

## Evidence

### Repo-Internal References

- The application entry point operation list includes `replace`, and the dispatcher routes it through `_replace` before the normal write/preview path. [1]
- The operation table now registers the step plane split by intent (`set_step` update-only, `add_step` create-only, `remove_step` delete-only) alongside the moved `skip_step`. [2]
- The four step adapters are one-line delegations to the extracted step-plane module; this module registers and validates, it no longer owns the addressing rule. [3]
- `read_steps` is a read-only special operation that publishes nothing and returns only the checklist, never the whole authored document. [4]
- The terminal-status guard admits exactly one exception: a `remove_step` carrying a nonblank reason, recognized through the step plane's shared reason reader. [5]
- `_replace` validates a full document through the shared create/build path and refuses a replacement whose slug/kind would move the JSON document path. [6]
- Focused application-layer tests prove `replace` rewrites `steps`, `codeExamples`, and `decisions`, preserves dry-run no-mutation behavior, and rejects document path changes. [7]
- Leaf operations plan master sync, include it in previews, and write changed leaf/master docs together. [8]

- The planner owns same-root master discovery, row derivation, manual-scope preservation, and derived master status. [9]

- The task-document schema model this application entry point validates and writes; its class body now ends at its integration-branch normaliser. [10]
- The markdown renderer this application entry point drives. [11]
- The JSON/markdown store this application entry point drives. [12]
- The payload builder that wraps this application entry point. [13]
- The contract helpers used to resolve the task root + lifecycle key. [14]
- The public dispatcher prepares and validates a complete candidate before delegating preview/apply to the publication boundary. [15]
- Create and replace share `_build_doc`, which invokes the raw-section scaffolding boundary before task-model validation. [16]
- The extracted helper atomically validates list/member shape and appends only missing canonical register scaffolds. [17]
- The fail-closed leaf-authoring guard: refuses a leaf whose derived master link nothing would ever bind, and states the planning allowance as a guarantee. [18]
- The `elif` arm that reaches the guard from the shared create/replace builder. [19]
- The two end-to-end cases that pin the refusal's message and the still-working planning flow. [20]
- Task document edits are prepared before publication; removed scaffolding tests are not current proof of execution. [21]

- Generic task-document edits preserve complete retired rows. [27]
- A special operation's answer reads its identity from the archive path when the called master has moved. [28]
- The operation list takes the sprint linkage operations, `retire_master` among them, from the linkage module. [29]

## 260928-MIK-L08 `knowledgeMaintenanceScope` Is Settable

`_MUTABLE_FIELDS` gained `knowledgeMaintenanceScope`, the MIK-R08 task-document field that makes a leaf's
worklist classify every entry of its memory base. `set_field` can therefore turn it on for an existing
leaf; the model's own validation still runs on the whole document. The field is classified `LIFECYCLE`,
not `NORMATIVE` (architect ruling 4), so setting it does not change the task's intent digest.

- The settable flat fields, now including the maintenance-scope flag. [22]
- The field's `LIFECYCLE` classification. [23]

## 260928-MIK-L11 `expectedKnowledgeEffects` Is Settable

`_MUTABLE_FIELDS` gained `expectedKnowledgeEffects`, the MIK-R11 declaration of a leaf's expected
invariant and family effects (MIK-R11 rule 1: written through `task_doc`). `set_field` validates the whole
document, so a malformed declaration (a repeat, a bad subject form, a label outside the vocabulary, a prose
`requirementRef`, an empty list, an extra key, or the field on a master) is refused by the model before any
write; `null` clears it. The field is classified `NORMATIVE`, so setting it changes the leaf's intent digest
and clearing it restores the former digest. Who may write it (the architect, or the worker with the
architect's approval) is procedural: `task_doc` has no per-field role gate, and the reviewer checks the
declaration against the packet (ruling Q3). No real task document may carry it before the L37 install
(ruling Q2, 2026-09-29T21:56:18+02:00).

- The settable flat fields, now including the declaration. [24]
- `set_field` sets it, the digest changes, and clearing restores it. [25]

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

- The current module exposes `TaskDocTarget`, `TaskDocEdit`, `task_doc_tool` at this ownership boundary. [26]

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
