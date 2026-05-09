# git_worktree_manager.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-10T01:01                           |
| lastVerifiedCommitHash | `b6a5c21f9309642125a468e63c8aad1a3f3beb88` |
| lastVerifiedCommitDate | 2026-05-10T01:01                           |

## Purpose

`git_worktree_manager.py` implements the C-09 command surface for worktree-backed task lifecycle operations.

## Code Commentary

### Logic

The script loads C-08, resolves context, creates or loads worktree contracts, dry-runs or creates code worktrees, validates shared memory via `memory.md`, blocks dirty or incompatible memory with explicit choices, bootstraps clean-start shared memory repos, reports lifecycle-aware status, performs approval-gated closeout with source-branch movement checks, performs approval-gated integration back to source branches, and performs approval-gated cleanup after integration.

`bootstrap_memory_repo` treats an existing `memory.md` as authoritative and returns `already-ledgered` instead of overwriting it. For new baselines it initializes the memory repo if needed, configures a local Git identity when one is absent, creates the standard `onboarding`, `docs`, and `system` directories, adds `docs/.gitkeep` when `docs/` would otherwise be empty, commits memory content, then writes and commits the initial ledger. Integration supports `ff-only` and `replay`: replay rebases code when parallel work already moved main, replays memory content without replaying the old ledger commit, and writes a fresh ledger mapping for the final landed commits. Cleanup removes registered worktrees, deletes local branches only when `git branch -d` proves they are merged, prunes empty worktree group folders, and marks the contract complete.

### Conventions

`start` creates the code worktree first. Shared memory is prepared only when the source memory repo is clean and a compatible ledger exists, or when the user selects an explicit recovery path. Clean-start bootstraps the shared memory repo, prepares the recorded memory worktree, and records the new memory base commit. Baseline adoption can also call the bootstrap path directly through C-10. If the human selects disabled memory, the persisted contract is converted to disabled mode instead of retaining fake shared-memory paths. `status` emits phase, summary, next action, next command, and dirty worktree flags. `closeout`, `integrate`, and `cleanup` all refuse to run without `--approved`; cleanup also refuses to run before integration has completed.

### Invariants And Boundaries

The script does not push. Shared-memory closeout commits code first, memory content second, and ledger updates third. Integration must not move source branches until both code and memory commits are fast-forwardable. If replay conflicts, it stops before moving main and reports that a developer decision is required. Cleanup may remove worktrees and merged local branches only after integration completion and approval.

### Todos

No current implementation todo is recorded for the helper. Future polish can improve external workflow metadata once an external task system is integrated.

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
| Lifecycle status reports phase, summary, next action, next command, and dirty flags. | L83-L84; L140-L203 | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py) |
| Shared-memory start blocks a dirty source memory repo so refreshed onboarding and ledger updates must be committed before worktree creation. | L305-L344 | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py) |
| Integration validates completed closeout state, clean source/worktree checkouts, and matching closeout heads before source branches can move. | L554-L584 | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py) |
| Replay integration stops on code or memory conflicts before moving source branches, records blocked integration state, and memory replay creates a fresh ledger row for the integrated code and memory content commits. | L539-L549; L586-L646 | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py) |
| Cleanup removes recorded worktrees, deletes merged branches, removes empty worktree directories, marks cleanup completed, and reports already-clean/idempotent outcomes. | L794-L843; L905-L909 | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py) |

## Cross-Repo References

No sibling repository evidence is needed for the helper itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-10T00:56: Updated after shared-memory start began blocking dirty memory repos and integration blocks became contract-visible.
- 2026-05-10T00:47: Updated after adding wrapper-aware contract resolution, lifecycle status guidance, richer command summaries, and cleanup command behavior.
- 2026-05-10T00:36: Refreshed verification metadata after the integration command landed on main.
- 2026-05-09T23:55: Updated after adding approval-gated integration with ff-only, replay, conflict blocking, and cleanup prompt behavior.
- 2026-05-09T21:59: Created onboarding for the new C-09 helper implementation.
- 2026-05-09T22:10: Updated behavior notes for clean-start worktree preparation, disabled-memory contract conversion, and closeout source-branch checks.
- 2026-05-09T22:46: Updated bootstrap notes for existing-ledger protection, local Git identity setup, empty docs preservation, and C-10 adoption reuse.
