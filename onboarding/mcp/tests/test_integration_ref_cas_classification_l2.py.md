# mcp/tests/test_integration_ref_cas_classification_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_ref_cas_classification_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces integration ref cas classification l2 behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_compare_and_swap_failure_requires_same_generation_recovery`, `test_unchanged_cas_interruption_recovers_same_generation`, `test_partial_intended_cas_interruption_recovers_same_generation`, `test_full_intended_cas_interruption_recovers_same_generation`. The suite forces claim transfer, door authority, exact protected-ref classification, publication recovery, and same-generation reconciliation without moving lifecycle evidence into the queue.

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
| The file defines `test_compare_and_swap_failure_requires_same_generation_recovery`, `test_unchanged_cas_interruption_recovers_same_generation`, `test_partial_intended_cas_interruption_recovers_same_generation`, `test_full_intended_cas_interruption_recovers_same_generation` as its principal forcing seams. | L148-L206; L606-L608; L609-L611; L612-L614 | `mcp/tests/test_integration_ref_cas_classification_l2.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces one shared live-ref classifier for compare-and-swap loss across fresh integration and public recovery.

### Current Invariants

- CAS failure is classified from exact expected and observed refs.
- Recovery continues the same generation or returns a bounded decision; no caller-specific fallback is allowed.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-24T00:18+02:00 — No content impact: the architect applied the hook-requested formatter
  collapse to one legal-control list assertion. The current principal-seam name and shifted
  citations were reconciled; asserted behavior is unchanged.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
