# mcp/tests/test_quality_retry_proof.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_retry_proof.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-10T07:30+02:00 |
| lastVerifiedCommitHash |  `b537abe20cf2498ef38e86e29ca586b5eec38466`|
| lastVerifiedCommitDate |  2026-08-10T08:37:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Forcing suite for local quality-proof reuse. It proves that retry acceleration is a pipeline
contract with structural invalidation, not an agent assertion that old tests were probably fine.

## Code Commentary

### Logic

The suite writes real Coverage.py databases with collection, changed-test, and unchanged-test
contexts and proves filtering retains only the unchanged runtime evidence. It rejects support
modules and deleted tests as delta inputs. A real temporary Git repository then proves the state
transition from fresh proof publication to exact reuse, changed-test delta, and source-change
invalidation. The wrapper-level case drives the actual command builder and cache controller: the
first passed pytest plus post-coverage failure publishes proof; the next test-only edit runs that
one module with `--cov-append --cov-context=test`; a deliberately inconclusive delta triggers a
second, fresh full pytest selection and reaches the final verdict. A separate exact-proof case
forces Ruff to fail and proves cached JSON is discarded, pytest stays skipped, and neither
coverage-derived rail is called.

The production-shaped cases additionally prove tracked directory symlinks are hashed by link
identity without traversing their targets, malformed inventories and proof artifacts fail closed,
newly selected test modules qualify only through the explicit delta rule, and the wrapper's
no-coverage fallback, artifact-preparation refusal, cached-result scope error, and exact
cached-pytest branches report their own verdicts.

### Invariants And Boundaries

- Coverage context tests use Coverage.py's public `CoverageData` interface.
- Wrapper proof tests use real Git state and the real snapshot/cache controller.
- Only external subprocess execution and post-coverage arithmetic are doubled; command selection,
  manifest publication, filtering, invalidation, and fallback orchestration are real.
- Cached coverage cannot survive a newly failing cheap rail, even on an exact-tree retry.
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
| Retry proof owns manifest compatibility, context filtering, and publication. | `RetryPlan`; `prepare`; `_filtered_coverage_data` | mcp/src/agents_remember/code_quality/retry_proof.py:63-134; mcp/src/agents_remember/code_quality/retry_proof.py:136-206; mcp/src/agents_remember/code_quality/retry_proof.py:393-444 |
| The wrapper owns delta command selection, automatic full fallback, and stale-artifact deletion when a cheap rail prevents pytest. | `_pytest_step`; `complete_coverage_rails`; `run_fixed_checks` | mcp/src/agents_remember/code_quality/check.py:205-224; mcp/src/agents_remember/code_quality/check.py:431-473; mcp/src/agents_remember/code_quality/check.py:563-608 |

## Cross-Repo References

No meaningful cross-repository boundary is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| Temporary repositories and cache directories are isolated inside each test. | — | — |

## Update History

- 2026-08-10T12:20+02:00 — Added the real tracked-directory-symlink regression plus fail-closed
  inventory/artifact, cached-scope, and exact/delta fallback branch coverage after the first live
  closeout proofs.
- 2026-08-10T07:30+02:00 — Created with the content-addressed quality retry pipeline, including
  exact-proof stale-artifact refusal after a newly failing cheap rail. Verification
  metadata remains blank until closeout stamps the code commit.
