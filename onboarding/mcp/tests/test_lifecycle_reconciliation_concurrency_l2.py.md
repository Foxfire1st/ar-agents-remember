# mcp/tests/test_lifecycle_reconciliation_concurrency_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_reconciliation_concurrency_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T14:18+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces lifecycle reconciliation concurrency l2 behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are
`test_public_control_reconciliation_cannot_overwrite_concurrent_worker_progress`,
`test_stale_cancel_at_commit_boundary_returns_and_executes_exact_recovery`, and the three
`test_direct_recovery_*` cases. The suite forces task-addressed legal controls, immutable
same-generation retry/recovery, evidence-safe cancellation, write-ahead successor revision, door
publication, concurrency, executable refusal paths, and total translation of direct-landing
recovery outcomes.

### Conventions

Tests address operations by task/contract plus kind and generation, assert durable evidence and public legal controls, and compare state across failure cuts. Helpers remain test-only and invoke the same public/domain seams as production.

### Invariants And Boundaries

- A passing assertion must prove the advertised action executes or terminates safely; payload shape alone is insufficient.
- Queue projection is never accepted as lifecycle evidence, and private operation identifiers do not cross the public test boundary.
- Failure-path assertions check non-mutation or exact same-generation recovery, not merely an exception string.
- Only a classified developer-decision state refuses typed recovery. Recoverable typed
  direct-landing failures retain status, expected/observed facts, and the current durable record;
  an untyped runtime invariant failure propagates and is never converted into operation state.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to these repository-internal forcing tests.

## Repo-Internal References

The test source is the direct evidence for the regression contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The file defines concurrency, same-generation recovery, developer-decision refusal, typed failure preservation, and loud invariant propagation as its principal forcing seams. | `test_public_control_reconciliation_cannot_overwrite_concurrent_worker_progress`; `test_stale_cancel_at_commit_boundary_returns_and_executes_exact_recovery`; `test_direct_recovery_state_refuses_only_developer_decisions`; `test_direct_recovery_failure_preserves_typed_error_and_current_record`; `test_direct_recovery_does_not_translate_invariant_runtime_errors` | mcp/tests/test_lifecycle_reconciliation_concurrency_l2.py:40-247 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Update History

- 2026-08-28T14:18+02:00 — Reconciled the concurrency-test citation with its final symbol name;
  the proof still requires invariant runtime errors to remain visible.

- 2026-08-28T11:32+02:00 — Replaced runtime-interruption recovery forcing with the invariant that
  untyped runtime defects propagate; typed direct failures remain the sole translated family.

- 2026-08-27T19:47+02:00 — PDLS exact-candidate retry forcing exposed uncovered branches in the
  lifecycle recovery CRAP repair. Added focused developer-decision, typed-error, durable-record,
  and interruption forcing; the paired pure and Dagger delta tests pass. The verification hash is
  the immutable non-landed PDLS evidence candidate, not a moved real branch.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
