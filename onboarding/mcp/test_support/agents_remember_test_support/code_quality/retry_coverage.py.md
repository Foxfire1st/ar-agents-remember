# mcp/test_support/agents_remember_test_support/code_quality/retry_coverage.py

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

## Evidence

### Docs References

No external domain contract is configured. The implementation uses Coverage.py's installed public
`CoverageData` and `Coverage` APIs.

### Repo-Internal References

- Context proof requires branch arcs and pytest runtime contexts. [1]
- Unchanged contexts are extracted to a separate retained database. [2]
- Retained and fresh evidence are merged and atomically republished fail closed. [3]
- Focused forcing proves successful composition, a known-empty retained subset, and two-artifact cleanup on failure. [4]

### Cross-Repo References

None. Retry artifacts remain inside the Dagger-owned cache/report boundary.
