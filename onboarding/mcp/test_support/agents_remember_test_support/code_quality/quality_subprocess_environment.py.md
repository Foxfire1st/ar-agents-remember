# mcp/test_support/agents_remember_test_support/code_quality/quality_subprocess_environment.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/quality_subprocess_environment.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python quality verification overview](overview.md)

## Purpose

Owns the environment boundary between one admitted quality-wrapper invocation and the candidate
tests/rails it launches, including checkout-local import-root construction.

## Code Commentary

### Logic

`child_environment` removes a closed set of outer-wrapper execution controls: retry disable/cache,
retry forcing identities, and the progress-report path. Candidate tests still inherit semantic
facts such as CI invocation, Dagger admission attestation, attempt nonce, memory cap, and ordinary
process environment. `build` then prepends source import roots and selects the active Coverage.py
database for the child rail.

`source_import_roots` resolves file and directory coverage targets to stable package parents while
deduplicating order. It was extracted from the oversized wrapper so environment construction has
one owner and nested wrapper tests cannot mutate the outer run's evidence locations.

### Invariants And Boundaries

- Only the five named outer-invocation controls are stripped; there is no prefix or unknown-value
  fallback.
- Admission, invocation, nonce, and memory-limit semantics survive into candidate tests.
- The outer retry cache and progress path cannot be overwritten by a nested quality-wrapper test.
- The module builds subprocess inputs only; it does not execute or admit a rail.

### Todos

None.

## Docs References

No external domain documentation governs this repository-owned process boundary.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The closed outer-only set and child filtering are explicit. | `OUTER_INVOCATION_ONLY`; `child_environment` | mcp/test_support/agents_remember_test_support/code_quality/quality_subprocess_environment.py:9-25 |
| Child construction preserves semantics while setting checkout import roots and coverage output. | `build` | mcp/test_support/agents_remember_test_support/code_quality/quality_subprocess_environment.py:28-44 |
| Import roots are derived from product file/directory targets once. | `source_import_roots` | mcp/test_support/agents_remember_test_support/code_quality/quality_subprocess_environment.py:47-65 |
| Focused forcing proves only outer controls disappear. | `test_outer_retry_controls_do_not_leak_into_candidate_tests` | mcp/tests/test_quality_subprocess_environment.py:6-29 |

## Cross-Repo References

None.

## Update History

- 2026-08-27T18:33+02:00 — Created after the Dagger retry matrix exposed nested quality tests
  overwriting outer cache/progress evidence. Verification metadata remains empty until closeout.
