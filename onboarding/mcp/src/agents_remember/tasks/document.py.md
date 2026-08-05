# mcp/src/agents_remember/tasks/document.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/document.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                        |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

The `ar-task-document/v1` schema: the persisted, JSON-primary source of truth for a
task's plan and progress. `task.md` is a render of it; the JSON is never produced by
parsing markdown back.

## Code Commentary

### Logic

`TaskDocument` (and the nested `Step`/`SubStep`/`Decision`/`CodeExample`, plus
`TaskEnclosureRef`, `SubTaskRef`, and `Section`) extend `_Doc`, a `BaseModel` with
`extra="forbid", populate_by_name=True` — unknown keys are a schema error and field
name or alias both validate. The `schema_` field defaults to `TASK_DOCUMENT_SCHEMA`
and serializes under the `schema` alias. `DocKind` is `light`|`subTask`|`master` — `light` is
retained only so any legacy `light` document still loads; the `task_doc` application entry point no longer authors
new ones (every task is master/leaf). `DocStatus` stays in the `w-02-light-task-workflow` template vocabulary
(`planning`|`inProgress`|`Completed`) so the rendered `**Status:**` line is always
valid; `StepStatus` is a 4-state (`pending`|`inProgress`|`blocked`|`done`) carrying the
dashboard's granularity. `seriesContractPath` names the root task series contract when one exists, and
`enclosures[]` names leaf enclosure contracts (`leafId` + `enclosurePath`) that can bind the doc to a
lifecycle through observer projection. A `master` carries the series index — `subTasks` (`SubTaskRef`:
number/name/file/status/scope) — and an ordered `sections` render plan (`Section`:
`freeform`|`subTasks`|`sharedDecisions` + heading + body); a `@model_validator(mode="after")`
keeps the kinds disjoint (master forbids `steps`/`codeExamples`/`codeExamplesNote`/`lifecycleId`;
`light`/`subTask` forbid `subTasks`, `orchestrates`, and non-freeform `sections` but may carry
freeform `sections` (R4), and forbid `codeExamplesNote` alongside non-empty `codeExamples`).

A master may also carry `orchestrates: list[str]` (L14, the orchestration-command relation): a
master doc with a non-empty list **is** an orchestration task, and each entry names a master task
it commands (its task folder, doc id, or title — the dashboard matches forgivingly). Additive by
design — `default_factory=list`, no new `DocKind`, no migration; docs without the field validate
and serialize exactly as before, and masters named nowhere stay top-level.

`step_total`/`step_done` count the progress-bearing leaves (`_leaf_statuses`: a step's
substeps when it has any, else the step itself), and `current_step` returns the first
in-progress/blocked step, else the first unfinished one, else `None`.

`series_total`/`series_done` (R1) are the master analog: a master's checkboxes are its
`subTasks` (each subtask is one box), so `series_total` = `len(subTasks)` and `series_done` counts
subtasks whose **declared** status is `Completed`. The declared subtask status is the lever and is
authoritative — a slice marked `Completed` in the master counts done even if its own leaf doc still has
open boxes; series progress is never derived from a slice's internal steps.

A `Step` also carries an optional `outcome` (R2): the checkbox-line deliverable, distinct from the heading
`title`. It is `None`-defaulted so `exclude_none` keeps existing step JSON byte-identical; the renderer puts
`outcome` on the `- [ ]` line (a bare step with neither `outcome` nor substeps renders as just its heading).

A leaf doc also carries an optional `codeExamplesNote` (R3): a free string explaining why `codeExamples`
is empty (e.g. "Drafted at the plan gate."), so a deferred planning slice reads as *deferred* rather than
as if no examples are needed. It is `None`-defaulted (`exclude_none` keeps existing JSON byte-identical);
the kind guard forbids it on a master and forbids pairing it with non-empty `codeExamples`.

For lossless round-trip of our real hand files (R4), a leaf doc also carries: a descriptive `statusNote`
(rendered as a suffix beside the strict status enum — the enum stays the dashboard lever), `headerNotes`
(a `HeaderNote` list → extra `**Key:** value` header lines such as Verified/Source), and freeform
`sections` (the master-only field, now legal on a leaf, `freeform` kind only — rendered after References as
the escape hatch for bespoke prose; the standard template sections stay the backbone).

### Invariants And Boundaries

- Persisted/served contract, **not** an MCP response model (peer of
  `observer.projection`); it round-trips, so changes must stay backward-readable.
- The markdown checkbox is binary; the richer `StepStatus` lives only in the JSON.
- `schema_` must serialize as `schema` (alias) — always dump `by_alias=True`.
- **`light` is load-compatibility only:** the `DocKind` literal keeps `light` so legacy documents still
  deserialize, but `task_doc` create/replace refuse to author it (`application/task_doc_tools.py`) — new
  tasks are `master` or `subTask` (leaf).
- A master carries **no authored `lifecycleId`** (validator-enforced): it spans the series, not one
  leaf lifecycle. The observer still projects the master as an active task document with
  `lifecycleId=None` unless a root lifecycle is structurally attached.
- `seriesContractPath` and `enclosures[]` are linkage fields, not a second task schema; they let root
  series contracts and leaf enclosure contracts coexist under `ar-task-document/v1`.
- **Declared subtask status is authoritative (R1):** `series_done` reads the master's
  `subTasks[].status`, never a slice's leaf-step rollup — a subtask marked `Completed` is done in the
  series even with open internal boxes.
- **`codeExamplesNote` describes an absence (R3):** valid only on a leaf doc with empty `codeExamples`;
  the renderer shows it in place of the "no code examples" placeholder.
- **Leaf escape hatch (R4):** a leaf may carry freeform `sections` + `headerNotes` + a `statusNote`; the
  `subTasks` series index and non-freeform sections stay master-only, and `DocStatus` stays a strict enum
  (the `_MARKER`/observer lever — never loosened to a free string).
- **`orchestrates` is master-only (L14):** the validator rejects it on `light`/`subTask` docs
  ("a {kind} document has no orchestrates (master-only)") — an orchestration task is a `master`
  doc carrying the field, never a new kind; insignia/hierarchy consumers (observer projection →
  dashboard) treat an empty list as "not an orchestration task".

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The renderer consumes this model. | `render_markdown` | mcp/src/agents_remember/tasks/render.py:28-48 |
| The store reads/writes this model. | `read_task_doc`; `write_task_doc` | mcp/src/agents_remember/tasks/store.py:32-33; mcp/src/agents_remember/tasks/store.py:36-37 |
| The persisted-contract peer this mirrors. | `TaskDocNode` | mcp/src/agents_remember/observer/projection.py:608-654 |

## Update History

- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired the scoped task-document citation claims; final exact frozen-snapshot check is clean.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-06T23:57:42+02:00 — 260703-L14 (visual hierarchy + chat grouping): `TaskDocument` gained
  `orchestrates: list[str]` (default `[]`) — the orchestration-command relation; a master doc with a
  non-empty list IS an orchestration task naming the masters it commands. The kind validator now
  rejects the field on non-master docs (master-only, like `subTasks`). Additive: no new kind, no
  migration, docs without the field are byte-identical.
  Verification metadata pinned until closeout stamps the L14 commit.
- 2026-06-29T21:24+02:00 — Post-landing cleanup (master/leaf-only): clarified that `light` survives in
  `DocKind` for legacy-load compatibility only — the `task_doc` controller refuses to author new `light`
  documents, so every task is `master` or `subTask` (leaf). Schema unchanged (a code comment documents the
  retention). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:39+02:00 — Task 17 schema-side clarification: master docs still forbid authored
  `lifecycleId`, but that is no longer treated as a projection exclusion; the observer projects active
  master docs with optional runtime lifecycle attachment. Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: `TaskDocument` replaced `contractPath` with `seriesContractPath` plus `enclosures: list[TaskEnclosureRef]`, allowing one task document to refer to its root series contract and one or more leaf enclosure contracts. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:03 — Slice 3c reopened (R4, leaf-doc fidelity): added `HeaderNote` + optional `statusNote`/`headerNotes`, and relaxed the kind-guard so a leaf may carry freeform `sections` (still forbids the `subTasks` series index + non-freeform sections); `DocStatus` stays a strict enum. Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T05:15 — Slice 3c reopened (R3, deferred-examples honesty): added optional leaf-only `codeExamplesNote` (`None`-defaulted so `exclude_none` keeps existing JSON byte-identical) and extended the kind-guard `@model_validator` — a master forbids it, and a leaf forbids it alongside non-empty `codeExamples`. Verification metadata pinned until closeout stamps the R3 code commit.
- 2026-06-19T04:18 — Slice 3c reopened (R2, heading-vs-outcome): `Step` gained an optional `outcome` (the checkbox-line deliverable, distinct from the heading `title`; `None`-defaulted so `exclude_none` keeps existing JSON byte-identical). The renderer puts it on the `- [ ]` line. Verification metadata pinned until closeout stamps the R2 code commit.
- 2026-06-19T03:17 — Slice 3c reopened (R1, masters observable): added `series_total`/`series_done` — the master analog of `step_total`/`step_done`. A master's checkboxes are its `subTasks` (each one box); `series_done` counts the **declared** `Completed` subtasks, authoritative over a slice's own leaf steps. Verification metadata pinned until closeout stamps the R1 code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: added `kind:"master"` with `SubTaskRef` (series index) + ordered `Section` (`freeform`/`subTasks`/`sharedDecisions`) and a kind-guard `@model_validator` (master ⇒ no steps/codeExamples/lifecycleId; light/subTask ⇒ no subTasks/sections). Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1: the `ar-task-document/v1` Pydantic schema + progress helpers. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
