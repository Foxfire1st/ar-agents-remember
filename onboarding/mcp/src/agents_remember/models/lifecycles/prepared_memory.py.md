# mcp/src/agents_remember/models/lifecycles/prepared_memory.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Typed physical code view and realized memory candidate.

## Code Commentary

### Logic

The view binds the logical code/memory pair to exact selected preparation references, common repository, actual code commit/tree and created/existing disposition. An existing code view uses the real logical checkout; a created view names its distinct private root. The memory candidate binds that view and the realized memory tree. Structural model validity does not replace current physical Git or selected journal readback.

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

- `PreparedCodeExecutionView` owns the corresponding behavior described above. [1]
- `PreparedMemoryCandidate` owns the corresponding behavior described above. [2]

### Cross-Repo References

No cross-repository source is needed for this card.
