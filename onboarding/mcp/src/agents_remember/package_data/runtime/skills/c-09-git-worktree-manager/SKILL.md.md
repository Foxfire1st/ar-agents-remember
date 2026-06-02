# c-09-git-worktree-manager/SKILL.md

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember-md                                           |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-05-26T16:25+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff` |
| lastVerifiedCommitDate | 2026-06-02T16:24:22+02:00|

## Purpose

This skill documents `c-09-git-worktree-manager` skill, the Git worktree lifecycle manager for Agents
Remember tasks. `c-09-git-worktree-manager` skill now owns worktree start, attach/status, external-memory
compatibility before worktree start, integration, and cleanup. Closeout
sequencing belongs to `c-12-closeout` skill; `c-09-git-worktree-manager` skill only supplies the worktree-specific
`contract.md` path and the integration/cleanup follow-up rules.

## Code Commentary

### Logic

The skill defines the worktree MCP entrypoints for start, attach, status,
worktree closeout tool handoff, integration, and cleanup. It states that `c-09-git-worktree-manager` skill
begins after the normal intake and onboarding gate, uses context resolved by the `c-08-ar-coordination-context-resolver` skill
through the MCP worktree tools, refuses external-memory worktree start while
the source memory repo has uncommitted content or ledger changes, and reports
recoverable lifecycle state through typed next-operation hints.

The worktree closeout section is deliberately a routing section, not a parallel
closeout doctrine. It sends the approval gate, missing-onboarding check, code
commit, onboarding/entity refresh, memory quality gate, memory content commit,
ledger update, and ledger commit to `c-12-closeout` skill. For worktree-backed tasks, `c-09-git-worktree-manager` skill
contributes the task `contract.md` used by `worktree_closeout_preview` and
`worktree_closeout_apply`; after closeout, `c-09-git-worktree-manager` skill resumes ownership for
integration and cleanup.

### Conventions

`c-09-git-worktree-manager` skill is a wrapper, not a replacement workflow. Task identity should be settled
before worktree creation: `w-02-light-task-workflow` skill creates `<task-root>/<task-slug>/task.md`, then
`c-09-git-worktree-manager` skill places `contract.md` beside it. External memory incompatibility is
interactive and offers reconciliation, disabled memory, or custom handling; its
common trigger is starting off a freshly-merged gated branch whose PR merge
commit the ledger has not mapped, which `c-11-memory-carryover-from-branch` skill carryover (run after the merge) now
maps automatically so `reconciliation` is not needed. Dirty source memory blocks
start until memory content and ledger updates are committed or the developer
chooses another path.

Integration remains human-gated. `ff-only` lands closed task branches when
source branches did not move; `replay` handles parallel non-overlapping work by
replaying code and memory content, then regenerating the final memory ledger
row. Cleanup remains human-gated and removes worktrees plus merged local task
branches only after integration.

### Invariants And Boundaries

`c-09-git-worktree-manager` skill must not use divergent memory as trusted context, must not bypass `c-12-closeout` skill's
explicit closeout approval gate, and must not create closeout commits outside
`c-12-closeout` skill's code-memory-ledger sequence. Worktree status reports lifecycle phase,
dirty flags, summary, and typed next hints instead of shell commands.
Integration must not move source branches until code and memory commits are
fast-forwardable or replay has produced mediated commits. Cleanup requires
completed integration and explicit approval.

### Todos

No current implementation todo is recorded for the skill contract.

### Docs References

No external documentation is needed for this repository-local skill.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `c-09-git-worktree-manager` skill owns worktree lifecycle and routes closeout to `c-12-closeout` skill. | L8-L14; L63-L74; L97-L105 | [`c-09-git-worktree-manager` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| `c-12-closeout` skill owns the shared closeout approval and code-memory-ledger sequence for direct and worktree closeout. | L8-L29; L33-L82 | [`c-12-closeout` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md) |
| Integration remains owned by the `c-09-git-worktree-manager` skill and covers fast-forward and replay strategies after closeout. | L76-L86 | [`c-09-git-worktree-manager` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| Cleanup remains owned by the `c-09-git-worktree-manager` skill and requires completed integration plus explicit approval. | L88-L94 | [`c-09-git-worktree-manager` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-06-02T04:25+02:00: Dropped the retired heavy-task workflow from the wrapped-workflow list and the intake decision step (now chat, `w-02-light-task-workflow` skill light task, or master + light sub-task series). `l-01-session-job-lifecycle` skill series, Sub-task B/S6, mcp 1.1.0.
- 2026-06-02T04:00+02:00: Added a Start/Attach/Status note that the external-memory "no compatible state" prompt's common trigger is a freshly-merged gated branch whose PR merge commit is unmapped, and that `c-11-memory-carryover-from-branch` skill carryover now maps it automatically after the merge (so `reconciliation` is usually unnecessary). `l-01-session-job-lifecycle` skill series, Sub-task C, mcp 1.1.0.
- 2026-05-29T20:25+02:00: Reviewed for the act-by-default `dry_run` flip — the `c-09-git-worktree-manager` skill worktree examples now omit `dry_run=false` and carry a preview-first note (`dry_run=true` then the real run).
- 2026-05-26T16:25+02:00: Updated after closeout guidance moved to `c-12-closeout` skill and `c-09-git-worktree-manager` skill became worktree lifecycle plus integration/cleanup only.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T05:03+02:00: Updated after `c-09-git-worktree-manager` skill worktree status guidance switched from next safe commands to typed `nextOperation`/`nextTool`/`nextArgs` hints.
- 2026-05-24T04:34+02:00: Updated after closeout guidance routed post-code-commit drift through `c-02-memory-quality-control` skill memory quality control.
- 2026-05-24T03:24+02:00: Updated after `c-09-git-worktree-manager` skill closeout adopted the pre-code-commit `check_missing_onboarding` pass for newly added files.
- 2026-05-24T02:47+02:00: Updated closeout guidance to run drift after the code commit, refresh memory, run `memory_quality_check`, then commit memory and ledger.
- 2026-05-16T18:17+02:00: Documented that external-memory closeout refreshes affected repo entity catalog fingerprints after the code commit and before the memory-content commit.
- 2026-05-12T10:59: Updated the direct-closeout contract after ledger branch metadata stopped being a compatibility condition.
- 2026-05-11T19:42: Refreshed verification metadata to `aa85d3862bf21fed791e3170e6957f9288c319e8` and corrected `c-09-git-worktree-manager` skill source citation ranges after confirming the coordination rename behavior remains current.
- 2026-05-11T18:34: Updated after `c-09-git-worktree-manager` skill command examples adopted `--code-repository-name` and `--code-repository-root`.
- 2026-05-10T03:01: Updated after the `c-09-git-worktree-manager` skill contract added direct checkout closeout for approved micro edits.
- 2026-05-10T01:55: Updated after the closeout contract documented code-commit-first onboarding metadata refresh before memory commit.
- 2026-05-10T01:19: Updated after `c-09-git-worktree-manager` skill split implementation approval from explicit commit approval and added closeout preview guidance.
- 2026-05-10T00:56: Updated to capture the clean external-memory baseline gate before `c-09-git-worktree-manager` skill worktree start.
- 2026-05-10T00:47: Updated for pre-worktree intake, wrapper task placement, lifecycle status, and cleanup command behavior.
- 2026-05-10T00:36: Refreshed verification metadata after approval-gated integration landed on main.
- 2026-05-09T23:55: Updated after documenting the `c-09-git-worktree-manager` skill integration phase and replay/conflict rules.
- 2026-05-09T22:57: Refreshed verification metadata and replaced task-artifact citations with current skill/spec evidence.
- 2026-05-09T22:10: Updated closeout boundary to include source-branch movement checks.
- 2026-05-09T21:59: Created onboarding for the new `c-09-git-worktree-manager` skill.
