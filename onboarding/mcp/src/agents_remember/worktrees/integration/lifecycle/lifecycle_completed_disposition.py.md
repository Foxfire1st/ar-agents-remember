# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_completed_disposition.py

## Governing Overview

[Lifecycle operation integration overview](overview.md)

## Purpose

Checks exact completed-owner eligibility and an idle integration claim for journal disposition. The current public disposition is direct-landing retirement.

## Code Commentary

### Logic

It checks integration-claim idleness, exact retained owner and completed-but-unintegrated state before terminal disposition. A completed direct landing is recognised by the shared `completed_direct_owner` predicate from its own doorless record: kind, derived fingerprint/key identity, active disposition, completed status and the generation pinned by the control caller. The helper retains a separate closeout-owner check for stored door evidence. Direct supersede is refused because the record claims no door; retire is its owner disposition.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Completed status alone does not authorize disposition: integration must be incomplete and its claim must be idle. A direct owner is not inferred from a door publication; a stored direct record carrying a door is not an exact owner.
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


- Completed disposition checks exact ownership and an idle integration claim. [2]


### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

No additional cross-repository evidence applies.
