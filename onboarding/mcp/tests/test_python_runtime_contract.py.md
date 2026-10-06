# mcp/tests/test_python_runtime_contract.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Runs the Python builder installer against controlled command fixtures to prove a full clone is validated before atomic no-clobber publication, a valid existing builder is reused, and a foreign builder is refused without deleting its marker. It also carries the negative runtime-admission witness: the checker must end in the named version refusal before it can import a standard-library module the interpreter lacks. This file no longer asserts every package/CI Python-version surface or the old publisher-race matrix.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

The negative admission witness (`test_unsupported_version_is_named_before_importing_new_stdlib_modules`)
runs the checker under a simulated 3.13.15 interpreter whose `compression` import fails, and asserts
exit 1, empty stdout and the exact named refusal naming the expected and observed versions and the
executable. The real older-interpreter matrix supplements it with actual 3.11, 3.12 and 3.13
interpreters.

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

- Runtime builder is fully cloned atomically published and reused [1]
- Existing foreign builder is refused and preserved [2]

- The negative admission witness proves the named refusal precedes any newer standard-library import. [3]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
