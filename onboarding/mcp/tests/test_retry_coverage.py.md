# mcp/tests/test_retry_coverage.py

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

## Evidence

### Docs References

No external domain documentation is configured for this repository-owned forcing proof.

### Repo-Internal References

- Complementary retained and delta arcs become one scored database/JSON pair. [1]
- An all-contexts-affected delta publishes fresh contexts without inventing retained data. [2]
- A merge refusal removes both public artifacts. [3]
- The production merge owner performs fail-closed publication. [4]

### Cross-Repo References

None.
