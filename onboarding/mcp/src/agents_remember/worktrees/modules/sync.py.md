# mcp/src/agents_remember/worktrees/modules/sync.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/sync.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-26T08:30+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[worktrees/modules/overview.md](overview.md)

## Purpose

`sync.py` is the narrow public composition root for resumable, contract-addressed
`worktree_sync`. It establishes the canonical worktree contract, refreshes remote evidence,
serializes live mutation, and delegates either ordinary leaf/direct synchronization or
atomic-series selection plus synchronization to their focused transaction owners.

## Code Commentary

### Logic

`sync_result(args)` loads the configured contract and applies the sync-worktree admission rule.
Only leaf contracts require their ordinary code worktree to exist; a series transaction may create
operation-owned temporary `.sync` worktrees instead. It rejects invalid resolution/memory-choice
combinations before any fetch, selector, ref, or journal mutation.

A dry run does not fetch, acquire integration/store locks, publish series selection, or create
journal residue. It reports `skipped-preview` fetch evidence and asks the transaction driver for an
exact read-only projection. A live call refreshes code and external-memory upstreams outside the
integration-authority lock, then `_sync_live` re-reads and compares the complete contract under the
lock. If it changed during refresh, the result is `sync-contract-changed-retry` with the current
canonical contract path; the function never mutates against the stale object.

Under authority, series contracts delegate to
`sync_selected_atomic_series_under_authority`: the source-pair selector becomes `reconciling`, the
exact pair is reconciled, and only a proven-current candidate becomes `active`. Leaf/direct
contracts delegate to `sync_contract_under_authority`. Durable operation phase, retained conflicts,
continue/cancel, exact rollback, ledger-pair admission, and contract base updates belong to the
focused sync transaction modules rather than this facade.

### Conventions

This file deliberately contains no merge algorithm, journal parser, selector fallback, or queue
reader. Public expected failures (`ContractError`, `OSError`, `RuntimeError`, `UnicodeError`, and
`ValueError`) are translated at one boundary into `sync-operation-refused` with the observed fetch
evidence. Transaction-specific blocked/recovery states remain typed data returned by their owner.

Fetch is evidence refresh, not mutation authority: failure is reported per side and local protected
refs are re-read under the integration lock. Resolution uses `resolution_action` (`continue` or
`cancel`) on the same contract-addressed tool; no public operation id is accepted.

### Invariants And Boundaries

- Input validation precedes fetch, selector publication, journal writes, and Git mutation.
- Preview is observation-only and cannot claim selection or operation lifecycle authority.
- The contract is re-read under the source-pair integration lock after remote refresh.
- A genuine merge conflict is retained in the reported worktree for agent resolution; it is not
  aborted or converted into queue state.
- Atomic-series exposure follows successful exact reconciliation; selection never comes from task
  prose, queue order, or a compatibility reader.
- Expected contract/source failures return a controlled result rather than escaping the public MCP
  boundary.

### Todos

Reconcile exact source line ranges and any Dagger-driven state-vocabulary changes before final
verification metadata is stamped.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Anchor | Source |
| --- | --- | --- |


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public facade validates input, keeps preview mutation-free, refreshes outside the lock, rereads under authority, and dispatches by contract kind. | `sync_result`; `_sync_live` | mcp/src/agents_remember/worktrees/modules/sync.py:29-68; mcp/src/agents_remember/worktrees/modules/sync.py:71-100 |
| Shared upstream refresh reports per-side evidence without treating the remote as local mutation authority. | `fetch_source_upstreams` | mcp/src/agents_remember/worktrees/sync_source_refresh.py:9-29 |
| Atomic-series sync binds source-pair selection to reconciliation-before-exposure. | `sync_selected_atomic_series_under_authority` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:113-136 |
| Ordinary transaction routing owns durable resume, continue, cancel, and recovery behavior. | `sync_contract_under_authority` | mcp/src/agents_remember/worktrees/sync_transaction.py:72-100 |
| Stable status and recovery evidence lives at the enclosure-root journal, not in the queue. | `SyncOperationStore`; `observe_sync_operation` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:145-295; mcp/src/agents_remember/worktrees/sync_transaction_state.py:298-314 |
| Focused integration tests exercise public preview, retained conflicts, continuation, cancellation, and recovery. | `WorktreeSyncTests` | mcp/tests/test_worktree_sync.py:176-548 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Update History

- 2026-08-26T08:30+02:00 — Rebounded source-refresh and public sync-suite citations to the frozen
  file extents; behavior claims are unchanged.

- 2026-08-26T03:37+02:00 — Replaced the obsolete abort-on-conflict/local-merge description with
  the current public facade: mutation-free preview, pre-lock source refresh, post-refresh contract
  reread, series selection plus sync, ordinary resumable sync, retained conflicts, explicit
  continue/cancel, and one controlled expected-failure boundary. Verification remains
  post-Dagger/closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


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