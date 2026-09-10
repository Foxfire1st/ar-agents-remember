# mcp/tests/test_terminal_liveness_deferred_work.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_terminal_liveness_deferred_work.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-08T14:35+02:00 |
| lastVerifiedCommitHash |  `bb38d04e472439574f4eed7337f1639aac99f514`|
| lastVerifiedCommitDate |  2026-09-10T11:50:15+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation entries are configured in the resolved memory root. The module tests repository-owned serving and catalog behavior, so no external domain claim is needed.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

The test cases are grounded in the production sweeper's batch and deferred-drain sequence and in the source's row-local quarantine guard. These references describe the behavior under test; they do not claim a certification result.

| Finding | Anchor | Source |
| --- | --- | --- |
| The full and starting sweeps collect pending syncs inside the catalog batch, then drain them and invoke callbacks after the batch exits. | `refresh`; `_refresh_starting_rows` | mcp/src/agents_remember/serving/terminal_liveness.py:174-221; mcp/src/agents_remember/serving/terminal_liveness.py:223-270 |
| The deferred drain re-reads committed rows before invoking the observer, while the row-local guard records `interactionSyncError` and continues on later rows. | `_run_deferred_interaction_syncs`; `_observe_control_snapshot` | mcp/src/agents_remember/serving/terminal_liveness.py:302-324; mcp/src/agents_remember/serving/terminal_liveness.py:534-584 |
| The module exercises full/starting order, aborted-pass suppression, guarded continuation, and post-commit failure durability with the real catalog and sweeper seams. | `TerminalLivenessDeferredWorkTests` | mcp/tests/test_terminal_liveness_deferred_work.py:101-366 |
| The candidate classifies this module once in the explicit unit-regression lane. | "mcp/tests/test_terminal_liveness_deferred_work.py" | mcp/tests/test-evidence-lanes.toml:103-103 |

## Cross-Repo References

No meaningful cross-repository implementation boundary is established by this repository-owned unit-regression module.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-10T11:24+02:00 — 260831-LOCR-L28 curator: corrected this module's evidence-lane classification from `integration` to `unit-regression`. It is hermetic and integration was already at exactly its 150-collected-case cap, so the earlier registration would have taken the lane to 155 and broken full-suite collection. The lane citation now names the module's own manifest row (`mcp/tests/test-evidence-lanes.toml:103-103`) instead of a block range, and the Purpose/Conventions wording follows the corrected lane. No behavioral or verification claim changed; verification remains closeout-owned because the source is an uncommitted candidate.
- 2026-09-08T14:35+02:00 — Created the file card for the R28 deferred-work proof. Recorded the full/starting post-commit ordering, aborted-pass suppression, row-local quarantine continuation, and escaping post-commit failure boundary from the current source. Verification remains closeout-owned because the source is an uncommitted candidate.
