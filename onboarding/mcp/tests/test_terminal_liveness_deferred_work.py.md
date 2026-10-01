# mcp/tests/test_terminal_liveness_deferred_work.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

This hermetic unit-regression module proves the terminal liveness sweeper's collect-then-drain boundary for hosted-interaction side effects. It keeps the R28 verification surface adjacent to the real catalog and sweeper seams while leaving production ownership and lifecycle cadence to their existing owners.

## Code Commentary

### Logic

The test fixture builds temporary `TerminalCatalog` files, a live fake host, adapter snapshots, and the existing sweeper callbacks. The full-sweep case records batch exit before registration, compaction, deferred synchronization, and turn-state callbacks, and checks that each downstream hook reads committed catalog truth. The rate-limited starting-row case checks the same release boundary and synchronization-before-callback order. Separate cases verify that a batch-body exception dispatches no collected work, a row-local observer failure records `interactionSyncError` while later rows continue, and catalog reads, quarantine writes, or turn callbacks that escape after commit fail without undoing durable row state.

### Conventions

The module uses `unittest` fixtures and explicit temporary catalogs so the assertions exercise the real serving classes rather than a parallel fake implementation. It is hermetic — temporary catalogs, in-process classes and mocks, no `worktree_services` — and is classified in the repository's `unit-regression` evidence lane, which also keeps the integration lane inside its 150-collected-case cap; focused host results remain development evidence and do not grant certification authority.

### Invariants And Boundaries

Deferred observers and callbacks must run with `catalog._batch` released and must see the row written by the committed batch. A batch-body failure skips every side effect collected by that pass. A guarded observer failure is row-local and does not stop the drain; an unguarded catalog or callback failure escapes after commit while the committed catalog row remains durable. The module does not claim the serving caller's no-lock posture, GET-route ownership, R22 dirty-partial mechanics, R23 registration eligibility, or R11 retry semantics.

### Todos

The caller-level no-cross-store-lock assertion remains an adjacent L01/R18 composition concern and should be added only in that owning candidate. No production synchronization, outbox, retry loop, or fallback belongs in this file.

## Evidence

### Docs References

No Domain Documentation entries are configured in the resolved memory root. The module tests repository-owned serving and catalog behavior, so no external domain claim is needed.

### Repo-Internal References

The test cases are grounded in the production sweeper's batch and deferred-drain sequence and in the source's row-local quarantine guard. These references describe the behavior under test; they do not claim a certification result.

- The full and starting sweeps collect pending syncs inside the catalog batch, then drain them and invoke callbacks after the batch exits. [1]
- The deferred drain re-reads committed rows before invoking the observer, while the row-local guard records `interactionSyncError` and continues on later rows. [2]
- The module exercises full/starting order, aborted-pass suppression, guarded continuation, and post-commit failure durability with the real catalog and sweeper seams. [3]
- The candidate classifies this module once in the explicit unit-regression lane. [4]
### Cross-Repo References

No meaningful cross-repository implementation boundary is established by this repository-owned unit-regression module.
