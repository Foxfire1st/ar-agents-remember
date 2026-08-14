# mcp/tests/test_inbox_rebinding_mechanics.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_inbox_rebinding_mechanics.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T00:08+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite pins durable inbox transition idempotence and replacement rebinding. Row ownership is
re-resolved from the subject task-document reference and seat role through task containment to the
unique current parent occupant; dispatch briefs remain exact-pinned, stamped structural owners are
the bounded fallback, and ambiguous structural occupants refuse instead of guessing a role mailbox.
The remaining cases cover notifier action/evaluation/retention branches, legacy terminal folding,
stale-snapshot authority, in-flight supersession, and delivery to the replacement's current seat.

## Code Commentary

### Logic

- `TransitionIdempotenceTests` cit:([`TransitionIdempotenceTests`], mcp/tests/test_inbox_rebinding_mechanics.py:72-141) — landed/superseded/unresolved/
  expired/rebind idempotence; rebind only rewrites pending rows; expiry can readdress the
  terminal marker.
- `RowOwnerDerivationTests` cit:([`RowOwnerDerivationTests`], mcp/tests/test_inbox_rebinding_mechanics.py:143-224) — task containment resolves manager rows to the
  unique current orchestrator; stamped document-and-role owners rebind to their current occupant;
  dispatch briefs and unroutable rows return empty, while ambiguous structural owners refuse.
- `ActionSkipBranchTests` cit:([`ActionSkipBranchTests`], mcp/tests/test_inbox_rebinding_mechanics.py:226-493) — rebind/rebind-expired/expire/unresolved
  skip branches, replacement-appeared reroute, missing-entry silence, and the stale-sweep
  idempotent-false branch asserting final store states.
- `EvaluationBranchTests` cit:([`EvaluationBranchTests`], mcp/tests/test_inbox_rebinding_mechanics.py:495-544) — unparseable death stamps keep the grace
  unmeasured; running seats have no death stamp; unparseable created-at skips pending expiry.
- `KeepRetentionBranchTests` cit:([`KeepRetentionBranchTests`], mcp/tests/test_inbox_rebinding_mechanics.py:547-595) — legacy consumed marker retention,
  terminal-marker retention windows, and immediate ladder-resolved drops.
- `LoopModeTests` cit:([`LoopModeTests`], mcp/tests/test_inbox_rebinding_mechanics.py:598-667) — loop/cadence behavior for the last-good settings and
  relay-death surfaces.
- `LegacyLandedFoldTests` cit:([`LegacyLandedFoldTests`], mcp/tests/test_inbox_rebinding_mechanics.py:669-788) — a pre-migration by-rule state-signal
  row folds into the formal `landed` state exactly once (`_fold_legacy_landed`, N13).
- `CapFillBranchTests` cit:([`CapFillBranchTests`], mcp/tests/test_inbox_rebinding_mechanics.py:790-835) — terminal markers fill the remaining cap slots
  newest-first (D4 eviction class).
- `StaleSnapshotTerminalAuthorityTests` cit:([`StaleSnapshotTerminalAuthorityTests`], mcp/tests/test_inbox_rebinding_mechanics.py:838-942) — the F1
  shapes: concurrent supersede survives a stale landing append; concurrent landed survives a
  stale unresolved; concurrent expired survives a stale landing; stale unresolved after landed
  appends nothing; same-state idempotence still holds — each asserting final folded state and
  snapshot-count stability.
- `SupersedeDuringInFlightDeliveryTests` cit:([`SupersedeDuringInFlightDeliveryTests`], mcp/tests/test_inbox_rebinding_mechanics.py:944-1059) — the
  e2e false-ack shape: delivery blocked mid-flight, explicit supersede, release — final state
  `superseded`/`overtaken`, NOT `landed`.
- `ReboundDeliveryToReplacementTests` cit:([`ReboundDeliveryToReplacementTests`], mcp/tests/test_inbox_rebinding_mechanics.py:1061-1187) — sweep 1
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
| The terminal/rebind transitions under test. | `mark_landed`; `mark_superseded`; `mark_unresolved`; `mark_expired`; `rebind_entry` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:240-262; mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:265-293; mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:296-322; mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:325-352; mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:355-393 |
| The row-owner derivation under test. | `derive_row_owner` | mcp/src/agents_remember/controlplane/signal_routing.py:280-298 |
| The rebind/expiry predicates under test. | `evaluate_rebind_findings`; `evaluate_pending_expiry_findings` | mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:127-172; mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:175-198 |
| The legacy-landed migration fold under test. | `_fold_legacy_landed` | mcp/src/agents_remember/serving/agent_notifier.py:198-226 |
| The retention branches under test. | `_keep_inbox_entry`; `inbox_keep_ids` | mcp/src/agents_remember/controlplane/interaction_retention.py:140-163; mcp/src/agents_remember/controlplane/interaction_retention.py:199-221 |
| The e2e delivery/rebound seams under test. | `deliver_inbox_entry` | mcp/src/agents_remember/serving/inbox_delivery.py:165-223 |
| The rebind/grace-expiry actions under test. | `_rebind_due`; `_rebind_expired` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:163-286 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary participates in this suite. | — | — |

## 260713-TES-L5 Current Delta — Nudge Store Gone From Harnesses

All four sweep-context builders drop `OrchestrationNudgeStore`; no harness needs it because
the sweep no longer nudges. Rebind/grace/expiry mechanics are unchanged.

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T00:08+02:00 — Replaced the obsolete spawn-provenance/role-mailbox description with
  current task-document containment and unique-occupant refusal semantics; the transition subtest's
  integer diagnostic is serialization-only for xdist. Verification metadata remains pinned until
  closeout.

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_inbox_rebinding_mechanics.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the current staged inbox-rebinding mechanics harness; the existing assertions remain accurate. Verification metadata remains pinned until closeout.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the nudge-store removal from all
  rebinding-mechanics harness contexts. Verification metadata pinned until closeout stamps
  the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: created this file-level onboarding card for
  the new rebinding-mechanics forcing suite (33 test methods: transition idempotence, owner
  derivation, action/evaluation/retention branches, legacy fold, cap fill, F1 stale-snapshot
  authority, supersede-during-in-flight e2e, rebound delivery-to-B). Verification metadata
  pinned until closeout stamps the 260713-TES-L4 commit.
