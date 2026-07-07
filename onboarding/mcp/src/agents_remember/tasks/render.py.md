# mcp/src/agents_remember/tasks/render.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/render.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T23:57:48+02:00                     |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063` |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
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
commanded master names in backticks when `doc.orchestrates` is non-empty (L14; master-only by
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

Output is **deterministic** by construction: section bodies carry no leading/trailing
blank lines and join their blocks with single blanks, so there is no global
blank-line normalization that would corrupt blank lines inside code fences.

### Invariants And Boundaries

- The single writer of the rendered markdown; nothing parses markdown back.
- Determinism is a contract (golden + round-trip tests depend on byte-stability);
  preserve the no-global-normalization approach so code-fence content survives.
- Follows the `w-02` `template.md` section order; that template is the render spec.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The model it renders. | [document.py](agents-remember/mcp/src/agents_remember/tasks/document.py) |
| The render-back precedent (model → markdown section helpers). | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |

## Update History

- 2026-07-06T23:57:48+02:00 — 260703-L14 (visual hierarchy + chat grouping): `_header_lines` renders
  `**Orchestrates:** \`name\`, …` after the `**Master:**` line when `doc.orchestrates` is non-empty
  — the orchestration-command relation surfaces in the rendered markdown; absent field ⇒ no line,
  existing renders byte-identical. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-06-19T06:03 — Slice 3c reopened (R4, leaf-doc fidelity): `_header_lines` now appends a `statusNote` suffix on `**Status:**` + the `headerNotes` lines, and leaf `render_markdown` appends freeform `sections` after References. Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T05:15 — Slice 3c reopened (R3, deferred-examples honesty): `_code_example_lines` gained a `note` parameter — for an empty `codeExamples` it renders `doc.codeExamplesNote` when set (e.g. "Drafted at the plan gate.") instead of the "no code examples are needed" default; `render_markdown` passes `doc.codeExamplesNote` through. Verification metadata pinned until closeout stamps the R3 code commit.
- 2026-06-19T04:18 — Slice 3c reopened (R2, heading-vs-outcome): `_step_lines` now puts the distinct `Step.outcome` on the checkbox line (`- [x] {outcome or title}`) and drops the line for a bare step (no outcome, no substeps) — the heading is the step, no redundant title echo. Verification metadata pinned until closeout stamps the R2 code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: added the `_render_master` path (ordered `sections` walk — `freeform` verbatim, `subTasks`/`sharedDecisions` generated; `_MARKER` status→emoji), dispatched from `render_markdown` on `kind == "master"`. The light/subTask renderer is unchanged. Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1: the deterministic `TaskDocument` → markdown renderer. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
