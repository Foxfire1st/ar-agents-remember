# mcp/test_support/agents_remember_test_support/testing/cadence_runner.py

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Runs scheduled stress, provider-bump, and migration-window evidence in the pinned Dagger
environment without creating a second acceptance route.

## Code Commentary

### Logic

`run_cadence_evidence` requires Dagger admission, validates the lifecycle catalog, selects one
closed trigger expression, forces serial pytest, and writes a structured non-accepting result plus
phase/event artifacts. The result binds exact candidate/machine provenance, selected population,
topology, command, phase definitions, repetitions, limitations, and content-addressed artifacts.
An empty migration population produces a loud not-applicable result with provenance but does not
claim execution.
If pytest omits the phase report or writes an unusable one, the runner emits a content-addressed
failure artifact and returns a failing route result. Missing evidence can never be serialized as a
successful cadence execution.

### Conventions

The Dagger module owns container construction; this module owns only the in-container cadence
command and result schema.

### Invariants And Boundaries

- Host execution refuses before inventory or pytest.
- Release and diagnostic triggers are rejected so this cannot shadow full quality or the direct
  exact-node route.
- Every result says `acceptanceEligible=false` and `certifying=false`.

### Todos

None.

## Evidence

### Docs References

No external domain documentation governs the local cadence command.

### Repo-Internal References

- Only scheduled, provider-bump, and migration triggers can execute. [1]
- The Dagger public route remains explicitly non-accepting. [2]

### Cross-Repo References

No cross-repository cadence authority is owned here.
