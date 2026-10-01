# mcp/src/agents_remember/application/structural/reviewer_parent.py

## Governing Overview

[structural application overview](overview.md)

## Purpose

Centralizes structural-parent derivation and dispatch provenance for identity-free reviewer seats.

## Code Commentary

### Logic

`ambient_reviewer_parent` maps a leaf reviewer to its owning master manager and a master reviewer to
that master's manager. Sprint reviewer dispatch refuses because architect and orchestrator are both
valid owners. `resolve_dispatch_provenance` stamps the resolved parent into both spawn provenance and
the expected reviewer generation.

### Conventions

An existing bound caller supplies explicit parent authority. Ambient derivation is allowed only when
topology has one unambiguous owner.

### Invariants And Boundaries

- Parent identity is generation-bound and includes both task document and role.
- Sprint ambiguity refuses before host effects.
- Non-reviewer roles do not acquire reviewer-parent metadata.
- The helper never guesses between architect and orchestrator.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Ambient parent derivation is topology- and altitude-specific. [1]
- Dispatch provenance carries the exact reviewer parent. [2]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
