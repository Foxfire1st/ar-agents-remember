# mcp/tests/test_active_projector_singleflight.py

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Proves concurrent reconnects replace one retired active projector exactly once.

## Code Commentary

### Logic

The async regression drives two callers through the same post-retirement service lookup and
asserts that they converge on one newly constructed projector rather than racing into duplicate
pollers and projection graphs.

### Conventions

The test targets lifecycle ownership, not mapper behavior.

### Invariants And Boundaries

- A retired projector is never reused.
- Concurrent replacement is singleflight at the service boundary.
- The resulting callers share one live projector.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Replacement owner. [1]

### Cross-Repo References

No meaningful cross-repository references found.
