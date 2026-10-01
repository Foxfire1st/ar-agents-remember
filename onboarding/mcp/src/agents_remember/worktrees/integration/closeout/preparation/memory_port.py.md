# mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_port.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Typed prepared-memory certification request, result and port.

## Code Commentary

### Logic

The request carries the actual lifecycle handoff and prepared memory candidate. The result carries exact Gate-5 semantic inputs and original result/certificate references. The protocol delegates certification to the registered producer; a constructed response alone does not authorize publication.

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

- `PreparedMemoryCertificationRequest` owns the corresponding behavior described above. [1]
- `PreparedMemoryCertificationResult` owns the corresponding behavior described above. [2]
- `PreparedMemoryCertificationPort` owns the corresponding behavior described above. [3]

### Cross-Repo References

No cross-repository source is needed for this card.
