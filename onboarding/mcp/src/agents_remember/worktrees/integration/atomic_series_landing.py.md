# mcp/src/agents_remember/worktrees/integration/atomic_series_landing.py

## Governing Overview

[Integration overview](overview.md)

## Purpose

Checks atomic-series ownership before landing to protected repository or memory targets.

## Code Commentary

### Logic

It resolves live series contracts and repository identity, reports precise blockers, and distinguishes active authority from terminal cleanup artifacts.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Only the exact live atomic series may own its protected landing surface; ambiguity, foreign identity, or an unresolved owner blocks mutation.
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

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

- No meaningful cross-repository reference applies. [3]
