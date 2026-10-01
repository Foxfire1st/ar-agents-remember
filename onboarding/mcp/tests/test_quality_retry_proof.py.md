# mcp/tests/test_quality_retry_proof.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Forces exact quality-proof reuse and dependency-owned delta selection with temporary source, support, fixture and coverage artifacts. Exact identity can reuse a full proof; changed selection, source or global input forces the appropriate fresh population. Support and fixture changes select their declared consumers without adding unaffected tests. This is a proof-selection fixture, not a new live Dagger acceptance run.

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

- Full proof becomes exact then test delta and source change invalidates [1]
- Retry reruns declared support and fixture consumers but not unaffected tests [2]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
