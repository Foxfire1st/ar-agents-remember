# mcp/tests/test_quality_retry_proof.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_retry_proof.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Forces exact quality-proof reuse and dependency-owned delta selection with temporary source, support, fixture and coverage artifacts. Exact identity can reuse a full proof; changed selection, source or global input forces the appropriate fresh population. Support and fixture changes select their declared consumers without adding unaffected tests. This is a proof-selection fixture, not a new live Dagger acceptance run.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Full proof becomes exact then test delta and source change invalidates | `test_full_proof_becomes_exact_then_test_delta_and_source_change_invalidates` | mcp/tests/test_quality_retry_proof.py:27-93 |
| Retry reruns declared support and fixture consumers but not unaffected tests | `test_retry_reruns_declared_support_and_fixture_consumers_but_not_unaffected_tests` | mcp/tests/test_quality_retry_proof.py:96-179 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): recorded the L19 selection-identity
  forcing — `selection_digest` threaded through inputs/plans, the
  `exact-selection-identity-changed` stale-identity cache-miss case, and the
  `selection-digest` manifest finding. Verification is pinned to the owning commit.

- 2026-08-28T11:32+02:00 — Added explicit missing-distribution forcing for retry tool-version
  identity.

- 2026-08-27T19:13+02:00 — Made nested cache ownership explicit, retained the inner wrapper
  transcript on assertion failure, and covered the all-contexts-affected delta state.
- 2026-08-27T18:33+02:00 — Replaced the stale in-place append claim with the isolated
  retained/fresh database and explicit post-pytest merge contract.
- 2026-08-27T17:19+02:00 — Updated command proof for the collection/execution split: canonical
  roots are collected while the retry plugin receives only the affected module path.
- 2026-08-27T15:11+02:00 — Added the regression boundary for Dagger's per-exec telemetry transport:
  explicitly named transport changes preserve retry identity, while unclassified environment
  changes still invalidate it.
- 2026-08-26T10:44:52+02:00 — Reconciled retry proof with canonical dependency-owned delta selection, declared fixture consumers, global-input invalidation, and removal of the private eligibility heuristic.

- 2026-08-24T21:23+02:00 — Applied the typed Dagger admission boundary to all retry-proof paths.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-10T12:20+02:00 — Added the real tracked-directory-symlink regression plus fail-closed
  inventory/artifact, cached-scope, and exact/delta fallback branch coverage after the first live
  closeout proofs.
- 2026-08-10T07:30+02:00 — Created with the content-addressed quality retry pipeline, including
  exact-proof stale-artifact refusal after a newly failing cheap rail. Verification
  metadata remains blank until closeout stamps the code commit.
