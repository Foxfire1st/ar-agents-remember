# mcp/tests/test_inbox_rebinding_mechanics.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_inbox_rebinding_mechanics.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T06:48+02:00 |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840` |
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The mechanics-level R7 regression suite for 260713-TES-L4 (33 test methods): transition
idempotence across the formal terminal vocabulary; N14 row-owner derivation (dispatch-brief
exact-pinned, manager→orchestrator replacement, stamped-owner fallbacks, fail-closed role
mailboxes); the rebind/expire/unresolved action skip branches; rebind-grace and pending-expiry
evaluation branches (unparseable stamps keep grace unmeasured); retention branches for legacy
consumed and terminal markers; loop-mode behavior; the N13 legacy-landed fold; the D4 cap-fill
eviction branch; the F1 stale-snapshot terminal-authority shapes (concurrent supersede/landed/
expired/unresolved against stale appends) and the supersede-during-in-flight-delivery e2e;
and delivery of a rebound row to the replacement in the next sweep. All tests were red before
implementation and assert the FINAL folded store state.

## Code Commentary

### Logic

- `TransitionIdempotenceTests` cit:([`TransitionIdempotenceTests`], mcp/tests/test_inbox_rebinding_mechanics.py:60-129) — landed/superseded/unresolved/
  expired/rebind idempotence; rebind only rewrites pending rows; expiry can readdress the
  terminal marker.
- `RowOwnerDerivationTests` cit:([`RowOwnerDerivationTests`], mcp/tests/test_inbox_rebinding_mechanics.py:131-287) — dispatch-brief never derives an owner;
  manager rows resolve a live orchestrator or its scoped replacement; stamped-owner fallbacks
  cover manager/orchestrator/architect; unroutable rows return an empty owner; unknown subjects
  and ambiguous scopes fall back to role mailboxes.
- `ActionSkipBranchTests` cit:([`ActionSkipBranchTests`], mcp/tests/test_inbox_rebinding_mechanics.py:289-525) — rebind/rebind-expired/expire/unresolved
  skip branches, replacement-appeared reroute, missing-entry silence, and the stale-sweep
  idempotent-false branch asserting final store states.
- `EvaluationBranchTests` cit:([`EvaluationBranchTests`], mcp/tests/test_inbox_rebinding_mechanics.py:527-576) — unparseable death stamps keep the grace
  unmeasured; running seats have no death stamp; unparseable created-at skips pending expiry.
- `KeepRetentionBranchTests` cit:([`KeepRetentionBranchTests`], mcp/tests/test_inbox_rebinding_mechanics.py:578-627) — legacy consumed marker retention,
  terminal-marker retention windows, and immediate ladder-resolved drops.
- `LoopModeTests` cit:([`LoopModeTests`], mcp/tests/test_inbox_rebinding_mechanics.py:629-698) — loop/cadence behavior for the last-good settings and
  relay-death surfaces.
- `LegacyLandedFoldTests` cit:([`LegacyLandedFoldTests`], mcp/tests/test_inbox_rebinding_mechanics.py:700-773) — a pre-migration by-rule state-signal
  row folds into the formal `landed` state exactly once (`_fold_legacy_landed`, N13).
- `CapFillBranchTests` cit:([`CapFillBranchTests`], mcp/tests/test_inbox_rebinding_mechanics.py:825-870) — terminal markers fill the remaining cap slots
  newest-first (D4 eviction class).
- `StaleSnapshotTerminalAuthorityTests` cit:([`StaleSnapshotTerminalAuthorityTests`], mcp/tests/test_inbox_rebinding_mechanics.py:823-927) — the F1
  shapes: concurrent supersede survives a stale landing append; concurrent landed survives a
  stale unresolved; concurrent expired survives a stale landing; stale unresolved after landed
  appends nothing; same-state idempotence still holds — each asserting final folded state and
  snapshot-count stability.
- `SupersedeDuringInFlightDeliveryTests` cit:([`SupersedeDuringInFlightDeliveryTests`], mcp/tests/test_inbox_rebinding_mechanics.py:929-1045) — the
  e2e false-ack shape: delivery blocked mid-flight, explicit supersede, release — final state
  `superseded`/`overtaken`, NOT `landed`.
- `ReboundDeliveryToReplacementTests` cit:([`ReboundDeliveryToReplacementTests`], mcp/tests/test_inbox_rebinding_mechanics.py:1047-1150) — sweep 1
  rebinds to the replacement with no push; sweep 2 pushes the same durable row to the
  replacement's session exactly once and it lands with `deliveredToSession` on the new seat
  (F3 delivery-to-B proof).

### Conventions

Simulation-harness style shared with `test_inbox_arrival_guarantee.py`: temp-rooted stores,
fake catalog rows, injected clocks, production transitions/actions (`store.transition`,
`run_agent_notifier_sweep`, `deliver_inbox_entry`), and final-folded-store assertions rather
than action-string-only checks.

### Invariants And Boundaries

- Terminal states are not interchangeable: a stale snapshot must never overwrite a different
  terminal truth (F1) — every terminal transition is a lock-held latest-fold operation.
- Rebind clears per-attempt adapter correlation and resets the attempt clock (N14); the
  replacement starts a fresh delivery schedule.
- Grace expiry readdresses the terminal marker to the scoped architect mailbox (N3 mailbox-not-
  rung); dispatch-brief rows never rebind.
- Compaction keeps pending rows so the sweep can stamp `expired` first (§9); the cap remains the
  hard bound.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`; the
rebinding/terminal mechanics are same-repository runtime behavior proven by source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines these mechanics; the F1 review shapes and the N-rulings are the authority. | `StaleSnapshotTerminalAuthorityTests` | mcp/tests/test_inbox_rebinding_mechanics.py:823-927 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The lock-held latest-fold transition primitive under test. | `transition` | mcp/src/agents_remember/controlplane/operator_inbox_store.py:73-100 |
| The terminal/rebind transitions under test. | `mark_landed`; `mark_superseded`; `mark_unresolved`; `mark_expired`; `rebind_entry` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:253-275; mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:278-306; mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:309-335; mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:338-365; mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:368-406 |
| The row-owner derivation under test. | `derive_row_owner` | mcp/src/agents_remember/controlplane/signal_routing.py:393-412 |
| The rebind/expiry predicates under test. | `evaluate_rebind_findings`; `evaluate_pending_expiry_findings` | mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:176-246 |
| The legacy-landed migration fold under test. | `_fold_legacy_landed` | mcp/src/agents_remember/serving/agent_notifier.py:222-250 |
| The retention branches under test. | `_keep_inbox_entry`; `inbox_keep_ids` | mcp/src/agents_remember/controlplane/interaction_retention.py:140-163; mcp/src/agents_remember/controlplane/interaction_retention.py:199-221 |
| The e2e delivery/rebound seams under test. | `deliver_inbox_entry` | mcp/src/agents_remember/serving/inbox_delivery.py:165-223 |
| The rebind/grace-expiry actions under test. | `_rebind_due`; `_rebind_expired` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:163-286 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary participates in this suite. | — | — |

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: created this file-level onboarding card for
  the new rebinding-mechanics forcing suite (33 test methods: transition idempotence, owner
  derivation, action/evaluation/retention branches, legacy fold, cap fill, F1 stale-snapshot
  authority, supersede-during-in-flight e2e, rebound delivery-to-B). Verification metadata
  pinned until closeout stamps the 260713-TES-L4 commit.
