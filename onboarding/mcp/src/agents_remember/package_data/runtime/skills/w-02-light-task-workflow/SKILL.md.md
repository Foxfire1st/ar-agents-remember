# w-02-light-task-workflow/SKILL.md

## Purpose

This skill defines `w-02-light-task-workflow` skill, the light durable task workflow for medium-risk or multi-step changes that need a task artifact; work that outgrows a single-page plan escalates to a master + light sub-task series rather than a separate heavy workflow.

## Code Commentary

### Logic

Since L10 the JSON-primary paragraph anchors the thin-doc example to the smallest single-session build instead of a 'chat build': chat is never a build route (the l-01 invariant), so the thin doc — title plus a few steps — is the MINIMUM build artifact, not an optional upgrade over a doc-less chat.

`w-02-light-task-workflow` skill creates or updates one task wrapper folder under the `c-08-ar-coordination-context-resolver` skill resolved task root, writes the durable task document as `task.md`, stops for approval before implementation, uses the artifact checklist as the live execution record, and for worktree-backed tasks stops again for explicit commit approval before `c-09-git-worktree-manager` skill closeout creates commits. Dashboard task 14 clarifies that closeout is not task completion: after the task branch lands on its parent branch, `lifecycle_finalize_task` proves the edge, runs or verifies cleanup, and sets the leaf task plus immediate parent row to `Completed`. When a task outgrows a single-page plan it escalates to a master + light sub-task series (`master-template.md`): one wrapper folder with a master `task.md` plus flat numbered `NN_<name>.md` sub-tasks, run as one task / one workflow / one worktree with a commit per slice and a single integrate + finalization + release at the end.

### Conventions

The task document is JSON-primary (slice 3c): an `ar-task-document/v1` JSON is the source of truth and `task.md` is a deterministic render produced by the `task_doc` MCP tool (the `template.md` is the render spec; the format also covers a series master via `kind:"master"` — a `subTasks` index + ordered `sections` — though masters stay hand-authored markdown until the runtime ships `task_doc`). The skill keeps planning and implementation in one `task.md` file inside a wrapper folder. The folder is created as soon as the task class, naming, and workflow variables are clear, before any `c-09-git-worktree-manager` skill worktree start. The task document requires explicit objective, requirements, an optional `## Design` section sized per the Task Collaboration Doctrine, steps, decision log, open questions, and references. A planning slice that defers its code examples to the plan gate records that with `codeExamplesNote` (set via `set_field`) so the rendered Proposed Code Examples section reads as deferred rather than as if none are needed. A leaf doc may also carry a `statusNote` (descriptive status suffix), `headerNotes` (extra `**Key:** value` header lines), and freeform `sections` appended after References — the escape hatch for bespoke prose; the standard template sections stay the backbone (R4). `dry_run=true` on any op previews (rendered + diff + `wouldLose`) without writing — the safe way to adopt a hand `.md` (R5).

### Invariants And Boundaries

`w-02-light-task-workflow` skill task artifacts are planning and execution state. They can trigger onboarding updates through `c-05-create-or-update-onboarding-files` skill, but they should not be treated as onboarding content. If a light task later becomes worktree-backed, `c-09-git-worktree-manager` skill stores `contract.md` beside `task.md` in the same wrapper folder. Refreshed external-memory onboarding content must be committed, **with the computed ledger cache excluded**, before that `c-09-git-worktree-manager` skill worktree start. Implementation approval does not authorize closeout commits; the agent must present a commit preview and wait for explicit commit approval. Worktree-backed task status reaches `Completed` through `lifecycle_finalize_task`, not immediately after closeout.

### Todos

No current todo is recorded for this workflow skill.

### Docs References

No external domain documentation applies to this repository-local workflow skill.

No relevant external documentation found.

## Evidence

### Repo-Internal References

`w-02-light-task-workflow` skill is the approved workflow used by the preliminary onboarding task and the worktree task stack.

- The skill defines the task wrapper plus `task.md` as the durable plan/checklist artifact for medium work. [1]
- Agent responsibilities include creating the wrapper artifact, stopping for implementation approval, implementing checklist items, presenting a worktree-backed commit preview, waiting for commit approval before closeout commits, and leaving completion to `lifecycle_finalize_task` after the branch lands. [2]
- Invariants require wrapper folders, resolved roots, no implementation before approval, a clean committed external-memory baseline — refreshed onboarding content committed with the computed ledger cache excluded — before `c-09-git-worktree-manager` skill start, separate commit approval before closeout commits, recording the settled design in the task file's `## Design` section when the Task Collaboration Doctrine warrants it, and no stale task state. [3]

### Cross-Repo References

No sibling repository evidence is needed for the current workflow skill.

No meaningful cross-repo references found.

## Series-Contract Notes

The packaged light-task workflow describes master series as integration-branch wrappers and leaf sub-tasks as the worktree-backed units with their own enclosure contracts and closeout/finalization.
