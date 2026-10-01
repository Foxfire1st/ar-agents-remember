# mcp/test_support/agents_remember_test_support/testing/retry_selection.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository-owned pytest plugin.

No relevant external documentation was configured.

### Repo-Internal References

The wrapper owns when this plugin is loaded; the focused suite owns its fail-closed item filtering.

- Delta commands retain canonical collection roots and pass one explicit affected path per module. [1]
- The hook records successful module collection, partitions exact paths, and keeps genuinely uncollected paths fail-loud. [2]
- Focused tests prove narrow selection, explicit zero-body collection, and all input-refusal families. [3]

### Cross-Repo References

No meaningful cross-repository boundary is involved.

The plugin acts only inside this repository's Dagger-admitted pytest route.
