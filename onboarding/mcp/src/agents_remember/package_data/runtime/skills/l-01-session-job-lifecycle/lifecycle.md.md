# l-01-session-job-lifecycle/lifecycle.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/lifecycle.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T03:30+02:00                     |
| lastVerifiedCommitHash | `dc25f5a63de359926985c925096aad9019968bf4` |
| lastVerifiedCommitDate | 2026-06-02T18:31:01+02:00|

## Purpose

This companion file is the detailed `l-01-session-job-lifecycle` skill spine: it describes what each of the six phases (orient, ground, frame, decide, build, close) does, the doctrine it carries forward from the retired chat workflow, and the gates between phases. It is where the modernized retrieval and onboarding discipline live in prose.

## Code Commentary

### Logic

Six phases run in order with one branch. `orient` resolves `c-08-ar-coordination-context-resolver` skill context and pulls `context_packet` (onboarding freshness + provider readiness). `ground` runs the single `c-02-memory-quality-control` skill task-start gate and reads committed-state onboarding. `frame` reframes via the tasks doctrine, pulls evidence through `c-04-retrieval-strategy-router` skill, runs the job opening move, and ends at the plan gate. `decide` is the single build-mode branch: read-only exit, or always-worktree build (chat vs durable `w-02-light-task-workflow` skill). `build` implements in the worktree with live per-section onboarding and green tools.md checks before each commit. `close` previews the `c-09-git-worktree-manager` skill closeout, stops at the commit gate, runs the external-memory invariant, lands per git-workflow.md, cleans up, carries over memory, and maps the ledger to the landed commit including the post-merge merge commit.

### Conventions

`c-04-retrieval-strategy-router` skill strategy selection is by question: Semantics (grepai) for "where/what", Relationship (cgc) for callers/callees/impact, Intent (onboarding + bounded source confirmation) for hidden contracts. The paired source+onboarding read is expressed as the Intent strategy. Incremental, pushable commits keep the work-loss window small.

### Invariants And Boundaries

The `c-02-memory-quality-control` skill gate runs once and is not re-triggered just because the job later changes files; do not plan against clean-source drifted/missing-verification/orphaned onboarding until refreshed via `c-05-create-or-update-onboarding-files` skill; leave dirty-source drift alone (dirty != ignore, still read it). No implementation before the frame plan gate. Changed source files need their sidecar body updated this job, not only metadata. Checks green before each commit. The agent never pushes a protected branch directly; landing follows git-workflow.md. A read-only exit skips the close phase entirely.

### Todos

No current todo is recorded for this lifecycle spine file.

### Docs References

No external domain documentation applies to this repository-local lifecycle file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The spine sequences the core skills and defers landing to the repo git-workflow doctrine.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `close` defers landing (PR-gated) and the post-merge ledger entry to `system/git-workflow.md`. | n/a | [git-workflow template](agents-remember-md/mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/git-workflow.md) |
| The entry contract and per-job lenses live alongside this file. | n/a | [SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this lifecycle file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-02T03:30+02:00: Created file-level onboarding for the `l-01-session-job-lifecycle` skill spine companion file, including the close-phase step that maps the ledger to the landed PR merge commit so a later worktree bases off the merged branch without manual reconciliation.
