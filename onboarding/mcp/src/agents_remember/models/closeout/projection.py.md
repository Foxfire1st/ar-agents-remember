# mcp/src/agents_remember/models/closeout/projection.py

## Governing Overview

[Closeout projection models overview](overview.md)

## Purpose

Defines strict persisted models for disposable closeout scheduling projections and task-document projection effects.

## Code Commentary

### Logic

The models bound problem/reason populations, validate valid-built versus invalid-empty state, and serialize invalidation/rebuild effects without lifecycle fields. No bound limits how many candidates a projection may carry.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Invalid projection state is empty; projection records never own claims, commits, certification, integration, or terminal lifecycle evidence.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

- No external domain source is required to establish this repository-owned implementation. [1]

### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- The module's concrete API, control flow, and validation boundary are implemented here. [2]
- Persisted projection state carries an unbounded `members` list beside its bounded `sourceProblems`; membership uniqueness is enforced by validator, not by a population ceiling. [3]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

- No meaningful cross-repository reference applies. [4]
