# mcp/tests/test_spawn_agent_session.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Exercises the internal spawn primitive with a fake terminal host and real temporary catalog/task lineage. It creates a bound but explicitly unbriefed seat, preserves existing ownership on seat-taken refusal, and rejects forged structural parent provenance before host creation. Public dispatch remains responsible for the separate durable briefing transaction; no readiness or submitted-brief claim is fabricated.

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

- Spawns bound seat without brief or readiness claim [1]
- Seat taken is surfaced never overridden [2]
- Spawn refuses forged structural parent before host creation [3]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
