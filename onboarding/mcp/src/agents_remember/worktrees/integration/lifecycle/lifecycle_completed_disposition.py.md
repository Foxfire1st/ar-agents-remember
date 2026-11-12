# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_completed_disposition.py

## Governing Overview

[Lifecycle operation integration overview](overview.md)

## Purpose

Determines whether a completed closeout or direct operation has a legal terminal disposition.

## Code Commentary

### Logic

It checks integration-claim idleness, exact retained owner and completed-but-unintegrated state before terminal disposition. A completed direct landing is recognised by the shared `completed_direct_owner` predicate from its own doorless record: kind, derived fingerprint/key identity, active disposition, completed status and the generation pinned by the control caller. The closeout-owner branch and worker-exit guard remain independent. Direct supersede is refused because the record claims no door; retire is its owner disposition.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Completed status alone does not authorize disposition: integration must be incomplete, its claim idle and worker exit proven. A direct owner is not inferred from a door publication; a stored direct record carrying a door is not an exact owner.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

No configured external domain source applies; this is repository-owned behavior.

### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- Direct retire uses the shared owner predicate while existing integration and worker guards stay in force; direct supersede is refused. [2]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

No additional cross-repository evidence applies.
