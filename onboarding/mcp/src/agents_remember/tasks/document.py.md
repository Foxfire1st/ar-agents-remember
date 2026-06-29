# mcp/src/agents_remember/tasks/document.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/document.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-29T21:24+02:00                     |
| lastVerifiedCommitHash | `026b2468a8d456e35a4f80a86e66a574b1e81f4b` |
| lastVerifiedCommitDate | 2026-06-30T00:57:11+02:00|
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
retained only so any legacy `light` document still loads; the `task_doc` controller no longer authors
new ones (every task is master/leaf). `DocStatus` stays in the `w-02-light-task-workflow` template vocabulary
(`planning`|`inProgress`|`Completed`) so the rendered `**Status:**` line is always
valid; `StepStatus` is a 4-state (`pending`|`inProgress`|`blocked`|`done`) carrying the
dashboard's granularity. `seriesContractPath` names the root task series contract when one exists, and
`enclosures[]` names leaf enclosure contracts (`leafId` + `enclosurePath`) that can bind the doc to a
lifecycle through observer projection. A `master` carries the series index — `subTasks` (`SubTaskRef`:
number/name/file/status/scope) — and an ordered `sections` render plan (`Section`:
`freeform`|`subTasks`|`sharedDecisions` + heading + body); a `@model_validator(mode="after")`
keeps the kinds disjoint (master forbids `steps`/`codeExamples`/`codeExamplesNote`/`lifecycleId`;
`light`/`subTask` forbid `subTasks` and non-freeform `sections` but may carry freeform `sections`
(R4), and forbid `codeExamplesNote` alongside non-empty `codeExamples`).

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
  deserialize, but `task_doc` create/replace refuse to author it (`controllers/task_doc_tools.py`) — new
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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The renderer consumes this model. | [render.py](agents-remember/mcp/src/agents_remember/tasks/render.py) |
| The store reads/writes this model. | [store.py](agents-remember/mcp/src/agents_remember/tasks/store.py) |
| The persisted-contract peer this mirrors. | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |

## Update History

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
