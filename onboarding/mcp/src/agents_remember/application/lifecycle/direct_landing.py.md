# mcp/src/agents_remember/application/lifecycle/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Application lifecycle overview](overview.md)

## Purpose

Publishes the direct-landing application tool and its recovery guidance over the durable operation journal.

## Code Commentary

### Logic

It validates feature/config authority, invokes the direct landing owner, reads canonical operation projections, and returns exact resume, retry, cancel, or cleanup guidance for unreadable and terminal generations.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Direct landing is explicit and journal-backed; it is never an automatic fallback from queued closeout, and unreadable durable evidence refuses without scanning for substitutes.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `direct_landing_tool` | mcp/src/agents_remember/application/lifecycle/direct_landing.py:1-285 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `direct_landing_tool` | mcp/src/agents_remember/application/lifecycle/direct_landing.py:1-285 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `direct_landing_tool` | mcp/src/agents_remember/application/lifecycle/direct_landing.py:1-285 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
