# `w-02-light-task-workflow` workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-23T22:50+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|

## Purpose

This workflow file gives the step-by-step `w-02-light-task-workflow` skill procedure for creating a task wrapper, planning in `task.md`, approving implementation, implementing, validating, requesting separate commit approval for worktree-backed closeout, and finalizing a light durable task after its branch lands.

## Code Commentary

### Logic

The workflow starts with context resolution, drift checks, and approval before implementation
cit:(["Run the in-between task lifecycle"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:3-15).
It creates or reuses a wrapper folder under the resolved task root, with `task.md` as the durable
artifact and `enclosures/<leaf-id>/series-contract.md` as the leaf contract when a worktree-backed
task is opened cit:(["The durable artifact shape"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:16-45).
Planning runs the drift gate, gathers context, applies the collaboration doctrine, and authors the
JSON-primary task document through `task_doc`; the rendered `task.md` is not hand-edited
cit:([`task_doc`], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:46-94).
After approval, each implementation section is read and performed with its relevant checks
cit:(["For each implementation section", "read the step objective and its checkbox items", "read the relevant files or materials", "perform the approved work", "use the checks listed", "finish any remaining onboarding cleanup", "mark a substep complete only after", "mark the parent step checkbox complete only after"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:131-131; mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:133-135; mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:137-140).
Worktree closeout still stops for separate commit approval
cit:(["ask explicitly for commit/closeout approval"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:160-160).
Close prepares the completion handoff and cross-reference check; it does not own implementation or
unapproved commits cit:(["Cross-reference check"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:163-185).
When the plan outgrows one page, the series uses one master integration branch plus leaf enclosure
worktrees, integrates each leaf, and performs the final release on the master
cit:(["one master integration branch plus leaf enclosure worktrees"], mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:229-252).

### Conventions

The workflow treats `task.md` as active state inside the wrapper folder. It uses checkboxes for implementation progress and a decision log for durable choices, and refers to `c-08-ar-coordination-context-resolver` skill resolved `tools_path` and `sources_path`. When code examples are deferred to the plan gate, the planning step records that via `codeExamplesNote` so the render distinguishes deferred from none-needed.

### Invariants And Boundaries

Implementation cannot begin until the task artifact is approved. Drift detection must happen before planning if onboarding exists, and onboarding changes must be handled through `c-05-create-or-update-onboarding-files` skill. Worktree-backed closeout commits cannot be created until the developer approves the closeout preview.

### Todos

Add examples once a real `w-02-light-task-workflow` skill task wrapped by the `c-09-git-worktree-manager` skill has been run.

### Docs References

No external domain documentation applies to this repository-local workflow.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The workflow defines the concrete process behind the `w-02-light-task-workflow` skill.

| Finding | Anchor | Source |
| --- | --- | --- |
| The workflow goal is to run the in-between task lifecycle. | "Run the in-between task lifecycle" | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:5-5 |
| The workflow requires drift checking, approval before implementation, onboarding updates, and separate commit approval. | "drift check before planning"; "approval before implementation"; "onboarding update through"; "separate commit approval" | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:11-14 |
| The durable artifact shape is a wrapper folder plus `task.md` under the resolved task root. | "The durable artifact shape" | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:20-20 |
| A leaf contract lives at `enclosures/<leaf-id>/series-contract.md`. | "places its leaf contract at" | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:26-26 |
| The task document is JSON-primary with schema `ar-task-document/v1`. | "ar-task-document/v1" | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:77-77 |
| `codeExamplesNote` records deferred code examples distinctly from none-needed. | `codeExamplesNote` | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:87-87 |
| Closeout may call `lifecycle_finalize_task` only after every declared work unit is done or intentionally skipped. | `lifecycle_finalize_task` | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:161-161 |
| Final closure verifies that referenced workflow or skill paths still resolve. | "verify any referenced workflow or skill paths still resolve" | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:182-182 |
| A master series uses one master integration branch plus leaf enclosure worktrees. | "one master integration branch plus leaf enclosure worktrees" | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:235-235 |
| The master owns the final release step, while sub-tasks never bump the version. | "The master owns only the final release step" | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md:243-243 |

## Cross-Repo References

No sibling repository evidence is needed for the current workflow file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Series-Contract Notes

The workflow reference now distinguishes the master integration branch lifecycle from active leaf enclosure lifecycles and shows leaf closeout/integration before final master release.

## Update History
- 2026-08-04T09:54:46+02:00 — 260731-EFA-L6 S18-B07 second bounded correction: expanded the implementation-section claim through the ordered read, perform, cleanup, and completion steps; same-reviewer delta pending.

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: packaged workflow details now define the master integration branch plus per-leaf enclosure lifecycle, including active slice worktrees and final master release. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00: Dashboard task 14 — documented that closeout does not set worktree-backed tasks to `Completed`; `lifecycle_finalize_task` does so after the branch lands and cleanup/finalization is approved. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-19T05:15+02:00: Slice 3c reopened (R3, deferred-examples honesty) — the proposed-code-examples step now records deferral via `codeExamplesNote` so the render distinguishes deferred from none-needed. Synced from canonical `skills/`. Verification metadata pinned until closeout stamps the R3 code commit.
- 2026-06-13T22:34: Slice 3c commit 2 — step 7 now authors the task document via the `task_doc` MCP tool (JSON-primary; the tool renders `task.md`, `template.md` is the render spec). Verification metadata pinned until closeout stamps the 3c commit-2 code commit.
- 2026-06-02T04:25+02:00: Replaced the heavy-oriented "What This Workflow Does Not Cover" + "Relationship To Heavy Task Workflow" sections with a "When To Escalate To A Master Series" section, and dropped the "same naming convention as heavy-task-workflow" phrasing. `l-01-session-job-lifecycle` skill series, Sub-task B/S6, mcp 1.1.0.
- 2026-06-02T04:10+02:00: Added a "Master Task Series" section documenting escalation to a master + light sub-task series (one worktree per series, a commit per slice, one integrate + release at the end). `l-01-session-job-lifecycle` skill series, Sub-task B/S5, mcp 1.1.0.
- 2026-05-31T01:06+02:00: Added step 6 "Reframe and design before writing the plan" linking the Task Collaboration Doctrine and recording settled design in the task file's `## Design` section before implementation steps; renumbered later steps to 7 and 8, added the design item to the required-sections list, and refreshed the citations my insertion shifted.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` added clean-source versus dirty-source drift classification to `w-02-light-task-workflow` skill planning.
- 2026-05-24T04:34+02:00: Updated task-start references after `c-02-memory-quality-control` skill was renamed to memory quality control.
- 2026-05-10T01:19: Updated after Phase 2 gained the closeout dry-run and explicit commit approval handoff for worktree-backed tasks.
- 2026-05-10T00:56: Updated the `c-09-git-worktree-manager` skill handoff rule so refreshed external-memory onboarding and ledger changes are committed before worktree start.
- 2026-05-10T00:47: Updated `w-02-light-task-workflow` skill phase language so task wrapper folders are created before any `c-09-git-worktree-manager` skill worktree.
- 2026-05-09T22:57: Refreshed verification metadata and updated `w-02-light-task-workflow` skill citations.
- 2026-05-09T21:59: Updated for worktree-backed task folders and `c-08-ar-coordination-context-resolver` skill resolved tools/sources paths.
- 2026-05-09T21:15: Created first file-level onboarding baseline for `w-02-light-task-workflow` skill workflow steps.
