# c-09-git-worktree-manager/SKILL.md

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember-md                                           |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-06-10T10:26+02:00                     |
| lastVerifiedCommitHash | `f62c732df2acc30ec3766f83c176a24b39c0bc46` |
| lastVerifiedCommitDate | 2026-06-10T10:41:09+02:00|

## Purpose

This skill documents `c-09-git-worktree-manager` skill, the Git worktree lifecycle manager for Agents
Remember tasks. `c-09-git-worktree-manager` skill now owns worktree start, attach/status, external-memory
compatibility before worktree start, integration, and cleanup. Closeout
sequencing belongs to `c-12-closeout` skill; `c-09-git-worktree-manager` skill only supplies the worktree-specific
`contract.md` path and the integration/cleanup follow-up rules.

## Code Commentary

### Logic

The skill defines the worktree MCP entrypoints for start, attach, status,
mid-task sync, worktree closeout tool handoff, integration, and cleanup. Since
the GitHub #54 series it documents the stale-base preflight (start blocks when
a source branch is behind/diverged from its upstream, with
`stale_base_choice="fast-forward"`/`"proceed-stale"` recoveries), the
auto-created external-memory source branch (official-tip base, code branch
name as template, reported as `memorySourceBranch`), the fetch-free
`worktree_status` freshness block with its `syncHint`, and the new **Mid-Task
Sync** section: `worktree_sync` pulls a moved official line into the live
worktree atomically (new code tip must be ledger-mapped at the official memory
tip; sync early — before memories are written — for the pure fast-forward
path; `memory_sync_choice` recoveries when local memory commits diverge). It states that `c-09-git-worktree-manager` skill
begins after the normal intake and onboarding gate, uses context resolved by the `c-08-ar-coordination-context-resolver` skill
through the MCP worktree tools, refuses external-memory worktree start while
the source memory repo has uncommitted content or ledger changes, and reports
recoverable lifecycle state through typed next-operation hints. It now also
requires agents to identify the branch that `worktree_integrate` would move
before `worktree_start`; when that branch is protected, PR-gated, or otherwise
not directly landable, agents must first create or check out a pushable
integration branch and use that branch as the worktree `source_branch`. Before
calling `worktree_start`, agents must present a Worktree Intent Gate for
developer approval; the packet names the repo, build mode, branch policy,
source branch, work branch/worktree name, memory mode, landing path, and risks.

The worktree closeout section is deliberately a routing section, not a parallel
closeout doctrine. It sends the approval gate, missing-onboarding check, code
commit, onboarding/entity refresh, memory quality gate, memory content commit,
ledger update, and ledger commit to `c-12-closeout` skill. For worktree-backed tasks, `c-09-git-worktree-manager` skill
contributes the task `contract.md` used by `worktree_closeout_preview` and
`worktree_closeout_apply`; after closeout, `c-09-git-worktree-manager` skill resumes ownership for
integration and cleanup.
Before previewing integration, agents must also check out the recorded code and
memory `source_branch` in the source repositories because `worktree_integrate`
requires those active checkouts even for `dry_run=true`.

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
row. The recorded `source_branch` is the integration target, not just a base
branch: `worktree_integrate` will move it and will not open a PR or discover
protected-branch policy on its own. For PR-gated repositories, the approved
intent packet must make clear that the protected target is not the recorded
`source_branch`; the source branch is the pushable branch that will later be
pushed for PR. Integration preview also expects the recorded code and memory
source branches to be the active checkouts in the source repositories, so agents
should switch clean source checkouts before calling `worktree_integrate` with
`dry_run=true`. Cleanup remains human-gated and removes worktrees plus merged
local task branches only after integration.

### Invariants And Boundaries

`c-09-git-worktree-manager` skill must not use divergent memory as trusted context, must not bypass `c-12-closeout` skill's
explicit closeout approval gate, and must not create closeout commits outside
`c-12-closeout` skill's code-memory-ledger sequence. Worktree status reports lifecycle phase,
dirty flags, summary, and typed next hints instead of shell commands.
Integration must not move source branches until code and memory commits are
fast-forwardable or replay has produced mediated commits. The skill must not
call `worktree_start` until the developer has approved the Worktree Intent Gate.
For protected, PR-gated, or otherwise not-directly-landable target branches, the
selected `source_branch` must be a developer-approved pushable integration
branch created from that target, not the protected target itself. Cleanup
requires completed integration and explicit approval.

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
| `c-09-git-worktree-manager` skill owns worktree lifecycle and routes closeout to `c-12-closeout` skill. | L8-L13; L103-L115; L140-L152 | [`c-09-git-worktree-manager` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| `c-12-closeout` skill owns the shared closeout approval and code-memory-ledger sequence for direct and worktree closeout. | L8-L29; L33-L82 | [`c-12-closeout` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md) |
| The source-branch contract says protected, PR-gated, or otherwise not-directly-landable targets need a pushable integration branch before `worktree_start`, because integration lands into the recorded `source_branch`. | L49-L59; L72-L87; L121-L128 | [`c-09-git-worktree-manager` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| The Worktree Intent Gate must be explicitly approved before `worktree_start` and must name branch policy, source/work branches, memory mode, landing path, and risks. | L55-L75; L150-L151 | [`c-09-git-worktree-manager` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| Integration preview requires the recorded code and memory `source_branch` to be checked out in the source repositories, even for `dry_run=true`. | L117-L125 | [`c-09-git-worktree-manager` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| Integration remains owned by the `c-09-git-worktree-manager` skill and covers fast-forward and replay strategies after closeout. | L117-L134 | [`c-09-git-worktree-manager` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |
| Cleanup remains owned by the `c-09-git-worktree-manager` skill and requires completed integration plus explicit approval. | L136-L140 | [`c-09-git-worktree-manager` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-06-10T10:26+02:00 — GitHub #54: documented the stale-base preflight + `stale_base_choice` recoveries, the auto-created memory source branch, the `worktree_status` freshness block, `worktree_sync` in the MCP tools list, and the new Mid-Task Sync section (sync-early-before-memories doctrine).
- 2026-06-04T16:03+02:00: Added the integration-preview reminder that agents must check out the recorded code and memory `source_branch` in the source repositories before calling `worktree_integrate`, including `dry_run=true`.
- 2026-06-04T15:45+02:00: Added the Worktree Intent Gate: agents must present branch policy, pushable source branch, work branch/worktree name, memory mode, landing path, and risks for developer approval before `worktree_start`; PR-gated flows must show that the recorded `source_branch` is the pushable integration branch, not the protected target.
- 2026-06-03T04:06+02:00: Clarified the source-branch contract for protected or PR-gated targets: before `worktree_start`, choose a pushable integration branch as `source_branch`, because `worktree_integrate` lands into the recorded source branch and does not open PRs or infer branch protection.
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
