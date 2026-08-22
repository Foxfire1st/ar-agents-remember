# mcp/tests/test_lifecycle_worker_release_guards.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_worker_release_guards.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash |  `eb7ea60ab9919f009fef58f81afe5861aa1709da`|
| lastVerifiedCommitDate |  2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces the current worker release guard to preserve candidate ownership after a failed operation has crossed an irreversible evidence boundary.

## Code Commentary

### Logic

One case fails closeout after exact commit proof; the other fails integration after its irreversible boundary. Both assert that the worker does not run the reversible-release path and that current queue ownership remains visible. This is a safety test for the current scheduling adapter, not an assertion that queue state is authoritative lifecycle evidence.

### Invariants And Boundaries

- Reversible failure may release; proven Git mutation or irreversible integration may not.
- Worker cleanup cannot make consumed authority appear reusable.
- The journal/proof decides retention; queue ownership mirrors the current scheduling consequence.
- L3 owns the future disposable projection/invalidation lifecycle.

## Docs References

See task `260821-CLIVE-L1` L1-R4 through L1-R6 and the deferred queue redesign in L3.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Failed closeout with commit proof retains current ownership. | `test_failed_closeout_with_commit_proof_keeps_queue_ownership` | `mcp/tests/test_lifecycle_worker_release_guards.py:27-52` |
| Failed irreversible integration retains current ownership. | `test_failed_irreversible_integration_keeps_queue_ownership` | `mcp/tests/test_lifecycle_worker_release_guards.py:55-84` |

## Cross-Repo References

No cross-repository authority applies.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first verification stamp remains governed-closeout-owned.
