# `w-02-light-task-workflow` workflow.md

## Purpose

This workflow file gives the step-by-step `w-02-light-task-workflow` skill procedure for creating a task wrapper, planning in `task.md`, approving implementation, implementing, validating, requesting separate commit approval for worktree-backed closeout, and finalizing a light durable task after its branch lands.

## Code Commentary

### Logic

The synchronized workflow advances formal attempts only at review handoff or after rejection,
preserves internal protocol events separately, and links lightweight records to frozen expanded
evidence.

The workflow starts with context resolution, drift checks, and approval before implementation
cit:(["Run the in-between task lifecycle"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:3-15).
It creates or reuses a wrapper folder under the resolved task root, with `task.md` as the durable
artifact and `enclosures/<leaf-id>/series-contract.md` as the leaf contract when a worktree-backed
task is opened cit:(["The durable artifact shape"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:54-54).
Planning runs the drift gate, gathers context, applies the collaboration doctrine, and authors the
JSON-primary task document through `task_doc`; the rendered `task.md` is not hand-edited
cit:(["JSON-primary"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:114-114).
After approval, each implementation section is read and performed with its relevant checks
cit:(["For each implementation section", "read the step objective and its checkbox items", "read the relevant files or materials", "perform the approved work", "use the checks listed", "finish any remaining onboarding cleanup", "mark a substep complete only after", "mark the parent step checkbox complete only after"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:186-186; mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:188-190; mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:192-195).
Worktree closeout still stops for separate commit approval
cit:(["ask explicitly for commit/closeout approval"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:255-255).
Close prepares the completion handoff and cross-reference check; it does not own implementation or
unapproved commits cit:(["Cross-reference check"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:273-273).
When the plan outgrows one page, the series uses one master integration branch plus leaf enclosure
worktrees, integrates each leaf, and performs the final release on the master
cit:(["one master integration branch plus leaf enclosure worktrees"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:359-359).

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
- A master series uses one master integration branch plus leaf enclosure worktrees. [9]
- The master owns the final release step, while sub-tasks never bump the version. [10]

### Cross-Repo References

No sibling repository evidence is needed for the current workflow file.

No meaningful cross-repo references found.

## Series-Contract Notes

The workflow reference now distinguishes the master integration branch lifecycle from active leaf enclosure lifecycles and shows leaf closeout/integration before final master release.

## M38 Requirement-Acceptance Workflow Projection

The workflow assigns stable IDs without reuse, compiles each leaf's exact owned/inherited set, and
requires a builder envelope plus independent reviewer adjudication for every ID before closure.
Blocked or approved-change rows cite durable developer rulings. Requirement acceptance remains
separate from the stable-contract-or-expiry hold point for durable evidence. This installed copy is
synchronized from canonical workflow source.
Every packet uses an immutable `<stable-id>-<version>-<slug>.md` address and records its durable
corpus approval; a later semantic revision creates a new file instead of overwriting the approved
contract.

## M40-M45 Attempt-Workflow Projection

The installed workflow now appends immutable worker/reviewer attempt records, preserves successor
lineage and bounded invalidation, and maintains leaf-authoritative/rebuildable non-gating master
summary behavior.

## 2026-08-27 Attempt Boundary Clarification

This packaged projection preserves the canonical phase boundary: validate before append; a
malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
a malformed handed-off attempt requires independent rejection before successor handoff.
