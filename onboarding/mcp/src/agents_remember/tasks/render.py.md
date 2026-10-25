# mcp/src/agents_remember/tasks/render.py

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Render a `TaskDocument` to its `task.md` markdown form. This is the **only** writer of
the rendered markdown; the JSON document is the source of truth.

## Code Commentary

Leaf render prints state, decision and strict agreement fields; master order labels an open review, while older absent fields retain unchanged rendering.

### Logic

`render_markdown(doc)` assembles the document section by section, mirroring
`worktrees.worktree_contract.contract_to_text`: a header block (Status/Repo/Type/
Created, plus a `**Master:**` line for a sub-task, an `**Orchestrates:**` line listing the
commanded master names in backticks when `doc.orchestrates` is non-empty (master-only by
schema), a `**Knowledge maintenance scope:** \`true\`` line when `doc.knowledgeMaintenanceScope` is
true (MIK-R08), an `**Expected knowledge effects:**` block with one bullet per declaration (its subject, effect and
`requirementRef`) when `doc.expectedKnowledgeEffects` is set (MIK-R11), an optional
`statusNote` suffix on the
`**Status:**` line, and `headerNotes` as extra `**Key:** value` lines — R4), then one `_section()` per
`w-02-light-task-workflow` `template.md` heading (Objective, Requirements, Design,
Implementation Steps, Proposed Code Examples, Decision Log, Open Questions,
References). `subTask` docs get a `(Sub-task <id>)` title suffix. A step renders as a `### {id} — {title}` heading;
the checkbox line carries the distinct `outcome` (`- [{x}] {outcome or title}`, R2) with two-space-indented
substeps, and a **bare** step (no `outcome`, no substeps, and — since 260831-LOCR-L33 — no `note`) is
just its heading, so there is no redundant title echo. Since 260831-LOCR-L33 a top-level step's `note`
suffixes its checkbox line (`- [{x}] {outcome or title} — {note}`) exactly as a substep's does, AND
`step.note` joined the condition that draws that line at all: a step carrying only a note would
otherwise render as a bare heading and lose the note a second time, after it had already been lost in
the schema. The two halves of that fix belong together — persisting a field the renderer cannot show
still leaves it invisible to the human-facing view.
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

> **Retained historical source account — superseded by the current contract:**
> A `master` (`doc.kind == "master"`) dispatches to `_render_master`: the header block,
> then an ordered walk of `doc.sections`. A `freeform` section renders `## {heading}` +
> its `body` verbatim; a `subTasks` / `sharedDecisions` section renders the generated
> block (the `subTasks` index list — `_MARKER` maps `DocStatus` to check/emoji — or the
> `decisions` table) after an optional `body` intro. The `light`/`subTask` path is
> unchanged.

Current Markdown sequence for a master is header; the truthy fixed fields Objective, Non-goals, Requirements, Design and Acceptance in that order; persisted Execution Graph when present; Order when the supplied `master_order` is not None; authored sections in order; fallback Master Index when orchestrates/rows require it; discarded history. _master_fixed_prose_lines formats the fixed fields before authored sections and does not rewrite, deduplicate or migrate legacy freeform sections, so a legacy Objective section can coexist with the fixed Objective. Historically, the predecessor emitted only the fixed Non-goals/Acceptance fields here and did not automatically emit master Objective, Requirements or Design. The leaf sequence still places truthy Non-goals after Objective and truthy Acceptance after Design, retaining its existing later sections and bespoke extras. Nonempty raw waitsFor adds a header line in declared order; empty/None adds none. This is Markdown behavior, not the browser page skeleton.

Order is consumed, never read or derived here. It reports the number of Completed tasks and omits their rows, sorts remaining rows stably by wave, shows non-cycle inProgress as `in work`, adds the cycle annotation, and preserves gone/cycle/dependency facts supplied by the owner. When at least one cycle member is unfinished, it also emits `Legacy cycle members: ...` using the complete supplied cycle_ids, including Completed members; an entirely Completed cycle contributes to the Completed count but does not trigger that banner. The earlier renderer lacked that full-member banner; cycle identity itself is derived upstream.

Since 260815-DAG-L14 the master renderer also emits real sprint structure: a typed `masterRef`
row renders as a relative markdown link to the commanded master document (`_master_ref_link` —
`../<folder>/task.md` under `tasks/<repo>/`), while a row without one keeps the plain bold name +
file code span; a sprint with `orchestrates` + rows but no `subTasks` section still gets its
`## Master Index` section rendered (the durable markdown must show the sprint to master list); and
the header block gains a `**Seats:**` banner (`_seat_lines`) — one line per first-class `SprintSeat`
(role, state, optional label/identity) when `doc.seats` is non-empty. A row that carries a `retirement` proof
renders its scope text as the row's scope (when it has one) followed by "Retired <master key> at <time>: <reason>"
(`_subtask_lines`), so a sprint's markdown shows when and why a master was retired.

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
- Retains the fixed leaf-template backbone, with conditional Non-goals after Objective
  and Acceptance after Design; the master has its own header/prose/graph/Order/section
  sequence. Neither the browser skeleton nor authored freeform duplicates replace it.
- A single ordinal allocation table serves declarations and edge endpoints. Do not reintroduce a
  sanitizer, a collision suffix branch, or a second endpoint-id authority.
- Typed intent slots render as stable strings; decision prose and generic questions stay literal.
- **Every `DocStatus` needs a marker:** `_MARKER` is a direct lookup, not a defaulting one, so
  adding a status value without adding its marker raises at render time instead of silently
  rendering a wrong glyph. `abandoned` renders `⛔` alongside `Completed`/`inProgress`/`planning`.

### Todos

None.

## 260928-MIK-L08 The Maintenance-Scope Header Line


- The maintenance-scope header is drawn only for a truthy field; the current header also conditionally carries the raw waitsFor line.
## 260928-MIK-L11 The Expected-Knowledge-Effects Header Block

MIK-R11 adds a header block after the maintenance-scope line: when the leaf's document declares
`expectedKnowledgeEffects`, `_header_lines` appends `**Expected knowledge effects:**` and one bullet per
declaration, in declared order, naming its subject, effect and `requirementRef`. A document without the
field renders exactly as before (the worker's and reviewer's render hashes over every real task document are
byte-identical).


- Expected-knowledge-effects header bullets are drawn only when the declaration is truthy and retain declared order.
## External annotation input

render_markdown accepts optional externally supplied direct-grant evidence for the leaf header; it only formats describe(), never reads or writes the store. No grant argument gives the former rendering, and a master ignores the annotation. Determinism is over the document plus supplied graph/grant/master_order inputs, not the document alone. Authored JSON stays primary and there is no TaskDocument grant field.

The renderer accepts `master_order` alongside `graph_titles` and `direct_grant`. It uses Order only on the master path; a master ignores the leaf grant argument. Callers own Order derivation and any read cost; this formatting owner remains one-way.

## Evidence

### Docs References

No Domain Documentation sources are configured for this repository-internal renderer.

No relevant external documentation was available after checking the configured source registry.

### Repo-Internal References

- The step renderer suffixes a top-level note onto the checkbox line and draws that line when a note is the only reason to. [3]

- The renderer allocates private leaf ids once and supplies the same map to declarations and edges. [4]

- Declarations use qualified title identity and edge endpoints reuse the ordinal allocation. [5]
- The graph node model provides structural keys for the allocation. [6]

- The typed requirement/question renderers and the review task-intent line. [7]

- The status marker table is a direct lookup covering every `DocStatus`, including `abandoned`. [8]

- A retired master's row shows the retirement time and reason after its scope. [9]
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


- render_markdown formats external leaf-grant and supplied graph/master Order inputs; the master emits truthy fixed fields before preserved authored sections and renders full legacy-cycle identity when unfinished cycle work remains. It neither reads the grant store nor derives Order. [10]

- Leaf render prints state, decision and strict agreement fields; master order labels an open review, while older absent fields retain unchanged rendering. [11]
