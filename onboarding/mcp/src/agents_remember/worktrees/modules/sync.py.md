# mcp/src/agents_remember/worktrees/modules/sync.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/sync.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `abc7cbcc74921cdcb57a61529445f61641e919e7`                         |
| lastVerifiedCommitDate | 2026-07-31T21:50:08+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[worktrees/modules/overview.md](overview.md)

## Purpose

`sync.py` implements `worktree_sync` (issue #54): pull the moved official line
into a live worktree mid-task, advancing the contract's recorded code/memory
base pair atomically so a long-running task never bases on a stale pair and
end-of-series integration stays `ff-only`.

## Code Commentary

### Logic

`sync_result(args)` loads the contract, best-effort fetches each source
branch's upstream (`_fetch_source_upstreams` — offline degrades to reported
state and sync proceeds on local facts), and resolves the new official pair:
the code source branch tip must be ledger-mapped in `memory.md` **at the
official memory source branch tip** (`_consistent_pair_block`, read via
`git show <branch>:memory.md`); a mid-cycle official line blocks with guidance
to run carryover first. `_sync_code` merges the source branch into the code
work branch inside the worktree (ff when unchanged, never rebase — work
branches may be pushed); a conflicted merge is `merge --abort`ed and blocks
with the conflict file list. `_sync_memory` fast-forwards the memory work
branch when its HEAD is an ancestor of the official tip (the dominant
pre-closeout parked-memory case — the parallel cycle's sidecars and ledger
rows end up beneath the task's future work); local memory commits + a moved
official line return `needs-review` with `memory_sync_choice` recoveries:
`merge-memory` (merge attempted, conflicts — e.g. the append-ordered ledger —
abort cleanly and block) or `skip-memory` (memory deferred to end-of-task
carryover; only the code base advances). On success the contract's
`code_base_commit`/`memory_base_commit` move to the new pair and a `sync_log`
entry is appended, then the contract is rewritten. `dry_run` previews
(`would-sync` / `would-fast-forward` / `would-merge`) without mutating.

**The five helpers extracted in 260731-EFA-L2** (behaviour unchanged; every payload, summary
string and exit code is the same):

- `_stop_before_sync(contract, *, code_tip, memory_tip, external, fetch)` — the result when no
  branch should move: an inconsistent official pair, or `already-current`. Returns `None` to
  proceed.
- `_memory_sync_block(contract, code_sync, memory_sync, fetch)` — the blocked result when the
  memory side could not be advanced on its own (`needs-review` or `conflicts`). Returns `None`
  otherwise.
- `_memory_branch_move(contract, args, *, worktree_head, tip)` — the **decision**, as a string:
  `fast-forward` when the worktree head is an ancestor of the tip, `merge` when the caller chose
  `memory_sync_choice="merge-memory"`, else `needs-review`. Deciding once is what lets the dry-run
  path report `would-<move>` from the same rule the real path executes, instead of duplicating the
  ancestry test.
- `_move_memory_branch(worktree, source_branch, *, move, tip)` — performs the decided move. A
  failed fast-forward leaves nothing to abort; a failed merge does.
- `_aborted_merge_state(worktree, result)` — collect the conflicted paths and `merge --abort`, so
  the worktree is never left half-merged. **Shared by the code and memory paths**, which is why
  the two now report conflicts identically by construction.

### Conventions

States are data, never exceptions: `synced`, `would-sync`, `already-current`,
and blocked payloads with `next_guidance` recovery args mirror the start
module's blocked-state pattern.

**One bounded exception since 260731-EFA-L3.** `run_git` is now
`agents_remember.kernel.git_command.run_git` (the module-local copy in `modules.git` is
gone), and it always applies a timeout — the default local class
`GIT_LOCAL_TIMEOUT_SECONDS = 300`, which every `run_git` call in this file takes because
none passes `timeout=`. The only `except` in the module is `except LedgerError` around
`parse_ledger_text` in `_consistent_pair_block`, so a git command that outruns 300s raises
`subprocess.TimeoutExpired` out of `sync_result` rather than returning a blocked state.
That is a change of failure *shape*, not of reachability: the old local runner passed no
`timeout=` at all, so the same wedged `merge`/`show` hung the MCP tool call forever
instead. The bound names the slowest legitimate `merge`/`status` over a large tree, so
tripping it means git is stalled — typically on an index lock another process holds — not
that a real sync was cut short. Every state and payload the sync itself produces is
unchanged.

### Invariants And Boundaries

- The base pair moves together or not at all (modulo the explicit
  `skip-memory` choice, which advances code only and defers memory to
  carryover).
- The ledger is never auto-merged; conflicted merges always abort.
- A conflicted code merge must leave the worktree at its pre-merge HEAD.
- The sync mutates only the task's own worktrees and contract — official
  branches are never moved here (that is carryover's and integration's job).

### Todos

The freshness payload produced by `guidance.base_freshness` is the designed
message for a future change-notification ping (transport deferred until the
GitHub #53 notification plumbing settles; follow-up issue filed in sub-task E).

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Detection surface: `worktree_status`'s fetch-free freshness block recommends this tool. | [guidance.py](agents-remember/mcp/src/agents_remember/worktrees/modules/guidance.py) |
| The contract's `sync_log` field persists each base-pair advance. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Upstream fetch + ref helpers come from the freshness kernel. | [git_freshness.py](agents-remember/mcp/src/agents_remember/kernel/git_freshness.py) |
| The `run_git` every merge/ff/show in this module calls, and the `GIT_LOCAL_TIMEOUT_SECONDS` default that bounds them. | [kernel/git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |
| Sync behavior coverage: ff pair, mid-cycle block, conflicts, choices, dry-run. | [test_worktree_sync.py](agents-remember/mcp/tests/test_worktree_sync.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-07-31T20:58+02:00 — 260731-EFA-L3 curator: `run_git` now comes from
  `kernel.git_command`, not `modules.git`. The module's own logic is untouched, but the
  Conventions section asserted "States are data, never exceptions" without qualification and that no
  longer holds unconditionally: the shared runner always sets a timeout (the 300s
  `GIT_LOCAL_TIMEOUT_SECONDS` default, taken by all six `run_git` calls here — `_consistent_pair_block`,
  `_sync_code`, `_aborted_merge_state` x2, `_move_memory_branch` x2), the module's only `except` is
  `LedgerError`, so a stalled git raises `subprocess.TimeoutExpired` out of `sync_result` where the
  old unbounded local runner hung instead. Recorded that one bounded exception and added the
  `kernel/git_command.py` reference. Verification metadata pinned until closeout stamps the L3
  commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0911`/`PLR0912` armed with no
  exemptions): extracted `_stop_before_sync`, `_memory_sync_block`, `_memory_branch_move`,
  `_move_memory_branch` and the shared `_aborted_merge_state` (now used by both the code and memory
  merge paths). The dry-run `would-<move>` states are now derived from the same decision the real
  path executes. Every payload, summary string and exit code is unchanged. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-10T09:56+02:00: Created as issue #54 sub-task D — atomic mid-task base-pair sync with consistent-pair gate, merge/ff sides, memory_sync_choice recoveries, and contract sync_log.
