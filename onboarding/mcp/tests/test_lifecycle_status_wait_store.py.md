# mcp/tests/test_lifecycle_status_wait_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_status_wait_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Verifies the journal store's separate ordinary and meaningful revision counters and the non-mutating concurrency behavior of lifecycle status waits.

## Code Commentary

### Logic

Fixtures start one claimed generation without a detached worker and drive phase, approval, failure, completion and cancellation transitions. Heartbeats advance the ordinary record revision without advancing the meaningful wait cursor. Relevant transitions advance the meaningful revision exactly once, and restart reconstruction retains the cursor and terminal state.

Threaded waiter cases require meaningful changes to wake readers while heartbeat-only changes do not. Multiple waiters must not block writers; client cancellation must not mutate lifecycle state. Tampering with meaningfulRevision in a transform or violating transition monotonicity is rejected. The application result omits private operation identity.

### Conventions

Fixture doors and worker identities are synthetic, confined to the test's coordination tree. Concurrency tests assert bounded store behavior rather than an external harness session.

### Invariants And Boundaries

- Waiters do not hold write locks while sleeping.
- Client-side cancellation is not operation cancellation.
- Only the store transition authority assigns meaningfulRevision.
- Restarted readers recover the durable cursor without fabricating progress.

### Todos

No source behavior changed in this documentation repair.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Dual revision rules and restart reconstruction | `test_heartbeat_advances_record_revision_but_never_meaningful_revision`; `test_meaningful_transitions_advance_the_wait_revision_exactly_once`; `test_terminal_and_cancellation_transitions_advance_exactly_once`; `test_restart_reconstruction_keeps_cursor_and_terminal_transition` | mcp/tests/test_lifecycle_status_wait_store.py:635-712 |
| Wake conditions, multiple waiters and cancellation isolation | `test_wait_wakes_on_meaningful_change_but_not_heartbeats`; `test_multiple_waiters_never_block_writers`; `test_client_cancellation_never_mutates_lifecycle_state` | mcp/tests/test_lifecycle_status_wait_store.py:715-835 |
| Cursor tamper refusal and bounded public response | `test_store_transform_cannot_assign_meaningful_revision`; `test_transition_validator_refuses_a_meaningful_revision_mismatch`; `test_status_wait_application_payload_has_no_private_operation_identity` | mcp/tests/test_lifecycle_status_wait_store.py:838-916 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Repaired template markers and retained the distinction between record revisions, meaningful progress and non-mutating wait cancellation. Historical leaf-pass wording below is retained as history; this refresh establishes documentation currentness only.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): created
  this card for the new status-wait test module.
