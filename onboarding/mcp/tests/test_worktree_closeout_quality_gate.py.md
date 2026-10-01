# mcp/tests/test_worktree_closeout_quality_gate.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks exact-candidate containment in closeout: later worktree edits cannot enter an asynchronous accepted candidate, the materialized index must match that candidate, and a hook mutation invalidates it. These retained assertions do not restore the historical pre-code memory-preflight ordering or impose a new per-leaf full-suite/review loop.

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

- Async candidate refuses later worktree edits [1]
- Materialized index must equal the accepted candidate [2]
- Hook mutation invalidates the independently reviewed candidate [3]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
