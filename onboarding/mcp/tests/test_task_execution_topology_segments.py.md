# mcp/tests/test_task_execution_topology_segments.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks segment uniqueness, mutual exclusion of whole-master and segment nodes, endpoint addressing by a leaf sample and cycle refusal. It also checks derived placement of unassigned leaves, orchestrates membership and wave projection, and refusal of segments on atomic masters with the offending node identified.

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

- Leaf ids are unique sprint wide [1]
- Lump and segment appearances of one master are mutually exclusive [2]
- Edge endpoints address segments by leaf sample [3]
- Cycle through segments is refused [4]
- Unplaced leaf derives to the latest unblocked segment [5]
- Segmented membership matches orchestrates and waves run over nodes [6]
- Segment on atomic master is refused citing the node [7]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
