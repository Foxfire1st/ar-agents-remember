# {S}mcp/tests/test_lifecycle_status_wait_store.py{S}

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | {S}mcp/tests/test_lifecycle_status_wait_store.py{S} |
| doc_type | {S}file-level-onboarding{S} |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | {S}e375f2ebdc87f6843bc76168b646d606fa79caec{S} |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview | {S}overview.md{S} |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Store-and-observer forcing for the CCR-R15 wait cursor: heartbeat writes advance `recordRevision` but never `meaningfulRevision`; meaningful, terminal, and cancellation transitions advance the cursor exactly once; restart reconstruction keeps the cursor; the wait wakes on meaningful change but not heartbeats; multiple waiters never block writers; client cancellation never mutates lifecycle state; transforms cannot assign the meaningful revision; the transition validator refuses a cursor mismatch; observed projection returns None without a record; and the status-wait application payload carries no private operation identity.

## Code Commentary

### Logic

The module exercises `LifecycleOperationStore` transitions and the `wait_for_lifecycle_change` observer (including threaded multi-waiter runs) through fixture contracts, asserting the store's exactly-once cursor rules and the read-only wait behavior.

### Invariants And Boundaries

- Standalone per the evidence-lifecycle isolation rule; imports no pre-existing mcp/tests support
  module.
- Asserts public behavior through the typed outcome vocabulary and the store's dual-revision
  contract, never through private operation identity.

## Docs References

No configured external Domain Documentation source governs this test module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs these tests. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Heartbeats never advance the wait cursor. | `test_heartbeat_advances_record_revision_but_never_meaningful_revision` | mcp/tests/test_lifecycle_status_wait_store.py:635-652 |
| Meaningful transitions advance exactly once. | `test_meaningful_transitions_advance_the_wait_revision_exactly_once` | mcp/tests/test_lifecycle_status_wait_store.py:653-671 |
| Waiters never block writers. | `test_multiple_waiters_never_block_writers` | mcp/tests/test_lifecycle_status_wait_store.py:746-798 |
| Transform cannot assign the cursor. | `test_store_transform_cannot_assign_meaningful_revision` | mcp/tests/test_lifecycle_status_wait_store.py:838-852 |

## 260831-CCR-L15 Status-Wait Test Module

Created with the lifecycle status-change waiting tool (CCR-R15).

## Update History

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): created
  this card for the new status-wait test module.
