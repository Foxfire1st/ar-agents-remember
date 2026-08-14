# mcp/tests/test_state_signal_delivery.py

| Field                  | Value                                                      |
| ---------------------- | ---------------------------------------------------------- |
| repository             | agents-remember                                            |
| path                   | `mcp/tests/test_state_signal_delivery.py`                  |
| doc_type               | `file-level-onboarding`                                    |
| lastUpdated            | 2026-08-09T06:48+02:00                                      |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                    |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                              |

## Governing Overview

[mcp/tests overview](../overview.md)

## Purpose

The delivery-level gate suite for 260713-TES-L2: proves the availability gate holds a
`state-signal` row while its target is working, that `state_signal_landed` is unreachable via
a non-boundary-gated push (the F1 delivery seam), that boundary acceptance is terminal, that
queued acceptance is not, and that landed rows are excluded from redelivery/escalation.

## Code Commentary

### Logic

`StateSignalDeliveryTests` cit:([`StateSignalDeliveryTests`], mcp/tests/test_state_signal_delivery.py:88-229) drives `deliver_inbox_entry` through fake paster/session
seams:

- `test_boundary_gate_holds_when_target_is_working` cit:([`test_boundary_gate_holds_when_target_is_working`], mcp/tests/test_state_signal_delivery.py:118-136): zero adapter submissions,
  row recorded `queued`/`queued`.
- `test_state_signal_landed_is_unreachable_via_a_non_boundary_gated_push` cit:([`test_state_signal_landed_is_unreachable_via_a_non_boundary_gated_push`], mcp/tests/test_state_signal_delivery.py:138-155): the
  default admission cannot land a state-signal mid-turn (F1 regression).
- `test_boundary_gate_allows_at_turn_ended_and_acceptance_is_terminal` cit:([`test_boundary_gate_allows_at_turn_ended_and_acceptance_is_terminal`], mcp/tests/test_state_signal_delivery.py:157-179): accepted at
  the boundary lands (`state="landed"` since the N13/N16 migration) and schedules no further
  attempt.
- `test_busy_adapter_queued_acceptance_is_not_terminal` cit:([`test_busy_adapter_queued_acceptance_is_not_terminal`], mcp/tests/test_state_signal_delivery.py:181-198): queued acceptance keeps
  the row `state="pending"` (never landed).
- `test_landed_state_signal_is_not_redeliverable_or_ladder_eligible` cit:([`test_landed_state_signal_is_not_redeliverable_or_ladder_eligible`], mcp/tests/test_state_signal_delivery.py:200-228): `is_due`
  and escalation findings skip landed rows.

### Conventions

Unit-level delivery tests complement the sweep-level relay suite: this file pins the
fail-closed row-kind gate in `_delivery_refusal` independent of which caller drives delivery.

### Invariants And Boundaries

- The gate is enforced BY ROW KIND inside `_delivery_refusal`; caller admission is
  defense-in-depth.
- Acceptance at a boundary is terminal on this path; queued acceptance is not.
- Landed rows carry the formal `state="landed"` terminal (N13/N16) and are excluded from
  redelivery/escalation/reclamation.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines this delivery gate; the N1 boundary contract and tests are the authority. | `StateSignalDeliveryTests` | mcp/tests/test_state_signal_delivery.py:88-229 |

## Repo-Internal References

The suite exercises `serving/inbox_delivery.py`, `controlplane/operator_inbox_records.py`,
`controlplane/inbox_backoff.py`, and `serving/_agent_notifier_evaluation.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fail-closed row-kind gate under test. | `_delivery_refusal` | mcp/src/agents_remember/serving/inbox_delivery.py:107-162 |
| The boundary vocabulary the gate consults. | `seat_at_turn_boundary` | mcp/src/agents_remember/models/terminal_catalog.py:58-64 |
| Landed terminality and its backoff/escalation exclusions. | "def state_signal_landed("; "def is_due(" | mcp/src/agents_remember/controlplane/operator_inbox_records.py:29-29; mcp/src/agents_remember/kernel/primitives/inbox_backoff.py:99-99 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary participates in this suite. | — | — |

## Update History

- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: recorded the current landed-versus-queued state-signal
  delivery coverage against the staged source; verification metadata remains pinned until closeout.

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the formal `state="landed"`
  assertions (boundary acceptance lands; queued acceptance stays pending) after the N13/N16
  migration. Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: created this sidecar for the new
  delivery-gate suite (boundary hold, unreachable-landed regression, terminal vs queued
  acceptance, exclusion from redelivery/escalation). Verification metadata pinned to the leaf base `1c1629fc` until closeout stamps the 260713-TES-L2 commit.
