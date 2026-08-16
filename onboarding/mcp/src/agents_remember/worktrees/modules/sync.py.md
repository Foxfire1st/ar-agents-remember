# mcp/src/agents_remember/worktrees/modules/sync.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/sync.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T09:12+02:00                     |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a`                         |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
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
and blocked payloads with `recovery_guidance` recovery args mirror the start
module's blocked-state pattern.

**The next-move builder is `recovery_guidance`, not `next_guidance` (260731-EFA-L4).**
`_memory_sync_block`'s `needs-review` branch is this module's only next-move block, and it
calls `guidance.recovery_guidance("choose_memory_sync_recovery", tool="worktree_sync",
args=contract_next_args(contract), required_args=["memory_sync_choice"])`. The emitted keys
and their order are byte-identical to what `next_guidance` produced — `nextOperation`,
`nextTool`, `nextArgs`, `nextRequiredArgs` — so nothing on the wire moved. The split is in
the *type*: `next_guidance` is now narrowed to the phase machine's `NextOperation` /
`NextTool` `Literal`s, which `models.worktree.WorktreeSummary` imports, and
`choose_memory_sync_recovery` is deliberately not a member of them. It lives in
`RecoveryOperation` — the vocabulary for payloads that are a *block*, not a lifecycle
phase. This result is rendered as a `FlexibleToolResponse` and never reaches
`WorktreeSummary`, so widening the phase vocabulary to hold it would have put "blocked on a
moved official memory line" into the set the context packet's `nextOperation` claims to be.

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

| Finding | Anchor | Source |
| --- | --- | --- |


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Detection surface: `worktree_status`'s fetch-free freshness block in `base_freshness` recommends this tool. | `base_freshness` | mcp/src/agents_remember/worktrees/modules/guidance.py:319-369 |
| The contract declares `sync_log` as one entry per `worktree_sync` that advanced the recorded base pair. | `sync_log`; "one entry per worktree_sync"; "recorded base pair" | mcp/src/agents_remember/worktrees/worktree_contract.py:279-280; mcp/src/agents_remember/worktrees/worktree_contract.py:283-283 |
| The sync module persists the result of each base-pair advance. | `sync_result` | mcp/src/agents_remember/worktrees/modules/sync.py:36-119 |
| Upstream fetch + ref helpers come from the freshness kernel through `upstream_ref` and `fetch_remote`. | `upstream_ref`; `fetch_remote` | mcp/src/agents_remember/kernel/git_freshness.py:55-64; mcp/src/agents_remember/kernel/git_freshness.py:67-77 |
| The `run_git` every merge/ff/show in this module calls, and the `GIT_LOCAL_TIMEOUT_SECONDS` default that bounds them. | `run_git`; `GIT_LOCAL_TIMEOUT_SECONDS` | mcp/src/agents_remember/kernel/git_command.py:70-70; mcp/src/agents_remember/kernel/git_command.py:85-151 |
| `recovery_guidance` and the `RecoveryOperation` / `RecoveryTool` vocabularies this module's block belongs to, kept separate from the phase machine's `next_guidance`. | `recovery_guidance`; `RecoveryOperation`; `RecoveryTool` | mcp/src/agents_remember/worktrees/modules/guidance.py:37-54; mcp/src/agents_remember/worktrees/modules/guidance.py:146-160 |
| Sync behavior coverage: ff pair, mid-cycle block, conflicts, choices, dry-run, in `WorktreeSyncTests`. | `WorktreeSyncTests` | mcp/tests/test_worktree_sync.py:111-244 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Update History

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: re-read the expanded task-reopen/worktree-start recovery
  vocabulary and retained sync's separate recovery-guidance ownership with current anchors.
  Verification remains closeout-owned.
- 2026-08-04T13:15:12+02:00 — 260731-EFA-L6 S18-B02 curator: extended the sync-log contract claim through its defining comments and regenerated the final range with the scoped fixer.
- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 5 table citations for freshness, remote fetch, git timeout, recovery guidance, and sync tests; fixer-generated ranges verified.

- 2026-08-01T09:12+02:00 — 260731-EFA-L4 curator: the Conventions section said blocked payloads
  carry "`next_guidance` recovery args"; that call is gone. `_memory_sync_block` now calls
  `recovery_guidance("choose_memory_sync_recovery", tool="worktree_sync",
  args=contract_next_args(contract), required_args=["memory_sync_choice"])`, and the import block
  at the top of the module takes `recovery_guidance` in place of `next_guidance` (it imports no
  `next_guidance` at all now). Corrected the sentence and recorded why the split exists: the emitted
  keys are unchanged, but `next_guidance` is now narrowed to the phase vocabulary
  `WorktreeSummary` imports, and `choose_memory_sync_recovery` is a `RecoveryOperation` because this
  payload is a block rendered as a `FlexibleToolResponse`, not a lifecycle phase. Added the
  `guidance.py` reference row. Nothing else in this module changed — the five L2 helpers, the
  consistent-pair gate, both merge paths and the L3 timeout note all still describe the file
  exactly. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T20:58+02:00 — 260731-EFA-L3 curator: `run_git` now comes from
  `kernel.git_command`, not `modules.git`. The module's own logic is untouched, but the
  Conventions section asserted "States are data" without qualification and that no
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
