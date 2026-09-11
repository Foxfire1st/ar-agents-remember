# mcp/tests/test_state_signal_boundary_delivery.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/tests/test_state_signal_boundary_delivery.py`       |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated | 2026-09-10T11:42+02:00 |
| lastVerifiedCommitHash | `8a46bc8d186d9444bf9a83b21ad4683ec4937e3d` |
| lastVerifiedCommitDate | 2026-09-11T11:04:29+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Forces one boundary-aware durable state-signal delivery machine on the existing owner-signal/inbox
path, headless and without a dashboard read: the row is durable before the source's emitted marker
is stamped, a `working` manager holds that same row with zero adapter submissions, and the row
reaches the current manager at its next admissible turn boundary — across an occupant replacement, a
fresh notifier context, and a failed protocol submission. Row identity, marker state, and attempt
state are asserted directly rather than inferred from a green result.

## Code Commentary

### Logic

Six retained cases, one delivery guarantee each:

1. `test_persist_failure_keeps_marker_unset_and_retry_publishes_one_row` — the first inbox
   append/renew raises, so no marker and no row exist and nothing is submitted; the next sweep
   publishes exactly one row and the marker callback observes that durable row.
2. `test_held_signal_follows_replacement_manager_on_the_same_row` — manager A holds the row while
   `working`; A is replaced by B, whose bind resets the attempt clock (`attemptCount=0`,
   `lastAttemptAt=None`); B's later boundary drains that same row id to B exactly once.
3. `test_held_signal_survives_a_fresh_notifier_context` — the durable files are re-read through
   brand-new stores and a new notifier context, and the held row still lands unchanged.
4. `test_held_signal_lands_at_each_classified_turn_boundary` — `turn-ended` and `awaiting-input`
   each drain the same held row through the shared protocol path.
5. `test_ready_idle_manager_receives_the_signal_without_a_hold` — an occupant already at the
   ready-idle boundary is admissible for the initial post, with no hold.
6. `test_failed_submission_keeps_the_same_row_pending_until_the_next_boundary` — a rejected
   submission leaves one pending row with its backoff intact and later lands that same row.

The case-2 guarantee is the reason the production predicate exists: a rebound state-signal row has
no ordinary redelivery path, so boundary-drain eligibility for a pending row with no attempt clock
is state-signal-scoped (`state_signals._boundary_follows_last_attempt`).

The module drives real stores, a real inbox log, and the production sweep/action entry points. The
`_World.restarted` helper rebuilds the store objects over the same durable files instead of
reusing in-memory state, and `StateSignalBoundaryDeliveryTests._submit_patch` patches
`inbox_delivery.submit_control_prompt` with an accepted receipt so no live adapter is needed.

### Conventions

The tests use the repository interpreter with `-n 0 -m ''` (both unit and integration markers
selected). The table lists retained test definitions, not collected parametrized or subtest counts.
No dashboard, HTTP, or acknowledgement path is read or required by any case.

### Invariants And Boundaries

- The durable inbox row is the delivery authority and the wake intent; the source marker never
  substitutes for it.
- A `working` target is never injected into: the held row stays `queued` with zero submissions.
- Row identity is preserved across hold, replacement, restart, and retry (`len(rows) == 1`).
- Coverage limit recorded from source: `evaluate_boundary_drain_findings` requires a non-null
  `turn_state_changed_at`, so a held row addressed to a never-classified ready-idle occupant waits
  for that occupant's first *classified* boundary. That is a delay, not row loss — the row stays
  pending and is re-evaluated every sweep — and it is not reachable for a manager already observed
  `working`. No case here claims drain at an unclassified boundary.
- This card records source inspection. It does not claim acceptance, certification, or an
  independent review result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file.

| Finding | Anchor | Source |
| --- | --- | --- |
| Persist-before-marker ordering, one row on retry, no submission while the append fails | `test_persist_failure_keeps_marker_unset_and_retry_publishes_one_row` | mcp/tests/test_state_signal_boundary_delivery.py:299-360 |
| A held row re-addressed to the replacement occupant lands once on the same row id | `test_held_signal_follows_replacement_manager_on_the_same_row` | mcp/tests/test_state_signal_boundary_delivery.py:362-401 |
| A row persisted by one notifier context is delivered by a later fresh context | `test_held_signal_survives_a_fresh_notifier_context` | mcp/tests/test_state_signal_boundary_delivery.py:403-430 |
| Each classified boundary state drains the same held row through the protocol path | `test_held_signal_lands_at_each_classified_turn_boundary` | mcp/tests/test_state_signal_boundary_delivery.py:432-460 |
| An already ready-idle manager is admissible for the initial post without a hold | `test_ready_idle_manager_receives_the_signal_without_a_hold` | mcp/tests/test_state_signal_boundary_delivery.py:462-474 |
| A failed submission keeps one pending row with its backoff, later landed unchanged | `test_failed_submission_keeps_the_same_row_pending_until_the_next_boundary` | mcp/tests/test_state_signal_boundary_delivery.py:476-531 |
| Fresh store objects over the same durable files model a restarted notifier process | `_World` | mcp/tests/test_state_signal_boundary_delivery.py:202-237 |
| The accepted-receipt patch keeps the delivery assertion on the shared protocol seam | `_submit_patch` | mcp/tests/test_state_signal_boundary_delivery.py:291-297 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-10T11:42+02:00 — 260831-LOCR-L09 curator: created this sidecar for the six-case boundary-delivery forcing module (persist-before-marker, held-row replacement, fresh context, classified boundaries, ready-idle initial post, failed-submission retry) and recorded the state-signal-scoped no-attempt drain plus the unclassified-boundary delay limit. Source inspection only; verification metadata remains closeout-owned.
