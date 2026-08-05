# w-02-light-task-workflow/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T12:30+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|

## Purpose

This skill defines `w-02-light-task-workflow` skill, the light durable task workflow for medium-risk or multi-step changes that need a task artifact; work that outgrows a single-page plan escalates to a master + light sub-task series rather than a separate heavy workflow.

## Code Commentary

### Logic

Since L10 the JSON-primary paragraph anchors the thin-doc example to the smallest single-session build instead of a 'chat build': chat is never a build route (the l-01 invariant), so the thin doc — title plus a few steps — is the MINIMUM build artifact, not an optional upgrade over a doc-less chat.

`w-02-light-task-workflow` skill creates or updates one task wrapper folder under the `c-08-ar-coordination-context-resolver` skill resolved task root, writes the durable task document as `task.md`, stops for approval before implementation, uses the artifact checklist as the live execution record, and for worktree-backed tasks stops again for explicit commit approval before `c-09-git-worktree-manager` skill closeout creates commits. Dashboard task 14 clarifies that closeout is not task completion: after the task branch lands on its parent branch, `lifecycle_finalize_task` proves the edge, runs or verifies cleanup, and sets the leaf task plus immediate parent row to `Completed`. When a task outgrows a single-page plan it escalates to a master + light sub-task series (`master-template.md`): one wrapper folder with a master `task.md` plus flat numbered `NN_<name>.md` sub-tasks, run as one task / one workflow / one worktree with a commit per slice and a single integrate + finalization + release at the end.

### Conventions

The task document is JSON-primary (slice 3c): an `ar-task-document/v1` JSON is the source of truth and `task.md` is a deterministic render produced by the `task_doc` MCP tool (the `template.md` is the render spec; the format also covers a series master via `kind:"master"` — a `subTasks` index + ordered `sections` — though masters stay hand-authored markdown until the runtime ships `task_doc`). The skill keeps planning and implementation in one `task.md` file inside a wrapper folder. The folder is created as soon as the task class, naming, and workflow variables are clear, before any `c-09-git-worktree-manager` skill worktree start. The task document requires explicit objective, requirements, an optional `## Design` section sized per the Task Collaboration Doctrine, steps, decision log, open questions, and references. A planning slice that defers its code examples to the plan gate records that with `codeExamplesNote` (set via `set_field`) so the rendered Proposed Code Examples section reads as deferred rather than as if none are needed. A leaf doc may also carry a `statusNote` (descriptive status suffix), `headerNotes` (extra `**Key:** value` header lines), and freeform `sections` appended after References — the escape hatch for bespoke prose; the standard template sections stay the backbone (R4). `dry_run=true` on any op previews (rendered + diff + `wouldLose`) without writing — the safe way to adopt a hand `.md` (R5).

### Invariants And Boundaries

`w-02-light-task-workflow` skill task artifacts are planning and execution state. They can trigger onboarding updates through `c-05-create-or-update-onboarding-files` skill, but they should not be treated as onboarding content. If a light task later becomes worktree-backed, `c-09-git-worktree-manager` skill stores `contract.md` beside `task.md` in the same wrapper folder. Refreshed external-memory onboarding and ledger changes must be committed before that `c-09-git-worktree-manager` skill worktree start. Implementation approval does not authorize closeout commits; the agent must present a commit preview and wait for explicit commit approval. Worktree-backed task status reaches `Completed` through `lifecycle_finalize_task`, not immediately after closeout.

### Todos

No current todo is recorded for this workflow skill.

### Docs References

No external domain documentation applies to this repository-local workflow skill.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

`w-02-light-task-workflow` skill is the approved workflow used by the preliminary onboarding task and the worktree task stack.

| Finding | Anchor | Source |
| --- | --- | --- |
| The skill defines the task wrapper plus `task.md` as the durable plan/checklist artifact for medium work. | `## Task Artifact` | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/SKILL.md:26-38 |
| Agent responsibilities include creating the wrapper artifact, stopping for implementation approval, implementing checklist items, presenting a worktree-backed commit preview, waiting for commit approval before closeout commits, and leaving completion to `lifecycle_finalize_task` after the branch lands. | `## Agent Responsibilities` | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/SKILL.md:61-76 |
| Invariants require wrapper folders, resolved roots, no implementation before approval, a clean committed external-memory baseline before `c-09-git-worktree-manager` skill start, separate commit approval before closeout commits, recording the settled design in the task file's `## Design` section when the Task Collaboration Doctrine warrants it, and no stale task state. | `## Invariants` | mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/SKILL.md:87-112 |

## Cross-Repo References

No sibling repository evidence is needed for the current workflow skill.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Series-Contract Notes

The packaged light-task workflow describes master series as integration-branch wrappers and leaf sub-tasks as the worktree-backed units with their own enclosure contracts and closeout/finalization.

## Update History

- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 3 citation items; scoped citation check now passes.

- 2026-07-06T12:30+02:00 — L10 owner ruling (builder escalation #1): the JSON-primary paragraph's 'chat build' thin-doc example is re-anchored to the smallest single-session build — chat is never a build route; the thin doc IS the minimum artifact. Verification metadata pinned until closeout stamps the L10 commit.

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: packaged light-task workflow now says JSON task docs bind to leaf enclosures, master series use an integration branch, and each active slice gets its own enclosure/worktree. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: documented that worktree-backed light tasks become `Completed` through `lifecycle_finalize_task` after the landed edge is proven, not immediately after closeout. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-19T07:23+02:00: Slice 3c reopened (R5, dry-run/preview) — documented `dry_run=true`: previews (rendered + diff + `wouldLose`) without writing, the safe way to adopt a hand `.md`. Synced from canonical `skills/`. Verification metadata pinned until closeout stamps the R5 code commit.
- 2026-06-19T06:03+02:00: Slice 3c reopened (R4, leaf-doc fidelity) — documented the leaf extensions: a `statusNote` suffix, `headerNotes` extra header lines, and freeform `sections` (the escape hatch, appended after References; the standard sections stay the backbone). Synced from canonical `skills/`. Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T05:15+02:00: Slice 3c reopened (R3, deferred-examples honesty) — documented `codeExamplesNote`: a planning slice that defers its code examples to the plan gate records that via `set_field` so the render reads as deferred rather than none-needed. Synced from canonical `skills/`. Verification metadata pinned until closeout stamps the R3 code commit.
- 2026-06-14T00:16: Slice 3c commit 3 — the JSON-primary format now also covers a series master (`kind:"master"`: a `subTasks` index + ordered `sections`); corrected the Conventions note (the prior "master files stay hand-authored" rationale — a clobbering re-render — no longer applies; masters stay markdown only until the runtime ships `task_doc`). Synced from canonical `skills/`. Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34: Slice 3c commit 2 — documented the JSON-primary task-document format: the `task_doc` MCP tool authors the `ar-task-document/v1` JSON and renders `task.md`; `template.md`/`master-template.md` are the render spec; series master files stay hand-authored markdown (synced from canonical `skills/`). Verification metadata pinned until closeout stamps the 3c commit-2 code commit.
- 2026-06-02T04:25+02:00: Removed heavy-workflow references after W-01 retirement — the Purpose, When To Use, and naming notes no longer point at the heavy workflow; escalation now routes to a master + light sub-task series. L-01 series, Sub-task B/S6, mcp 1.1.0.
- 2026-06-02T04:10+02:00: Added master-task composition — a new `master-template.md` companion, a "Master-Task Composition (task series)" section, and invariant 13 (escalate a too-large task to a master + light sub-task series; one wrapper folder with flat `NN_<name>.md` sub-tasks, one shared worktree, a commit per slice, one integrate + release at the end). `l-01-session-job-lifecycle` skill series, Sub-task B/S5, mcp 1.1.0.
- 2026-05-31T01:06+02:00: Added invariant 12 requiring the settled design in the task file's `## Design` section when the Task Collaboration Doctrine warrants it, and noted the optional design section in conventions.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T04:34+02:00: Updated task-start references after `c-02-memory-quality-control` skill was renamed to memory quality control.
- 2026-05-12T18:51+02:00: Refreshed after the skill frontmatter moved to the lowercase `w-02-light-task-workflow` name.
- 2026-05-11T19:42: Refreshed verification metadata to `aa85d3862bf21fed791e3170e6957f9288c319e8` after confirming `w-02-light-task-workflow` skill remains current after the coordination rename.
- 2026-05-10T01:19: Updated after `w-02-light-task-workflow` skill gained an explicit worktree-backed commit approval handoff before `c-09-git-worktree-manager` skill closeout commits.
- 2026-05-10T00:56: Updated after adding the committed external-memory baseline requirement before `c-09-git-worktree-manager` skill start.
- 2026-05-10T00:47: Updated after light tasks moved from flat task files to wrapper folders containing `task.md`.
- 2026-05-09T21:15: Created first file-level onboarding baseline for `w-02-light-task-workflow` skill documentation.
