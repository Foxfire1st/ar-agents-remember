# mcp/src/agents_remember/serving/ambient_seat.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/ambient_seat.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T06:47+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Serving overview](overview.md)

## Purpose

Resolves the calling structural seat from trusted hosted-process environment and the authoritative
catalog. It is the boundary that keeps agents from supplying their own session or lifecycle ids.

## Code Commentary

### Logic

`resolve_ambient_seat` reads plane-seeded hosted context, finds its catalog row, and verifies the
current task-document+role binding before returning the occupant.

### Conventions

All failure cases are typed `AmbientSeatError` statuses so application tools can fail closed.

### Invariants And Boundaries

- Request payloads never participate in caller identity.
- Unknown, stale, retired, or mismatched hosted evidence is refused.
- There is no global current-role fallback.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Ambient caller resolution is a single trusted-context function. | `resolve_ambient_seat` | mcp/src/agents_remember/serving/ambient_seat.py:16-70 |

## Cross-Repo References


## Update History

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for trusted ambient caller resolution.
