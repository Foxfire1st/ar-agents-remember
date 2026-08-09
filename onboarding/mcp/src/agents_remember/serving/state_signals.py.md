# mcp/src/agents_remember/serving/state_signals.py

| Field                  | Value                                                     |
| ---------------------- | --------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/serving/state_signals.py`        |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated            | 2026-08-09T06:48+02:00|
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840`                                    |
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview      | `overview.md`                                             |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

The predicate library of the worker→manager and compound-idle state-signal relay
(260713-TES-L2 + L3): facts from catalog turn truth, never inference. It produces the
four mechanical findings — a completed/interrupted worker turn that has not been relayed
(`state-signal-due`), a manager seat whose whole live worker set is simultaneously at a turn
boundary and not yet relayed (`compound-idle-due`), a seat (worker or manager) still
`turn-ended` long after rows landed at its boundary (`non-reaction-due`), and pending rows
whose target seat crossed a turn boundary after the last attempt (`boundary-drain`) — plus
the held-row predicate that keeps a boundary-held signal off the redelivery/escalation
safety nets while its owner is alive but mid-turn. **260713-TES-L4 (N16/N13/N2)**: landing is
now the formal `state == "landed"` (the by-rule predicate folded into the schema), and the
boundary-drain predicate skips rows addressed to dead seats — the N2/N14 rebind machinery owns
them, and a dead seat has no boundary to cross.

## Code Commentary

### Logic

`NON_REACTION_WINDOW_SECONDS = 300.0` cit:([`NON_REACTION_WINDOW_SECONDS`], mcp/src/agents_remember/serving/state_signals.py:28-30) is the leaf-authored bounded window (R5),
mirroring the pickup-staleness convention.

`evaluate_state_signal_findings` cit:([`evaluate_state_signal_findings`], mcp/src/agents_remember/serving/state_signals.py:128-157) scans running worker harness rows at
`turn_state="turn-ended"` whose `terminal_outcome` is `completed` or `interrupted`, has a
`terminal_evidence_id`, and has not yet been relayed (`state_signal_emitted_for` != that id).
The evidence id is the per-seat+turn dedupe identity.

`evaluate_non_reaction_findings` cit:([`evaluate_non_reaction_findings`], mcp/src/agents_remember/serving/state_signals.py:182-229) finds formal `state == "landed"` rows at this seat
(`deliveredToSession` + `adapterDeliveryState="accepted"` + `adapterAcceptedAt`), takes the
oldest, and — once it is older than the window and the seat is still `turn-ended` — emits one
`non-reaction-due` finding per landed-row episode, deduped by `non_reaction_emitted_for`. It
covers BOTH `worker` and `manager` seats since 260713-TES-L3: the emitter routes a worker's
residue through the L2 manager path and a manager's residue one hop up to its orchestrator
(see `_agent_notifier_actions.py.md`). The scan is O(catalog × inbox) per sweep, bounded by
compaction and fleet caps (accepted note F7).

### 260713-TES-L3 Compound-Idle Predicates

`COMPOUND_IDLE_SWEEP_LATENCY_SECONDS = 10.0` cit:([`COMPOUND_IDLE_SWEEP_LATENCY_SECONDS`], mcp/src/agents_remember/serving/state_signals.py:32-35) is the recorded N6 latency
bound: one agent-notifier sweep at the default 10 s cadence, so a set observed idle is
signaled no later than ~one sweep after that tick.

`_compound_worker_index` cit:([`_compound_worker_index`], mcp/src/agents_remember/serving/state_signals.py:38-67) is a SINGLE catalog scan per sweep: live managers and live
workers indexed by spawner id and master key, so every compound-idle set is assembled in
O(catalog + sets), never O(managers × catalog). Status is gated FIRST here — non-running
rows (retired/exited/landed) are never indexed, so their stale turn state never counts.

`compound_idle_sets` cit:([`compound_idle_sets`], mcp/src/agents_remember/serving/state_signals.py:69-103) returns every live manager's member tuple keyed by manager id.
Membership is **master-scoped on EVERY arm** (fix round 1, F1): a worker joins only when its
binding (`binding_leaf_key` / `replacement_for_leaf`) shares the manager's `repo/master`
prefix, whether or not the manager spawned it — the `by_spawner` arm is filtered by the same
`master_key` check as the `by_master` arm, so a cross-master spawned worker neither blocks
nor joins. A manager with no workers never forms a set (F3 ruling: zero-worker no-signal,
fail-closed); a running member with `turn_state=None` is unknown ≠ idle and fails the set
closed; idle = `turn_state ∈ {turn-ended, awaiting-input}`; `working`/`stale` means the set
is not idle. An unbound manager (no master anchor) never forms a set (accepted residual R1).

`compound_idle_signature` cit:([`compound_idle_signature`], mcp/src/agents_remember/serving/state_signals.py:104-111) is the episode identity: sorted
`member-id:turn_state:turn_state_changed_at` over every live member. A seat returning to
activity changes the signature, which is the re-arm — there is no separate marker-clearing
write.

`evaluate_compound_idle_findings` cit:([`evaluate_compound_idle_findings`], mcp/src/agents_remember/serving/state_signals.py:159-180) emits one `compound-idle-due`
finding per un-relayed set (`compound_idle_emitted_for != signature`), one finding per
manager seat, with `source_id=signature` carried only as the trigger — the emitter derives
the ACTION-time signature and never consumes this informational value (R2 residual).

`compound_idle_response` cit:([`compound_idle_response`], mcp/src/agents_remember/serving/state_signals.py:286-297) builds the self-contained payload naming the
manager and every set member (`id@binding-or-replacement`), so the orchestrator can combine
the pure seat-state fact with the non-reaction residue fact (N15/N16) without remembering
who was in the set.

`evaluate_boundary_drain_findings` cit:([`evaluate_boundary_drain_findings`], mcp/src/agents_remember/serving/state_signals.py:231-274) is the N15 drain: pending, not-yet-landed rows
whose target is at a turn boundary (`seat_at_turn_boundary`) and whose `lastAttemptAt` predates
the boundary transition (`turn_state_changed_at`) are pushed. Rows without a fresh boundary
stay on the durable backoff schedule; rows addressed to a dead/replaced seat are skipped here
and owned by the rebind path (N2/N14, L4).

`state_signal_held_on_boundary` cit:([`state_signal_held_on_boundary`], mcp/src/agents_remember/serving/state_signals.py:114-126) is the F1 fix: a non-landed `state-signal` row whose
target is a LIVE running seat is excluded from escalation and the redeliverable budget —
delivery timing belongs to the boundary gate, and the row keeps the ordinary safety net only
when the target is dead/archived.

`state_signal_response` / `non_reaction_response` cit:([`state_signal_response`, `non_reaction_response`], mcp/src/agents_remember/serving/state_signals.py:276-283; mcp/src/agents_remember/serving/state_signals.py:299-305) build the self-contained payload:
session, leaf, turn/evidence id, outcome, timestamps, and interrupt origin.

### Conventions

Findings carry the sweep's standard identity fields (session, leaf, role, source id) so
`act_on_finding` can resolve the owner at action time. The relay emits facts only; it never
judges, never schedules respawn, and never reasons about expectation deadlines.

### Invariants And Boundaries

- Exactly one durable row per seat+turn (evidence-id keyed); re-projection renews the same
  row, a new turn mints a distinct row.
- `acceptance=queued` from a busy adapter is NOT a landing; only correlated acceptance at a
  turn boundary is terminal on this path (`state_signal_landed`).
- Killed seats stay `exited` and hung seats stay `stale`: neither produces a done signal.
- Landed rows carry the formal `state="landed"` terminal (N13/N16 migration); the old
  by-rule pending landing no longer exists.
- Non-reaction residue is a distinct fact, never worded or modeled as "unconsumed rows"; it
  now covers worker→manager AND manager→orchestrator (L3), and the compound-idle predicate
  stays a pure seat-state signal that rides alongside it.
- Compound-idle sets are master-scoped on every arm, status-first, unknown≠idle, and never
  empty: zero-worker managers and unbound managers never signal (F1/F3/R1 pins).
- Residual R1 (accepted, folded into 260713-TES-L4): a held row whose boundary push returns
  queued/unconfirmed waits for the next boundary — delayed, never lost or duplicated.

### Todos

- F7 note (accepted): `evaluate_non_reaction_findings` scans the full inbox per catalog row;
  an index by `deliveredToSession` would make it linear.
- R1 note (accepted): periodic reconciliation-only redelivery of held state-signal rows is
  owned by 260713-TES-L4 deliver-until-LANDED.

## Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`; the
relay semantics are same-repository runtime behavior proven by source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines this relay; the catalog turn truth and tests are the authority. | `evaluate_state_signal_findings` | mcp/src/agents_remember/serving/state_signals.py:128-157 |

## Repo-Internal References

The predicates read `TerminalCatalog` and `OperatorInboxStore` directly (never the
projection); the actions that consume the findings live in `_agent_notifier_actions.py`, and
the landing predicate lives on the inbox record.

| Finding | Anchor | Source |
| --- | --- | --- |
| The catalog row's terminal truth, boundary vocabulary, and dedupe markers. | `seat_at_turn_boundary`; "class TerminalCatalogEntry:" | mcp/src/agents_remember/serving/terminal_catalog.py:95-103; mcp/src/agents_remember/serving/terminal_catalog.py:106-220 |
| Terminality for landed state-signal rows (accepted at boundary). | `state_signal_landed` | mcp/src/agents_remember/controlplane/operator_inbox_records.py:66-74 |
| The action layer: emit, non-reaction, boundary drain, held-row exclusions. | `_emit_state_signal`; `_emit_non_reaction`; `_drain_boundary`; `_FINDING_ACTIONS` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:758-817; mcp/src/agents_remember/serving/_agent_notifier_actions.py:879-936; mcp/src/agents_remember/serving/_agent_notifier_actions.py:939-948; mcp/src/agents_remember/serving/_agent_notifier_actions.py:956-969 |
| The relay simulation suites (incident-#1, boundary hold, dedupe, rebinding, idle flap, non-reaction). | `StateSignalRelayTests`; `StateSignalDeliveryTests` | mcp/tests/test_state_signal_relay.py:128-735; mcp/tests/test_state_signal_delivery.py:88-229 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this relay. | — | — |

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: updated the landing vocabulary to the formal
  `state="landed"` (non-reaction scan now filters on the terminal state; the by-rule pending
  predicate is gone), and recorded the dead-seat skip in `evaluate_boundary_drain_findings`
  (N2/N14 — rebind machinery owns dead-target rows). Verification metadata pinned until
  closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: added the compound-idle predicate family
  (`_compound_worker_index`, `compound_idle_sets`, `compound_idle_signature`,
  `evaluate_compound_idle_findings`, `compound_idle_response`,
  `COMPOUND_IDLE_SWEEP_LATENCY_SECONDS=10.0`), master-scoped membership on every arm,
  zero-worker no-signal, action-time-signature semantics, and widened the non-reaction
  predicate from worker-only to worker+manager scope. Verification metadata pinned until
  closeout stamps the 260713-TES-L3 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: created this sidecar for the new
  state-signal predicate module (NON_REACTION_WINDOW_SECONDS=300, three finding families,
  held-on-boundary exclusion, self-contained payloads, R1/F7 accepted notes). Verification
  metadata pinned to the leaf base `1c1629fc` until closeout stamps the 260713-TES-L2 commit.
