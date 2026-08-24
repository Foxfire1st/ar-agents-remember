# mcp/src/agents_remember/testing/dependency_closure.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/dependency_closure.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Builds the fail-closed transitive closure for an exact direct-test request across module import
time, class lifecycle, autouse and parameter fixtures, helpers, imported functions, constructors,
and effectful calls.

## Code Commentary

`DependencyClosureAnalyzer.analyze` walks targets in request order and returns either one complete
`ResolvedDependencyClosure` or the first `ClosureRefusal`. Calls are de-duplicated by source path,
function name, and line number so recursion terminates without conflating same-named methods in
different classes. Candidate-owned symbols recurse; external/unknown symbols must match explicit
safe policy or refuse.

## Invariants And Boundaries

- Cache identity is a source identity, not `(file, name)` alone.
- Unsafe/unknown transitive dependencies refuse the whole request before execution.
- Dynamic declarations, state mutation, async helpers outside the cohort, ambiguous fixtures, and
  inherited/generated constructors refuse rather than guessing.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The analyzer returns complete closure or first stable refusal. | `DependencyClosureAnalyzer.analyze` | mcp/src/agents_remember/testing/dependency_closure.py:53-70 |
| Function scan identity includes source line. | `_analyze_function` | mcp/src/agents_remember/testing/dependency_closure.py:170-204 |
| Forcing proof covers same-named safe and unsafe methods. | `test_same_named_methods_do_not_share_dependency_cache` | mcp/tests/test_direct_test_eligibility.py:224-251 |

## Update History

- 2026-08-24T20:55+02:00 — Created for 260824-PDLS and records the CodeRabbit cache-identity repair.
