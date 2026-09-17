# mcp/tests/test_terminal_liveness_deferred_work.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_terminal_liveness_deferred_work.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T19:00+02:00 |
| lastVerifiedCommitHash |  `420669c459aab3650cdaa5b3e5271e71d7d94c0e`|
| lastVerifiedCommitDate |  2026-09-17T10:54:08+02:00|
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
| The full and starting sweeps collect pending syncs inside the catalog batch, then drain them and invoke callbacks after the batch exits. | `refresh`; `_refresh_starting_rows` | mcp/src/agents_remember/serving/terminal_liveness.py:174-221; mcp/src/agents_remember/serving/terminal_liveness.py:223-268 |
| The deferred drain re-reads committed rows before invoking the observer, while the row-local guard records `interactionSyncError` and continues on later rows. | `_run_deferred_interaction_syncs`; `_observe_control_snapshot` | mcp/src/agents_remember/serving/terminal_liveness.py:300-322; mcp/src/agents_remember/serving/terminal_liveness.py:532-582 |
| The module exercises full/starting order, aborted-pass suppression, guarded continuation, and post-commit failure durability with the real catalog and sweeper seams. | `TerminalLivenessDeferredWorkTests` | mcp/tests/test_terminal_liveness_deferred_work.py:101-366 |
| The candidate classifies this module once in the explicit unit-regression lane. | "mcp/tests/test_terminal_liveness_deferred_work.py" | mcp/tests/test-evidence-lanes.toml:142-142 |
## Cross-Repo References

No meaningful cross-repository implementation boundary is established by this repository-owned unit-regression module.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_deferred_work.py" repointed to mcp/tests/test-evidence-lanes.toml:142-142. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 0 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-12T01:06:15+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_deferred_work.py" repointed to mcp/tests/test-evidence-lanes.toml:115-115. No content impact: mechanical anchor-range projection bound to citation source snapshot 1740540b8733028dd833a3538d739271e8925ea5f51911a0f8dcd8c49e7e1c13; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-10T12:23+02:00 — 260831-LOCR-L20 curator post-sync repair: the L20↔L28 manifest union
  inserted `test_terminal_evidence_cursors.py` at manifest row 103, shifting this module's own row to
  104. The lane citation above was recomputed to `mcp/tests/test-evidence-lanes.toml:104-104`; the
  previous `103-103` now addresses the sibling L20 module's row. Citation coordinates only — the
  `unit-regression` classification, the hermetic boundary, and all verification ownership are
  unchanged. Repaired here because the breakage was caused by the union landing in this leaf's
  manifest candidate; the owning L28 seat may fold it into its own account.

- 2026-09-10T11:53+02:00 — 260831-LOCR-L09 curator: shifted this card's lane citation by one line, `mcp/tests/test-evidence-lanes.toml:103-103` → `104-104`, after the LOCR-L09 row `test_state_signal_boundary_delivery.py` was registered earlier in the same `unit-regression` bracket and moved every following manifest row down one. The anchor and claim bytes are unchanged; no behavioral or verification claim changed.

- 2026-09-10T11:52:46+02:00 — 260831-LOCR-L25 curator: repointed this card's lane citation from `mcp/tests/test-evidence-lanes.toml:103-103` to `104-104`. The move is a pure coordinate shift: L25's new `mcp/tests/test_parked_external_await_separation.py` unit-regression row was inserted above this module's row. The claim, its anchor, and the lane classification are unchanged; no behavioral or verification claim changed, and verification remains closeout-owned.

- 2026-09-10T11:24+02:00 — 260831-LOCR-L28 curator: corrected this module's evidence-lane classification from `integration` to `unit-regression`. It is hermetic and integration was already at exactly its 150-collected-case cap, so the earlier registration would have taken the lane to 155 and broken full-suite collection. The lane citation now names the module's own manifest row (`mcp/tests/test-evidence-lanes.toml:103-103`) instead of a block range, and the Purpose/Conventions wording follows the corrected lane. No behavioral or verification claim changed; verification remains closeout-owned because the source is an uncommitted candidate.
- 2026-09-08T14:35+02:00 — Created the file card for the R28 deferred-work proof. Recorded the full/starting post-commit ordering, aborted-pass suppression, row-local quarantine continuation, and escaping post-commit failure boundary from the current source. Verification remains closeout-owned because the source is an uncommitted candidate.
