# mcp/src/agents_remember/tasks/ — JSON-Primary Task Documents Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `mcp/src/agents_remember/tasks/`                 |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-08-20T05:04+02:00 |
| lastVerifiedCommitHash | `8071a64497ed88f8f423e853dc9440532fd573af` |
| lastVerifiedCommitDate | 2026-08-20T02:19:58+02:00|
| governingOverview      | `../../../../overview.md`                         |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Current Structural Topology Contract

`document_refs.py` indexes real sprint/master/leaf task documents, validates canonical
repository-qualified references, and walks containment without synthesizing role anchors. This
topology supplies structural authorization and dashboard hierarchy; it does not inspect liveness or
select a runtime occupant. Since 260815-DAG-L13 a nature-less standalone master resolves at master
altitude by default (only an explicit `organizational` standalone stays a dead-end), migration
recovery strings name the `author_execution_graph` bootstrap, and the public `commanded_masters`
derives alias-commanded membership for the atomic-sequential default without re-resolving the
sprint from disk.

## Purpose

`tasks/` owns the **JSON-primary task document**: the persisted `ar-task-document/v1`
record is the source of truth for a task's plan and progress, and `task.md` (or
`<slug>.md` for a sub-task) is a deterministic *render* of it. The JSON is never
produced by parsing markdown back. From L11 until 260731-EFA-L6 the route also owned leaf reopen
semantics; `reopen.py` has since moved to `worktrees/reopen.py`, because reopening rewrites the
leaf's enclosure contract and ranking it as a task operation made `tasks` and `worktrees` mutually
dependent (`layers.toml`). What stays here is `leaf_doc.py` (exact case-insensitive leaf-doc lookup
plus the explicit `lifecycleId` restamp worktree start applies across restarts) and the document
reset itself, which reopen still drives through this route's `store.py`. This is the work-content layer the observer projects as active
task documents, with lifecycle/enclosure bindings attached when available, so the dashboard can show
planned and running work from the same JSON source (slice 3c; closes note-03 gap #8).

## Hot Path Summary

The `task_doc` MCP tool authors documents: its application entry point
(`application/task_doc_tools.py`) loads or creates the JSON, applies one operation,
and rewrites both the JSON and the rendered markdown through this package. Leaf writes
can also plan a same-root master-row update through `master_sync.py`, so the parent
master `subTasks[]` checklist follows deterministic leaf facts without overwriting
manual `scope` prose. Start at
`document.py` for the schema, `render.py` for the markdown shape (the
`w-02-light-task-workflow` `template.md` is the spec), and `store.py` for the atomic
JSON+md write/read, including batch writes when a leaf and master must be persisted
together.

## Route Model

- `document.py` — the `ar-task-document/v1` Pydantic schema (`TaskDocument` +
  `Step`/`SubStep`/`Decision`/`CodeExample`, plus `SubTaskRef`/`Section` for masters),
  the `DocKind` (`light`|`subTask`|`master`), `DocStatus`, and `StepStatus` Literals,
  the progress helpers (`step_total`/`step_done`/`current_step` for leaves; `series_total`/`series_done`
  for a master's `subTasks` checkboxes — R1), the optional leaf-only `codeExamplesNote`
  (R3) plus the leaf header companions `statusNote`/`headerNotes` (`HeaderNote`) and freeform leaf
  `sections` (R4 — bespoke prose appended after the template), the master-only `orchestrates`
  list (L14 — the orchestration-command relation: a master with a non-empty list IS an
  orchestration task naming the masters it commands; additive, no new kind), and an after-validator
  that keeps the three kinds disjoint (master ⇒ `subTasks` + structured `sections`, no
  `steps`/`codeExamples`/`codeExamplesNote`/`lifecycleId`; light/subTask ⇒ no `subTasks`, no
  `orchestrates`, freeform-only
  `sections` (R4), and no `codeExamplesNote` alongside non-empty `codeExamples`). A persisted/served
  contract, **not** an MCP response model (peer of `observer.projection`). Leaf docs can name their root
  `seriesContractPath` and one or more `enclosures[]` leaf enclosure contracts.
- `render.py` — `render_markdown(doc)`: the only writer of the rendered markdown.
  Section helpers assemble lines from the model (mirroring
  `worktrees.worktree_contract.contract_to_text`); output is deterministic. A step renders a `### {id} — {title}`
  heading + a `- [ ] {outcome or title}` checkbox carrying the distinct `Step.outcome` (R2; a bare step with no
  outcome and no substeps is heading-only). An empty Proposed Code Examples section renders
  `codeExamplesNote` when set (a deferred slice) instead of the default "no code examples are
  needed" placeholder (R3). The header carries an optional `statusNote` suffix + the `headerNotes` lines
  (and, on an orchestration master, an `**Orchestrates:**` line listing the commanded names — L14),
  and a leaf appends its freeform `sections` after References (R4). A `master`
  dispatches to `_render_master`: an ordered `sections` walk where `freeform` bodies
  render verbatim and `subTasks`/`sharedDecisions` render the generated list/table.
- `store.py` — `read_task_doc` / `write_task_doc` (atomic JSON source + rendered
  `.md`), `write_task_docs` (batch prepare-all-then-write persistence for coupled
  leaf/master edits), and `doc_stem` (`task` for a light **or master** doc, `<slug>` for a sub-task).
- `master_sync.py` — the leaf-to-master row planner used by `task_doc`: same-root
  master discovery, `SubTaskRef` derivation from leaf id/title/rendered filename/status, manual
  `scope` preservation, strict parent-master validation, and the step/substep status collapse that
  maps any active/blocked/done progress to master `inProgress` and all-done progress to `Completed`.

## Invariants And Boundaries

- **JSON is the source of truth; markdown is generated.** The renderer is the only
  writer of the `.md`; nothing parses the markdown back into a document. A re-render
  fully regenerates the body, so any prose not in the model is dropped. Series *master*
  files (with bespoke sections) are covered too: a master keeps its prose in ordered
  `freeform` `sections` (rendered verbatim) and its machine-readable parts in
  `subTasks` + `decisions`, so the round-trip is lossless. The shipped `task_doc` runtime
  authors the JSON source and regenerates its markdown view; hand-editing the rendered
  markdown is outside the contract and is overwritten by the next write.
- The fold is pure data: the renderer takes an already-validated model; all I/O lives
  in `store.py`, and reads go through `model_validate_json`.
- Step/substep status carries dashboard granularity (4-state); the markdown checkbox
  is binary (`done` → `[x]`), so the richer state lives only in the JSON.
- Lifecycle binding is optional runtime context. A leaf/light document may carry a direct
  `lifecycleId` or matching `enclosures[].enclosurePath`; worktree-backed durable tasks store their
  leaf contract under `enclosures/<leaf-id>/series-contract.md`, while a master/root task may also name
  `seriesContractPath`. The document remains readable before those bindings exist.
- Master-row sync is same-root only. Cross-series `master` refs remain navigation metadata; automatic
  writes never cross into another task folder. Existing master `scope` text is manual and preserved.
- Coupled leaf/master writes prepare every JSON and rendered markdown payload before replacing files,
  and reject duplicate output targets up front; that guard is necessary because a coupled operation
  would otherwise silently let one document target overwrite another.
- **`cleanup: reopened` is no longer written in this route.** Its sole producer, `reopen.py`, moved
  to `worktrees/reopen.py` in 260731-EFA-L6 — see that file's sidecar for the current account. The
  history below is kept because the failure it describes was this route's, and because the reader
  reset it documents still runs through this route's `store.py`. `reopen.py` (now line 94) remains
  the package's only producer of that contract cell; `worktrees/modules/start.py` (line 482) and
  `observer/reducer.py` (line 319) only read it, both pairing it with `abandoned` as
  recreate-fresh. That made this route the sole cause of a wire failure until 260731-EFA-L4:
  `models/worktree.py` hand-wrote `CleanupStatus = Literal["pending", "completed", "abandoned"]`,
  so a context packet for a reopened task raised a pydantic `ValidationError` **inside an MCP
  tool handler that has no `except` for one** — for a value only this file writes. The fix is at
  both ends. The reader now imports the contract's own `CleanupStatus`, which includes
  `reopened`; and the four vocabulary cells `reopen_task` moves (`human_review_status`,
  `closeout_status`, `integration_status`, `cleanup`) go through
  `worktree_contract.ContractCells` + `amend_contract` (now line 71) instead of being
  `dataclasses.replace` keywords, because typeshed declares `replace(obj, /, **changes: Any)` and
  pyright therefore checked none of them. The free-text resets (`code_commit`,
  `memory_content_commit`, `ledger_commit`, `commit_approval_note`, `integration_strategy`, the
  three `integrated_*` commits, `lifecycle_id`, `memory_state`, `approved_for_commit`) stay on
  the inner `replace`, since they have no vocabulary to be checked against. The contract this
  writes is byte-identical to before; what changed is that the writer is now checked against the
  vocabulary the reader publishes.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `task_doc` application entry point authors documents through this package. | `task_doc_tool` | mcp/src/agents_remember/application/task_doc_tools.py:190-275 |
| Leaf writes keep same-root master rows synchronized through the dedicated planner. | `plan_master_sync` | mcp/src/agents_remember/tasks/master_sync.py:34-83 |
| The task-document renderer regenerates markdown from the validated `TaskDocument`. | `render_markdown` | mcp/src/agents_remember/tasks/render.py:28-48 |
| The persisted worktree contract is the analogous model-to-text precedent. | `contract_to_text` | mcp/src/agents_remember/worktrees/worktree_contract.py:689-740 |
| The persisted-contract peer this schema mirrors. | `WorkspaceProjection` | mcp/src/agents_remember/observer/projection.py:1131-1153 |

## 260718-CHATS-L5I Current Route Impact

Task reopening now clears the completed landing-final artifact as part of restoring live task state and exposes a clearing failure, so a historical completed landing projection does not survive as the current truth for reopened work. Since 260731-EFA-L6 that clearing lives in `worktrees/reopen.py`, not in this route; the document half of the same reset still runs through this route's `store.py`.

Route indexes are intentionally not regenerated during this partitioned curator pass; the manager will run the single aggregate refresh after all curator ownership is complete. Existing verification metadata remains pre-commit.

## 260731-EFA-L9 Route Impact — Vocabulary Moved

The task-document vocabulary (`StepStatus`/`DocStatus`/`CompletionBlocker`) moved to `models/task_document.py` by L9; tasks modules now import it from there. Task-document behavior is unchanged.

## L23 Final Candidate Route Disposition

Task documents are the canonical sprint/master/leaf identity for source lineage, route review, and
durable lifecycle addressing. A cleaned completed leaf is first converted into an exact task-reopen
plan, before deliberately removed descendant branches can be mistaken for lineage failure.

## 260815-DAG-L3 Queue-Governed Task Facts

Sprint, master, and leaf task-document writers now publish through the sprint queue lock whenever
the topology is queue-managed. The short selected/in-flight lane freezes the whole sprint task-fact
set because one addressed leaf write can synchronize its master row; an atomic blocker permits only
topology-stable recovery inside its own master. Sprint completion additionally proves every exact
graph master is `Completed` with no unresolved completion rows, then atomically closes the quiescent
queue; reopening reverses that closed state through the same recoverable publication path.

## 260815-DAG-L4 L4 Topology Publication Authority

Task-document execution-topology edits are validated under the same repository authority as Git mutation. Candidate graphs cannot promote live leaf work branches into protected supers/atomic refs, detach live owners, or contradict an existing atomic series edge.

## 260815-DAG-L14 Task-Document Route

The `ar-task-document/v1` schema gains `SprintSeat`/`seats` (sprint-only, unique among
non-retired roles) and typed `SubTaskRef.masterRef` rows; the renderer emits real relative
master links, the generated Master Index for sprints, and the `**Seats:**` header block;
`validate_sprint_linkage` hard-fails new-shape drift.

## Update History

- 2026-08-20T05:04+02:00 — 260815-DAG-L14 route impact: the task document schema gains sprint
  `seats` + typed `masterRef` rows, the renderer emits real links/seats, and linkage validation
  is wired. Verified at code commit 8071a644.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: `document_refs.py` resolves a nature-less
  standalone master at master altitude by default, names the `author_execution_graph` bootstrap in
  migration-required refusals, and exposes `commanded_masters` for the atomic-sequential default's
  alias-derived membership; the task-route purpose is unchanged. Verification remains
  closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled this governing route with the frozen integration-authority implementation and forcing surface. Verification remains closeout-owned.

- 2026-08-15T09:10+02:00 — 260815-DAG-L3 route impact: documented queue-governed task
  publication, whole-lane freeze, atomic recovery scope, and exact sprint completion/reopen rules.
  Verification remains closeout-owned.

- 2026-08-15T03:20:17+02:00 — 260815-DAG-L1 independent-review repair: graph-wave reads now bind
  validation and derivation to one resolved sprint snapshot, preserving deterministic output if
  the persisted sprint changes during the operation.
- 2026-08-15T03:10:06+02:00 — 260815-DAG-L1 targeted-Dagger repair: topology forcing now covers
  multi-parent wave release, non-sprint use, candidate root/repository confinement, and the exact
  migration refusal matrix; the task route retains graph-derived ordering as its only ordering
  mechanism.
- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: topology lookup now exposes the
  affected-sprint alias census, closing folder/id/title drift and collision paths while retaining
  exact graph membership as the one mechanical authority.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1 route impact: the task route now owns the strict
  execution-nature and reasoned AON graph schema, exact cross-document membership validation,
  deterministic graph rendering/waves, and rollback-safe cross-root document publication.

- 2026-08-14T06:25+02:00 — L23 final candidate review: task documents expose canonical parent
  series/leaf identity for lineage and route review, and completed-leaf start routes through an
  exact task-reopen plan before removed descendant refs are inspected. Verification remains
  closeout-owned.

- 2026-08-11T19:58+02:00 — 260731-EFA-L19 curator: reconciled task-document ownership with
  canonical structural addressing and current role-altitude rules; task documents remain the public
  routing identity rather than runtime session coordinates.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 route impact: L9 caller/import re-points recorded and body updated.

- 2026-08-04T02:35:12+02:00 — S18-B05 curator delta: resolved provisional source-local citation bindings with fixer-generated current-source ranges; no approved semantic claim changes.
- 2026-08-04T01:28:33+02:00 — S18-SR2-B05 worker: replaced the obsolete pre-runtime hand-authoring statement with the shipped JSON-authoring/render contract and separated the task renderer from the worktree model-to-text precedent.
- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T01:05+02:00 — 260731-EFA-L6 route impact: **`reopen.py` LEFT this route** for `worktrees/reopen.py`. Reopen rewrites the leaf's enclosure contract, emits a `WorktreeCommandResult` and renders through the worktree status payload; ranked as a task operation it made `tasks` and `worktrees` mutually dependent (`layers.toml`) — the task-document store could not be loaded without the whole worktree lifecycle. Corrected the three places this overview claimed the ownership: the Purpose's "since L11 the route also owns leaf reopen semantics", the `cleanup: reopened` invariant's "written here and nowhere else", and the CHATS-L5I landing-final clearing. What genuinely stays is `leaf_doc.py` and the document half of the reset, which reopen still drives through this route's `store.py`, so the invariant's account is kept rather than deleted and now points at the new home. Three cross-file anchors in it were stale and were re-derived against the moved file: the `cleanup: reopened` write line 86 → 94, `amend_contract` line 63 → 71, and `observer/reducer.py` line 318 → 319 (`start.py` line 482 verified correct). Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No route impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T00:00+02:00 — 260731-EFA-L4 curator: this route's only L4 change is `reopen.py`
  (+27/-17), and it is worth a route-level invariant rather than a file-sidecar note, because the
  fact it exposes belongs to the route: **`cleanup: reopened` has exactly one writer in the whole
  package, and it is this file.** Verified by grep across `mcp/src/agents_remember` — the only
  other occurrences are reads (`worktrees/modules/start.py` line 482,
  `observer/reducer.py` line 318) and the `Literal` declaration itself
  (`worktrees/worktree_contract.py` line 55). Verified against `abc7cbcc` that
  `models/worktree.py` then declared `CleanupStatus = Literal["pending", "completed",
  "abandoned"]` — no `reopened` — so the packet could not report a task this route had reopened.
  Recorded the mechanism of the fix on this side: the four vocabulary cells now travel through
  `ContractCells`/`amend_contract` (line 63) rather than as `dataclasses.replace` keywords, which
  typeshed types `**changes: Any` and pyright therefore never checked, while the free-text resets
  stay on the inner `replace`. Read both revisions of the function and confirmed the resulting
  contract is unchanged — same fields, same values, same order. No task-document schema, render
  rule, master-sync contract or file placement moved, so the Purpose, Hot Path Summary and Route
  Model are untouched. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T16:55+02:00 — No route impact: re-verified the attestation below in the exact form the
  closeout gate reads. Both changed files in this route (`master_sync.py`, `render.py`) were parsed
  at the L2 base commit and at the current revision and their syntax trees are identical, so
  wrapping the `MasterSyncError(...) from exc` raise and the `headerNotes` list comprehension across
  lines changed no task-document schema, render rule, header ordering or master-sync contract this
  overview describes. Which module owns which responsibility in this route is untouched.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation, no route impact. Two files in this route
  (`master_sync.py`, `render.py`) were touched by the whole-tree `ruff format` pass (commit
  `00e8379`) and by nothing else: a `raise ... from exc` and a list comprehension with a trailing
  comment were reflowed across lines. No task-document schema, render rule, master-sync contract or
  file placement changed, so this overview was re-read against the current source and deliberately
  **not** rewritten — every claim below still holds. Worth knowing for anyone reading task
  documents *about* L2: the leaf plan text is not memory, and closeout owns it. Verification
  metadata pinned until closeout stamps the L2 commit.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: updated the route body for the current backend/shared behavior; aggregate route-index generation remains manager-owned.

- 2026-07-06T23:59:12+02:00 — 260703-L14 (visual hierarchy + chat grouping) route impact: the schema
  now carries the ORCHESTRATION-COMMAND relation — `document.py` gained the master-only
  `orchestrates` list (an orchestration task is a master doc with a non-empty list; owner ruling —
  additive, no new kind, no migration) and `render.py` renders it as an `**Orchestrates:**` header
  line. `set_field` (controllers route) mutates it; the observer projects it onto `TaskDocNode`
  for the dashboard hierarchy. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T03:30+02:00 — No route impact: 260703-L11 (tasks tab shows worktree truth) reviewed `reopen.py`'s `cleanup: reopened` semantics as the projection's documented meaning (contract-reset-awaiting-restart); no file in this route changed — the existence flags live in the observer route.
- 2026-07-03T00:35+02:00 — L11 route impact: `reopen.py` and `leaf_doc.py` join the route — reopening is a TASK operation (contract + doc reset; worktree recreation stays with worktree_start), and the doc-to-lifecycle binding is explicit-restamp, never heuristic.
- 2026-06-29T21:24+02:00 — No route impact: `document.py` gained a comment noting `DocKind`'s `light` is
  retained only for legacy load-compat (the `task_doc` controller refuses to author new `light` docs); the
  schema and route model are unchanged (detail in the document.py file sidecar; task 260628_post-landing-cleanup).
- 2026-06-26T20:18+02:00 — Task 21 task-doc sync: added `master_sync.py` to the route model and clarified
  that `store.write_task_docs` persists coupled leaf/master edits after preparing all payloads. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:39+02:00 — Task 17 task-document route correction: clarified that task docs are active
  work-content records with optional lifecycle/enclosure binding, so planning docs remain readable before
  an enclosure exists. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: task documents now model `seriesContractPath` plus `enclosures[]` instead of `contractPath`, allowing root series contracts and leaf enclosure contracts to coexist without a second task-document schema. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:03 — Slice 3c reopened (R4, leaf-doc fidelity): `document.py` gained `HeaderNote` + optional `statusNote`/`headerNotes`, and the kind guard relaxed so a leaf may carry freeform `sections` (still forbids the `subTasks` index + non-freeform sections); `render.py` renders the header companions and appends leaf freeform sections after References; `set_section` relaxed to leaf. `DocStatus` stays a strict enum. The w-02 skill documents the extensions. Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T05:15 — Slice 3c reopened (R3, deferred-examples honesty): `document.py` gained an optional leaf-only `codeExamplesNote` and `render.py` renders it for an empty `codeExamples` (a deferred planning slice) instead of the "no code examples are needed" default; the kind guard forbids it on a master and alongside non-empty examples, and the w-02 skill (template/SKILL/workflow) now teaches the field. Verification metadata pinned until closeout stamps the R3 code commit.
- 2026-06-19T04:18 — Slice 3c reopened (R2, heading-vs-outcome): `document.py` `Step` gained an optional `outcome` and `render.py` puts it on the checkbox line (a bare step is heading-only) — closing the schema's heading-vs-outcome collapse, matching the w-02 template. Verification metadata pinned until closeout stamps the R2 code commit.
- 2026-06-19T03:17 — Slice 3c reopened (R1, masters observable): `document.py` gained the master progress helpers `series_total`/`series_done` (a master's checkboxes are its `subTasks`; declared `Completed` is the lever, authoritative over a slice's leaf steps), re-exported by the package facade and consumed by the observer's folder-keyed series projection. Verification metadata pinned until closeout stamps the R1 code commit.
- 2026-06-14T00:16 — Slice 3c commit 3 (master JSON support): the route now covers `kind:"master"` — a structured `subTasks` series index + an ordered `sections` passthrough (`document.py`), the `_render_master` path (`render.py`), and `doc_stem` mapping master → `task` (`store.py`). Closes the commit-1 master de-scope (ordered sections preserve bespoke prose losslessly). Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1 (task persistence layer): the JSON-primary `ar-task-document/v1` schema (`document.py`), the deterministic renderer (`render.py`), and the JSON+markdown store (`store.py`). Scope is `light`+`subTask` documents; series master files stay hand-authored markdown. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
