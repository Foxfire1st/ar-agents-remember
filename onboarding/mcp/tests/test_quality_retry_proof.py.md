# mcp/tests/test_quality_retry_proof.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_retry_proof.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | db57101a9001ede8c681ff9de4eb0147d8b636bc |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Forcing suite for local quality-proof reuse. It proves that retry acceleration is a pipeline
contract with structural invalidation, not an agent assertion that old tests were probably fine.
L19 forces the immutable selection identity as part of that structural invalidation.

## Code Commentary

### Logic

The suite writes real Coverage.py databases with collection, changed-test, and unchanged-test
contexts and proves filtering retains only the unchanged runtime evidence. It rejects support
modules and deleted tests as delta inputs. A real temporary Git repository then proves the state
transition from fresh proof publication to exact reuse, changed-test delta, and source-change
invalidation. The wrapper-level case drives the actual command builder and cache controller: the
first passed pytest plus post-coverage failure publishes proof; the next test-only edit runs that
module through `--ar-retry-execute-path` while pytest still receives the canonical collection root,
with `--cov-context=test`. Retained prior coverage stays in a separate database; the fresh pytest
database is explicitly merged after the delta passes rather than relying on `--cov-append`, which
pytest-cov/xdist can overwrite. A deliberately inconclusive delta triggers a second, fresh full
pytest selection and reaches the final verdict. A separate exact-proof case forces Ruff to fail and
proves cached JSON is discarded, pytest stays skipped, and neither coverage-derived rail is called.
The wrapper test declares its own disposable retry-cache root because the production child-process
boundary intentionally strips the outer Dagger wrapper's cache owner; failures include the captured
inner wrapper transcript rather than discarding the causal retry state.

Retry delta ownership now comes from the same canonical dependency/evidence catalog as targeted
selection. A changed shared support module reruns its static import consumer, a changed catalogued
fixture reruns its declared consumer, and a changed production module reruns its import consumer
without rerunning unaffected tests. A global test input such as `conftest.py` invalidates reuse and
forces a fresh population. The suite uses synthetic catalogs through the public fixture helper and
no longer tests the removed private `_eligible_test_delta` heuristic. Mismatch/refusal output names
stable causal reasons such as `global-test-input`, `selected-population-changed`, and
`unusable-context-proof`.

L19 threads the `selection_digest` through every `RetryInputs`/`RetryPlan` fixture and adds
`stale_identity = retry_proof.prepare(replace(inputs, selection_digest="b"*64), ...)` to the
exact-proof lifecycle case, asserting a fresh run and the
`exact-selection-identity-changed` cache-miss reason; the manifest-miss case also asserts the
`selection-digest` finding.

The production-shaped cases additionally prove tracked directory symlinks are hashed by link
identity without traversing their targets, malformed inventories and proof artifacts fail closed,
newly selected test modules qualify only through the explicit delta rule, and the wrapper's
no-coverage fallback, artifact-preparation refusal, cached-result scope error, and exact
cached-pytest branches report their own verdicts.

`test_retry_environment_identity_ignores_only_explicit_runtime_transport` reproduces the changing
Dagger OpenTelemetry ports, trace parent, and baggage seen across fresh containers. It proves those
named transport values do not perturb the environment digest while a separate unclassified
quality-context value still does.
Tool-version identity also distinguishes an unavailable distribution with the explicit `absent`
value, so package removal invalidates proof deterministically.

### Invariants And Boundaries

- Coverage context tests use Coverage.py's public `CoverageData` interface.
- Wrapper proof tests use real Git state and the real snapshot/cache controller.
- Nested wrapper proofs own an explicit disposable cache and never borrow the outer Dagger cache.
- Only external subprocess execution and post-coverage arithmetic are doubled; command selection,
  manifest publication, filtering, invalidation, and fallback orchestration are real.
- Cached coverage cannot survive a newly failing cheap rail, even on an exact-tree retry.
- A changed immutable selection digest can never reuse the previous proof (L19).
- A local dependency install behind a tracked symlink cannot disable content-addressed reuse or
  make external dependency bytes part of the repository snapshot.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this test contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured for this suite. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Retry proof owns manifest compatibility, retained-context preparation, and publication lifecycle; the selection digest is part of the identity. | `RetryPlan`; `prepare` | mcp/test_support/agents_remember_test_support/code_quality/retry_proof.py:117-203; mcp/test_support/agents_remember_test_support/code_quality/retry_proof.py:205-248 |
| Coverage composition owns filtering, explicit retained/fresh merge, JSON regeneration, and fail-closed publication. | `retain_unchanged_contexts`; `merge_delta_artifacts` | mcp/test_support/agents_remember_test_support/code_quality/retry_coverage.py:27-99 |
| The wrapper owns canonical delta collection, exact affected execution paths, explicit merge completion, automatic full rerun, and stale-artifact deletion when a cheap rail prevents pytest. | `execute_quality_rails`; `complete_coverage_rails`; `_pytest_result_failures`; `_merge_retry_coverage` | mcp/test_support/agents_remember_test_support/code_quality/check.py:201-295; mcp/test_support/agents_remember_test_support/code_quality/check.py:526-565 |
| A changed selection identity invalidates an otherwise exact proof. | `test_full_proof_becomes_exact_then_test_delta_and_source_change_invalidates` | mcp/tests/test_quality_retry_proof.py:58-125 |

## Cross-Repo References

No meaningful cross-repository boundary is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| Temporary repositories and cache directories are isolated inside each test. | — | — |

## 260824-PDLS Admission Boundary

Every retry-proof preparation now requires `QUALITY_TEST_ADMISSION`. The suite proves exact reuse,
delta reuse, disablement, and fail-closed invalidation only inside the certifying route; direct
diagnostic results cannot seed or consume retry proof.

## Update History

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
