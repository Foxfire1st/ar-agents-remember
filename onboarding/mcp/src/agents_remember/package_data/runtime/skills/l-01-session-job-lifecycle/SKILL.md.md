# l-01-session-job-lifecycle/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T03:30+02:00                     |
| lastVerifiedCommitHash | `dc25f5a63de359926985c925096aad9019968bf4` |
| lastVerifiedCommitDate | 2026-06-02T18:31:01+02:00|

## Purpose

This file is the entry contract for `l-01-session-job-lifecycle` skill, the session job lifecycle the coordinator routes every session into. It defines the shared spine (orient -> ground -> frame -> decide -> build -> close), the build-mode decision that is now the only task-format call, the four job lenses, and the invariants that keep memory and tests in lockstep with code.

## Code Commentary

### Logic

The skill frames `l-01-session-job-lifecycle` skill as a canvas rather than a task format. It states the spine at a glance, then carries the build-mode decision (read-only exit, chat build, or durable `w-02-light-task-workflow` skill task), the relationship to the core skills it sequences (`c-02-memory-quality-control` skill, `c-04-retrieval-strategy-router` skill, `c-05-create-or-update-onboarding-files` skill, `c-08-ar-coordination-context-resolver` skill, `c-09-git-worktree-manager` skill, `c-11-memory-carryover-from-branch` skill), and eleven invariants. Detailed phase behavior lives in `lifecycle.md`; the per-job lenses live in `job-variants.md`.

### Conventions

The frontmatter `name` is lowercase (`l-01-session-job-lifecycle`) so the flat-layout installer accepts it (`[a-z0-9][a-z0-9-]*`); the folder name keeps an uppercase ID prefix matching the sibling-skill directory convention. The skill is multi-file like the `w-02-light-task-workflow` skill (SKILL.md entry plus companion files). It supersedes the retired chat workflow without naming it by a dead identifier.

### Invariants And Boundaries

Every session enters `l-01-session-job-lifecycle` skill; the job type is a lens, never a gate. `build => worktree`; `durable task => worktree + task.md`; `chat build => worktree, no artifact`; `read-only => no worktree`. No implementation before the `frame` plan gate; implementation approval is not commit approval. Onboarding is refreshed live per completed plan-section; tools.md checks run green before each incremental commit. The agent never pushes a protected branch on its own authority. `l-01-session-job-lifecycle` skill must cover everything the retired chat workflow did plus the job lens and read-only exit, with no default-path regression.

### Todos

No current todo is recorded for this lifecycle skill.

### Docs References

No external domain documentation applies to this repository-local lifecycle skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

`l-01-session-job-lifecycle` skill is the lifecycle the coordinator `AGENTS.md` routes into; it sequences the C-0x core skills and hands off to `w-02-light-task-workflow` skill for durable task builds.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The coordinator and root `AGENTS.md` route every session into `l-01-session-job-lifecycle` skill and reduce task-format choice to `l-01-session-job-lifecycle` skill's build-mode step. | n/a | [coordinator AGENTS.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md) |
| The spine detail and the per-job lenses live in the two companion files. | n/a | [lifecycle.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/lifecycle.md) |

## Cross-Repo References

No sibling repository evidence is needed for this lifecycle skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-02T03:30+02:00: Created file-level onboarding for the new L-01 session job lifecycle skill, the canvas the coordinator routes into; it supersedes the retired chat workflow (W-03) by migrating and modernizing its doctrine and adds the job lens plus the read-only exit.
