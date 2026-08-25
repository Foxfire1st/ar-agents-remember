# mcp/src/agents_remember/models/closeout/projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/closeout/projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Closeout projection models overview](overview.md)

## Purpose

Defines strict persisted models for disposable closeout scheduling projections and task-document projection effects.

## Code Commentary

### Logic

The models bound candidate/problem/reason populations, validate valid-built versus invalid-empty state, and serialize invalidation/rebuild effects without lifecycle fields.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Invalid projection state is empty; projection records never own claims, commits, certification, integration, or terminal lifecycle evidence.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `MAX_CLOSEOUT_CANDIDATES` | mcp/src/agents_remember/models/closeout/projection.py:1-141 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `MAX_CLOSEOUT_CANDIDATES` | mcp/src/agents_remember/models/closeout/projection.py:1-141 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `MAX_CLOSEOUT_CANDIDATES` | mcp/src/agents_remember/models/closeout/projection.py:1-141 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
