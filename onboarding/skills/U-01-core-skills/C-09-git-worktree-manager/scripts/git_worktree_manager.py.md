# git_worktree_manager.py

| Field                  | Value                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------- |
| repository             | agents-remember-md                                                                  |
| path                   | `skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py` |
| doc_type               | `file-level-onboarding`                                                             |
| lastUpdated            | 2026-05-11T19:42                                                                    |
| lastVerifiedCommitHash | `aa85d3862bf21fed791e3170e6957f9288c319e8`                                          |
| lastVerifiedCommitDate | 2026-05-11T19:32                                                                    |

## Purpose

`git_worktree_manager.py` implements the C-09 command surface for task Git lifecycle operations, including worktree-backed tasks and approved direct checkout closeout.

## Code Commentary

### Logic

The script loads C-08, resolves context using `code_repository_name`/`code_repository_root`, creates or loads worktree contracts, dry-runs or creates code worktrees, validates shared memory via `memory.md`, blocks dirty or incompatible memory with explicit choices, bootstraps clean-start shared memory repos, reports lifecycle-aware status, prepares non-mutating closeout previews, performs commit-approval-gated closeout with source-branch movement checks and code-commit-first onboarding metadata refresh, performs approval-gated direct checkout closeout for small approved current-branch edits, performs approval-gated integration back to source branches, and performs approval-gated cleanup after integration.

`bootstrap_memory_repo` treats an existing `memory.md` as authoritative and returns `already-ledgered` instead of overwriting it. For new baselines it initializes the memory repo if needed, configures a local Git identity when one is absent, creates the standard `onboarding`, `docs`, and `system` directories, adds `docs/.gitkeep` when `docs/` would otherwise be empty, commits memory content, then writes and commits the initial ledger. Shared-memory closeout computes changed code paths, plans required sidecar onboarding metadata refreshes from a C-08 context, blocks before committing if required onboarding or verification metadata is missing, commits code, captures the code commit date, rewrites affected onboarding metadata to that exact code commit, commits memory content, then writes and commits the ledger. Direct closeout uses the same metadata planning helpers without a task contract, requires shared memory with matching code/memory branches and matching `memory.md` branch metadata, and follows the same code-then-memory-then-ledger sequence. Integration supports `ff-only` and `replay`: replay rebases code when parallel work already moved main, replays memory content without replaying the old ledger commit, and writes a fresh ledger mapping for the final landed commits. Cleanup removes registered worktrees, deletes local branches only when `git branch -d` proves they are merged, prunes empty worktree group folders, and marks the contract complete.

### Conventions

`start` creates the code worktree first. Shared memory is prepared only when the source memory repo is clean and a compatible ledger exists, or when the user selects an explicit recovery path. Clean-start bootstraps the shared memory repo, prepares the recorded memory worktree, and records the new memory base commit. Baseline adoption can also call the bootstrap path directly through C-10. If the human selects disabled memory, the persisted contract is converted to disabled mode instead of retaining fake shared-memory paths. `status` and `attach` can load a direct `--contract-path` without requiring code repository name resolution; task-name lookup still goes through C-08. `status` emits phase, summary, next action, next command, and dirty worktree flags, including `commit-approval-pending` when worktree changes need a closeout preview. Real `closeout` and `direct-closeout` refuse to commit without `--approved` and `--approval-note`; dry-run closeout is explicitly non-mutating, can run before commit approval, and reports the metadata refresh plan. `direct-closeout` is intended for approved micro edits in the current checkout, not for parallel or long-running tasks that need worktree isolation. `integrate` and `cleanup` refuse to run without `--approved`; cleanup also refuses to run before integration has completed.

### Invariants And Boundaries

The script does not push. Shared-memory worktree closeout and direct closeout both commit code first, refresh affected onboarding verification metadata to the created code commit, commit memory content second, and commit ledger updates third only after explicit commit approval. Neither path may create a memory content commit whose affected onboarding metadata still points at pre-closeout code, and both block before the code commit when required sidecar onboarding or verification metadata is missing. Direct closeout also blocks when shared memory is not resolved, code and memory branches differ, ledger branch metadata differs, or no code/memory changes exist. Integration must not move source branches until both code and memory commits are fast-forwardable. If replay conflicts, it stops before moving main and reports that a developer decision is required. Cleanup may remove worktrees and merged local branches only after integration completion and approval.

### Todos

No current implementation todo is recorded for the helper. Future polish can improve external workflow metadata once an external task system is integrated and can extend direct closeout to internal memory if that topology needs ledgered closeout semantics.

### Docs References

No external documentation is needed for this standard-library helper.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                                                                                                                                                                                                                                                                      | Citations                | Source Path                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| The worktree design spec defines start flow, memory compatibility, and closeout sequencing.                                                                                                                                                                                                                                                  | L995-L1098               | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md)                            |
| C-09 must wrap workflows without replacing them.                                                                                                                                                                                                                                                                                             | L1081-L1098; L1107-L1153 | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md)                            |
| The bootstrap helper configures missing local Git identity, refuses to overwrite an existing ledger, preserves empty docs with `.gitkeep`, and writes the initial ledger.                                                                                                                                                                    | L97-L105; L397-L464      | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py)    |
| C-10 adoption delegates initial baseline creation to C-09 rather than duplicating Git mutation behavior.                                                                                                                                                                                                                                     | L135-L176                | [adopt_memory_baseline.py](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/scripts/adopt_memory_baseline.py) |
| Lifecycle status reports phase, summary, next action, next command, `code_repository_name`, dirty flags, and `commit-approval-pending` for uncommitted worktree changes.                                                                                                                                                                     | L145-L220                | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py)    |
| Direct contract-path status and attach load the contract without requiring C-08 code repository name/root resolution.                                                                                                                                                                                                                        | L223-L239                | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py)    |
| Shared-memory start blocks a dirty source memory repo so refreshed onboarding and ledger updates must be committed before worktree creation.                                                                                                                                                                                                 | L317-L344                | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py)    |
| Closeout helper functions compute changed paths, plan sidecar onboarding refreshes from C-08 storage rules, validate required onboarding metadata, and rewrite affected metadata to the new code commit/date for both contract-backed and direct closeout paths.                                                                             | L507-L598                | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py)    |
| Closeout dry-run emits a commit approval preview plus the metadata refresh order without requiring approval; real closeout requires both `--approved` and `--approval-note`, commits code first, refreshes onboarding metadata, commits memory content, writes the ledger, and records the note in the contract.                             | L623-L736; L1208-L1216   | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py)    |
| Direct closeout validates shared-memory branch state, emits a dry-run preview with `code_repository_name` and `code_repository_root`, requires explicit approval plus an approval note, commits code first, refreshes onboarding metadata, commits memory, updates `memory.md`, and commits the ledger without creating a worktree contract. | L738-L855; L1218-L1228   | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py)    |
| Integration validates completed closeout state, clean source/worktree checkouts, and matching closeout heads before source branches can move.                                                                                                                                                                                                | L874-L904                | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py)    |
| Replay integration stops on code or memory conflicts before moving source branches, records blocked integration state, and memory replay creates a fresh ledger row for the integrated code and memory content commits.                                                                                                                      | L906-L967; L969-L1066    | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py)    |
| Cleanup removes recorded worktrees, deletes merged branches, removes empty worktree directories, marks cleanup completed, and reports already-clean/idempotent outcomes.                                                                                                                                                                     | L1073-L1159              | [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py)    |

## Cross-Repo References

No sibling repository evidence is needed for the helper itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-11T19:42: Refreshed verification metadata to `aa85d3862bf21fed791e3170e6957f9288c319e8` and repaired stale helper citation ranges after verifying the coordination rename behavior.
- 2026-05-11T18:34: Updated after C-09 switched its resolver-facing CLI, context calls, and direct closeout payloads to `code_repository_name` and `code_repository_root`.
- 2026-05-10T03:01: Updated after C-09 added direct checkout closeout for approved micro edits while preserving the code-then-memory-then-ledger invariant.
- 2026-05-10T01:55: Updated after shared-memory closeout began refreshing affected onboarding verification metadata to the newly created code commit before committing memory content.
- 2026-05-10T01:19: Updated after closeout gained a non-mutating commit preview, explicit approval note requirement, and commit-approval-pending status.
- 2026-05-10T01:04: Updated after direct contract-path status/attach stopped requiring repo-name context.
- 2026-05-10T00:56: Updated after shared-memory start began blocking dirty memory repos and integration blocks became contract-visible.
- 2026-05-10T00:47: Updated after adding wrapper-aware contract resolution, lifecycle status guidance, richer command summaries, and cleanup command behavior.
- 2026-05-10T00:36: Refreshed verification metadata after the integration command landed on main.
- 2026-05-09T23:55: Updated after adding approval-gated integration with ff-only, replay, conflict blocking, and cleanup prompt behavior.
- 2026-05-09T21:59: Created onboarding for the new C-09 helper implementation.
- 2026-05-09T22:10: Updated behavior notes for clean-start worktree preparation, disabled-memory contract conversion, and closeout source-branch checks.
- 2026-05-09T22:46: Updated bootstrap notes for existing-ledger protection, local Git identity setup, empty docs preservation, and C-10 adoption reuse.
