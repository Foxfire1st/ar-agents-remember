# mcp/test_support/agents_remember_test_support/code_quality/retry_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/retry_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python quality verification overview](overview.md)

## Purpose

Owns Coverage.py artifact validation, conservative retained-context extraction, and explicit
retained/fresh delta composition for the dependency-aware Dagger retry route.

## Code Commentary

### Logic

`validate_context_proof` requires branch arcs and runtime contexts before reuse. A delta calls
`retain_unchanged_contexts`, which drops changed-test and unattributed collection contexts into a
dedicated retained database under one synthetic cached context. Pytest-cov writes a separate clean
active database. Only after pytest passes does `merge_delta_artifacts` read both, merge through
Coverage.py's public `CoverageData.update`, regenerate JSON from the merged database with the
repository configuration, and atomically publish the data/JSON pair.

When every prior context belongs to the affected population, `retain_unchanged_contexts` returns
`False` and leaves no database. The caller carries that explicit state into the merge as `None`, so
the delta database is authoritative without pretending an empty file exists. An expected retained
database that is actually missing still fails closed; absence is accepted only when extraction
proved there were zero retained arcs.

Any missing configuration, unreadable database, absent delta branch arcs, Coverage.py analysis
failure, or filesystem failure removes both public artifacts and raises a typed runtime failure.
Downstream CRAP/diff-coverage rails therefore cannot score a retained-only, delta-only, or stale
JSON result.

### Invariants And Boundaries

- Retained proof is never the live pytest-cov/xdist output database.
- A known-empty retained subset is distinct from a missing expected retained database.
- A delta JSON report is generated from the same merged database that becomes the public data file.
- Temporary artifacts are private sibling files and are cleaned on success or refusal.
- This is verification infrastructure; it creates no acceptance, lifecycle, or product authority.

### Todos

None.

## Docs References

No external domain contract is configured. The implementation uses Coverage.py's installed public
`CoverageData` and `Coverage` APIs.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Context proof requires branch arcs and pytest runtime contexts. | `validate_context_proof` | mcp/test_support/agents_remember_test_support/code_quality/retry_coverage.py:18-24 |
| Unchanged contexts are extracted to a separate retained database. | `retain_unchanged_contexts` | mcp/test_support/agents_remember_test_support/code_quality/retry_coverage.py:27-53 |
| Retained and fresh evidence are merged and atomically republished fail closed. | `merge_delta_artifacts` | mcp/test_support/agents_remember_test_support/code_quality/retry_coverage.py:56-99 |
| Focused forcing proves successful composition, a known-empty retained subset, and two-artifact cleanup on failure. | `test_retained_and_delta_contexts_merge_before_json_is_scored`; `test_empty_retained_subset_merges_only_fresh_delta_contexts`; `test_merge_failure_removes_both_public_artifacts` | mcp/tests/test_retry_coverage.py:11-140 |

## Cross-Repo References

None. Retry artifacts remain inside the Dagger-owned cache/report boundary.

## Update History

- 2026-08-27T19:13+02:00 — Distinguished a legitimately empty retained-context subset from a
  missing expected database after the real matrix exercised an all-contexts-affected delta.
- 2026-08-27T18:33+02:00 — Created after the real retry matrix exposed pytest-cov/xdist replacing
  an in-place retained database. Verification metadata remains empty until governed closeout.
