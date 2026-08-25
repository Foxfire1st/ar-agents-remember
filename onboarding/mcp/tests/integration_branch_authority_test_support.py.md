# mcp/tests/integration_branch_authority_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/integration_branch_authority_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash | `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e` |
| lastVerifiedCommitDate | 2026-08-25T17:21:45+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Builds real repository, contract, task-topology, atomic blocker, closed-leaf, and exact-series preview fixtures reused by the split authority test suites.

## Code Commentary

Shared fixture construction uses production task documents, queue state, contracts, Git refs, and external-memory ledger commits so the main and edge suites do not counterfeit authority or depend on one another.

## Invariants And Boundaries

- The suite exercises production owners rather than copying their state-transition logic.
- Refusal cases assert no unauthorized Git, contract, queue, task, or memory mutation.
- Crash/retry cases retain exact durable identity and expected-old facts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared production-shaped helpers construct configured repository, closed leaf, atomic sprint, blocker, series, and exact-preview facts. | `_authority_fixture`, `_closed_leaf_worktree`, `_add_atomic_master_to_sprint`, `_assert_exact_series_preview` | mcp/tests/integration_branch_authority_test_support.py:115-267; mcp/tests/integration_branch_authority_test_support.py:49-67; mcp/tests/integration_branch_authority_test_support.py:280-307; mcp/tests/integration_branch_authority_test_support.py:527-581 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include the module forcing surface. The L2 additions force journal-owned claim transfer, exact protected-ref decisions, source-movement reconciliation, and organizational disposition/repair without queue-owned lifecycle evidence.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises the module forcing surface. | L1-L581 | `mcp/tests/integration_branch_authority_test_support.py` |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Provides shared exact-repository, protected-ref, organizational-completion, and atomic-series fixtures for the split integration authority suites.

### Current Invariants

- Fixtures bind current contract, task, door, journal, repository, and ref facts explicitly.
- No queue row or inferred path substitutes for protected-ref authority.


## PDLS Reconciliation

Shared integration-authority builders now expose the canonical current topology and bounded scenario overrides used by collision and publication forcing.

The test continues to exercise production-owned behavior. No diagnostic result is treated as
certifying evidence and no fallback or threshold exception was introduced.
## Update History

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T05:12+02:00 — L11 landed-wave refresh: the leaf-segment graph-model commit
  (f2e2f4b9) touched this source; card re-verified against the current file, verification stamp
  advanced to f2e2f4b9. Body unchanged — the documented contract still holds.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: extended the support surface for organizational-completion branch and recovery forcing. Verification remains closeout-owned.

- 2026-08-16T05:18+02:00 — Dagger fixture repair: code-only authority fixtures now model configured internal memory explicitly, keeping code-only integration behavior while satisfying exact runtime memory-mode authority.
- 2026-08-16T04:06+02:00 — 260815-DAG-L4 Dagger repair: shared closed-leaf helpers now materialize the exact contract-recorded code and external-memory worktrees, and the atomic-series helpers persist each child leaf's exact closeout, integration, queue-binding, and memory-ledger landing facts before series seal tests run.
- 2026-08-16T03:24+02:00 — 260815-DAG-L4: moved shared configured-repository and closed-leaf fixture builders out of the main authority test so both split suites stay independently importable and below the test-file size limit. Verification remains closeout-owned.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created integration-authority forcing support onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
