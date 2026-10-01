# mcp/test_support/agents_remember_test_support/testing/lane_manifest.py

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Loads the one exhaustive, explicit lane assignment for every current Python test file and bounded
class/node override.

## Code Commentary

### Logic

The loader validates schema, categories, confined paths, current selectors, duplicates, conflicts,
missing test files, and stale rows. It produces a digest plus full included/excluded population for
cadence and retry compatibility.

### Conventions

File lanes are mandatory; narrow overrides are explicit and most-specific.

### Invariants And Boundaries

- No unknown item defaults to unit.
- Diagnostic evidence cannot enter accepting lanes.
- Retry identity binds the full lane population, not only selected files.

### Todos

None.

## Evidence

### Docs References

The lane taxonomy is repository-owned in `docs/design/python-evidence-system.md`.

### Repo-Internal References

The authority file is `mcp/tests/test-evidence-lanes.toml`; `test_evidence_lanes.py` forces missing,
unknown, and conflicting cases.

### Cross-Repo References

No cross-repository boundary applies.
