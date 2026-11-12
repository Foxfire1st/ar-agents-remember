# mcp/test_support/agents_remember_test_support/testing/evidence_lanes.py

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Defines the complete executable category and cadence registry applied during certifying pytest
collection.

## Code Commentary

### Logic

`EVIDENCE_LANES` gives every evidence category one marker, authority, minimum fidelity, expected
lifetime, and trigger set. `expression_for` maps affected, provider-bump, scheduled, migration, and
release triggers to explicit pytest populations. During collection, `category_for_item` first
requires the test file to have exactly one entry in the exhaustive lane manifest and then verifies
that any marker agrees with that declaration. The resolved category is attached to every report
item. When xdist workers collect, `pytest_collection` keeps a worker's `pytest.UsageError` in the
worker output under `WORKER_REFUSAL`, and `pytest_testnodedown` ends the controller's run with it,
so a refusal raised in a worker reaches the terminal as one usage error instead of an internal
error.

### Conventions

There is no unmarked-unit convention. Every test file must declare one category in
`mcp/tests/test-evidence-lanes.toml`; an exact-node override is permitted only where that narrower
identity is intentional. Missing, stale, unknown, duplicate, or marker-conflicting declarations
are collection errors.

### Invariants And Boundaries

- Categories and markers are unique, and the lane manifest exhausts the current test-file
  population; omissions and conflicts refuse collection.
- Affected execution excludes sustained stress, while release has no marker filter.
- Diagnostic evidence uses exact-node selection and cannot be selected by this plugin.
- Category assignment does not itself grant acceptance authority.
- A worker's collection refusal is not swallowed by xdist: the controller ends the run
  with the worker's message, exactly as a run without workers.

### Todos

None.

## Evidence

### Docs References

No external documentation owns the repository cadence taxonomy.

### Repo-Internal References

- The eight lanes define authority, fidelity, lifetime, and triggers. [1]
- Registry validation and collection routing are fail-closed. [2]

- A worker's collection refusal reaches the controller once, as a usage error. [4]
- The manifest loader proves complete, non-conflicting test-file coverage before collection. [5]

### Cross-Repo References

No adjacent repository controls lane membership.

