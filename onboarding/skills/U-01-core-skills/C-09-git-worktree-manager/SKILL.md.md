# C-09-git-worktree-manager/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-10T01:01                           |
| lastVerifiedCommitHash | `b6a5c21f9309642125a468e63c8aad1a3f3beb88` |
| lastVerifiedCommitDate | 2026-05-10T01:01                           |

## Purpose

This skill documents C-09, the Git worktree manager that wraps existing task workflows with pre-worktree intake expectations, code/memory worktree setup, lifecycle status, human-approved closeout, human-approved integration back to source branches, and human-approved cleanup.

## Code Commentary

### Logic

The skill defines `start`, `attach`, `status`, `bootstrap-memory`, `closeout`, `integrate`, and `cleanup` helper commands. It states that C-09 begins after the existing onboarding gate and task intake, uses C-08 for facts, uses shared helpers for ledgers/contracts, requires refreshed onboarding and ledger changes to be committed before shared-memory worktrees start, and requires human approval before closeout, integration, or cleanup.

### Conventions

C-09 is a wrapper, not a replacement workflow. Task identity should be settled before worktree creation: W-02 creates `<task-root>/<task-slug>/task.md`, then C-09 adds `contract.md` beside it. Shared memory incompatibility is interactive and offers reconciliation, clean start, disabled memory, or custom handling; dirty source memory blocks start until memory content and ledger updates are committed or the developer chooses disabled memory. Integration has two strategies: `ff-only` for unchanged source branches and `replay` for parallel non-overlapping work that already moved source branches.

### Invariants And Boundaries

C-09 must not use divergent memory as trusted reference context and must not auto-commit at workflow finish. Closeout requires explicit approval and stops when recorded source branches moved since task start. Integration requires explicit approval, must not move source branches until code and memory commits are fast-forwardable, must regenerate memory ledger rows after replay, and must ask before cleanup. Cleanup requires integration completion and explicit approval.

### Todos

No current implementation todo is recorded for the skill contract. Further polish should stay in the helper and tests unless the workflow contract changes again.

### Docs References

No external documentation is needed for this repository-local skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| C-09 wraps existing workflows, owns worktree state and shared-memory compatibility, and exposes `start`, `attach`, `status`, `bootstrap-memory`, `closeout`, `integrate`, and `cleanup`. | L10-L23 | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) |
| Pre-worktree intake runs before C-09 start: C-08, C-02/AGENTS choice point, commit refreshed memory and ledger, workflow mode selection, slug review, task wrapper creation, then worktree creation. | L26-L40 | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) |
| Shared memory start validates a clean source memory repo and `memory.md`, and reports explicit choices when no compatible memory state exists. | L42-L53 | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) |
| Closeout is human-gated and the shared-memory closeout order commits code, commits memory content, prepends `memory.md`, commits the ledger, and updates the contract. | L54-L66 | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) |
| Integration is human-gated, supports `ff-only` and `replay`, regenerates ledger rows after memory content replay, blocks conflicts before source branches move, and asks about cleanup after success. | L68-L79 | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) |
| Cleanup is human-gated, requires completed integration, removes worktrees, deletes merged local branches, prunes empty worktree folders, and is idempotent. | L81-L85 | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) |
| The worktree design spec defines the same wrapper/non-replacement boundary and C-09 ownership model. | L1218-L1248 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-10T00:56: Updated to capture the clean shared-memory baseline gate before C-09 worktree start.
- 2026-05-10T00:47: Updated for pre-worktree intake, wrapper task placement, lifecycle status, and cleanup command behavior.
- 2026-05-10T00:36: Refreshed verification metadata after approval-gated integration landed on main.
- 2026-05-09T23:55: Updated after documenting the C-09 integration phase and replay/conflict rules.
- 2026-05-09T21:59: Created onboarding for the new C-09 skill.
- 2026-05-09T22:10: Updated closeout boundary to include source-branch movement checks.
- 2026-05-09T22:57: Refreshed verification metadata and replaced task-artifact citations with current skill/spec evidence.
