# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T16:57+02:00 |
| lastVerifiedCommitHash | `8dcf0645fdbc3aa490132d5947b22227d45ff302` |
| lastVerifiedCommitDate | 2026-08-26T16:57:26+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Lifecycle operation integration overview](overview.md)

## Purpose

Coordinates task-addressed lifecycle start, observe, retry, resume, cancel, and projection.

## Code Commentary

### Logic

It claims waiting closeout candidates, creates or replaces generations, publishes initial doors,
starts detached workers, handles exact duplicate/retry cases, and exposes current projections. After a
generation is safely cancelled, replacement binds the current exact waiting door and still requires
proven worker exit; current candidate-tree and first-ready checks remain in the subsequent claim
transaction.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- A failed or terminal generation has an explicit convergent retry route; claim/door/generation publication is ordered and idempotent; queue state is scheduling input, not operation authority.
- Cancellation releases the old operation only after worker exit proof. A fresh generation follows
  current door and task truth rather than requiring a stale direct claimed-door edge.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `STALE_HEARTBEAT_SECONDS` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:1-1118 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `STALE_HEARTBEAT_SECONDS` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:1-1118 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `STALE_HEARTBEAT_SECONDS` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py:1-1118 |

## Update History

- 2026-08-26T16:57+02:00 — Removed direct claimed-door ancestry as cancelled-generation
  authority. Replacement now requires the current exact waiting door plus durable cancellation and
  worker-exit proof; exact candidate and first-ready checks remain claim-owned.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
