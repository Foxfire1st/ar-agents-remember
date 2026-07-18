# dashboard/src/data/sessionCapabilities.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/sessionCapabilities.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Exact-live-session capability client and pure model/effort menu/effective-marker derivations.

## Code Commentary

### Logic

Fetches only `/api/terminal/{session}/capabilities`, validates the bare snapshot, and separates
404, 409, 503, malformed, and transport outcomes. Menus use the chosen model row's
`sessionSettable` effort options in advertised order plus top-level nullable `selectedEffort`;
`configOptions` is never consulted. `effectiveSelection` chooses the freshest server snapshot or
later echo-verified evidence independently per field.

### Conventions

Provider-qualified keys remain opaque strings. A staged model re-gates the menu and exposes its
settable default only as a pre-highlight suggestion.

### Invariants And Boundaries

Live controls never use the pre-session capability cache. Null selected effort with a non-empty
menu means "effort not echoed"; a row with no settable options means no effort control.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Exact-session classification, menu rules, cycling, and effective selection. | L1-L248 | [sessionCapabilities.ts](sessionCapabilities.ts) |
| Boundary and derivation tables, including fresh Claude and provider-qualified Pi keys. | L36-L238 | [sessionCapabilities.test.ts](sessionCapabilities.test.ts) |
| Wire shapes validated by the client. | L1-L117 | [../types/harnessCapabilities.ts](../types/harnessCapabilities.ts) |
| Exact-session serializer and error contract implemented by the daemon. | L162-L227 | [harness_capabilities.py](../../../mcp/src/agents_remember/serving/harness_capabilities.py) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here; the API implementation is in this repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R1/R3/R7 after final reviewer PASS.
  Verification metadata is pinned to the contract base until the uncommitted code lands.
