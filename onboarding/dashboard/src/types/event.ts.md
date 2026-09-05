# dashboard/src/types/event.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/types/event.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:47:44+00:00 |
| lastVerifiedCommitHash | `08e92217a7e4a08f9e14bb11855726e4d6be7f68` |
| lastVerifiedCommitDate | 2026-06-14T21:50:39+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Governing route overview](../overview.md)

## Purpose

Declares the dashboard's TypeScript shape for observer events.

## Code Commentary

### Logic

Trust has four values and Actor has three. ObserverEvent requires schema, id, ts, kind, trust and actor; data and the lifecycle, enclosure, repository, session and span identifiers are optional.

### Conventions

Wire names remain camelCase and align with the Python event envelope. Provenance distinguishes declared, observed, inferred and approved facts.

### Invariants And Boundaries

This file supplies static types only. Its schema field is a string; it performs no runtime event validation.

### Todos

None recorded.

## Docs References

No domain documentation is configured. This card describes repository source only.

## Repo-Internal References

These constructs establish the behavior described above.

| Finding | Anchor | Source |
| --- | --- | --- |
| Closed provenance vocabularies and event field shape | `Trust`; `Actor`; `ObserverEvent` | dashboard/src/types/event.ts:1-22 |
| Python envelope supplies the corresponding wire names and provenance values | `Trust`; `Actor`; `Event` | mcp/src/agents_remember/observer/events.py:25-64 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

## Update History

- 2026-09-05T06:47:44+00:00 — Created during L31 full-population memory recovery from frozen ea359649; verification records the actual source-touching commit. Documentation evidence only.
