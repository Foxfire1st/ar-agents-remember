# mcp/tests/test_quality_report_publication_security.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Exercises report-publication confinement: an exported artifact outside the declared profile inventory refuses, nested legacy-directory symlinks cannot remove external reports, and generation symlinks cannot substitute external evidence. Profile-bound fixtures establish the artifact authority; this file no longer proves the old runtime-digest mutation matrix.

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

- Export cannot publish an artifact outside the profile inventory [1]
- Nested legacy directory symlink cannot delete external reports [2]
- Generation symlink cannot substitute external evidence [3]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
