# mcp/tests/test_wire_contract.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Uses small Python programs to test the modeled wire-mutation detector. Dump-returning callees taint callers, assignment and copied dictionaries remain detectable, sanctioned model updates before dumping are accepted, and read-only use is not mutation. The source programs are detector input, not a repeated repository-wide census.

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

- A function returning a dump makes its callers taint sources [1]
- A plain key assignment is caught [2]
- A copy does not launder the dump [3]
- Setting fields on the model before the dump is the sanctioned pattern [4]
- Reading a dumped dict is not mutating it [5]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
