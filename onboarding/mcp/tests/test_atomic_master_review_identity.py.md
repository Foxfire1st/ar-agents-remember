# mcp/tests/test_atomic_master_review_identity.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Checks the identity and compatibility properties of the CCR-R26 atomic-master route-review models
and aggregate scope. It is preparation evidence for the combined integration review, not a leaf
acceptance gate or final certification suite.

## Code Commentary

### Logic

The module preserves the baseline leaf route-review digest/currentness behavior, exercises aggregate
master identity and ordered membership, and checks that standalone/organizational review behavior is
not accidentally collapsed into the atomic-master boundary. The tests also cover the explicit
membership and normative-intent inputs used by the aggregate.

### Conventions

Assertions are source-level behavioral checks; no test result here grants review authority or changes
the route policy.

### Invariants And Boundaries

- Atomic children do not acquire independent route-review publication.
- Aggregate identity is sensitive to canonical membership/order and child intent inputs.
- Existing non-atomic route behavior remains independently represented.

### Todos

Final combined master integration execution remains parent-owned.

## Evidence

### Docs References

No relevant external documentation was configured.

No external documentation source was configured for this test module.

### Repo-Internal References

- Baseline leaf digest/currentness compatibility. [1]
- Operational bookkeeping does not change aggregate identity. [2]
- Normative and membership changes alter aggregate identity. [3]
- Models under test. [4]

### Cross-Repo References

No meaningful cross-repo implementation reference is required for this preparation test card. The
coordination requirement is tracked in the task report.
