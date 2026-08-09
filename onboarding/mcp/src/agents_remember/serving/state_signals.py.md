# mcp/src/agents_remember/serving/state_signals.py

| Field                  | Value                                                     |
| ---------------------- | --------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/serving/state_signals.py`        |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated            | 2026-08-09T01:21+02:00                                     |
| lastVerifiedCommitHash | `7af76249ff1aa728d34a6e81c5f09c8bcb797484`                                    |
| lastVerifiedCommitDate | 2026-08-09T02:17:45+02:00|
| governingOverview      | `overview.md`                                             |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

The predicate library of the worker→manager state-signal relay (260713-TES-L2): facts from
catalog turn truth, never inference. It produces the three new mechanical findings — a
completed/interrupted worker turn that has not been relayed (`state-signal-due`), a worker
still `turn-ended` long after rows landed at its boundary (`non-reaction-due`), and pending
rows whose target seat crossed a turn boundary after the last attempt (`boundary-drain`) —
plus the held-row predicate that keeps a boundary-held signal off the redelivery/escalation
safety nets while its manager is alive but mid-turn.

## Code Commentary

### Logic

`NON_REACTION_WINDOW_SECONDS = 300.0` cit:([`NON_REACTION_WINDOW_SECONDS`], mcp/src/agents_remember/serving/state_signals.py:25-27) is the leaf-authored bounded window (R5),
mirroring the pickup-staleness convention.

`evaluate_state_signal_findings` cit:([`evaluate_state_signal_findings`], mcp/src/agents_remember/serving/state_signals.py:44-73) scans running worker harness rows at
`turn_state="turn-ended"` whose `terminal_outcome` is `completed` or `interrupted`, has a
`terminal_evidence_id`, and has not yet been relayed (`state_signal_emitted_for` != that id).
The evidence id is the per-seat+turn dedupe identity.

`evaluate_non_reaction_findings` cit:([`evaluate_non_reaction_findings`], mcp/src/agents_remember/serving/state_signals.py:75-122) finds pending inbox rows landed at this seat
(`deliveredToSession` + `adapterDeliveryState="accepted"` + `adapterAcceptedAt`), takes the
oldest, and — once it is older than the window and the seat is still `turn-ended` — emits one
`non-reaction-due` finding per landed-row episode, deduped by `non_reaction_emitted_for`. It
is worker→manager scope only; manager-target rows are excluded. The scan is O(catalog ×
inbox) per sweep, bounded by compaction and fleet caps (accepted note F7).

`evaluate_boundary_drain_findings` cit:([`evaluate_boundary_drain_findings`], mcp/src/agents_remember/serving/state_signals.py:124-167) is the N15 drain: pending, not-yet-landed rows
whose target is at a turn boundary (`seat_at_turn_boundary`) and whose `lastAttemptAt` predates
the boundary transition (`turn_state_changed_at`) are pushed. Rows without a fresh boundary
stay on the durable backoff schedule.

`state_signal_held_on_boundary` cit:([`state_signal_held_on_boundary`], mcp/src/agents_remember/serving/state_signals.py:30-42) is the F1 fix: a non-landed `state-signal` row whose
target is a LIVE running seat is excluded from escalation and the redeliverable budget —
delivery timing belongs to the boundary gate, and the row keeps the ordinary safety net only
when the target is dead/archived.

`state_signal_response` / `non_reaction_response` cit:([`state_signal_response`, `non_reaction_response`], mcp/src/agents_remember/serving/state_signals.py:169-185) build the self-contained payload:
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
- Landed rows remain `state=pending` until the L4 schema migration; they are terminal by rule
  on this path.
- Non-reaction residue is a distinct fact, never worded or modeled as "unconsumed rows".
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
| No external/domain document defines this relay; the catalog turn truth and tests are the authority. | `evaluate_state_signal_findings` | mcp/src/agents_remember/serving/state_signals.py:44-73 |

## Repo-Internal References

The predicates read `TerminalCatalog` and `OperatorInboxStore` directly (never the
projection); the actions that consume the findings live in `_agent_notifier_actions.py`, and
the landing predicate lives on the inbox record.

| Finding | Anchor | Source |
| --- | --- | --- |
| The catalog row's terminal truth, boundary vocabulary, and dedupe markers. | `seat_at_turn_boundary`; "class TerminalCatalogEntry:" | mcp/src/agents_remember/serving/terminal_catalog.py:95-103; mcp/src/agents_remember/serving/terminal_catalog.py:106-220 |
| Terminality for landed state-signal rows (accepted at boundary). | `state_signal_landed` | mcp/src/agents_remember/controlplane/operator_inbox_records.py:54-65 |
| The action layer: emit, non-reaction, boundary drain, held-row exclusions. | `_emit_state_signal`; `_emit_non_reaction`; `_drain_boundary`; `_FINDING_ACTIONS` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:614-675; mcp/src/agents_remember/serving/_agent_notifier_actions.py:676-726; mcp/src/agents_remember/serving/_agent_notifier_actions.py:727-741; mcp/src/agents_remember/serving/_agent_notifier_actions.py:744-755 |
| The relay simulation suites (incident-#1, boundary hold, dedupe, rebinding, idle flap, non-reaction). | `StateSignalRelayTests`; `StateSignalDeliveryTests` | mcp/tests/test_state_signal_relay.py:128-735; mcp/tests/test_state_signal_delivery.py:88-229 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this relay. | — | — |

## Update History

- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: created this sidecar for the new
  state-signal predicate module (NON_REACTION_WINDOW_SECONDS=300, three finding families,
  held-on-boundary exclusion, self-contained payloads, R1/F7 accepted notes). Verification
  metadata pinned to the leaf base `1c1629fc` until closeout stamps the 260713-TES-L2 commit.
