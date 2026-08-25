# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Lifecycle operation integration overview](overview.md)

## Purpose

Derives public legal controls from durable lifecycle, door, repair, and integration evidence.

## Code Commentary

### Logic

It builds a context from the canonical record and contract, classifies recovery needs, and returns exact resume/retry/cancel/cleanup controls and arguments without mutation.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Controls are projections of current durable evidence; unavailable actions stay absent and no control may imply a transition the journal cannot validate.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `LifecycleControlProjectionContext` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py:1-594 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `LifecycleControlProjectionContext` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py:1-594 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `LifecycleControlProjectionContext` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_control_projection.py:1-594 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
