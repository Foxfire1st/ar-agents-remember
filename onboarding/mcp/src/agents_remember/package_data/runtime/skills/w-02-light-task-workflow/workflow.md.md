# `w-02-light-task-workflow` workflow.md

## Purpose

This workflow file gives the step-by-step `w-02-light-task-workflow` skill procedure for creating a task wrapper, planning in `task.md`, approving implementation, implementing, validating, requesting separate commit approval for worktree-backed closeout, and finalizing a light durable task after its branch lands. It is the packaged synchronized copy of canonical `skills/w-02-light-task-workflow/workflow.md`, not a separately authoritative procedure.

## Code Commentary

### Logic

The synchronized workflow advances formal attempts only at review handoff or after rejection,
preserves internal protocol events separately, and links lightweight records to frozen expanded
evidence.

The workflow starts with context resolution, drift checks, and approval before implementation
cit:(["Run the in-between task lifecycle"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:3-15).
It creates or reuses a wrapper folder under the resolved task root, with `task.md` as the durable
artifact and `enclosures/<leaf-id>/series-contract.md` as the leaf contract when a worktree-backed
task is opened cit:(["The durable artifact shape", "places its leaf contract at", "enclosures/<leaf-id>/series-contract.md"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:54-63).
Planning runs the drift gate, gathers context, applies the collaboration doctrine, and authors the
JSON-primary task document through `task_doc`; generated Markdown is not hand-edited. For a new
series, create the master first through `task_doc` `create` with `kind:"master"`, then create indexed
child documents before leaf `waitsFor` writes. Existing hand-authored Markdown remains unchanged
until intentionally migrated
cit:(["JSON-primary", "ar-task-document/v1", "kind:\"master\"", "Existing hand-authored Markdown documents"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:114-118).
After approval, each implementation section is read and performed with its relevant checks
cit:(["For each implementation section", "read the step objective and its checkbox items", "read the relevant files or materials", "perform the approved work", "use the checks listed", "finish any remaining onboarding cleanup", "mark a substep complete only after", "mark the parent step checkbox complete only after"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:190-199).
Worktree closeout still stops for separate commit approval
cit:(["ask explicitly for commit/closeout approval"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:259-259).
Close prepares the completion handoff and cross-reference check; it does not own implementation or
unapproved commits cit:(["Close does not own implementation work", "Prepare the completion handoff", "Cross-reference check"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:264-275; mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:277-283).
When the plan outgrows one page, the series uses one master integration branch plus leaf enclosure
worktrees, integrates each leaf, and performs the final release on the master
cit:(["one master integration branch plus leaf enclosure worktrees", "integrate each leaf branch back into the master integration branch", "The master owns only the final release step"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:364-372).

### Conventions

The workflow treats `task.md` as active state inside the wrapper folder. It uses checkboxes for implementation progress and a decision log for durable choices, and refers to `c-08-ar-coordination-context-resolver` skill resolved `tools_path` and `sources_path`. When code examples are deferred to the plan gate, the planning step records that via `codeExamplesNote` so the render distinguishes deferred from none-needed.

### Invariants And Boundaries

Implementation cannot begin until the task artifact is approved. Drift detection must happen before planning if onboarding exists, and onboarding changes must be handled through `c-05-create-or-update-onboarding-files` skill. Worktree-backed closeout commits cannot be created until the developer approves the closeout preview.

### Todos

Add examples once a real `w-02-light-task-workflow` skill task wrapped by the `c-09-git-worktree-manager` skill has been run.


## CCR-R12@v5 Light-Task Boundary

A light-task handoff records relevant targeted checks and honest failed or not-run results before the authorized Git transaction. Its commit legs suppress automatic quality and test hooks while ordinary explicit Git hook policy outside closeout/integration remains unchanged. Curation is the exception: the curator always runs the complete memory-quality operation as part of curation, and closeout and integration carry its completed result as a prerequisite, while full code quality, full tests, certification, and review remain explicit operations rather than automatic closeout or integration prerequisites.

### Docs References

No external domain documentation applies to this repository-local workflow.

No relevant external documentation found.

## Packaged Ordering Projection

The series introduction now calls the numbered filenames stable creation IDs and the master list an index. Exact same-master waitsFor through task_doc determines order. This source port does not execute or certify a workflow.

- Stable IDs/index and waitsFor-derived ordering in package and canonical owner. \[11] [11]

- One owned primary acceptance block and separate dependency/preservation checks. \[12] [12]
## Evidence

### Repo-Internal References

The workflow defines the concrete process behind the `w-02-light-task-workflow` skill.

- The workflow goal is to run the in-between task lifecycle. [1]
- The workflow requires drift checking, approval before implementation, onboarding updates, and separate commit approval. [2]
- The durable artifact shape is a wrapper folder plus `task.md` under the resolved task root. [3]

- A leaf contract lives at `enclosures/<leaf-id>/series-contract.md`. [4]

- The task document is JSON-primary with schema `ar-task-document/v1`. [5]

- `codeExamplesNote` records deferred code examples distinctly from none-needed. [6]

- Closeout may call `lifecycle_finalize_task` only after every declared work unit is done or intentionally skipped. [7]

- Final closure verifies that referenced workflow or skill paths still resolve. [8]

- Stable creation filenames and master index are separate from exact same-master waitsFor-derived Order; the master provides integration and each active leaf its enclosure/worktree. [9]

- Only the master performs the final version bump/release after all leaves land; leaves do not bump. [10]
### Cross-Repo References

No sibling repository evidence is needed for the current workflow file.

No meaningful cross-repo references found.

## Series-Contract Notes

The workflow reference now distinguishes the master integration branch lifecycle from active leaf enclosure lifecycles and shows leaf closeout/integration before final master release.

## M38 Requirement-Acceptance Workflow Projection

The workflow preserves stable IDs and immutable approved versions. Each leaf owns exactly one primary requirement revision with its complete packet; adjacent requirements are dependency or preservation constraints and the leaf must not claim them closed. Each handoff supplies one primary acceptance block with evidence, and the independent verdict adjudicates that primary. Multiple independent requirements require split leaves; one requirement may have several manifestations. Blocked/approved-change exceptions cite durable developer rulings, and requirement acceptance remains separate from the durable-evidence stable-contract-or-expiry hold. The packaged source copy is synchronized with canonical source; its presence does not prove runtime installation or migration. Version-addressed packets retain approval provenance; semantic revisions create new files rather than overwrite approved contracts.

## M40-M45 Attempt-Workflow Projection

The packaged workflow specifies immutable worker/reviewer attempt records, preserves successor
lineage and bounded invalidation, and maintains leaf-authoritative/rebuildable non-gating master
summary behavior.

## 2026-08-27 Attempt Boundary Clarification

This packaged projection preserves the canonical phase boundary: validate before append; a
malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
a malformed handed-off attempt requires independent rejection before successor handoff.
