# mcp/tests/test_lifecycle_resume_invariant_owner_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_resume_invariant_owner_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces lifecycle resume invariant owner l2 behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_resume_preserves_approval_commits_worker_door_and_irreversible_boundary`, `test_resume_preserves_quality_and_integration_publication`, `test_resume_preserves_closeout_finalization_proof`, `test_resume_preserves_organizational_repair_and_cancellation_evidence`. The suite forces task-addressed legal controls, immutable same-generation retry/recovery, evidence-safe cancellation, write-ahead successor revision, door publication, concurrency, and executable refusal paths.

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
| The file defines `test_resume_preserves_approval_commits_worker_door_and_irreversible_boundary`, `test_resume_preserves_quality_and_integration_publication`, `test_resume_preserves_closeout_finalization_proof`, `test_resume_preserves_organizational_repair_and_cancellation_evidence` as its principal forcing seams. | L92-L126; L129-L164; L167-L191; L194-L276 | `mcp/tests/test_lifecycle_resume_invariant_owner_l2.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces the store choke point shared by ordinary update and crash-resume reconstruction.

### Current Invariants

- Resume preserves approval, door identity, commits, worker facts, certification, publication, cancellation, and repair evidence.
- Only narrowly authorized phase/status recovery differences are admitted.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
