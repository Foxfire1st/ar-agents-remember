# mcp/tests/test_state_signal_relay.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Simulates multiple relay ticks to preserve the finished-worker signal even without an inbox row, revalidate topology and landed episodes before non-reaction actions, hold a busy manager at the boundary then land once, rebind a replaced owner, route a master-bound reviewer to the current manager, fence malformed or ambiguous topology per subject, avoid done signals for killed or hung seats, and withhold any owner wake while a seat's own turn is still open. Injected delivery and clock boundaries make these relay assertions deterministic.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

The current structural-routing cases exercise action-time replacement, missing/ambiguous parent
topology isolation, owner disappearance after finding revalidation, and action-time refusal without
publishing a row or source marker. These cases protect the R08 refusal and retry boundary while
leaving delivery/recovery and canonical seat selection to their owning modules.

The non-completion boundary also covers an open turn. A seat whose `turn_state` is still `working`
reports nothing to its owner even while stale adapter outcome fields survive on its row; the same
seat produces exactly one owner-addressed signal once its turn has ended. That case holds the
ended-turn trigger in place so the parked open-turn external-await design cannot be adopted here as
a fallback producer.

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

- Incident 1 finished worker without inbox row still signals manager [1]
- Non reaction action revalidates current topology and landed episode [2]
- Busy manager holds at boundary then lands exactly once [3]
- Owner rebinding after manager replacement [4]
- Master-bound reviewer reaches the current manager after replacement [5]
- Missing or ambiguous parent topology fences one subject while preserving an unrelated finding [6]
- Owner disappearance after finding revalidation leaves the source eligible and unmarked [7]
- Action-time topology refusal fences the subject without a marker [8]
- No done signal for killed or hung seats [9]
- An open turn never wakes the owner before terminal evidence [10]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
