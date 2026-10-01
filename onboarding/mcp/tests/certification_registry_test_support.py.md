# mcp/tests/certification_registry_test_support.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Owns repository-neutral composition vocabulary shared by the retained certification suites. It supplies generic portable profiles, rail/result builders, plan
rebuilders, and bounded graph families without declaring an Agents Remember production profile.

## Code Commentary

### Logic

`RailSpec` and `ObservationSpec` describe compact test intent. Builders produce valid five-gate
registries, candidate-bound plans, results, and manifests, while specialized graph factories
generate linear, dense, shared-artifact, distinct-artifact, self-query, raw-declaration-overflow,
and exact-budget cases.

### Conventions

Underscored helpers are test-composition seams, not production API. Current direct imports are in the registry-contract, plan-authority, and closeout-certification recovery modules; the retired edge suites do not establish current coverage.

### Invariants And Boundaries

- Fixtures use a sample repository and portable owners; they do not encode Agents Remember rails.
- Valid defaults model all five gates, with Gate 5 memory-domain authority and Gates 1–4
  repository-profile authority.
- Graph and padding builders make scaling and exact-cap assertions reproducible.
- Shared support contains no executable test collection and no fallback registry.

### Todos

Keep new consumers explicit in `mcp/tests/evidence-lifecycle.toml`.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

No configured domain documentation could be checked.

### Repo-Internal References

- Portable gate classes and authorities are centralized in the generic rail builder. [1]
- Registry, plan, result, and manifest helpers compose the valid baseline available to the retained consumers. [2]
- Graph families construct reproducible dependency, raw-overflow, and artifact scaling boundaries. [3]
- The plan-authority suite directly imports the permanent support owner. [4]
- The registry-contract suite directly imports the permanent support owner. [5]

### Cross-Repo References

No cross-repository implementation is consumed.

- The support vocabulary intentionally names `sample-repository` and `portable-ci`. [6]
