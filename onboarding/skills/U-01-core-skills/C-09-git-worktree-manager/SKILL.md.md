# C-09-git-worktree-manager/SKILL.md

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember-md                                           |
| path                   | `skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-05-12T10:59                                             |
| lastVerifiedCommitHash | `3274222c6f818f2241073eecd351cc6f6cb43e07`                   |
| lastVerifiedCommitDate | 2026-05-12T11:38:46+02:00|

## Purpose

This skill documents C-09, the Git lifecycle manager that wraps existing task workflows with pre-worktree intake expectations, code/memory worktree setup, lifecycle status, human-approved worktree closeout, human-approved direct checkout closeout, human-approved integration back to source branches, and human-approved cleanup.

## Code Commentary

### Logic

The skill defines `start`, `attach`, `status`, `bootstrap-memory`, `closeout`, `direct-closeout`, `integrate`, and `cleanup` helper commands. It states that C-09 begins after the existing onboarding gate and task intake, uses C-08 for facts through `--code-repository-name` or `--code-repository-root`, uses shared helpers for ledgers/contracts, requires refreshed onboarding and ledger changes to be committed before shared-memory worktrees start, separates implementation approval from commit approval, refreshes affected onboarding metadata between code and memory commits during shared-memory closeout, supports approved direct current-checkout closeout for micro edits, and requires human approval before real closeout, integration, or cleanup.

### Conventions

C-09 is a wrapper, not a replacement workflow. Task identity should be settled before worktree creation: W-02 creates `<task-root>/<task-slug>/task.md`, then C-09 adds `contract.md` beside it. Shared memory incompatibility is interactive and offers reconciliation, clean start, disabled memory, or custom handling; dirty source memory blocks start until memory content and ledger updates are committed or the developer chooses disabled memory. Closeout dry-run is the non-mutating commit preview path and reports the onboarding metadata refresh plan; real closeout needs `--approved` plus an approval note, commits code first, refreshes affected onboarding verification metadata to that code commit, then commits memory and ledger. Direct closeout follows the same approval and commit ordering without a worktree contract, and is reserved for approved small current-checkout edits or memory-only polish where worktree isolation would add no value. Integration has two strategies: `ff-only` for unchanged source branches and `replay` for parallel non-overlapping work that already moved source branches.

### Invariants And Boundaries

C-09 must not use divergent memory as trusted reference context and must not auto-commit at workflow finish. Closeout dry-run may run before commit approval because it does not mutate Git. Real worktree closeout requires explicit commit approval evidence, stops when recorded source branches moved since task start, and must not create a memory content commit whose affected onboarding metadata still points at pre-closeout code. Direct closeout also requires explicit commit approval evidence, requires shared memory with matching code/memory checkout branches, and blocks before code commit when required onboarding is missing. Integration requires explicit approval, must not move source branches until code and memory commits are fast-forwardable, must regenerate memory ledger rows after replay, and must ask before cleanup. Cleanup requires integration completion and explicit approval.

### Todos

No current implementation todo is recorded for the skill contract. Further polish should stay in the helper and tests unless the workflow contract changes again.

### Docs References

No external documentation is needed for this repository-local skill.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                                                                                                                                                                                                                                                                                                                      | Citations                | Source Path                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------- |
| C-09 wraps existing workflows, owns worktree state, direct checkout closeout, and shared-memory compatibility, and exposes commands that accept `--code-repository-name` or `--code-repository-root` for C-08 context resolution.                                                                                                                                                            | L8-L29; L47-L58; L81-L99 | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)          |
| Pre-worktree intake runs before C-09 start: C-08, C-02/AGENTS choice point, commit refreshed memory and ledger, workflow mode selection, slug review, task wrapper creation, then worktree creation.                                                                                                                                                                                         | L31-L45                  | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)          |
| Shared memory start validates a clean source memory repo and `memory.md`, and reports explicit choices when no compatible memory state exists.                                                                                                                                                                                                                                               | L47-L58                  | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)          |
| Closeout dry-run prepares the commit preview without approval and reports the metadata refresh plan; real shared-memory closeout is human-gated, requires an approval note, fails when required onboarding is missing, commits code, refreshes affected onboarding metadata to that code commit, commits memory content, prepends `memory.md`, commits the ledger, and updates the contract. | L60-L79                  | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)          |
| Direct closeout is the C-09-owned current-checkout path for approved micro edits; it dry-runs first, requires explicit commit approval, validates shared-memory branch state, fails before committing when onboarding is missing, then commits code, refreshes onboarding metadata, commits memory, and commits the ledger.                                                                  | L81-L99                  | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)          |
| Integration is human-gated, supports `ff-only` and `replay`, regenerates ledger rows after memory content replay, blocks conflicts before source branches move, and asks about cleanup after success.                                                                                                                                                                                        | L101-L112                | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)          |
| Cleanup is human-gated, requires completed integration, removes worktrees, deletes merged local branches, prunes empty worktree folders, and is idempotent.                                                                                                                                                                                                                                  | L114-L118                | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)          |
| The worktree design spec defines the same wrapper/non-replacement boundary and C-09 ownership model.                                                                                                                                                                                                                                                                                         | L1218-L1248              | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-12T10:59: Updated the direct-closeout contract after ledger branch metadata stopped being a compatibility condition.
- 2026-05-11T19:42: Refreshed verification metadata to `aa85d3862bf21fed791e3170e6957f9288c319e8` and corrected C-09 source citation ranges after confirming the coordination rename behavior remains current.
- 2026-05-11T18:34: Updated after C-09 command examples adopted `--code-repository-name` and `--code-repository-root`.
- 2026-05-10T03:01: Updated after the C-09 contract added direct checkout closeout for approved micro edits.
- 2026-05-10T01:55: Updated after the closeout contract documented code-commit-first onboarding metadata refresh before memory commit.
- 2026-05-10T01:19: Updated after C-09 split implementation approval from explicit commit approval and added closeout preview guidance.
- 2026-05-10T00:56: Updated to capture the clean shared-memory baseline gate before C-09 worktree start.
- 2026-05-10T00:47: Updated for pre-worktree intake, wrapper task placement, lifecycle status, and cleanup command behavior.
- 2026-05-10T00:36: Refreshed verification metadata after approval-gated integration landed on main.
- 2026-05-09T23:55: Updated after documenting the C-09 integration phase and replay/conflict rules.
- 2026-05-09T21:59: Created onboarding for the new C-09 skill.
- 2026-05-09T22:10: Updated closeout boundary to include source-branch movement checks.
- 2026-05-09T22:57: Refreshed verification metadata and replaced task-artifact citations with current skill/spec evidence.
