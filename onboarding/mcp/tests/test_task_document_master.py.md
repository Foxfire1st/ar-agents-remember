# mcp/tests/test_task_document_master.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks master task authoring without creating a lifecycle, numbered subtask insertion/update, trust in the master's own declared rows at completion (a child leaf is neither read nor regraded), and refusal to erase or change unresolved row identity/multiplicity. A declared completed row stands; removal deletes a ready leaf and row but leaves all bytes untouched on unresolved refusal.

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

- Create master writes task json without lifecycle [1]
- Set subtask inserts then updates by number [2]
- Set subtask completed trusts the declared row without grading the child leaf [3]
- Replace cannot erase or change unresolved row identity or multiplicity [4]
- Master completion does not regrade a pending child leaf [5]
- Remove subtask deletes leaf doc and row [6]
- Remove subtask refuses unresolved row without touching any file [7]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
