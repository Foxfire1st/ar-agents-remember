# mcp/src/agents_remember/worktrees/modules/abandon.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/abandon.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T01:32+02:00 |
| lastVerifiedCommitHash | `abc7cbcc74921cdcb57a61529445f61641e919e7`                |
| lastVerifiedCommitDate | 2026-07-31T21:50:08+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`abandon.py` is the discard-without-integration lifecycle operation for
worktree-backed tasks. Unlike `cleanup.py` (which requires a completed
integration), abandon runs at any lifecycle stage and reclaims the isolated
provider stack, removes code and memory worktrees, deletes task branches, and
removes the worktree group directory.

## Code Commentary

### Logic

`abandon_result(args: WorktreeArgs)` requires explicit approval (or dry-run),
then delegates to four sub-operations: `teardown_worktree_providers` reclaims
Docker containers, networks, and the `provider-runtime/` tree; `_abandon_worktrees`
calls `remove_registered_worktree` with the `force` flag passed through;
`_abandon_branches` calls `_abandon_branch` for the code work branch, memory
work branch, and memory integration branch; `_abandon_directories` removes the
worktree group dir (force-removes with `remove_tree` when `force=True`,
otherwise `remove_empty_dir`).

`_abandon_branch` checks for unmerged commits via `git log --oneline
<base>..<branch>`. Without `force` it refuses to delete a branch that has
unmerged commits, recording them in the result under `unmergedCommits` with a
`hint`. With `force` it calls `delete_branch_force` (which uses `git branch
-D`). An already-absent branch is always a no-op.

`_abandon_blockers` collects worktrees and branches that are neither removed
nor would-remove — i.e. kept because of a real blocking reason. If any blockers
exist, the contract is not marked `cleanup="abandoned"` and the state is
`"abandon-blocked"`. On a clean run the contract is stamped and state is
`"abandoned"`. Dry-run yields `"would-abandon"`.

### Invariants And Boundaries

- Requires explicit `--approved` or `dry_run`; refuses silently-destructive
  real runs.
- Without `force`, dirty worktrees and unmerged branches are blockers; commits
  are surfaced so the caller can decide whether to lose them.
- With `force`, `git worktree remove --force` and `git branch -D` are used;
  the contract is stamped as abandoned only when no blockers remain.
- Provider teardown runs before worktree/branch removal so the provider stack
  is reclaimed even when Git operations subsequently fail.
- The contract `cleanup` field is set to `"abandoned"` on success; this value
  causes a subsequent `start` call to recreate rather than reattach.
- The docstring points at the `l-01-agent-lifecycles` skill's
  read-only/abandon exit as the lifecycle entry that drives this operation.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider teardown is delegated to `provider_teardown.py`. | [provider_teardown.py](agents-remember/mcp/src/agents_remember/worktrees/modules/provider_teardown.py) |
| `remove_registered_worktree`, `delete_branch_if_merged`, `delete_branch_force`, `remove_empty_dir` are reused from `cleanup.py`. | [cleanup.py](agents-remember/mcp/src/agents_remember/worktrees/modules/cleanup.py) |
| `WorktreeArgs` types the abandon input. | [args.py](agents-remember/mcp/src/agents_remember/worktrees/modules/args.py) |
| The server registers `worktree_abandon` with `force` forwarded from the MCP layer. | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| Unit tests cover unmerged-branch refusal, force discard, blocker reporting, and dry-run teardown. | [test_worktree_abandon.py](agents-remember/mcp/tests/test_worktree_abandon.py) |

## Update History

- 2026-07-31T20:59+02:00 — 260731-EFA-L3 curator: No content impact: the leaf's whole diff to
  `abandon.py` is one import line — `run_git` moved from `modules.git` to
  `agents_remember.kernel.git_command`, `branch_exists` still comes from `modules.git` — and this
  sidecar never described a git runner, a subprocess style or a timeout, so it had nothing to
  correct. Re-verified every behavioural claim against the current file: `_abandon_branch`'s
  unmerged probe is still `run_git(repo, ["log", "--oneline", f"{base_branch}..{branch}"])`
  (`_unmerged_commits`), the force path still routes to `delete_branch_force` (`git branch -D`) and
  `remove_registered_worktree(..., force=True)` (`git worktree remove --force`), and
  `_abandon_blockers` / `_abandon_state` still produce `abandoned` / `abandon-blocked` /
  `would-abandon` unchanged. The shared runner's guard and timeout classes are documented on their
  owner, `kernel/git_command.py`, and on `modules/git.py` which lost the local copy.
- 2026-07-05T01:32+02:00 - L9 lifecycle convergence: docstring vocabulary updated to the l-01-agent-lifecycles orchestrator read-only/abandon exit; behavior unchanged. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-10T07:30+02:00 — `abandon_result` blocks (exit 2) without `force` while a live background provider setup owns the worktree (fresh heartbeat); `force=true` overrides, and a stale heartbeat does not block (GitHub #53).
- 2026-06-02T16:24+02:00: Docstring now references the `l-01-agent-lifecycles` skill in full for the read-only/abandon exit (was "L-01"). Reference-style normalization; behavior unchanged.
- 2026-06-01T00:00+02:00 — Created onboarding for the new abandon module.
