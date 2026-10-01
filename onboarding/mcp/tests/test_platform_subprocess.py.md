# mcp/tests/test_platform_subprocess.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Exercises the POSIX subprocess boundary: Windows-backed PATH entries are filtered, enclosure reports own native temporary files, native tool resolution ignores Windows shims, and explicit Windows commands or temporary roots refuse. Native Windows inputs remain unchanged. These cases use temporary paths and explicit platform arguments; they do not execute a Windows installation.

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

- Native environment uses enclosure reports and filters windows path [1]
- Native command prefers the linux tool after a windows path [2]
- Native command refuses an explicit windows shim [3]
- Native environment refuses windows backed temp root [4]
- Windows runner keeps its environment and paths unchanged [5]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
