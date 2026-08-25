# mcp/src/agents_remember/worktrees/integration/closeout/door_source.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/door_source.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Closeout integration overview](overview.md)

## Purpose

Reconstructs and validates the canonical closeout-door source used for scheduling and recovery.

## Code Commentary

### Logic

It resolves task and series identities, validates waiting publication evidence and candidate bindings, and returns typed source/refusal facts without borrowing lifecycle authority from the queue.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- A door source must match exact task, contract, candidate, and generation identity; stale or missing publication never becomes an inferred waiting candidate.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `DoorSourceContext` | mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:1-481 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `DoorSourceContext` | mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:1-481 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `DoorSourceContext` | mcp/src/agents_remember/worktrees/integration/closeout/door_source.py:1-481 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
