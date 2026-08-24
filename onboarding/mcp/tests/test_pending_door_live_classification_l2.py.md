# mcp/tests/test_pending_door_live_classification_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pending_door_live_classification_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces pending door live classification l2 behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_initial_pending_door_third_contract_is_total_across_public_surfaces`, `test_unreadable_pending_door_status_and_stale_handler_share_exact_decision`, `test_unreadable_initial_door_git_evidence_is_bounded_and_non_mutating`, `test_all_pending_door_dispositions_refuse_live_third_state_without_mutation`. The suite forces task-addressed legal controls, immutable same-generation retry/recovery, evidence-safe cancellation, write-ahead successor revision, door publication, concurrency, and executable refusal paths.

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
| The file defines `test_initial_pending_door_third_contract_is_total_across_public_surfaces`, `test_unreadable_pending_door_status_and_stale_handler_share_exact_decision`, `test_unreadable_initial_door_git_evidence_is_bounded_and_non_mutating`, `test_all_pending_door_dispositions_refuse_live_third_state_without_mutation` as its principal forcing seams. | L123-L164; L167-L192; L195-L259; L263-L348 | `mcp/tests/test_pending_door_live_classification_l2.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces exact public classification when a journaled closeout-door publication is pending, unreadable, or observes third-state bytes.

### Current Invariants

- Status and stale handlers return the same bounded decision semantics.
- No disposition mutates through ambiguous door evidence or treats it as absent.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
