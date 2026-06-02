# L-01-session-job-lifecycle/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/L-01-session-job-lifecycle/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T03:30+02:00                     |
| lastVerifiedCommitHash | `4e80f678776b449b4bc1a756fc4f3f8d5ce5198c` |
| lastVerifiedCommitDate | 2026-06-02T03:41:17+02:00|

## Purpose

This file is the entry contract for L-01, the session job lifecycle the coordinator routes every session into. It defines the shared spine (orient -> ground -> frame -> decide -> build -> close), the build-mode decision that is now the only task-format call, the four job lenses, and the invariants that keep memory and tests in lockstep with code.

## Code Commentary

### Logic

The skill frames L-01 as a canvas rather than a task format. It states the spine at a glance, then carries the build-mode decision (read-only exit, chat build, or durable W-02 task), the relationship to the core skills it sequences (C-02, C-04, C-05, C-08, C-09, C-11), and eleven invariants. Detailed phase behavior lives in `lifecycle.md`; the per-job lenses live in `job-variants.md`.

### Conventions

The frontmatter `name` is lowercase (`l-01-session-job-lifecycle`) so the flat-layout installer accepts it (`[a-z0-9][a-z0-9-]*`); the folder name keeps the uppercase `L-01-` prefix matching the W-0x/U-01 sibling convention. The skill is multi-file like W-02 (SKILL.md entry plus companion files). It supersedes the retired chat workflow without naming it by a dead identifier.

### Invariants And Boundaries

Every session enters L-01; the job type is a lens, never a gate. `build => worktree`; `durable task => worktree + task.md`; `chat build => worktree, no artifact`; `read-only => no worktree`. No implementation before the `frame` plan gate; implementation approval is not commit approval. Onboarding is refreshed live per completed plan-section; tools.md checks run green before each incremental commit. The agent never pushes a protected branch on its own authority. L-01 must cover everything the retired chat workflow did plus the job lens and read-only exit, with no default-path regression.

### Todos

No current todo is recorded for this lifecycle skill.

### Docs References

No external domain documentation applies to this repository-local lifecycle skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

L-01 is the lifecycle the coordinator `AGENTS.md` routes into; it sequences the C-0x core skills and hands off to W-02 for durable task builds.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The coordinator and root `AGENTS.md` route every session into L-01 and reduce task-format choice to L-01's build-mode step. | n/a | [coordinator AGENTS.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md) |
| The spine detail and the per-job lenses live in the two companion files. | n/a | [lifecycle.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/L-01-session-job-lifecycle/lifecycle.md) |

## Cross-Repo References

No sibling repository evidence is needed for this lifecycle skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-02T03:30+02:00: Created file-level onboarding for the new L-01 session job lifecycle skill, the canvas the coordinator routes into; it supersedes the retired chat workflow (W-03) by migrating and modernizing its doctrine and adds the job lens plus the read-only exit.
