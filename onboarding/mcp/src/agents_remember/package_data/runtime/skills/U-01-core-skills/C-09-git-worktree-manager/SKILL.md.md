# C-09-git-worktree-manager/SKILL.md

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember-md                                           |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-05-26T16:25+02:00                     |
| lastVerifiedCommitHash | `b9b032e0dc9afe70a20db348a8705c2b81d448bb` |
| lastVerifiedCommitDate | 2026-06-02T04:13:16+02:00|

## Purpose

This skill documents C-09, the Git worktree lifecycle manager for Agents
Remember tasks. C-09 now owns worktree start, attach/status, external-memory
compatibility before worktree start, integration, and cleanup. Closeout
sequencing belongs to C-12; C-09 only supplies the worktree-specific
`contract.md` path and the integration/cleanup follow-up rules.

## Code Commentary

### Logic

The skill defines the worktree MCP entrypoints for start, attach, status,
worktree closeout tool handoff, integration, and cleanup. It states that C-09
begins after the normal intake and onboarding gate, uses C-08-resolved context
through the MCP worktree tools, refuses external-memory worktree start while
the source memory repo has uncommitted content or ledger changes, and reports
recoverable lifecycle state through typed next-operation hints.

The worktree closeout section is deliberately a routing section, not a parallel
closeout doctrine. It sends the approval gate, missing-onboarding check, code
commit, onboarding/entity refresh, memory quality gate, memory content commit,
ledger update, and ledger commit to C-12. For worktree-backed tasks, C-09
contributes the task `contract.md` used by `worktree_closeout_preview` and
`worktree_closeout_apply`; after closeout, C-09 resumes ownership for
integration and cleanup.

### Conventions

C-09 is a wrapper, not a replacement workflow. Task identity should be settled
before worktree creation: W-02 creates `<task-root>/<task-slug>/task.md`, then
C-09 places `contract.md` beside it. External memory incompatibility is
interactive and offers reconciliation, disabled memory, or custom handling; its
common trigger is starting off a freshly-merged gated branch whose PR merge
commit the ledger has not mapped, which C-11 carryover (run after the merge) now
maps automatically so `reconciliation` is not needed. Dirty source memory blocks
start until memory content and ledger updates are committed or the developer
chooses another path.

Integration remains human-gated. `ff-only` lands closed task branches when
source branches did not move; `replay` handles parallel non-overlapping work by
replaying code and memory content, then regenerating the final memory ledger
row. Cleanup remains human-gated and removes worktrees plus merged local task
branches only after integration.

### Invariants And Boundaries

C-09 must not use divergent memory as trusted context, must not bypass C-12's
explicit closeout approval gate, and must not create closeout commits outside
C-12's code-memory-ledger sequence. Worktree status reports lifecycle phase,
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
| C-09 owns worktree lifecycle and routes closeout to C-12. | L8-L14; L63-L74; L97-L105 | [C-09 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) |
| C-12 owns the shared closeout approval and code-memory-ledger sequence for direct and worktree closeout. | L8-L29; L33-L82 | [C-12 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-12-closeout/SKILL.md) |
| Integration remains C-09-owned and covers fast-forward and replay strategies after closeout. | L76-L86 | [C-09 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) |
| Cleanup remains C-09-owned and requires completed integration plus explicit approval. | L88-L94 | [C-09 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-06-02T04:25+02:00: Dropped the retired heavy-task workflow from the wrapped-workflow list and the intake decision step (now chat, W-02 light task, or master + light sub-task series). L-01 series, Sub-task B/S6, mcp 1.1.0.
- 2026-06-02T04:00+02:00: Added a Start/Attach/Status note that the external-memory "no compatible state" prompt's common trigger is a freshly-merged gated branch whose PR merge commit is unmapped, and that C-11 carryover now maps it automatically after the merge (so `reconciliation` is usually unnecessary). L-01 series, Sub-task C, mcp 1.1.0.
- 2026-05-29T20:25+02:00: Reviewed for the act-by-default `dry_run` flip — the C-09 worktree examples now omit `dry_run=false` and carry a preview-first note (`dry_run=true` then the real run).
- 2026-05-26T16:25+02:00: Updated after closeout guidance moved to C-12 and C-09 became worktree lifecycle plus integration/cleanup only.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T05:03+02:00: Updated after C-09 worktree status guidance switched from next safe commands to typed `nextOperation`/`nextTool`/`nextArgs` hints.
- 2026-05-24T04:34+02:00: Updated after closeout guidance routed post-code-commit drift through C-02 memory quality control.
- 2026-05-24T03:24+02:00: Updated after C-09 closeout adopted the pre-code-commit `check_missing_onboarding` pass for newly added files.
- 2026-05-24T02:47+02:00: Updated closeout guidance to run drift after the code commit, refresh memory, run `memory_quality_check`, then commit memory and ledger.
- 2026-05-16T18:17+02:00: Documented that external-memory closeout refreshes affected repo entity catalog fingerprints after the code commit and before the memory-content commit.
- 2026-05-12T10:59: Updated the direct-closeout contract after ledger branch metadata stopped being a compatibility condition.
- 2026-05-11T19:42: Refreshed verification metadata to `aa85d3862bf21fed791e3170e6957f9288c319e8` and corrected C-09 source citation ranges after confirming the coordination rename behavior remains current.
- 2026-05-11T18:34: Updated after C-09 command examples adopted `--code-repository-name` and `--code-repository-root`.
- 2026-05-10T03:01: Updated after the C-09 contract added direct checkout closeout for approved micro edits.
- 2026-05-10T01:55: Updated after the closeout contract documented code-commit-first onboarding metadata refresh before memory commit.
- 2026-05-10T01:19: Updated after C-09 split implementation approval from explicit commit approval and added closeout preview guidance.
- 2026-05-10T00:56: Updated to capture the clean external-memory baseline gate before C-09 worktree start.
- 2026-05-10T00:47: Updated for pre-worktree intake, wrapper task placement, lifecycle status, and cleanup command behavior.
- 2026-05-10T00:36: Refreshed verification metadata after approval-gated integration landed on main.
- 2026-05-09T23:55: Updated after documenting the C-09 integration phase and replay/conflict rules.
- 2026-05-09T22:57: Refreshed verification metadata and replaced task-artifact citations with current skill/spec evidence.
- 2026-05-09T22:10: Updated closeout boundary to include source-branch movement checks.
- 2026-05-09T21:59: Created onboarding for the new C-09 skill.
