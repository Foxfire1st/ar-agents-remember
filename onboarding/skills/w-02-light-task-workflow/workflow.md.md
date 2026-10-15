# skills/w-02-light-task-workflow/workflow.md

## Current Canonical Contract

The workflow sequences approved canonical requirements before task topology, then JSON-primary task projection, live-checklist implementation and separate commit approval. A task owns one primary requirement revision and records dependency/preservation checks without claiming to close them. Formal delivery attempts advance only at exact-candidate review handoff; internal implementation/test/evidence reruns remain experimental protocol. The one physical journal and its separately authored adjudications stay authoritative; master summaries are rebuildable, not gates. Independent review is requested by the developer or approved brief, not automatically required before every closure. The single-page heuristic is guidance, not a hard size boundary. Finalization requires every declared parent/nested step explicitly done or intentionally skipped; a cleanup-containing final step is cleaned, marked and then finalized against the already-clean contract. The unchanged general workflow does not grant this Curator transaction or task-edit authority. Earlier inherited full-memory-quality opt-in wording does not override the Curator owner's complete standing curation operation.

The current Phase 0 wording names sprint, master or leaf documents after corpus approval; removal of the former standalone-task phrase does not create a taskless or standalone role-start route.

This qualification governs the named current seams; incompatible earlier generalizations remain historical, not restored authority. No source inspection here establishes execution, a launch, a test result, a CODE/MEMORY grade or a completed closeout.

- Light-task workflow preserves corpus approval, one primary revision, exact handoff attempts, non-gating summaries and explicit finalization/cleanup order. [8]
- The Curator owner requires the complete curation operation; optional full-quality/test requests do not waive it. [7]


## Governing Overview

[repository onboarding overview](../../overview.md)

## Purpose

This workflow governs the planning, approval, implementation, evidence, and closeout lifecycle for
one light task or a master plus light-subtask series.

## Code Commentary

### Logic

Phase 0 compiles independently falsifiable obligations into stable, versioned canonical packets,
cold-reads them, and obtains developer approval before any task topology exists. Later phases
project those exact revisions into tasks, implement against a live checklist, maintain one
acceptance envelope per revision, and require independent adjudication before closure.

A changed obligation creates a new version-addressed packet, invalidates only affected acceptance,
updates affected projections, and rebriefs affected leaves. Task documents summarize topology and
never become alternate requirement authorities.

Delivery attempts form a separate append-only axis and advance only when an exact candidate is
handed to independent review, or after rejection when its successor is handed off. Internal
implementation/test/evidence reruns remain separate protocol events. Lightweight worker records
bind exact candidates, requirement-specific facts, predecessors, and content-addressed expanded
evidence; reviewer records independently adjudicate those attempts, and failure classes determine
recovery ownership. Leaf journals remain authority. A rebuildable master summary exposes formal
attempts/rejections/current state/dominant class, excludes protocol events, and cannot gate or lock
any task, lifecycle, closeout, integration, or queue operation.

### Conventions

- Use one planning wrapper with `requirements/README.md` and immutable revision packets.
- Tool-managed `light`, `subTask`, and new `master` documents are JSON-primary and rendered
  through `task_doc`; generated Markdown is not hand-edited. Create a new series master with
  `create` and `kind:"master"` first, then indexed child documents before leaf `waitsFor` writes.
  Existing hand-authored Markdown remains unchanged until intentionally migrated. [6]
- Decision logs are append-only and timestamps use `YYYY-MM-DDTHH:MM`.
- Escalate to a master series when the implementation plan no longer fits one page.

### Invariants And Boundaries

- No sprint, master, task, or leaf is authored before corpus approval.
- Every leaf owns exactly one primary requirement revision.
- One revision may have multiple independently executable manifestation leaves.
- Requirement acceptance and durable-evidence lifecycle remain independent gates.
- Worktree commits still require their separate approval.
- Accepted attempts reopen only through independently proven regression plus owner-recorded bounded
  invalidation, or an approved semantic revision.

### Todos

None.


## CCR-R12@v5 Light-Task Boundary

A light-task handoff records relevant targeted checks and honest failed or not-run results before the authorized Git transaction. Its commit legs suppress automatic quality and test hooks while ordinary explicit Git hook policy outside closeout/integration remains unchanged. Full quality, full tests, full memory quality, certification, and review remain explicit operations and are not automatic closeout or integration prerequisites.

## Evidence

### Docs References

No external Domain Documentation source governs this workflow.

### Repo-Internal References

- Requirement compilation, cold read, and approval precede topology. [1]

- Tasks carry filtered projections rather than rewritten contracts. [2]

- Implementation maintains one acceptance block per exact revision. [3]

- Requirement changes version, invalidate, update, and rebrief affected work. [4]

- Phase 2 and closure append exact worker/reviewer records, while master-series summaries remain rebuildable and non-gating. [5]
### Cross-Repo References

The context resolver supplies target-repository paths, tools, and memory policy; this workflow does
not hard-code them.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.

- JSON-primary current authoring and master-first series creation precede child waitsFor; generated renders are not hand-edited and existing Markdown is not automatically migrated. [6]


## Inherited Distribution Commentary

The following complete distribution-copy account preserves useful inherited explanations and historical references. The current qualification above controls changed seams; unverified remainder is inherited scope, not a newly certified contract. Historical labels allocate no new reference numbers.

> # `w-02-light-task-workflow` workflow.md
>
> ## Purpose
>
> This workflow file gives the step-by-step `w-02-light-task-workflow` skill procedure for creating a task wrapper, planning in `task.md`, approving implementation, implementing, validating, requesting separate commit approval for worktree-backed closeout, and finalizing a light durable task after its branch lands.
>
> ## Code Commentary
>
> ### Logic
>
> The synchronized workflow advances formal attempts only at review handoff or after rejection,
> preserves internal protocol events separately, and links lightweight records to frozen expanded
> evidence.
>
> The workflow starts with context resolution, drift checks, and approval before implementation
> cit:(["Run the in-between task lifecycle"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:3-15).
> It creates or reuses a wrapper folder under the resolved task root, with `task.md` as the durable
> artifact and `enclosures/<leaf-id>/series-contract.md` as the leaf contract when a worktree-backed
> task is opened cit:(["The durable artifact shape"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:54-54).
> Planning runs the drift gate, gathers context, applies the collaboration doctrine, and authors the
> JSON-primary task document through `task_doc`; the rendered `task.md` is not hand-edited
> cit:(["JSON-primary"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:114-114).
> After approval, each implementation section is read and performed with its relevant checks
> cit:(["For each implementation section", "read the step objective and its checkbox items", "read the relevant files or materials", "perform the approved work", "use the checks listed", "finish any remaining onboarding cleanup", "mark a substep complete only after", "mark the parent step checkbox complete only after"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:186-186; mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:188-190; mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:192-195).
> Worktree closeout still stops for separate commit approval
> cit:(["ask explicitly for commit/closeout approval"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:255-255).
> Close prepares the completion handoff and cross-reference check; it does not own implementation or
> unapproved commits cit:(["Cross-reference check"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:273-273).
> When the plan outgrows one page, the series uses one master integration branch plus leaf enclosure
> worktrees, integrates each leaf, and performs the final release on the master
> cit:(["one master integration branch plus leaf enclosure worktrees"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:359-359).
>
> ### Conventions
>
> The workflow treats `task.md` as active state inside the wrapper folder. It uses checkboxes for implementation progress and a decision log for durable choices, and refers to `c-08-ar-coordination-context-resolver` skill resolved `tools_path` and `sources_path`. When code examples are deferred to the plan gate, the planning step records that via `codeExamplesNote` so the render distinguishes deferred from none-needed.
>
> ### Invariants And Boundaries
>
> Implementation cannot begin until the task artifact is approved. Drift detection must happen before planning if onboarding exists, and onboarding changes must be handled through `c-05-create-or-update-onboarding-files` skill. Worktree-backed closeout commits cannot be created until the developer approves the closeout preview.
>
> ### Todos
>
> Add examples once a real `w-02-light-task-workflow` skill task wrapped by the `c-09-git-worktree-manager` skill has been run.
>
>
> ## CCR-R12@v5 Light-Task Boundary
>
> A light-task handoff records relevant targeted checks and honest failed or not-run results before the authorized Git transaction. Its commit legs suppress automatic quality and test hooks while ordinary explicit Git hook policy outside closeout/integration remains unchanged. Curation is the exception: the curator always runs the complete memory-quality operation as part of curation, and closeout and integration carry its completed result as a prerequisite, while full code quality, full tests, certification, and review remain explicit operations rather than automatic closeout or integration prerequisites.
>
> ### Docs References
>
> No external domain documentation applies to this repository-local workflow.
>
> No relevant external documentation found.
>
> ## Evidence
>
> ### Repo-Internal References
>
> The workflow defines the concrete process behind the `w-02-light-task-workflow` skill.
>
> - The workflow goal is to run the in-between task lifecycle. (historical reference 1)
> - The workflow requires drift checking, approval before implementation, onboarding updates, and separate commit approval. (historical reference 2)
> - The durable artifact shape is a wrapper folder plus `task.md` under the resolved task root. (historical reference 3)
> - A leaf contract lives at `enclosures/<leaf-id>/series-contract.md`. (historical reference 4)
> - The task document is JSON-primary with schema `ar-task-document/v1`. (historical reference 5)
> - `codeExamplesNote` records deferred code examples distinctly from none-needed. (historical reference 6)
> - Closeout may call `lifecycle_finalize_task` only after every declared work unit is done or intentionally skipped. (historical reference 7)
> - Final closure verifies that referenced workflow or skill paths still resolve. (historical reference 8)
> - A master series uses one master integration branch plus leaf enclosure worktrees. (historical reference 9)
> - The master owns the final release step, while sub-tasks never bump the version. (historical reference 10)
>
> ### Cross-Repo References
>
> No sibling repository evidence is needed for the current workflow file.
>
> No meaningful cross-repo references found.
>
> ## Series-Contract Notes
>
> The workflow reference now distinguishes the master integration branch lifecycle from active leaf enclosure lifecycles and shows leaf closeout/integration before final master release.
>
> ## M38 Requirement-Acceptance Workflow Projection
>
> The workflow assigns stable IDs without reuse, compiles each leaf's exact owned/inherited set, and
> requires a builder envelope plus independent reviewer adjudication for every ID before closure.
> Blocked or approved-change rows cite durable developer rulings. Requirement acceptance remains
> separate from the stable-contract-or-expiry hold point for durable evidence. This installed copy is
> synchronized from canonical workflow source.
> Every packet uses an immutable `<stable-id>-<version>-<slug>.md` address and records its durable
> corpus approval; a later semantic revision creates a new file instead of overwriting the approved
> contract.
>
> ## M40-M45 Attempt-Workflow Projection
>
> The installed workflow now appends immutable worker/reviewer attempt records, preserves successor
> lineage and bounded invalidation, and maintains leaf-authoritative/rebuildable non-gating master
> summary behavior.
>
> ## 2026-08-27 Attempt Boundary Clarification
>
> This packaged projection preserves the canonical phase boundary: validate before append; a
> malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
> a malformed handed-off attempt requires independent rejection before successor handoff.

Inherited reference 1 commentary (not a revalidated target):

> The workflow goal is to run the in-between task lifecycle.
>
> Anchor: "Run the in-between task lifecycle"

Inherited reference 10 commentary (not a revalidated target):

> The master owns the final release step, while sub-tasks never bump the version.
>
> Anchor: "The master owns only the final release step"

Inherited reference 2 commentary (not a revalidated target):

> The workflow requires drift checking, approval before implementation, onboarding updates, and separate commit approval.
>
> Anchor: "drift check before planning"; "approval before implementation"; "onboarding update through"; "separate commit approval"

Inherited reference 3 commentary (not a revalidated target):

> The durable artifact shape is a wrapper folder plus `task.md` under the resolved task root.
>
> Anchor: "The durable artifact shape"

Inherited reference 4 commentary (not a revalidated target):

> A leaf contract lives at `enclosures/<leaf-id>/series-contract.md`.
>
> Anchor: "places its leaf contract at"

Inherited reference 5 commentary (not a revalidated target):

> The task document is JSON-primary with schema `ar-task-document/v1`.
>
> Anchor: "ar-task-document/v1"

Inherited reference 6 commentary (not a revalidated target):

> `codeExamplesNote` records deferred code examples distinctly from none-needed.
>
> Anchor: `codeExamplesNote`

Inherited reference 7 commentary (not a revalidated target):

> Closeout may call `lifecycle_finalize_task` only after every declared work unit is done or intentionally skipped.
>
> Anchor: `lifecycle_finalize_task`

Inherited reference 8 commentary (not a revalidated target):

> Final closure verifies that referenced workflow or skill paths still resolve.
>
> Anchor: "verify any referenced workflow or skill paths still resolve"

Inherited reference 9 commentary (not a revalidated target):

> A master series uses one master integration branch plus leaf enclosure worktrees.
>
> Anchor: "one master integration branch plus leaf enclosure worktrees"

## Canonical Source Ownership

The verified byte-equal package copy is derived output, not an independent role/task/permission authority. Whole-source evidence does not certify inherited statements or a whole requirement.
