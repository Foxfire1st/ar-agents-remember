# l-01-session-job-lifecycle/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-12T19:47+02:00                     |
| lastVerifiedCommitHash | `6f1a7e9028d5d4858cf9c645f2448d5395fafc6a` |
| lastVerifiedCommitDate | 2026-06-12T19:52:16+02:00|

## Purpose

This file is the complete entry contract for `l-01-session-job-lifecycle` skill, the session job lifecycle the coordinator routes every session into. It now carries the full shared spine inline (request -> trust checkpoint -> reframe/research -> decide -> build -> close), the build-mode decision that is the only task-format call, research-only exits after investigation, the two remaining companion files (`job-variants.md` and `deep-research-report-template.md`), and the invariants that keep memory, developer agreement, evidence gathering, onboarding, and tests in lockstep with code. The previous `lifecycle.md` companion was consolidated into this file so agents cannot stop after `SKILL.md` and skip the phase doctrine.

## Code Commentary

### Logic

The skill frames `l-01-session-job-lifecycle` skill as a canvas rather than a task format. It now states the front half as a developer/model collaboration loop: the developer states the request, the model resolves context through `context_packet(... include_providers=true, include_drift=true)`, the model handles drift and provider readiness before trusting memory, the model gathers `c-04-retrieval-strategy-router` evidence for a `tasks/AGENTS.md` reframe, and the developer agrees or revises that reframe before deeper research. It then carries the build-mode decision (research-only exit, chat build, or durable `w-02-light-task-workflow` skill task), the relationship to the core skills it sequences (`c-04-retrieval-strategy-router` skill, `c-05-create-or-update-onboarding-files` skill, `c-08-ar-coordination-context-resolver` skill, `c-09-git-worktree-manager` skill, `c-11-memory-carryover-from-branch` skill), and the invariants that protect the collaboration and build gates.

The former `lifecycle.md` phase detail is now inline. `request` receives the developer's raw request and identifies the target repository; the trust checkpoint reveals whether the request is inside Agents Remember managed-repo scope and requires lifecycle re-entry if later work crosses that boundary. `trust checkpoint` runs `context_packet(repo_id="<repo-id>", include_providers=true, include_drift=true, include_freshness=true)`, reports repo/memory/provider/drift facts — including any `indexing` busy targets from the providers summary, which the agent relays to the developer as healthy-but-mid-scan (results may be partial until the scan completes), plus branch freshness (GitHub #54: behind/diverged code or memory checkouts mean the local official line is stale and should be fast-forwarded before trusting analysis; `ledgerMapsCodeHead=false` means the memory checkout does not match the code state) — asks about clean-source onboarding drift, treats dirty-source drift as active work-in-progress, and recovers degraded providers before relying on them. `reframe and research` gathers `c-04-retrieval-strategy-router` evidence for a `tasks/AGENTS.md` reframe, gets developer agreement or revision, then performs proof-bearing deeper research. `decide` is the single build-mode branch: research-only exit, or a worktree build that first presents the worktree intent packet and waits for developer approval before `worktree_start`. `build` implements in the worktree with live per-section onboarding and green checks before each commit, watching `worktree_status`'s freshness block and syncing a moved official line in early via `worktree_sync` (GitHub #54: before memories are written, the sync is a pure fast-forward and integration stays ff-only). `close` previews the `c-09-git-worktree-manager` skill closeout (worktree-only — the close step no longer offers a `direct_closeout_preview` alternative, issue #62), stops at the commit gate, runs the external-memory invariant, integrates the worktree branch into the approved source/integration branch before PR-gated landing, cleans up, carries over memory, and maps the ledger to the landed commit including the post-merge merge commit.

The per-job lenses live in `job-variants.md`; the reusable deep research report and evidence-ledger shape lives in `deep-research-report-template.md`.

The skill also carries the gate protocol: every lifecycle gate (reframe agreement, plan gate, worktree intent, commit approval, push approval, integration, cleanup) is two turns, never one. The report turn delivers the complete gate report as plain assistant output ending with the approval question in prose; the action turn invokes the gated tool only after the developer replies. The report turn must not contain a structured question widget, a mutating tool call, or any permission-triggering operation, because harnesses render approval prompts over or instead of same-turn prose and the developer never sees a report attached to its own approval prompt.

### Conventions

The frontmatter `name` is lowercase (`l-01-session-job-lifecycle`) so the flat-layout installer accepts it (`[a-z0-9][a-z0-9-]*`), and the skill directory uses the same lowercase ID. The skill remains multi-file like the `w-02-light-task-workflow` skill, but its phase behavior lives in `SKILL.md` rather than in a separate lifecycle companion. It supersedes the retired chat workflow without naming it by a dead identifier.

### Invariants And Boundaries

Every session enters `l-01-session-job-lifecycle` skill; the job type is a lens, never a gate. The model must run the MCP context packet with providers and drift before trusting onboarding or provider-backed context. Clean-source drift creates a developer choice point for `c-05-create-or-update-onboarding-files`; dirty-source drift is reported as active work-in-progress. Degraded providers are recovered through MCP provider/runtime operations and rechecked. Persistent provider issues are reported to the developer before provider-backed evidence is used. The developer is the state authority for reframe agreement: the model does not proceed to deeper research while the developer disagrees. Research reports use the deep research template and still list onboarding docs, semantic queries, code graph queries, source files, and truth gaps. `build => worktree`; `durable task => worktree + task.md`; `chat build => worktree, no artifact`; `research-only => no worktree`. Before `worktree_start`, the model must present a worktree intent packet and the developer must approve or revise it. No implementation before the `frame` plan gate; implementation approval is not commit approval. Onboarding is refreshed live per completed plan-section; tools.md checks run green before each incremental commit. The agent never pushes a protected branch on its own authority. `l-01-session-job-lifecycle` skill must cover everything the retired chat workflow did plus the job lens, developer-agreed reframe, proof-bearing research, and research-only exit, with no default-path regression.

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
| The coordinator and root `AGENTS.md` route every session into `l-01-session-job-lifecycle` skill and reduce task-format choice to `l-01-session-job-lifecycle` skill's build-mode step. | n/a | [coordinator AGENTS.md](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md) |
| The lifecycle phase spine now lives inline in `SKILL.md`; companion files are limited to the job lenses and deeper-research report template. | L17-L20; L49-L216 | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md) |
| The build-mode invariant requires a developer-approved worktree intent packet before `worktree_start`. | L147-L168 | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md) |
| The gate protocol makes every lifecycle gate a report turn followed by an action turn, with no approval mechanism raised in the report turn. | L28-L45 | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this lifecycle skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-12T19:47+02:00 — Added the Gate Protocol section: every lifecycle gate is two turns (report turn delivering the full gate report ending with a prose approval question, then the action turn invoking the gated tool after the developer replies); the report turn must not raise question widgets, mutating tool calls, or permission prompts, which harnesses render over same-turn prose.
- 2026-06-11T06:47+02:00 — Issue #62 worktree-only closeout: the close step offers only `worktree_closeout_preview`; the conditional `direct_closeout_preview` escape hatch ("only if the repo's git-workflow.md permits a direct-checkout build") was removed.
- 2026-06-10T10:26+02:00 — GitHub #54: trust checkpoint adds `include_freshness=true` (branch freshness + `ledgerMapsCodeHead` reporting), and the build phase gains the watch-and-sync-early doctrine (`worktree_status` freshness → `worktree_sync` before memories are written).
- 2026-06-10T06:20+02:00 — Body-quality pass: merged the `indexing` busy-target relay into the trust-checkpoint prose in Logic (documentation only).
- 2026-06-09T22:10+02:00 — Trust checkpoint step 5 now tells agents to report the providers summary's `indexing` busy targets to the developer: those providers are healthy but mid-scan, and their results may be partial until the scan completes (paired with the 2.5.0 `ProviderSummary.indexing` field).
- 2026-06-09T15:26+02:00: Consolidated the detailed lifecycle spine from the deleted `lifecycle.md` companion into `SKILL.md`, leaving only `job-variants.md` and `deep-research-report-template.md` as companion files. Updated references and preserved the phase behavior in this sidecar so agents get the complete lifecycle contract from the skill entry file. Verification metadata remains pinned until closeout refreshes it to the code commit.
- 2026-06-04T15:45+02:00: Updated the entry-contract onboarding for the new worktree intent gate: before `worktree_start`, the model must present repo/build mode, branch policy, source and work branches, memory mode, landing path, and risks for developer approval.
- 2026-06-04T14:50+02:00: Updated the entry-contract onboarding for the new deep research report template companion file and the invariant that deeper research reports use that template while preserving the lifecycle's proof categories. Verification metadata remains pinned until closeout refreshes it to the code commit.
- 2026-06-03T03:05+02:00: Updated the entry-contract onboarding for the recast front half: request, context packet with providers and drift, drift/provider choice points, developer-agreed reframe, proof-bearing deeper research, and research-only exits. Verification metadata remains pinned until closeout refreshes it to the code commit.
- 2026-06-02T03:30+02:00: Created file-level onboarding for the new L-01 session job lifecycle skill, the canvas the coordinator routes into; it supersedes the retired chat workflow (W-03) by migrating and modernizing its doctrine and adds the job lens plus the no-worktree answer exit.
