# mcp/tests/test_lifecycle_worker_release_guards.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_worker_release_guards.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces failed workers to preserve the journal generation after truthful irreversible evidence. The
historical test names retain “queue ownership”, but the assertions now specifically prove that the
worker does not publish a `queueReleaseFailure` lifecycle result.

## Code Commentary

### Logic

One case fails closeout after exact commit proof; the other fails integration after its
irreversible boundary. Both assert `input-required` on the same durable operation and absence of a
worker-authored `queueReleaseFailure`. Scheduling projection may mirror the consequence, but the
journal/proof owns retention.

### Invariants And Boundaries

- Reversible failure may release; proven Git mutation or irreversible integration may not.
- Worker cleanup cannot make consumed authority appear reusable.
- The journal/proof decides retention; queue projection is not recovery evidence.
- Worker execution never repairs, requeues, or releases the scheduling projection directly.

## Docs References

See task `260821-CLIVE-L1` L1-R4 through L1-R6 and the deferred queue redesign in L3.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Failed closeout with commit proof retains the same journal generation. | `test_failed_closeout_with_commit_proof_keeps_queue_ownership` | mcp/tests/test_lifecycle_worker_release_guards.py:27-47 |
| Failed irreversible integration retains the same journal generation. | `test_failed_irreversible_integration_keeps_queue_ownership` | mcp/tests/test_lifecycle_worker_release_guards.py:50-74 |

## Cross-Repo References

No cross-repository authority applies.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_failed_closeout_with_commit_proof_keeps_queue_ownership`, `test_failed_irreversible_integration_keeps_queue_ownership`. The L2 additions force locator-rooted journal access, legal task-addressed controls, write-ahead successors, exact worker termination, total expected-failure projection, and same-generation convergence.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_failed_closeout_with_commit_proof_keeps_queue_ownership`, `test_failed_irreversible_integration_keeps_queue_ownership`. | L27-L47; L50-L74 | `mcp/tests/test_lifecycle_worker_release_guards.py` |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces journal retention after a worker reports failure beyond mutation intent, commit proof, or the integration irreversible boundary.

### Current Invariants

- The operation remains input-required with its irreversible evidence intact.
- The source intentionally asserts that no queue-release side channel is recorded; lifecycle authority is journal-owned despite legacy test names.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first verification stamp remains governed-closeout-owned.
