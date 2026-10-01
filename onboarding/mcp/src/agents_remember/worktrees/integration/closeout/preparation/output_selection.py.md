# mcp/src/agents_remember/worktrees/integration/closeout/preparation/output_selection.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Exact raw output publication into the existing object store and journal.

## Code Commentary

### Logic

The owner reobserves the caller, builds the output from exact raw commit bytes, validates its intent relationship, publishes the typed object and reopens authority before selecting its reference. An already selected output must match exactly. An object merely present in the store does not become selected authority.

### Conventions

Use the named source owners directly. This source was introduced in landed commit `245057ab16e19afdaabd5c188c9576b22e0c0870` and remains byte-identical at the recovery code candidate. Its behavior was re-read against that source during memory recovery; the existing metadata owner still owns the pending verification stamp.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

### Todos

No source-local TODO is asserted here.

## Evidence

### Docs References

No configured domain documentation applies.

### Repo-Internal References

- `retain_prepared_output` owns the corresponding behavior described above. [1]

### Cross-Repo References

No cross-repository source is needed for this card.
