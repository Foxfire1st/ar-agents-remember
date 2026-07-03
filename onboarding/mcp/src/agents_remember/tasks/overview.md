# mcp/src/agents_remember/tasks/ — JSON-Primary Task Documents Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `mcp/src/agents_remember/tasks/`                 |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-03T00:35+02:00 |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`       |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `../../../../overview.md`                         |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`tasks/` owns the **JSON-primary task document**: the persisted `ar-task-document/v1`
record is the source of truth for a task's plan and progress, and `task.md` (or
`<slug>.md` for a sub-task) is a deterministic *render* of it. The JSON is never
produced by parsing markdown back. Since L11 the route also owns leaf reopen semantics: `reopen.py` (the `task_reopen`
tool's implementation — reset a fully landed leaf back to planning under its exact
leaf id) and `leaf_doc.py` (exact case-insensitive leaf-doc lookup plus the explicit
`lifecycleId` restamp worktree start applies across restarts). This is the work-content layer the observer projects as active
task documents, with lifecycle/enclosure bindings attached when available, so the dashboard can show
planned and running work from the same JSON source (slice 3c; closes note-03 gap #8).

## Hot Path Summary

The `task_doc` MCP tool authors documents: its controller
(`controllers/task_doc_tools.py`) loads or creates the JSON, applies one operation,
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
  `sections` (R4 — bespoke prose appended after the template), and an after-validator
  that keeps the three kinds disjoint (master ⇒ `subTasks` + structured `sections`, no
  `steps`/`codeExamples`/`codeExamplesNote`/`lifecycleId`; light/subTask ⇒ no `subTasks` + freeform-only
  `sections` (R4), and no `codeExamplesNote` alongside non-empty `codeExamples`). A persisted/served
  contract, **not** an MCP response model (peer of `observer.projection`). Leaf docs can name their root
  `seriesContractPath` and one or more `enclosures[]` leaf enclosure contracts.
- `render.py` — `render_markdown(doc)`: the only writer of the rendered markdown.
  Section helpers assemble lines from the model (mirroring
  `worktrees.worktree_contract.contract_to_text`); output is deterministic. A step renders a `### {id} — {title}`
  heading + a `- [ ] {outcome or title}` checkbox carrying the distinct `Step.outcome` (R2; a bare step with no
  outcome and no substeps is heading-only). An empty Proposed Code Examples section renders
  `codeExamplesNote` when set (a deferred slice) instead of the default "no code examples are
  needed" placeholder (R3). The header carries an optional `statusNote` suffix + the `headerNotes` lines,
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
  `subTasks` + `decisions`, so the round-trip is lossless. Live adoption of the format
  follows the runtime shipping `task_doc`; the documents themselves stay hand-authored
  markdown until then.
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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The `task_doc` controller authors documents through this package. | [task_doc_tools.py](agents-remember/mcp/src/agents_remember/controllers/task_doc_tools.py) |
| Leaf writes keep same-root master rows synchronized through the dedicated planner. | [master_sync.py](agents-remember/mcp/src/agents_remember/tasks/master_sync.py) |
| The render-back precedent: the worktree contract regenerates its markdown from its model. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The persisted-contract peer this schema mirrors. | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |

## Update History

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
