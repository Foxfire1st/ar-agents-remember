# l-01-session-job-lifecycle/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-04T14:50+02:00                     |
| lastVerifiedCommitHash | `39ab8694f3f0a83f75a5484fa39e526e78d2cdad` |
| lastVerifiedCommitDate | 2026-06-04T15:08:01+02:00|

## Purpose

This file is the entry contract for `l-01-session-job-lifecycle` skill, the session job lifecycle the coordinator routes every session into. It defines the shared spine (request -> trust checkpoint -> reframe/research -> decide -> build -> close), the build-mode decision that is now the only task-format call, research-only exits after investigation, the four job lenses, the companion files including the deep research report template, and the invariants that keep memory, developer agreement, evidence gathering, and tests in lockstep with code.

## Code Commentary

### Logic

The skill frames `l-01-session-job-lifecycle` skill as a canvas rather than a task format. It now states the front half as a developer/model collaboration loop: the developer states the request, the model resolves context through `context_packet(... include_providers=true, include_drift=true)`, the model handles drift and provider readiness before trusting memory, the model gathers `c-04-retrieval-strategy-router` evidence for a `tasks/AGENTS.md` reframe, and the developer agrees or revises that reframe before deeper research. It then carries the build-mode decision (research-only exit, chat build, or durable `w-02-light-task-workflow` skill task), the relationship to the core skills it sequences (`c-04-retrieval-strategy-router` skill, `c-05-create-or-update-onboarding-files` skill, `c-08-ar-coordination-context-resolver` skill, `c-09-git-worktree-manager` skill, `c-11-memory-carryover-from-branch` skill), and the invariants that protect the collaboration and build gates. Detailed phase behavior lives in `lifecycle.md`; the per-job lenses live in `job-variants.md`; the reusable deep research report and evidence-ledger shape lives in `deep-research-report-template.md`.

### Conventions

The frontmatter `name` is lowercase (`l-01-session-job-lifecycle`) so the flat-layout installer accepts it (`[a-z0-9][a-z0-9-]*`); the folder name keeps an uppercase ID prefix matching the sibling-skill directory convention. The skill is multi-file like the `w-02-light-task-workflow` skill (SKILL.md entry plus companion files). It supersedes the retired chat workflow without naming it by a dead identifier.

### Invariants And Boundaries

Every session enters `l-01-session-job-lifecycle` skill; the job type is a lens, never a gate. The model must run the MCP context packet with providers and drift before trusting onboarding or provider-backed context. Clean-source drift creates a developer choice point for `c-05-create-or-update-onboarding-files`; dirty-source drift is reported as active work-in-progress. Degraded providers are recovered through MCP provider/runtime operations and rechecked. Persistent provider issues are reported to the developer before provider-backed evidence is used. The developer is the state authority for reframe agreement: the model does not proceed to deeper research while the developer disagrees. Research reports use the deep research template and still list onboarding docs, semantic queries, code graph queries, source files, and truth gaps. `build => worktree`; `durable task => worktree + task.md`; `chat build => worktree, no artifact`; `research-only => no worktree`. No implementation before the `frame` plan gate; implementation approval is not commit approval. Onboarding is refreshed live per completed plan-section; tools.md checks run green before each incremental commit. The agent never pushes a protected branch on its own authority. `l-01-session-job-lifecycle` skill must cover everything the retired chat workflow did plus the job lens, developer-agreed reframe, proof-bearing research, and research-only exit, with no default-path regression.

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
| The spine detail, per-job lenses, and reusable deep research report shape live in companion files listed by the entry contract. | L29-L33; L94-L98 | [SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this lifecycle skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-04T14:50+02:00: Updated the entry-contract onboarding for the new deep research report template companion file and the invariant that deeper research reports use that template while preserving the lifecycle's proof categories. Verification metadata remains pinned until closeout refreshes it to the code commit.
- 2026-06-03T03:05+02:00: Updated the entry-contract onboarding for the recast front half: request, context packet with providers and drift, drift/provider choice points, developer-agreed reframe, proof-bearing deeper research, and research-only exits. Verification metadata remains pinned until closeout refreshes it to the code commit.
- 2026-06-02T03:30+02:00: Created file-level onboarding for the new L-01 session job lifecycle skill, the canvas the coordinator routes into; it supersedes the retired chat workflow (W-03) by migrating and modernizing its doctrine and adds the job lens plus the no-worktree answer exit.
