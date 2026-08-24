# mcp/tests/test_direct_landing_operation_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_direct_landing_operation_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:19+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces direct landing operation recovery behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_public_preoutput_recover_and_cancel_controls_execute`, `test_direct_retry_reset_preserves_memory_and_ledger_admission_identity`, `test_direct_resume_cannot_clear_published_ledger_intent`, `test_post_admission_unreadable_ledger_persists_and_recovers_publicly`. The suite forces direct landing through journal creation, memory and ledger intent/commit crash cuts, conflicts, replay, and same-generation recovery; a transient lock or raw-Git retry is never treated as durable authority.

### Conventions

Tests address operations by task/contract plus kind and generation, assert durable evidence and public legal controls, and compare state across failure cuts. Helpers remain test-only and invoke the same public/domain seams as production.

### Invariants And Boundaries

- A passing assertion must prove the advertised action executes or terminates safely; payload shape alone is insufficient.
- Queue projection is never accepted as lifecycle evidence, and private operation identifiers do not cross the public test boundary.
- Failure-path assertions check non-mutation or exact same-generation recovery, not merely an exception string.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to these repository-internal forcing tests.

## Repo-Internal References

The test source is the direct evidence for the regression contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The file defines `test_public_preoutput_recover_and_cancel_controls_execute`, `test_direct_retry_reset_preserves_memory_and_ledger_admission_identity`, `test_direct_resume_cannot_clear_published_ledger_intent`, `test_post_admission_unreadable_ledger_persists_and_recovers_publicly` as its principal forcing seams. | L148-L177; L179-L255; L257-L285; L287-L326 | `mcp/tests/test_direct_landing_operation_recovery.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## 260821-DAGQC-L2 Action-Required Public Refusal

The operation-recovery cases prove that an existing action-required generation is retained for
same-generation recovery but projected publicly as `ok: false` and `state: refused`, with door and
journal lifecycle facts nested rather than promoted to the outcome plane.

## Update History

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: forced action-required recovery to retain nested journal evidence under the closed refused outcome. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
