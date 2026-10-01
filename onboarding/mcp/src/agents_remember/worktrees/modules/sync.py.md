# mcp/src/agents_remember/worktrees/modules/sync.py

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
`sync_selected_atomic_series_under_authority`: this contract's own contract-keyed activation record
becomes `reconciling`, its pinned source pair is reconciled, and only a proven-current candidate
becomes `active`. The activation record is keyed per series contract (`contract_fingerprint` over the
canonical contract path), so a sync never reads, pauses, or names another master's record — the only
surviving activation waiting reason is `atomic-series-reconciling` on the addressed contract, and
genuine wave dependencies stay with the sprint execution graph's own `predecessor-incomplete:`
reasons. Leaf/direct contracts delegate to `sync_contract_under_authority`. Durable operation phase,
retained conflicts, continue/cancel, exact rollback, ledger-pair admission, and contract base updates
belong to the focused sync transaction modules rather than this facade.

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
- The contract is re-read under the repository integration lock after remote refresh.
- A genuine merge conflict is retained in the reported worktree for agent resolution; it is not
  aborted or converted into queue state.
- Atomic-series exposure follows successful exact reconciliation of THIS contract's own activation
  record; selection never comes from task prose, queue order, another master's record, or a
  compatibility reader.
- Expected contract/source failures return a controlled result rather than escaping the public MCP
  boundary.

### Todos

Reconcile exact source line ranges and any Dagger-driven state-vocabulary changes before final
verification metadata is stamped.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public facade validates input, keeps preview mutation-free, refreshes outside the lock, rereads under authority, and dispatches by contract kind. [1]
- Shared upstream refresh reports per-side evidence without treating the remote as local mutation authority. [2]
- Atomic-series sync binds the public wrapper to the exact transaction on this contract's own activation record: it validates ownership, publishes `reconciling`, reconciles the pinned source pair, retains incomplete work in reconciling, and publishes `active` only after current-source proof; a foreign master is never read or named. [3]
- Ordinary transaction routing owns durable resume, continue, cancel, and recovery behavior. [4]
- Stable status and recovery evidence lives at the enclosure-root journal, not in the queue. [5]
- Focused integration tests exercise fast-forward sync and contract advance, a retained code merge conflict with continuation, stale-cache source-ref selection, and content-conflict preservation, including the knowledge conflict whose only working route is the manual continuation. [6]

### Cross-Repo References

No meaningful cross-repo references found.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.
