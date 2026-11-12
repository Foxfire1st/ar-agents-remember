# mcp/tests/test_structural_limits.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks structural detectors on small source trees: wide class surfaces and sibling-module methods retain their measured count, properties/setters and overloads count once, all function offenders are reported, crowded directories fail, and an existing declared directory deviation affects exactly its named directory. This documents unchanged structural policy; it does not create a CRAP-score exception mechanism.

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

- A wide class is reported with its measured surface [1]
- Moving methods into a sibling module does not lower the count [2]
- A property and its setter count once [3]
- Typing overloads count once [4]
- The function length check reports every offender not the first [5]
- The directory check rejects a crowded directory [6]
- A declared deviation silences exactly the directory it names [7]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
