# mcp/src/agents_remember/tasks/document.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/document.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-20T21:30+02:00                        |
| lastVerifiedCommitHash | `de3a0fd9204f2e64755032274fb4e741bfddf6df` |
| lastVerifiedCommitDate | 2026-08-20T21:16:45+02:00|
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

Since 260815-DAG-L14 the sprint document also carries first-class `seats` (`SprintSeat`:
role/label/identity/state — the manager-seat precedent on master docs, so seat task documents leave
the sprint task index while existing ones stay on disk as historical records) and a `subTasks` row
may carry a typed `masterRef` (`TaskDocumentRef` — the exact commanded master document it tracks,
rendered as a real markdown link). Both are sprint-only by validator
(`_check_sprint_rows_and_seats`): a `masterRef` row or non-empty `seats` requires `kind == "master"`
with non-empty `orchestrates`; seat roles are unique among planned/active seats (a retired → active
succession of the same role is the only reading consistent with a `state` field). The role
altitudes are declared here once — `SPRINT_ROLES` (architect/orchestrator/strategist/designer/
system-specialist), `MASTER_ROLES` (manager), `LEAF_ROLES` (worker/reviewer/curator) — and
`document_refs` re-exports them (importing from `document_refs` would cycle).

Execution topology is explicit and separate from containment. A commanded master declares the
closed `executionNature` value `organizational` or `atomic`; an orchestration sprint instead owns a
`SprintExecutionGraph` of `SprintExecutionNode` nodes and reasoned predecessor/successor edges.
Since 260815-DAG-L11 a node is either a `master` lump (the whole master) or a `segment` (one master
ref plus a non-empty, unique `leafIds` list); a legacy bare `{repository, path}` node lifts to a
lump on parse and serializes back to the bare shape, so lump-only graphs round-trip
byte-identically, and a lump compares equal to (and hashes like) its bare ref. Edges
(`SprintExecutionEdge`) gain an optional `judgmentId`, and each endpoint is a bare ref or a
`SprintExecutionEndpoint` (`ref` + `leafId`) addressing the segment that contains that leaf;
resolution to exactly one node happens in graph validation, never at parse time. The graph rejects
duplicate nodes/edges, self edges, undeclared or ambiguous endpoints, blank reasons/judgment ids,
and cycles; it enforces sprint-wide leaf-ownership uniqueness plus lump/segment mutual exclusion
per master, then derives deterministic topological waves over nodes without persisting positions.
Since 260815-DAG-L15 the acyclicity refusal names the exact cycle members
(`execution-graph must be acyclic; cycle members: A -> B`) — `derived_waves` leaves the residual
(cycle members plus nodes downstream of a cycle) to `_find_cycle_members`, which extracts one
deterministic cycle via the shared `_CycleSearch` DFS (`_residual_adjacency` + `_dfs_cycle_members`,
split under the complexity target), so the error carries the cycle instead of a bare refusal
(playthrough F4).
Legacy absence remains parseable only for the finite migration path; no validator infers a default.

`derived_leaf_placement` maps one master's planned leaf ids onto its authored segments and derives
a pure, never-persisted placement for unplaced leafs — a master's leaf set that grew after graph
authoring — into the master's latest unblocked segment (latest by derived wave, then declaration
order; `derived_all_blocked` flags the all-segments-blocked fallback). `leaf_placement_facts`
shapes unknown/unplaced placements as reported facts (never silent, never auto-written), and
`numbering_drift_hints` reports leaf-numbering inversions across derived waves as facts that never
refuse.

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
- **Acyclicity refusals name the cycle (L15):** `derived_waves` raises with the exact cycle members,
  never a bare "must be acyclic" — the member search is deterministic (declaration-order DFS).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The renderer consumes this model. | `render_markdown` | mcp/src/agents_remember/tasks/render.py:31-53 |
| The store reads/writes this model. | `read_task_doc`; `write_task_doc` | mcp/src/agents_remember/tasks/store.py:32-33; mcp/src/agents_remember/tasks/store.py:36-37 |
| The persisted-contract peer this mirrors. | `TaskDocNode` | mcp/src/agents_remember/observer/projection.py:739-812 |
| Acyclicity errors name the exact cycle members via the deterministic DFS helpers (L15-R8 F4). | `_find_cycle_members`; `_residual_adjacency`; `_dfs_cycle_members`; `_CycleSearch` | mcp/src/agents_remember/tasks/document.py:418-441; mcp/src/agents_remember/tasks/document.py:443-457; mcp/src/agents_remember/tasks/document.py:459-480; mcp/src/agents_remember/tasks/document.py:482-489 |

## L23 Final Candidate Disposition

Task-document readers derive canonical sprint, master, and leaf containment used by source-lineage
and route-review authority. Those document relationships, not branch names or runtime ids supplied by
an agent, select the task boundary.

## 260815-DAG-L15 Named Cycle Refusals

The playthrough F4 finding ("cycle errors never name the cycle members") is fixed in the graph model:
`SprintExecutionGraph.derived_waves` now raises `execution-graph must be acyclic; cycle members: A -> B`
using `_find_cycle_members` (Kahn residual → deterministic DFS slice between the repeated node), with
the traversal split into `_residual_adjacency` + `_dfs_cycle_members` + the `_CycleSearch` dataclass to
stay under the complexity target. The refusal dialect stays a `ValueError`-family shape that the
application boundary translates to the typed `TaskDocError` family.

## Update History

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: `derived_waves` acyclicity refusals now name the exact
  cycle members (`_find_cycle_members`/`_residual_adjacency`/`_dfs_cycle_members`/`_CycleSearch`,
  playthrough F4). Verified at code commit de3a0fd9.

- 2026-08-20T04:14+02:00 — 260815-DAG-L14: `TaskDocument` gained first-class sprint `seats`
  (`SprintSeat` — role/label/identity/state, sprint-only, unique among non-retired roles) and
  `SubTaskRef` gained the optional typed `masterRef` (the commanded master document a row tracks).
  `SPRINT_ROLES`/`MASTER_ROLES`/`LEAF_ROLES` moved here as the canonical altitude declaration.
  Verified at code commit 2f494982.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: the sprint graph model is now leaf-segmented —
  `SprintExecutionNode` lumps or per-master segments with legacy bare-ref lifting and byte-identical
  lump re-serialization, judgment-provenanced edges with segment-sampling endpoints, sprint-wide
  leaf uniqueness and lump/segment mutual exclusion, node-derived waves, and the pure
  `derived_leaf_placement` / `leaf_placement_facts` / `numbering_drift_hints` fact helpers.
  Verification remains closeout-owned.

- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: the JSON-primary task schema now distinguishes
  commanded-master execution nature from sprint-only reasoned AON graphs, derives stable waves, and
  rejects duplicate, unknown, self-referential, blank-reason, cyclic, or wrong-kind shapes.
- 2026-08-14T06:34+02:00 — L23 final candidate review: task-document parsing derives canonical
  parent series/master/leaf relationships used by transitive lineage and route-review authority.
  Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

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
