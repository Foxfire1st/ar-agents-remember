# mcp/tests/integration_branch_authority_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/integration_branch_authority_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-16T04:06+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Builds real repository, contract, task-topology, atomic barrier, closed-leaf, and exact-series preview fixtures reused by the split authority test suites.

## Code Commentary

Shared fixture construction uses production task documents, queue state, contracts, Git refs, and external-memory ledger commits so the main and edge suites do not counterfeit authority or depend on one another.

## Invariants And Boundaries

- The suite exercises production owners rather than copying their state-transition logic.
- Refusal cases assert no unauthorized Git, contract, queue, task, or memory mutation.
- Crash/retry cases retain exact durable identity and expected-old facts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared production-shaped helpers construct configured repository, closed leaf, atomic sprint, barrier, series, and exact-preview facts. | `_authority_fixture`, `_closed_leaf_worktree`, `_add_atomic_master_to_sprint`, `_assert_exact_series_preview` | mcp/tests/integration_branch_authority_test_support.py:36-53; mcp/tests/integration_branch_authority_test_support.py:94-196; mcp/tests/integration_branch_authority_test_support.py:209-234; mcp/tests/integration_branch_authority_test_support.py:284-338 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-16T05:18+02:00 — Dagger fixture repair: code-only authority fixtures now model configured internal memory explicitly, keeping code-only integration behavior while satisfying exact runtime memory-mode authority.
- 2026-08-16T04:06+02:00 — 260815-DAG-L4 Dagger repair: shared closed-leaf helpers now materialize the exact contract-recorded code and external-memory worktrees, and the atomic-series helpers persist each child leaf's exact closeout, integration, queue-binding, and memory-ledger landing facts before series seal tests run.
- 2026-08-16T03:24+02:00 — 260815-DAG-L4: moved shared configured-repository and closed-leaf fixture builders out of the main authority test so both split suites stay independently importable and below the test-file size limit. Verification remains closeout-owned.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created integration-authority forcing support onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
