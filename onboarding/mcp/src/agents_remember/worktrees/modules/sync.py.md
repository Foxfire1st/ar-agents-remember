# mcp/src/agents_remember/worktrees/modules/sync.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/sync.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T09:56+02:00                     |
| lastVerifiedCommitHash | `f62c732df2acc30ec3766f83c176a24b39c0bc46`                         |
| lastVerifiedCommitDate | 2026-06-10T10:41:09+02:00|
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

### Conventions

States are data, never exceptions: `synced`, `would-sync`, `already-current`,
and blocked payloads with `next_guidance` recovery args mirror the start
module's blocked-state pattern.

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
| Detection surface: `worktree_status`'s fetch-free freshness block recommends this tool. | [guidance.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/guidance.py) |
| The contract's `sync_log` field persists each base-pair advance. | [worktree_contract.py](agents-remember-md/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Upstream fetch + ref helpers come from the freshness kernel. | [git_freshness.py](agents-remember-md/mcp/src/agents_remember/kernel/git_freshness.py) |
| Sync behavior coverage: ff pair, mid-cycle block, conflicts, choices, dry-run. | [test_worktree_sync.py](agents-remember-md/mcp/tests/test_worktree_sync.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-06-10T09:56+02:00: Created as issue #54 sub-task D — atomic mid-task base-pair sync with consistent-pair gate, merge/ff sides, memory_sync_choice recoveries, and contract sync_log.
