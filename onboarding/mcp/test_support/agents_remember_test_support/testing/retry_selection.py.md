# mcp/test_support/agents_remember_test_support/testing/retry_selection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/retry_selection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Owns the pytest collection/execution boundary for dependency-aware retry proof. It lets pytest
collect the canonical candidate population so current import coverage is rebuilt, then executes
only test modules named by the dependency ownership graph.

## Code Commentary

### Logic

`pytest_addoption` accepts one repeated candidate-relative affected-module path. The try-last
collection hook resolves those paths under the candidate root, partitions collected items by exact
module path, reports unaffected items as deselected, and replaces the executable population with
the affected items. `pytest_collectreport` separately records Python modules whose collectors
completed successfully, including shared-definition modules with zero executable bodies. A path is
valid only when it owns an item or has that successful module-collection fact; genuinely missing,
uncollected, absolute/escaping, non-Python, or outside-root paths still raise `pytest.UsageError`.

### Conventions

- Collection remains complete; only execution is narrowed.
- Paths are candidate-relative files, not node-id globs or caller-authored expressions.
- Successful zero-body collection is an explicit observed state, not an optimistic fallback.
- The plugin is loaded only for a prepared delta plan by the quality wrapper.

### Invariants And Boundaries

- This plugin does not decide affectedness; `DependencyOwnershipGraph` owns that decision and the
  wrapper passes its exact result.
- It never turns an invalid or empty affected population into full execution.
- A zero-body module is accepted only after Pytest itself emits a passing collection report for
  that exact path; existence or a filename heuristic is insufficient.
- It is verification infrastructure and creates no product or acceptance authority.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this repository-owned pytest plugin.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation was configured. | — | — |

## Repo-Internal References

The wrapper owns when this plugin is loaded; the focused suite owns its fail-closed item filtering.

| Finding | Anchor | Source |
| --- | --- | --- |
| Delta commands retain canonical collection roots and pass one explicit affected path per module. | `_pytest_step` | mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py:247-287 |
| The hook records successful module collection, partitions exact paths, and keeps genuinely uncollected paths fail-loud. | `pytest_collectreport`; `pytest_collection_modifyitems`; `_refuse_uncollected_paths` | mcp/test_support/agents_remember_test_support/testing/retry_selection.py:47-119 |
| Focused tests prove narrow selection, explicit zero-body collection, and all input-refusal families. | `test_retry_selection_keeps_only_explicit_affected_modules`; `test_retry_selection_accepts_successfully_collected_zero_body_modules`; `test_retry_selection_rejects_missing_or_escaping_population` | mcp/tests/test_retry_selection.py:12-71 |

## Cross-Repo References

No meaningful cross-repository boundary is involved.

| Finding | Anchor | Source |
| --- | --- | --- |
| The plugin acts only inside this repository's Dagger-admitted pytest route. | — | — |

## Update History

- 2026-08-27T21:10+02:00 — Distinguished a passing zero-body Python module collection from an
  absent/uncollected retry path. The observed collection report is now required; missing paths
  remain fail-loud and no broad-execution fallback was added.
- 2026-08-27T17:19+02:00 — Created for the canonical-collection/affected-execution retry boundary.
  Verification metadata remains empty until governed closeout stamps the code commit.
