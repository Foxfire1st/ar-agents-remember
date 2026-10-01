# mcp/tests/test_sprint_role_seats.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks structural seat lookup stays within the exact sprint/repository and role altitude. Duplicate current occupants refuse, altitude mismatch refuses before occupant lookup, and reviewer parentage is exact at each review seam. These tests do not authorize agents to choose or impersonate another role.

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

- Same role on different sprints never crosses repository scope [1]
- Duplicate current occupants fail closed [2]
- Role altitude mismatch fails before any occupant lookup [3]
- Reviewer parent is exact for each review seam [4]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
