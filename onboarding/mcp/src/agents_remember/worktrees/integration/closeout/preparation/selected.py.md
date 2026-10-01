# mcp/src/agents_remember/worktrees/integration/closeout/preparation/selected.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Immutable selected preparation transport.

## Code Commentary

### Logic

The dataclass carries the handoff, exact intent and selected reference. The reobservation callback type connects shared execution to the current owning lifecycle. The transport itself performs no selection, scheduling or authorization.

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

- `SelectedCloseoutPreparation` owns the corresponding behavior described above. [1]

### Cross-Repo References

No cross-repository source is needed for this card.
