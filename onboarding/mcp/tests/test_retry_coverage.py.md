# mcp/tests/test_retry_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_retry_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pure forcing proof for explicit retained/fresh Coverage.py composition in a dependency-aware retry.

## Code Commentary

### Logic

The success case writes distinct real Coverage.py databases with complementary branch arcs and
contexts, merges them through the production owner, then reads both the public database and
generated JSON to prove neither half or stale JSON won publication. The refusal case supplies a
missing retained database and proves the merge removes both public outputs rather than leaving
partial evidence for later rails.

The all-contexts-affected case proves extraction reports a known-empty retained subset without
creating a placeholder database, then merges and publishes only the fresh delta contexts. This is
separate from the missing-file refusal: an explicitly expected retained path must still exist.

### Invariants And Boundaries

- Tests use Coverage.py public APIs and real filesystem artifacts.
- Success proves merged branch/context content, not merely a zero return code.
- Known-empty retained state is accepted only when extraction reports it explicitly.
- Failure proves both scored artifacts disappear.
- This pure unit-regression proof does not grant Dagger admission or acceptance authority.

### Todos

None.

## Docs References

No external domain documentation is configured for this repository-owned forcing proof.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Complementary retained and delta arcs become one scored database/JSON pair. | `test_retained_and_delta_contexts_merge_before_json_is_scored` | mcp/tests/test_retry_coverage.py:11-65 |
| An all-contexts-affected delta publishes fresh contexts without inventing retained data. | `test_empty_retained_subset_merges_only_fresh_delta_contexts` | mcp/tests/test_retry_coverage.py:68-113 |
| A merge refusal removes both public artifacts. | `test_merge_failure_removes_both_public_artifacts` | mcp/tests/test_retry_coverage.py:116-140 |
| The production merge owner performs fail-closed publication. | `merge_delta_artifacts` | mcp/test_support/agents_remember_test_support/code_quality/retry_coverage.py:56-99 |

## Cross-Repo References

None.

## Update History

- 2026-08-27T20:16+02:00 — Corrected the onboarding projection after moving the formatter
  regression to the dependency-neutral helper-invariant suite; this file remains coverage-only.
- 2026-08-27T19:13+02:00 — Added the explicit empty-retained-subset forcing case while preserving
  the separate missing-expected-database refusal.
- 2026-08-27T18:33+02:00 — Created with the isolated retry-coverage repair. Verification metadata
  remains empty until governed closeout.
