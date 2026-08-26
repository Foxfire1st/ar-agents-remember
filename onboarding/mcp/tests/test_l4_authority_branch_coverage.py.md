# mcp/tests/test_l4_authority_branch_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l4_authority_branch_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces fail-closed Git branch/default facts, exact lifecycle-operation and configured-contract
authority, integration recovery, topology publication, source lineage, and atomic-series edges.

## Code Commentary

Repository tests cover blank, cyclic, malformed, missing, detached, and Git-error branch facts.
Operation tests cover absent/wrong journal identity, source/candidate drift, code and memory repository
identity changes, and internal/external memory authority-shape mismatches.
The public integration preparation case advances the protected source inside queue/repository
publication and proves the structured source-moved refusal wins before irreversible progress.
Focused additions cover task-path/worktree ownership, stale worker recovery, queue binding identity,
candidate validation, torn ref recovery, unavailable organizational lineage, and incomplete atomic
leaf sets through the production helpers that own those checks.

## Invariants And Boundaries

- Negative cases reach the production authority owner, not duplicated test logic.
- A refusal occurs before protected-ref mutation.
- Code and external-memory identities remain exact and independently proven.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite owns focused negative forcing for repository and journal authority. | `IntegrationBranchRepositoryCoverageTests`; `IntegrationOperationAuthorityCoverageTests` | mcp/tests/test_l4_authority_branch_coverage.py:65-199; mcp/tests/test_l4_authority_branch_coverage.py:202-603 |
| Configured topology, integration validation/recovery, lineage, and series completeness are forced at their production owners. | `IntegrationBranchAuthorityCoverageTests`; `IntegrationValidationCoverageTests`; `LineageAndSeriesCoverageTests` | mcp/tests/test_l4_authority_branch_coverage.py:606-751; mcp/tests/test_l4_authority_branch_coverage.py:754-909; mcp/tests/test_l4_authority_branch_coverage.py:912-1042 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L1 Admission Migration

The closeout fixture now supplies the accepted normalized plan required by L1 while retaining the suite's branch-authority coverage. The redundant wrong-runtime-input authority case moved to the focused closeout model/admission matrix, so this suite remains about protected integration branches rather than duplicating input ownership. No queue ownership or compatibility fallback is introduced.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_canonical_local_branch_refuses_every_invalid_alias_shape`, `test_default_branch_authority_refuses_missing_and_malformed_facts`, `test_memory_default_branch_refuses_invalid_local_authority`, `test_branch_owner_enumeration_refuses_git_failure_and_skips_detached_rows`. The L2 additions force journal-owned claim transfer, exact protected-ref decisions, source-movement reconciliation, and organizational disposition/repair without queue-owned lifecycle evidence.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current test source exercises `test_canonical_local_branch_refuses_every_invalid_alias_shape`, `test_default_branch_authority_refuses_missing_and_malformed_facts`, `test_memory_default_branch_refuses_invalid_local_authority`, `test_branch_owner_enumeration_refuses_git_failure_and_skips_detached_rows`. | `test_canonical_local_branch_refuses_every_invalid_alias_shape`; `test_default_branch_authority_refuses_missing_and_malformed_facts`; `test_memory_default_branch_refuses_invalid_local_authority`; `test_branch_owner_enumeration_refuses_git_failure_and_skips_detached_rows` | mcp/tests/test_l4_authority_branch_coverage.py:69-101; mcp/tests/test_l4_authority_branch_coverage.py:103-139; mcp/tests/test_l4_authority_branch_coverage.py:141-177; mcp/tests/test_l4_authority_branch_coverage.py:179-202 |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Covers negative repository, operation, protected-ref, validation, lineage, and atomic-series authority branches.

### Current Invariants

- Every expected authority failure returns bounded evidence instead of leaking lower-layer exceptions.
- Tests preserve the separation between operation journal, contract, and protected-ref owners.


## PDLS Reconciliation

Focused authority branch forcing now covers the decomposed collision, override, and path-confinement helpers rather than one oversized implementation.

The test continues to exercise production-owned behavior. No diagnostic result is treated as
certifying evidence and no fallback or threshold exception was introduced.
## Update History

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 threaded the effective-nature argument into an internal surface-authority call; documented authority behavior is unchanged. Verification remains closeout-owned.

- 2026-08-17T13:20+02:00 — No content impact: L5 repair: re-pointed stale mock targets and return tuples to match the L5 integration API (publish_queue_candidate_integration_result_under_authority, branch_commit, 4-tuple _prepare_integration_commits, durable-removal-intent idempotency). The documented test intent and coverage surface are unchanged.

- 2026-08-16T09:55+02:00 — Added a real exact-series positive case to the atomic surface probe, proving canonical task-tree resolution rather than only false cases.
- 2026-08-16T09:45+02:00 — Added production-owner coverage for configured contract identity, lifecycle recovery, task publication, integration candidate/ref recovery, organizational lineage, and atomic-series completeness after the targeted Dagger diff-coverage report.
- 2026-08-16T08:12+02:00 — Created focused L4 negative-branch forcing during targeted Dagger coverage repair.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.


## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
