# mcp/src/agents_remember/testing/cohort_manifest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/cohort_manifest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Owns the strict checked-in schema for the bounded direct Python cohort. It converts the TOML into
typed files, configurations, and nodes before eligibility verifies candidate bytes.

## Code Commentary

### Logic

`load_direct_cohort_manifest` accepts exactly schema/policy v2, a maximum selection of eight, no
more than sixteen audited Python files, and the required pytest/lifecycle configuration bindings.
It normalizes confined paths, exact SHA-256 values, symbols, local imports, effect families, and
per-node closure. Every audited file must be reachable from a selected node through node closure or
declared local imports.

### Conventions

Manifest parsing is total and accumulates structural findings into one `CohortManifestError`. Exact
key checks make schema extension an explicit policy migration.

### Invariants And Boundaries

- This module parses declarations; `eligibility.py` verifies files, AST nodes, fixtures, symbols,
  hashes, and candidate currency.
- No path escape, duplicate member, missing configuration, unreachable audit file, unknown effect,
  or parameterized manifest node is accepted.
- There is no auto-refresh, compatibility reader, or inferred repository-wide population.

### Todos

None.

## Docs References

No external domain documentation governs this repository-owned manifest.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Typed schema, bounds, and manifest errors are closed. | `DirectCohortManifest` | mcp/src/agents_remember/testing/cohort_manifest.py:17-84 |
| Loading validates exact tables, population shape, and reachability. | `load_direct_cohort_manifest` | mcp/src/agents_remember/testing/cohort_manifest.py:89-248 |
| The checked-in manifest is the only admitted population. | "python-direct-cohort/v2" | mcp/tests/python-direct-cohort.toml:1-3 |

## Cross-Repo References

No cross-repository authority is owned here.

## Update History

- 2026-08-25T01:56+02:00 — Created after Candidate-A consolidation replaced the generic analyzer
  with one explicit content-sealed cohort.
