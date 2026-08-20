# mcp/src/agents_remember/tasks/render.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/render.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-20T04:12+02:00                     |
| lastVerifiedCommitHash | `2f494982971091a18023a0ecdb2a532a4201a7c5` |
| lastVerifiedCommitDate | 2026-08-20T00:11:16+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Render a `TaskDocument` to its `task.md` markdown form. This is the **only** writer of
the rendered markdown; the JSON document is the source of truth.

## Code Commentary

### Logic

`render_markdown(doc)` assembles the document section by section, mirroring
`worktrees.worktree_contract.contract_to_text`: a header block (Status/Repo/Type/
Created, plus a `**Master:**` line for a sub-task, an `**Orchestrates:**` line listing the
commanded master names in backticks when `doc.orchestrates` is non-empty (master-only by
schema), an optional `statusNote` suffix on the
`**Status:**` line, and `headerNotes` as extra `**Key:** value` lines — R4), then one `_section()` per
`w-02-light-task-workflow` `template.md` heading (Objective, Requirements, Design,
Implementation Steps, Proposed Code Examples, Decision Log, Open Questions,
References). `subTask` docs get a `(Sub-task <id>)` title suffix. A step renders as a `### {id} — {title}` heading;
the checkbox line carries the distinct `outcome` (`- [{x}] {outcome or title}`, R2) with two-space-indented
substeps, and a **bare** step (no `outcome`, no substeps) is just its heading — no redundant title echo.
Decisions render as a markdown table with `_cell()` escaping pipes/newlines; empty sections emit explicit
placeholders. For an empty "Proposed Code Examples" section, `_code_example_lines` renders the doc's
`codeExamplesNote` when set (e.g. "Drafted at the plan gate.") instead of the default
"No code examples are needed for this task." — so a deferred slice is distinguishable from one that
genuinely needs none (R3). A leaf doc may also carry freeform `sections`, rendered after References as
bespoke-prose extras (R4 — the master-only field, now legal on a leaf, `freeform` kind only).

A `master` (`doc.kind == "master"`) dispatches to `_render_master`: the header block,
then an ordered walk of `doc.sections`. A `freeform` section renders `## {heading}` +
its `body` verbatim; a `subTasks` / `sharedDecisions` section renders the generated
block (the `subTasks` index list — `_MARKER` maps `DocStatus` → ✅/🔨/⬜ — or the
`decisions` table) after an optional `body` intro. The `light`/`subTask` path is
unchanged.

Since 260815-DAG-L14 the master renderer also emits real sprint structure: a typed `masterRef`
row renders as a relative markdown link to the commanded master document (`_master_ref_link` —
`../<folder>/task.md` under `tasks/<repo>/`), while a row without one keeps the plain bold name +
file code span; a sprint with `orchestrates` + rows but no `subTasks` section still gets its
`## Master Index` section rendered (the durable markdown must show the sprint → master list); and
the header block gains a `**Seats:**` banner (`_seat_lines`) — one line per first-class `SprintSeat`
(role, state, optional label/identity) when `doc.seats` is non-empty.

Execution topology renders without scheduler interpretation: a commanded master's closed nature
appears in its header, while a sprint's `Execution Graph` section lists canonical nodes, every
reasoned dependency edge, and the deterministic waves derived from that graph. Since
260815-DAG-L11 the node/edge/wave labels go through `_graph_node_label` over
`SprintExecutionNode`: a segment node renders as `` `master.key` (leafs: `L1`, `L2`) `` with its
leaf list as the qualifier, and edge endpoints resolve through `graph.resolve_endpoint` before
labeling. No positional or priority field is introduced by the renderer.

Output is **deterministic** by construction: section bodies carry no leading/trailing
blank lines and join their blocks with single blanks, so there is no global
blank-line normalization that would corrupt blank lines inside code fences.

### Invariants And Boundaries

- The single writer of the rendered markdown; nothing parses markdown back.
- Determinism is a contract (golden + round-trip tests depend on byte-stability);
  preserve the no-global-normalization approach so code-fence content survives.
- Follows the `w-02` `template.md` section order; that template is the render spec.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The model it renders. | `TaskDocument` | mcp/src/agents_remember/tasks/document.py:602-716 |
| The render-back precedent (model → markdown section helpers). | `contract_to_text` | mcp/src/agents_remember/worktrees/worktree_contract.py:689-740 |

## Update History

- 2026-08-20T04:12+02:00 — 260815-DAG-L14: the master renderer now emits typed `masterRef` rows as
  real relative links to commanded master documents, renders the generated `## Master Index`
  section for sprints with `orchestrates` + rows but no `subTasks` section, and renders the
  `**Seats:**` header block for first-class sprint seats. Verified at code commit 2f494982.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: the execution-graph section renders `SprintExecutionNode`
  labels via `_graph_node_label` (segments carry their leaf list; edge endpoints resolve through the
  graph first); render stays free of scheduler interpretation. Verification remains closeout-owned.

- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: deterministic master Markdown now renders execution
  nature in the header and sprint graph nodes, justified dependencies, and derived waves as a section.
- 2026-08-14T06:34+02:00 — L23 final candidate review: rendered task documents project the
  canonical relationships and operation/review evidence without leaking private runtime identity.
  Verification remains closeout-owned.

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 4 initial citation findings (2 anchor, 0 prose, 2 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/tasks/render.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change whatsoever. Checked
  by parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-07-06T23:57:48+02:00 — 260703-L14 (visual hierarchy + chat grouping): `_header_lines` renders
  `**Orchestrates:** \`name\`, …` after the `**Master:**` line when `doc.orchestrates` is non-empty
  — the orchestration-command relation surfaces in the rendered markdown; absent field ⇒ no line,
  existing renders byte-identical. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-06-19T06:03 — Slice 3c reopened (R4, leaf-doc fidelity): `_header_lines` now appends a `statusNote` suffix on `**Status:**` + the `headerNotes` lines, and leaf `render_markdown` appends freeform `sections` after References. Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T05:15 — Slice 3c reopened (R3, deferred-examples honesty): `_code_example_lines` gained a `note` parameter — for an empty `codeExamples` it renders `doc.codeExamplesNote` when set (e.g. "Drafted at the plan gate.") instead of the "no code examples are needed" default; `render_markdown` passes `doc.codeExamplesNote` through. Verification metadata pinned until closeout stamps the R3 code commit.
- 2026-06-19T04:18 — Slice 3c reopened (R2, heading-vs-outcome): `_step_lines` now puts the distinct `Step.outcome` on the checkbox line (`- [x] {outcome or title}`) and drops the line for a bare step (no outcome, no substeps) — the heading is the step, no redundant title echo. Verification metadata pinned until closeout stamps the R2 code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: added the `_render_master` path (ordered `sections` walk — `freeform` verbatim, `subTasks`/`sharedDecisions` generated; `_MARKER` status→emoji), dispatched from `render_markdown` on `kind == "master"`. The light/subTask renderer is unchanged. Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1: the deterministic `TaskDocument` → markdown renderer. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
