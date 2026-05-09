# git_worktree_manager.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T23:55                           |
| lastVerifiedCommitHash | `82d7bbbb2cb222f168efd16d894aba260d7dfe75` |
| lastVerifiedCommitDate | 2026-05-09T22:42                           |

## Purpose

`git_worktree_manager.py` implements the C-09 command surface.

## Code Commentary

### Logic

The script loads C-08, resolves context, creates or loads worktree contracts, dry-runs or creates code worktrees, validates shared memory via `memory.md`, blocks incompatible memory with explicit choices, bootstraps clean-start shared memory repos, reports status, performs approval-gated closeout with source-branch movement checks, and performs approval-gated integration back to source branches.

`bootstrap_memory_repo` treats an existing `memory.md` as authoritative and returns `already-ledgered` instead of overwriting it. For new baselines it initializes the memory repo if needed, configures a local Git identity when one is absent, creates the standard `onboarding`, `docs`, and `system` directories, adds `docs/.gitkeep` when `docs/` would otherwise be empty, commits memory content, then writes and commits the initial ledger. Integration supports `ff-only` and `replay`: replay rebases code when parallel work already moved main, replays memory content without replaying the old ledger commit, and writes a fresh ledger mapping for the final landed commits.

### Conventions

`start` creates the code worktree first. Shared memory is prepared only when a compatible ledger exists or the user selects an explicit recovery path. Clean-start bootstraps the shared memory repo, prepares the recorded memory worktree, and records the new memory base commit. Baseline adoption can also call the bootstrap path directly through C-10. If the human selects disabled memory, the persisted contract is converted to disabled mode instead of retaining fake shared-memory paths. `closeout` refuses to run without `--approved` and stops if source branches moved since task start. `integrate` refuses to run without `--approved`, requires completed closeout and clean source/worktree checkouts, and asks about cleanup through its JSON payload instead of removing worktrees automatically.

### Invariants And Boundaries

The script does not push. Shared-memory closeout commits code first, memory content second, and ledger updates third. Integration must not move source branches until both code and memory commits are fast-forwardable. If replay conflicts, it stops before moving main and reports that a developer decision is required.

### Todos

Cleanup removal is still a follow-up operation after successful integration; the helper only asks whether cleanup should happen.

### Docs References

No external documentation is needed for this standard-library helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The worktree design spec defines start flow, memory compatibility, and closeout sequencing. | L995-L1098 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |
| C-09 must wrap workflows without replacing them. | L1081-L1098; L1107-L1153 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) |
| The bootstrap helper configures missing local Git identity, refuses to overwrite an existing ledger, preserves empty docs with `.gitkeep`, and writes the initial ledger. | L83-L87; L297-L359 | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py) |
| C-10 adoption delegates initial baseline creation to C-09 rather than duplicating Git mutation behavior. | L157-L176 | [adopt_memory_baseline.py](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/scripts/adopt_memory_baseline.py) |
| Integration validates completed closeout state, clean source/worktree checkouts, and matching closeout heads before source branches can move. | L465-L495 | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py) |
| Replay integration stops on code or memory conflicts before moving source branches, and memory replay creates a fresh ledger row for the integrated code and memory content commits. | L497-L557; L560-L635 | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py) |

## Cross-Repo References

No sibling repository evidence is needed for the helper itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-09T23:55: Updated after adding approval-gated integration with ff-only, replay, conflict blocking, and cleanup prompt behavior.
- 2026-05-09T21:59: Created onboarding for the new C-09 helper implementation.
- 2026-05-09T22:10: Updated behavior notes for clean-start worktree preparation, disabled-memory contract conversion, and closeout source-branch checks.
- 2026-05-09T22:46: Updated bootstrap notes for existing-ledger protection, local Git identity setup, empty docs preservation, and C-10 adoption reuse.
