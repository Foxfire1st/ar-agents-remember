# l-01-session-job-lifecycle/lifecycle.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-session-job-lifecycle/lifecycle.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-03T03:05+02:00                     |
| lastVerifiedCommitHash | `8db105a67d985bd09836f790ba862d668c786d8d` |
| lastVerifiedCommitDate | 2026-06-03T04:19:25+02:00|

## Purpose

This companion file is the detailed `l-01-session-job-lifecycle` skill spine: it describes what each of the six phases (request, trust checkpoint, reframe/research, decide, build, close) does, the doctrine it carries forward from the retired chat workflow, and the gates between phases. It is where the developer/model collaboration loop, modernized retrieval, trust checkpoint, and onboarding discipline live in prose.

## Code Commentary

### Logic

Six phases run in order with one branch. `request` receives the developer's raw request and identifies the target repository through `c-08-ar-coordination-context-resolver` skill or MCP authority. `trust checkpoint` runs `context_packet(repo_id="<repo-id>", include_providers=true, include_drift=true)`, reports repo/memory/provider/drift facts, asks the developer about clean-source onboarding drift, treats dirty-source drift as active work-in-progress, and recovers degraded providers through MCP provider/runtime operations before relying on them. `reframe and research` gathers `c-04-retrieval-strategy-router` evidence for a `tasks/AGENTS.md` reframe, gets developer agreement or revision, then performs deeper research whose report lists onboarding docs, semantic queries, code graph queries, source files, and remaining truth gaps. `decide` is the single build-mode branch: research-only exit, or always-worktree build (chat vs durable `w-02-light-task-workflow` skill). `build` implements in the worktree with live per-section onboarding and green tools.md checks before each commit. `close` previews the `c-09-git-worktree-manager` skill closeout, stops at the commit gate, runs the external-memory invariant, lands per git-workflow.md, cleans up, carries over memory, and maps the ledger to the landed commit including the post-merge merge commit.

### Conventions

`c-04-retrieval-strategy-router` skill strategy selection is by question: Semantics (grepai) for "where/what", Relationship (cgc) for callers/callees/impact, Intent (onboarding + bounded source confirmation) for hidden contracts. The paired source+onboarding read is expressed as the Intent strategy. Provider output remains discovery evidence, not final proof; deeper research must name the retrieval queries and source/onboarding reads it used. Incremental, pushable commits keep the work-loss window small.

### Invariants And Boundaries

The front trust checkpoint is mandatory before memory, provider-backed context, task files, or source interpretation are trusted. Clean-source drifted/missing-verification/orphaned onboarding is a developer choice point before planning; dirty-source drift is reported as active work-in-progress and not adopted unless the developer says so. Degraded providers must be recovered and rechecked or explicitly reported before provider-backed evidence is used. The developer must agree with the reframe before deeper research proceeds. No implementation before the frame plan gate. Changed source files need their sidecar body updated this job, not only metadata. Checks green before each commit. The agent never pushes a protected branch directly; landing follows git-workflow.md. A research-only exit skips the close phase entirely.

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

- 2026-06-03T03:05+02:00: Updated the lifecycle onboarding for the recast front half: developer request, mandatory context packet with providers and drift, clean-source drift choice point, dirty-source drift handling, provider recovery/reporting, evidence-backed reframe agreement, and deeper research proof requirements. Verification metadata remains pinned until closeout refreshes it to the code commit.
- 2026-06-02T03:30+02:00: Created file-level onboarding for the `l-01-session-job-lifecycle` skill spine companion file, including the close-phase step that maps the ledger to the landed PR merge commit so a later worktree bases off the merged branch without manual reconciliation.
