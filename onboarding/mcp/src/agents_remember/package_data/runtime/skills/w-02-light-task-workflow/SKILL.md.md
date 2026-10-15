# w-02-light-task-workflow/SKILL.md

## Purpose

This skill defines `w-02-light-task-workflow` skill, the light durable task workflow for medium-risk or multi-step changes that need a task artifact; work that outgrows a single-page plan escalates to a master + light sub-task series rather than a separate heavy workflow. This card describes the synchronized packaged runtime copy of canonical `skills/w-02-light-task-workflow/SKILL.md`, not a second workflow authority.

## Code Commentary

### Logic

Since L10 the JSON-primary paragraph anchors the thin-doc example to the smallest single-session build instead of a 'chat build': chat is never a build route (the l-01 invariant), so the thin doc — title plus a few steps — is the MINIMUM build artifact, not an optional upgrade over a doc-less chat.

`w-02-light-task-workflow` creates or updates the resolved wrapper and durable task artifact, stops for implementation approval, tracks the checklist, then separately requests explicit approval before worktree-backed closeout commits. Completion follows landing and `lifecycle_finalize_task`, not closeout alone. A plan that outgrows one page becomes a master plus flat numbered leaf files with stable creation IDs; exact same-master `waitsFor` IDs authored through `task_doc` derive Order rather than filenames or free-form prose. The master owns the integration branch and root contract; each active leaf owns its own enclosure/worktree, closeout, integration into the master and edge finalization. The master alone performs the final version bump/release after the leaves land.

### Conventions

The task document is JSON-primary: an `ar-task-document/v1` JSON is the source of truth, and `task.md` (or a sub-task Markdown file) is its deterministic render produced by `task_doc`. The tool manages `light`, `subTask`, and `master` documents; `template.md` and `master-template.md` are render specifications, not separate hand-authored new-document formats. Create a new series master through `task_doc` `create` with `kind:"master"` in the wrapper, then create its indexed child documents before writing any leaf's `waitsFor`. A master carries a structured `subTasks` index and ordered `sections` preserving its bespoke prose. Existing hand-authored Markdown documents remain unchanged until intentionally migrated; a Markdown-only master does not satisfy the JSON-primary prerequisite for `waitsFor` writes. These are the current source instructions, not evidence of runtime installation or a performed migration. [5] The skill keeps planning and implementation in one `task.md` file inside a wrapper folder. The planning wrapper and requirement corpus precede approval; task documents are created only after corpus approval and before any `c-09-git-worktree-manager` worktree start. The task document requires explicit objective, requirements, a `## Design` section sized per the Task Collaboration Doctrine (or an explicit no-design-needed note), steps, decision log, open questions, and references. A planning slice that defers its code examples to the plan gate records that with `codeExamplesNote` (set via `set_field`) so the rendered Proposed Code Examples section reads as deferred rather than as if none are needed. A leaf doc may also carry a `statusNote` (descriptive status suffix), `headerNotes` (extra `**Key:** value` header lines), and freeform `sections` appended after References — the escape hatch for bespoke prose; the standard template sections stay the backbone (R4). `dry_run=true` on any op previews (rendered + diff + `wouldLose`) without writing — the safe way to adopt a hand `.md` (R5).

### Invariants And Boundaries

`w-02-light-task-workflow` skill task artifacts are planning and execution state. They can trigger onboarding updates through `c-05-create-or-update-onboarding-files` skill, but they should not be treated as onboarding content. Current task path helpers name a root contract `series-contract.md` for standalone/task-root or master-series scope; an active leaf's own contract is `enclosures/<slugified-leaf-id>/series-contract.md`. The resolved contract supplies the selected worktree and lineage authority; the obsolete blanket `contract.md`-beside-`task.md` location is not current geometry. This storage account claims no source migration or runtime installation. Refreshed external-memory onboarding content must be committed, **with the computed ledger cache excluded**, before that `c-09-git-worktree-manager` skill worktree start. Implementation approval does not authorize closeout commits; the agent must present a commit preview and wait for explicit commit approval. Worktree-backed task status reaches `Completed` through `lifecycle_finalize_task`, not immediately after closeout.

### Todos

No current todo is recorded for this workflow skill.

### Docs References

No external domain documentation applies to this repository-local workflow skill.

No relevant external documentation found.

## Packaged Ordering Instructions

Stable filename numbers identify creation, not execution order. The package carries the canonical instruction unchanged; source presence is not runtime installation or an executed series.

- Master composition uses exact same-master waitsFor through task_doc and per-leaf worktrees. \[4] [4]
## Evidence

### Repo-Internal References

`w-02-light-task-workflow` skill is the approved workflow used by the preliminary onboarding task and the worktree task stack.

- The skill defines the task wrapper plus `task.md` as the durable plan/checklist artifact for medium work. [1]

- Packaged responsibilities retain distinct implementation/commit approval and finalization only after landing; major/nested completion obligations remain. [2]

- Packaged invariants preserve approval/onboarding/task-state boundaries and require master integration plus a separate enclosure/worktree per active leaf. [3]
### Cross-Repo References

No sibling repository evidence is needed for the current workflow skill.

No meaningful cross-repo references found.

## Series-Contract Notes

The packaged light-task workflow describes master series as integration-branch wrappers and leaf sub-tasks as the worktree-backed units with their own enclosure contracts and closeout/finalization.

- JSON-primary authoring manages light, subTask and master; new masters precede indexed children and waitsFor writes, existing Markdown remains until intentionally migrated, and approved corpus precedes task creation. [5]
