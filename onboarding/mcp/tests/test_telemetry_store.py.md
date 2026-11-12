# mcp/tests/test_telemetry_store.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks telemetry journal append/read, monotonic revisions, digest tampering, missing revisions and predecessor-chain failures. Replay is read-only instrumentation, same-revision different-byte append refuses, and byte capacity remains enforced. Eight retained functions replace the prior twenty-two-test claim without declaring instrumentation to be certification authority.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Append and read round trip preserves exact events [1]
- Append enforces monotonic event revision [2]
- Tampered journal entry is refused [3]
- Read refuses journal gap [4]
- Read refuses broken predecessor chain [5]
- Replay is read only instrumentation [6]
- Append cas collision refuses different bytes at same revision [7]
- Append enforces byte capacity limit [8]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
