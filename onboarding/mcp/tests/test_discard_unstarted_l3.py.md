# mcp/tests/test_discard_unstarted_l3.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_discard_unstarted_l3.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Force the complete discard-unstarted task-plane contract.

## Code Commentary

### Logic

The suite exercises preview/apply parity, nonblank reason validation, exact unstarted evidence, parent audit plus child removal, lost-response replay, started and unreadable refusal routes, registration-before-reclamation, and start-versus-discard serialization.

### Invariants And Boundaries

- Only provably unstarted leaves may be discarded.
- Discard never fabricates completion.
- Changed bytes, ambiguous evidence, or a winning start preserve the task and return exact routing.
- Successful discard produces ordinary projection invalidation/rebuild effects.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Source Range | Source Path |
| --- | --- | --- |
| The suite binds public task-doc, evidence, registration, and lifecycle seams. | L1-L89 | [source](mcp/tests/test_discard_unstarted_l3.py) |
| The test class forces success, refusal, crash replay, and concurrency cases. | L90-L706 | [source](mcp/tests/test_discard_unstarted_l3.py) |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
