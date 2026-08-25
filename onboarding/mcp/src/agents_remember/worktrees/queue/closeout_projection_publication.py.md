# mcp/src/agents_remember/worktrees/queue/closeout_projection_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_projection_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Closeout queue overview](overview.md)

## Purpose

Owns projection invalidation, rebuild, preview, and task-document mutation effects.

## Code Commentary

### Logic

It invalidates to empty, rebuilds from current sources, previews mutation blast radius, reports source problems, and emits a rebuild hint when task authoring invalidates an existing projection.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Task authoring is never blocked by queue state; an affected mutation clears the disposable projection and re-evaluates waiting candidates; no stale-row transition or silent fallback exists.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `ProjectionInvalidationReceipt` | mcp/src/agents_remember/worktrees/queue/closeout_projection_publication.py:1-237 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `ProjectionInvalidationReceipt` | mcp/src/agents_remember/worktrees/queue/closeout_projection_publication.py:1-237 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `ProjectionInvalidationReceipt` | mcp/src/agents_remember/worktrees/queue/closeout_projection_publication.py:1-237 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
