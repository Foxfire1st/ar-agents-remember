# mcp/src/agents_remember/worktrees/modules/abandon.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/abandon.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T09:52+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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

Since 260731-EFA-L4 that stamp is
`amend_contract(contract, ContractCells(cleanup="abandoned"))`, not `dataclasses.replace`; the
module no longer imports `replace` at all. `cleanup` is one of the six persisted vocabulary cells,
and typeshed declares `replace` as `**changes: Any`, so `replace(contract, cleanup=<anything>)` was
checked by nothing — including against the wire model that reports the value. The written contract
is unchanged.

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
  causes a subsequent `start` call to recreate rather than reattach. `"abandoned"` is a member of
  `worktree_contract.CleanupStatus`, and the write must go through `ContractCells` /
  `amend_contract` — no `replace` call here may carry a `cleanup=` keyword, because typeshed's
  `**changes: Any` means pyright would check nothing.
- The docstring points at the `l-01-agent-lifecycles` skill's
  read-only/abandon exit as the lifecycle entry that drives this operation.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Provider teardown is delegated to the provider-runtime teardown function. | `teardown_worktree_providers` | mcp/src/agents_remember/worktrees/modules/provider_teardown.py:27-46 |
| `remove_registered_worktree`, `delete_branch_if_merged`, `delete_branch_force`, and `remove_empty_dir` are reused from cleanup. | `remove_registered_worktree`; `delete_branch_if_merged`; `delete_branch_force`; `remove_empty_dir` | mcp/src/agents_remember/worktrees/modules/cleanup.py:46-61; mcp/src/agents_remember/worktrees/modules/cleanup.py:64-79; mcp/src/agents_remember/worktrees/modules/cleanup.py:115-131; mcp/src/agents_remember/worktrees/modules/cleanup.py:267-282 |
| `WorktreeArgs` types the abandon input. | `WorktreeArgs` | mcp/src/agents_remember/worktrees/modules/args.py:20-82 |
| The closeout registrar exposes `worktree_abandon` with `force` forwarded from the MCP layer. | "def worktree_abandon" | mcp/src/agents_remember/mcp/registration/closeout.py:110-110 |
| Unit tests cover unmerged-branch refusal, force discard, blocker reporting, and dry-run teardown. | `test_no_force_refuses_unmerged_and_reports_commits`; `test_force_discards_unmerged_branch`; `test_unmerged_branch_and_dirty_worktree_are_blockers`; `test_dry_run_lists_resources_without_touching_docker_or_disk` | mcp/tests/test_worktree_abandon.py:125-145; mcp/tests/test_worktree_abandon.py:174-180; mcp/tests/test_worktree_abandon.py:182-185; mcp/tests/test_worktree_abandon.py:189-199 |
| `CleanupStatus`, `ContractCells`, and `amend_contract` are the vocabulary and typed write used by the `abandoned` stamp. | `CleanupStatus`; `ContractCells`; `amend_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:68-68; mcp/src/agents_remember/worktrees/worktree_contract.py:183-198; mcp/src/agents_remember/worktrees/worktree_contract.py:201-229 |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: regenerated the reused-cleanup
  helper ranges and the closeout registrar row via the scoped fixer; exact non-fixing check
  returns zero findings.

- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 5 repository-reference citations (5/5 anchored and sourced; scoped citation check clean).

- 2026-08-01T09:52+02:00 — 260731-EFA-L4 curator: the `cleanup="abandoned"` stamp changed mechanism.
  `abandon_result` now writes `amend_contract(contract, ContractCells(cleanup="abandoned"))`, the
  `from dataclasses import replace` import is gone, and `ContractCells` / `amend_contract` were
  added to the `worktree_contract` import block. Recorded it and tightened the matching invariant:
  `cleanup` is one of the six persisted vocabularies, and `dataclasses.replace` types `**changes` as
  `Any`, so the old call was checked by nothing — not by pyright and not against the wire model that
  reports the value. Behaviour and the written contract are unchanged, so every other claim in this
  card still stands; I re-verified `_abandon_branch`'s unmerged probe, the force path
  (`delete_branch_force`, `remove_registered_worktree(force=True)`) and the
  `abandoned`/`abandon-blocked`/`would-abandon` states against the current file. Added the
  `worktree_contract.py` reference row. Verification metadata pinned until closeout stamps the L4
  commit.
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
