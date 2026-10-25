# skills/w-02-light-task-workflow/SKILL.md

## Governing Overview

[agents-remember — Onboarding Overview](../../overview.md)

## Purpose

This skill describes thin durable task orchestration for medium-risk or multi-step work: a reviewable plan, distinct implementation examples, explicit approval and decision tracking, with a single-page implementation plan as a rule of thumb rather than a hard threshold. Non-code work and small isolated code changes can fit the model. Larger or broader work composes a master with flat light sub-task plans instead of resurrecting a separate heavy workflow. Its historical “light” vocabulary must be distinguished from current master/leaf task-authoring admission.

## Current Source Qualification

The skill's own reading list now carries the two procedures the retired skills left behind: `workflows/worktree-operations.md` (intake and intent, start/attach/status, mid-task sync, closeout, integration, finalization and cleanup, reopening) and `workflows/closeout.md` (approval authority, durable gates, closeout order, granted branch-direct landing, failure conditions and boundaries). Its text therefore names this skill where the inherited copy names a worktree-manager or closeout skill: a worktree exists only after this skill's own intent work, the commit/closeout preview and approval stop belong here, and drift is checked with `c-05-create-or-update-onboarding-files` rather than a separate memory-quality skill.

## Code Commentary

### Thin plans and current task admission

The inherited thin-document clarification rejects a doc-less “chat build”: even the smallest single-session build has a title and explicit steps so it remains durable and dashboard-legible. Thin and full documents differ in content completeness, not by permission to implement without an artifact. The source retains that explanation.

The source’s JSON-primary transition paragraph still says the tool manages `light`/`subTask` and that masters remain hand-authored until runtime shipment. The actual task-doc construction definition now refuses `kind:"light"`, requires `master` or `subTask`, and derives the default from a leaf contract (`subTask`) or otherwise `master`. That implementation bounds the older instruction: thin content does not restore a separate light authoring route, and the transitional wording is not a current claim that `task_doc` is unshipped.

### Artifact, approval and execution

The source keeps one wrapper under the resolved task root with a durable `task.md`, created as soon as task class, naming and workflow variables are clear, before a worktree. Ticket-linked naming is `YYMMDD_#<number>_<short-slug>/task.md`; organic naming is `YYMMDD_<descriptive-slug>/task.md`. Task-local timestamps use `YYYY-MM-DDTHH:MM`. The template supplies objective, requirements, design where warranted, steps, code examples, decisions, questions and references. Checkboxes are the living implementation record; code-changing plans include examples for each distinct change type.

The agent searches for an existing active task of the same scope, aligns requirements and decisions with approved intent, checks onboarding drift before planning against it, stops for implementation approval, and then treats code, onboarding propagation and resolved tool checks as one implementation cycle. Worktree-backed closeout requires a separate explicit commit approval after preview. After landing, source guidance requires all declared parent/nested steps done, explicit standalone cleanup when that is the final step, and `lifecycle_finalize_task` to prove the edge, recognize/run cleanup and set the exact leaf and immediate parent row to Completed. Closeout itself is not completion.

The old commentary’s “one task / one workflow / one worktree, commit per slice, single integration/finalization/release” account is historical and superseded in its worktree/integration shape. The canonical skill and companion series scaffold instead use one master integration branch with one enclosure worktree per active leaf, each leaf’s own closeout, integration and finalization, and one final master version bump/release. The wrapper still holds master `task.md` and flat numbered `NN_<name>.md` plans; `master-template.md` remains the series scaffold.

### JSON-primary authoring and transition history

The durable model is `ar-task-document/v1` JSON with deterministic Markdown rendering. `template.md` and `master-template.md` specify render shape, not an independent editable format for tool-managed Markdown. The source names `task_doc` operations `create`, `set_status`, `set_step`, `skip_step`, `append_decision` and `set_field`; intentional skip targets one exact parent or nested step, needs a nonblank reason and does not cascade. Generated `task.md` is changed through the tool rather than hand editing. The schema’s master form carries `kind:"master"`, a structured `subTasks` index and ordered `sections` to preserve bespoke prose.

The plan keeps objective, requirements, a proportionate optional `## Design`, steps, decision log, open questions and references together. `codeExamplesNote` records intentional plan-gate deferral so the rendered examples say deferred rather than none needed. `statusNote` adds a descriptive status suffix, `headerNotes` adds key/value header lines, and freeform `sections` follows References without replacing standard structure. `dry_run=true` previews render, diff and `wouldLose` without writing; the source’s hand-authored migration sequence calls for confirming that content would not be lost before adoption. The inherited account’s “masters stay hand-authored until shipment” is transition history, not present evidence that masters lack tool support or that managed Markdown may be edited directly.

### Invariants and memory boundaries

Task artifacts hold planning and execution state, not onboarding truth. They can trigger `c-05-create-or-update-onboarding-files` updates; durable implementation findings are routed there during the implementation cycle or immediate closeout consolidation. Significant intent/design changes update the task file before edits continue, and settled design derives steps when the Task Collaboration Doctrine warrants it. Planning context includes resolved local docs, glossary/naming sources and affected onboarding; optional domain tools are supporting rather than universally mandatory.

The inherited boundary required a clean committed external-memory baseline before worktree start, with refreshed onboarding content committed and the computed ledger cache excluded. That retains the baseline/attribution intent. The old `contract.md` beside `task.md` placement describes an earlier address shape; the skill and series companions now describe master-root `series-contract.md` and each leaf’s `enclosures/<leaf-id>/series-contract.md`, work branch and worktree. Implementation and commit approvals are separate, checklist state must stay current, and finalization completes only the proved leaf/immediate-parent edge, not ancestors recursively.

Where onboarding is converted, the c-05 converted-card workflow supersedes legacy onboarding verification metadata and Update History: Markdown/reference authoring and source-bound history answers go through their defined owners. Task JSON/render state does not itself certify a memory card or waive memory publication boundaries.

### Inherited extension and evidence scope

The inherited card recorded no current todo for this workflow. That preserves the absence of a recorded action in that card, not a claim that the entire workflow or transition is complete.

The inherited documentation scope considered this a repository-local workflow with no applicable external domain documentation.

Its reference account reported no relevant external documentation. No fresh live-documentation search follows from that historical statement.

The inherited card described this as the approved workflow used by preliminary onboarding and the worktree task stack. That retains its contextual relationship without independently re-establishing approval or replaying those tasks.

The inherited reference scope did not require sibling-repository evidence for the workflow skill itself.

It reported no meaningful cross-repository references; this is a bounded historical search result rather than a new survey.

### Series contracts and lifecycle

The inherited series-contract note agrees with the current canonical skill’s master/leaf shape: master series are integration-branch wrappers, and leaf sub-tasks are worktree-backed units with their own enclosure contracts, closeout, integration and finalization. Companion guidance retains stable file numbers while the master Sub-tasks list owns execution order; each slice has its own checklist/commit and the master alone owns the final release. These descriptions do not prove that any particular integration, cleanup or release occurred.

## Evidence


- The source defines the resolved task wrapper and task.md, naming, scaffold, live checklist, distinct code examples and minute-precision timestamps. [1]


- Agent responsibilities separate implementation approval and commit approval, include onboarding/check cycles, and leave completion to exact step accounting and lifecycle finalization after landing. [2]


- Invariants preserve wrapper/checklist/design intent and the committed external-memory baseline with computed ledger excluded; new light-document authoring and legacy transition wording remain bounded by the actual task construction guard. [3]


- JSON-primary describes deterministic renders, explicit noncascading skip, deferred code examples, extensible fields and dry-run loss checking; light/master shipment claims are retained transition text, not current admission. [4]

- The current construction definition refuses kind light and derives master/subTask defaults from contract altitude. [5]

- Canonical series guidance assigns one master integration branch and one leaf enclosure/worktree per slice, with per-leaf closeout/integration/finalization and final master release. [6]


- The companion series convention keeps flat stable file IDs, master-owned ordering, per-leaf publication and test verification, and one final master release. [7]


- The workflow’s master-series section separates durable requirement/attempt records from disposable summary and assigns leaf enclosure integration and finalization. [8]

- Converted onboarding follows a metadata-free card/reference model instead of inheriting legacy task-era verification mechanics. [9]
