# C-09-git-worktree-manager/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-10T00:36                           |
| lastVerifiedCommitHash | `5f71bd68f78f8ac3e3e02df8e45086eb2a37c678` |
| lastVerifiedCommitDate | 2026-05-09T23:54                           |

## Purpose

This skill documents C-09, the Git worktree manager that wraps existing task workflows with code/memory worktree setup, status, human-approved closeout, and human-approved integration back to source branches.

## Code Commentary

### Logic

The skill defines `start`, `attach`, `status`, `bootstrap-memory`, `closeout`, and `integrate` helper commands. It states that C-09 uses C-08 for facts, shared helpers for ledgers/contracts, and human approval before commit, integration, or cleanup.

### Conventions

C-09 is a wrapper, not a replacement workflow. Shared memory incompatibility is interactive and offers reconciliation, clean start, disabled memory, or custom handling. Integration has two strategies: `ff-only` for unchanged source branches and `replay` for parallel non-overlapping work that already moved source branches.

### Invariants And Boundaries

C-09 must not use divergent memory as trusted reference context and must not auto-commit at workflow finish. Closeout requires explicit approval and stops when recorded source branches moved since task start. Integration requires explicit approval, must not move source branches until code and memory commits are fast-forwardable, must regenerate memory ledger rows after replay, and must ask before cleanup.

### Todos

Cleanup removal after integration still needs a dedicated helper path.

### Docs References

No external documentation is needed for this repository-local skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| C-09 wraps existing workflows, owns worktree state and shared-memory compatibility, and exposes `start`, `attach`, `status`, `bootstrap-memory`, `closeout`, and `integrate`. | L10-L22 | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) |
| Shared memory start validates `memory.md` and reports explicit choices when no compatible memory state exists. | L26-L35 | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) |
| Closeout is human-gated and the shared-memory closeout order commits code, commits memory content, prepends `memory.md`, commits the ledger, and updates the contract. | L39-L47 | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) |
| Integration is human-gated, supports `ff-only` and `replay`, regenerates ledger rows after memory content replay, blocks conflicts before source branches move, and asks about cleanup after success. | L53-L70 | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) |
| The worktree design spec defines the same wrapper/non-replacement boundary and C-09 ownership model. | L1218-L1248 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |

## Cross-Repo References

No sibling repository evidence is needed for the skill itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-10T00:36: Refreshed verification metadata after approval-gated integration landed on main.
- 2026-05-09T23:55: Updated after documenting the C-09 integration phase and replay/conflict rules.
- 2026-05-09T21:59: Created onboarding for the new C-09 skill.
- 2026-05-09T22:10: Updated closeout boundary to include source-branch movement checks.
- 2026-05-09T22:57: Refreshed verification metadata and replaced task-artifact citations with current skill/spec evidence.
