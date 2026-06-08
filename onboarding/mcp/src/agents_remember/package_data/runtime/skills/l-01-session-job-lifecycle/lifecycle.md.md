# l-01-session-job-lifecycle/lifecycle.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/lifecycle.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-04T15:45+02:00                     |
| lastVerifiedCommitHash | `19b33573a71c8634acfb836d4245f1ead8594f06` |
| lastVerifiedCommitDate | 2026-06-08T12:38:40+02:00|

## Purpose

This companion file is the detailed `l-01-session-job-lifecycle` skill spine: it describes what each of the six phases (request, trust checkpoint, reframe/research, decide, build, close) does, the doctrine it carries forward from the retired chat workflow, and the gates between phases. It is where the developer/model collaboration loop, modernized retrieval, trust checkpoint, and onboarding discipline live in prose.

## Code Commentary

### Logic

Six phases run in order with one branch. `request` receives the developer's raw request and identifies the target repository through `c-08-ar-coordination-context-resolver` skill or MCP authority. It now states that the upcoming Trust Checkpoint reveals whether the request is related to repositories managed by Agents Remember; if not, the lifecycle can exit early, but later work entering a managed-repo boundary must re-enter the lifecycle. `trust checkpoint` runs `context_packet(repo_id="<repo-id>", include_providers=true, include_drift=true)`, reports repo/memory/provider/drift facts, asks the developer about clean-source onboarding drift, treats dirty-source drift as active work-in-progress, and recovers degraded providers through MCP provider/runtime operations before relying on them. `reframe and research` gathers `c-04-retrieval-strategy-router` evidence for a `tasks/AGENTS.md` reframe, gets developer agreement or revision, then performs deeper research whose report uses `deep-research-report-template.md`, ties evidence to supported claims, and lists onboarding docs, semantic queries, code graph queries, source files, and remaining truth gaps. `decide` is the single build-mode branch: research-only exit, or a worktree build that first presents the worktree intent packet and waits for developer approval before `worktree_start`. `build` implements in the worktree with live per-section onboarding and green tools.md checks before each commit. `close` previews the `c-09-git-worktree-manager` skill closeout, stops at the commit gate, runs the external-memory invariant, integrates the worktree branch into the approved source/integration branch before PR-gated landing, cleans up, carries over memory, and maps the ledger to the landed commit including the post-merge merge commit.

### Conventions

`c-04-retrieval-strategy-router` skill strategy selection is by question: Semantics (grepai) for "where/what", Relationship (cgc) for callers/callees/impact, Intent (onboarding + bounded source confirmation) for hidden contracts. The paired source+onboarding read is expressed as the Intent strategy. Provider output remains discovery evidence, not final proof; deeper research uses the companion template to name retrieval queries, source/onboarding reads, evidence limits, and the claims each evidence row supports. Incremental, pushable commits keep the work-loss window small.

### Invariants And Boundaries

The front trust checkpoint is mandatory before memory, provider-backed context, task files, or source interpretation are trusted. Clean-source drifted/missing-verification/orphaned onboarding is a developer choice point before planning; dirty-source drift is reported as active work-in-progress and not adopted unless the developer says so. Degraded providers must be recovered and rechecked or explicitly reported before provider-backed evidence is used. The developer must agree with the reframe before deeper research proceeds. Deeper research still carries the lifecycle proof categories while delegating formatting and evidence IDs to the companion template. No `worktree_start` before the developer approves the worktree intent packet. No implementation before the frame plan gate. Changed source files need their sidecar body updated this job, not only metadata. Checks green before each commit. The agent never pushes a protected branch directly; landing follows git-workflow.md. A research-only exit skips the close phase entirely.

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
| `request` now allows early exit for requests unrelated to Agents Remember managed repositories and requires lifecycle re-entry when later work enters a managed-repo boundary. | L20-L33 | [lifecycle.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/lifecycle.md) |
| `decide` requires a developer-approved worktree intent packet before `worktree_start`, including branch policy, source/work branches, memory mode, landing path, and risks. | L115-L127 | [lifecycle.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/lifecycle.md) |
| `close` integrates the worktree branch into the approved source/integration branch before PR-gated landing, then defers the post-merge ledger entry to `system/git-workflow.md`. | L170-L180 | [lifecycle.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/lifecycle.md) |
| The entry contract and per-job lenses live alongside this file. | n/a | [SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/SKILL.md) |
| The deep research report template owns report shape and evidence formatting while this file keeps the lifecycle proof categories. | L87-L92; L44-L59; L102-L123 | [deep-research-report-template.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/deep-research-report-template.md) |

## Cross-Repo References

No sibling repository evidence is needed for this lifecycle file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-08T11:53+02:00: Updated lifecycle-spine onboarding for the Request-phase managed-repo boundary rule and typo-only wording cleanup. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-04T15:45+02:00: Updated the lifecycle onboarding for the new worktree intent gate and close-road wording: decide now requires approval of the intent packet before `worktree_start`, and close integrates into the approved source/integration branch before PR-gated landing.
- 2026-06-04T14:50+02:00: Updated the lifecycle onboarding for the new companion template: deeper research now links to `deep-research-report-template.md`, keeps required proof categories in the lifecycle, and requires evidence to support specific claims. Verification metadata remains pinned until closeout refreshes it to the code commit.
- 2026-06-03T03:05+02:00: Updated the lifecycle onboarding for the recast front half: developer request, mandatory context packet with providers and drift, clean-source drift choice point, dirty-source drift handling, provider recovery/reporting, evidence-backed reframe agreement, and deeper research proof requirements. Verification metadata remains pinned until closeout refreshes it to the code commit.
- 2026-06-02T03:30+02:00: Created file-level onboarding for the `l-01-session-job-lifecycle` skill spine companion file, including the close-phase step that maps the ledger to the landed PR merge commit so a later worktree bases off the merged branch without manual reconciliation.
