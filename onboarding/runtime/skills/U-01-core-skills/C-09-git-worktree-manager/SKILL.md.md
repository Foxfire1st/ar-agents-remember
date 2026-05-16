# C-09-git-worktree-manager/SKILL.md

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember-md                                           |
| path                   | `runtime/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-05-16T18:17+02:00                                       |
| lastVerifiedCommitHash | `403883337d2d0479dc2da02d1ce2a1a0f3983b93`                   |
| lastVerifiedCommitDate | 2026-05-16T18:21:41+02:00|

## Purpose

This skill documents C-09, the Git lifecycle manager that wraps existing task workflows with pre-worktree intake expectations, code/memory worktree setup, lifecycle status, human-approved worktree closeout, human-approved direct checkout closeout, human-approved integration back to source branches, and human-approved cleanup.

## Code Commentary

### Logic

The skill defines `start`, `attach`, `status`, `closeout`, `direct-closeout`, `integrate`, and `cleanup` helper commands. It states that C-09 begins after the existing onboarding gate and task intake, uses C-08 for facts through `--code-repository-name` or `--code-repository-root`, uses common helpers for ledgers/contracts, requires missing external memory roots to be initialized through C-00 before worktree start, requires refreshed onboarding and ledger changes to be committed before external-memory worktrees start, separates implementation approval from commit approval, refreshes affected file-level onboarding metadata and repo entity catalog fingerprints between code and memory commits during external-memory closeout, supports approved direct current-checkout closeout for micro edits, and requires human approval before real closeout, integration, or cleanup.

### Conventions

C-09 is a wrapper, not a replacement workflow. Task identity should be settled before worktree creation: W-02 creates `<task-root>/<task-slug>/task.md`, then C-09 adds `contract.md` beside it. External memory incompatibility is interactive and offers reconciliation, clean start, disabled memory, or custom handling; dirty source memory blocks start until memory content and ledger updates are committed or the developer chooses disabled memory. Closeout dry-run is the non-mutating commit preview path and reports the onboarding metadata and entity fingerprint refresh plan; real closeout needs `--approved` plus an approval note, commits code first, refreshes affected onboarding verification metadata and `git-blob-set-v1` entity fingerprints to that code commit, then commits memory and ledger. Direct closeout follows the same approval and commit ordering without a worktree contract, and is reserved for approved small current-checkout edits or memory-only polish where worktree isolation would add no value. Integration has two strategies: `ff-only` for unchanged source branches and `replay` for parallel non-overlapping work that already moved source branches.

### Invariants And Boundaries

C-09 must not use divergent memory as trusted reference context and must not auto-commit at workflow finish. Closeout dry-run may run before commit approval because it does not mutate Git. Real worktree closeout requires explicit commit approval evidence, stops when recorded source branches moved since task start, and must not create a memory content commit whose affected onboarding metadata or entity fingerprints still point at pre-closeout code. Direct closeout also requires explicit commit approval evidence, requires external memory with matching code/memory checkout branches, and blocks before code commit when required onboarding is missing. Integration requires explicit approval, must not move source branches until code and memory commits are fast-forwardable, must regenerate memory ledger rows after replay, and must ask before cleanup. Cleanup requires integration completion and explicit approval.

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
| C-09 wraps existing workflows, owns worktree state, direct checkout closeout, and external-memory compatibility, and exposes commands that accept `--code-repository-name` or `--code-repository-root` for C-08 context resolution.                                                                                                                                                            | L8-L29; L47-L58; L81-L99 | [C-09 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)          |
| Pre-worktree intake runs before C-09 start: C-08, C-02/AGENTS choice point, commit refreshed memory and ledger, workflow mode selection, slug review, task wrapper creation, then worktree creation.                                                                                                                                                                                         | L31-L45                  | [C-09 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)          |
| External memory start validates a clean source memory repo and `memory.md`, and reports explicit choices when no compatible memory state exists.                                                                                                                                                                                                                                               | L47-L58                  | [C-09 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)          |
| Closeout dry-run prepares the commit preview without approval and reports metadata and entity fingerprint refresh plans; real external-memory closeout is human-gated, requires an approval note, fails when required onboarding is missing, commits code, refreshes affected onboarding metadata and entity fingerprints to that code commit, commits memory content, prepends `memory.md`, commits the ledger, and updates the contract. | L60-L81                  | [C-09 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)          |
| Direct closeout is the C-09-owned current-checkout path for approved micro edits; it dry-runs first, requires explicit commit approval, validates external-memory branch state, fails before committing when onboarding is missing, then commits code, refreshes onboarding metadata and affected entity fingerprints, commits memory, and commits the ledger.                                                                  | L83-L100                  | [C-09 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)          |
| Integration is human-gated, supports `ff-only` and `replay`, regenerates ledger rows after memory content replay, blocks conflicts before source branches move, and asks about cleanup after success.                                                                                                                                                                                        | L101-L112                | [C-09 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)          |
| Cleanup is human-gated, requires completed integration, removes worktrees, deletes merged local branches, prunes empty worktree folders, and is idempotent.                                                                                                                                                                                                                                  | L114-L118                | [C-09 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)          |
| The worktree design spec defines the same wrapper/non-replacement boundary and C-09 ownership model.                                                                                                                                                                                                                                                                                         | L1218-L1248              | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

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
- 2026-05-09T21:59: Created onboarding for the new C-09 skill.
- 2026-05-09T22:10: Updated closeout boundary to include source-branch movement checks.
- 2026-05-09T22:57: Refreshed verification metadata and replaced task-artifact citations with current skill/spec evidence.
