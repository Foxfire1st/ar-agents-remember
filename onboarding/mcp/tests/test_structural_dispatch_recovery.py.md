# mcp/tests/test_structural_dispatch_recovery.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Forces spawn-and-pinned-brief recovery at durable boundaries. Failure before append retires only a proven unbriefed generation; post-append compaction failure preserves/reuses the briefed generation; receipt-binding ambiguity is reconciled rather than rolled back. A reviewer from another parent is neither reused nor retired, and terminal failed briefing replaces only that exact generation.

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

Receipt-bind recovery and failed-generation replacement use a zero dispatch-brief readiness wait and assert that the injected sleeper is never called. Their unknown-versus-rollback and retire/replace assertions remain unchanged.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Pre append failure retires only the proven unbriefed generation [1]
- Post append compaction failure keeps and reuses the briefed generation [2]
- Receipt bind failure is unknown not rollback and retry repairs it [3]
- Live reviewer from another parent is not reused or retired [4]
- Terminal failed brief retires and replaces that generation [5]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.

- Receipt-bind recovery keeps its unknown outcome with no fixture readiness sleep. [6]
