# mcp/src/agents_remember/tasks/render.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/render.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00|
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

Since 260831-CCR (commit `99dc249b`) the renderer renders the typed intent slot forms:
`_requirement_lines` (line 399) renders an `ApprovedRequirementPacketRef` as
`- `{stableId}@{version}` — `{path}`` instead of a raw repr; `_question_lines` (line 409) renders an
`AcceptanceObligationQuestion` as `- **Acceptance obligation `{id}`:** {question}`; and the Route
Review section (`_route_review_lines`, line 492) emits a `**Task intent:** `{schema}:{digest}``
line under the candidate tree when the review carries a `TaskIntentIdentity` (line 500-501),
pinned to the new normative intent identity.

A `master` (`doc.kind == "master"`) dispatches to `_render_master`: the header block,
then an ordered walk of `doc.sections`. A `freeform` section renders `## {heading}` +
its `body` verbatim; a `subTasks` / `sharedDecisions` section renders the generated
block (the `subTasks` index list — `_MARKER` maps `DocStatus` to check/emoji — or the
`decisions` table) after an optional `body` intro. The `light`/`subTask` path is
unchanged.

Since 260815-DAG-L14 the master renderer also emits real sprint structure: a typed `masterRef`
row renders as a relative markdown link to the commanded master document (`_master_ref_link` —
`../<folder>/task.md` under `tasks/<repo>/`), while a row without one keeps the plain bold name +
file code span; a sprint with `orchestrates` + rows but no `subTasks` section still gets its
`## Master Index` section rendered (the durable markdown must show the sprint to master list); and
the header block gains a `**Seats:**` banner (`_seat_lines`) — one line per first-class `SprintSeat`
(role, state, optional label/identity) when `doc.seats` is non-empty.

Execution topology renders without scheduler interpretation: a commanded master's closed nature
appears in its header, while a sprint's `Execution Graph` section lists canonical nodes, every
reasoned dependency edge, and the deterministic waves derived from that graph. Since
260815-DAG-L11 the node/edge/wave labels go through `_graph_node_label` over
`SprintExecutionNode`: a segment node renders as ```master.key` (leafs: `L1`, `L2`)`` with its
leaf list as the qualifier, and edge endpoints resolve through `graph.resolve_endpoint` before
labeling. DAGQC L1 separates private diagram identity from user-authored labels: `_mermaid_leaf_ids`
allocates `n<node ordinal>_l<leaf ordinal>` once from the canonical graph declaration order, and
both leaf declarations and edge endpoints consume that same allocation. Leaf titles are resolved
only through `(segment.ref, leaf id)`. No positional or priority field is introduced by the
renderer, and no lossy punctuation sanitizer remains.

Output is **deterministic** by construction: section bodies carry no leading/trailing
blank lines and join their blocks with single blanks, so there is no global
blank-line normalization that would corrupt blank lines inside code fences.

### Conventions

Private Mermaid ids are deterministic implementation details for one unchanged canonical graph.
Human task ids and titles stay escaped labels; no caller should treat an ordinal diagram id as
durable task identity.

### Invariants And Boundaries

- The single writer of the rendered markdown; nothing parses markdown back.
- Determinism is a contract (golden + round-trip tests depend on byte-stability);
  preserve the no-global-normalization approach so code-fence content survives.
- Follows the `w-02` `template.md` section order; that template is the render spec.
- A single ordinal allocation table serves declarations and edge endpoints. Do not reintroduce a
  sanitizer, a collision suffix branch, or a second endpoint-id authority.
- Typed intent slots render as stable strings; decision prose and generic questions stay literal.

### Todos

None.

## Docs References

No Domain Documentation sources are configured for this repository-internal renderer.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation was available after checking the configured source registry. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The renderer allocates private leaf ids once and supplies the same map to declarations and edges. | `_execution_graph_lines` | mcp/src/agents_remember/tasks/render.py:204-245 |
| Declarations use qualified title identity and edge endpoints reuse the ordinal allocation. | `_mermaid_node_lines`; `_mermaid_segment_lines`; `_mermaid_edge_lines`; `_mermaid_endpoint_id` | mcp/src/agents_remember/tasks/render.py:310-328; mcp/src/agents_remember/tasks/render.py:331-345; mcp/src/agents_remember/tasks/render.py:348-363; mcp/src/agents_remember/tasks/render.py:366-382 |
| The graph node model provides structural keys for the allocation. | `SprintExecutionNode` | mcp/src/agents_remember/tasks/document.py:218-273 |
| The typed requirement/question renderers and the review task-intent line. | `_requirement_lines`; `_question_lines`; `_route_review_lines` | mcp/src/agents_remember/tasks/render.py:399-407; mcp/src/agents_remember/tasks/render.py:409-417; mcp/src/agents_remember/tasks/render.py:492-512 |


## 260815-DAG-L12 Mermaid Document Diagram

The `## Execution Graph` section leads with a deterministic fenced mermaid `flowchart TD` diagram
(L12-R1): one subgraph per master box, one node per leaf, atomic masters as single lump nodes, and
labeled edges. DAGQC L1 makes the private leaf ids injective by deriving them from node/leaf
ordinals; declarations and endpoints share one precomputed map, while the visible label retains the
original leaf id and the master-qualified title. Labels remain whitespace-collapsed, truncated, and
pipe/quote-escaped. The compact machine-readable Nodes / Dependencies / Derived Waves lists stay
alongside the diagram.


## CCR-R02@v2 Intent Rendering

The renderer now surfaces the canonical `task-intent/v1` identity in the Route Review section
and renders typed approved-packet refs / acceptance obligations in their sections
(`requirements/CCR-R02-v2-normative-task-intent-identity.md`). Rendering remains deterministic
and one-way; markdown never becomes authority.

## Update History

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the task-document renderer now renders `ApprovedRequirementPacketRef` and
  `AcceptanceObligationQuestion` lines and emits the `**Task intent:**` identity line in the
  Route Review section when present. Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-24T13:43+02:00 — DAGQC L1: replaced lossy user-id sanitization with one canonical
  node/leaf-ordinal Mermaid-id allocation shared by declarations and endpoints; leaf labels now
  consume master-qualified titles. Verification metadata remains pinned until closeout.

- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   `render_markdown(doc, *, graph_titles=...)` and `_render_master` now accept the joined `SprintGraphTitles`; `_execution_graph_lines` emits the mermaid flowchart-TD block before the machine lists (L12-R1). Verified at code commit b7f2c8e2.

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
  `**Orchestrates:** `name`, …` after the `**Master:**` line when `doc.orchestrates` is non-empty
  — the orchestration-command relation surfaces in the rendered markdown; absent field = no line,
  existing renders byte-identical. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-06-19T06:03 — Slice 3c reopened (R4, leaf-doc fidelity): `_header_lines` now appends a `statusNote` suffix on `**Status:**` + the `headerNotes` lines, and leaf `render_markdown` appends freeform `sections` after References. Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T05:15 — Slice 3c reopened (R3, deferred-examples honesty): `_code_example_lines` gained a `note` parameter — for an empty `codeExamples` it renders `doc.codeExamplesNote` when set (e.g. "Drafted at the plan gate.") instead of the "no code examples are needed" default; `render_markdown` passes `doc.codeExamplesNote` through. Verification metadata pinned until closeout stamps the R3 code commit.
- 2026-06-19T04:18 — Slice 3c reopened (R2, heading-vs-outcome): `_step_lines` now puts the distinct `Step.outcome` on the checkbox line (`- [x] {outcome or title}`) and drops the line for a bare step (no outcome, no substeps) — the heading is the step, no redundant title echo. Verification metadata pinned until closeout stamps the R2 code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: added the `_render_master` path (ordered `sections` walk — `freeform` verbatim, `subTasks`/`sharedDecisions` generated; `_MARKER` status to emoji), dispatched from `render_markdown` on `kind == "master"`. The light/subTask renderer is unchanged. Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1: the deterministic `TaskDocument` to markdown renderer. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
