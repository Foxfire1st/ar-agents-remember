# mcp/tests/test_single_owner_primitives.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Uses small Python input programs to exercise single-writer detectors. It follows import aliases and constant program names, reads the program word from shell command strings, distinguishes gh from git, recognizes module and direct-import calls, and avoids confusing dataclasses.replace or unrelated names with the protected writer. It is detector behavior, not a repeated repository census.

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

- An import alias is followed to the name it binds [1]
- A program name hidden behind a constant is resolved [2]
- A shell command string is read down to its program word [3]
- Gh is not git [4]
- The module attribute form is caught [5]
- A bare replace from dataclasses is not the one from os [6]
- Direct imports and aliases are caught [7]
- Reexport without a call and unrelated local names are not callers [8]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
