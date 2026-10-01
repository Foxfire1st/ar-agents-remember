# mcp/test_support/agents_remember_test_support/testing/candidate_snapshot.py

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Produces the exact Git working-candidate identity used by non-accepting Dagger evidence.

## Code Commentary

### Logic

`candidate_snapshot` hashes the HEAD commit/tree, exact staged candidate tree, and every changed,
deleted, and untracked non-ignored path, including executable bits and symlink target text. Paths
are confined before bytes are read.

### Conventions

The digest is a working-candidate identity, not a substitute commit.

### Invariants And Boundaries

- Missing Git facts or non-file candidate entries refuse.
- Ignored dependency/cache directories do not become candidate content.

### Todos

None.

## Evidence

### Docs References

No external contract applies.

### Repo-Internal References

`evidence_provenance.py` embeds this payload in cadence, retry, and measurement evidence;
`route_measurement.py` proves it is unchanged across all measured runs.

### Cross-Repo References

No cross-repository boundary applies.
