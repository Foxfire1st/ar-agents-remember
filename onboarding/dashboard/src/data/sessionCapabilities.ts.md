# dashboard/src/data/sessionCapabilities.ts

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

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Exact-session classification, menu rules, cycling, and effective selection. [1]
- Boundary and derivation tables, including fresh Claude and provider-qualified Pi keys. [2]
- Wire shapes validated by the client. [3]
- Exact-session serializer and error contract implemented by the daemon. [4]

### Cross-Repo References

No meaningful cross-repo boundary is owned here; the API implementation is in this repository.

No cross-repo evidence applies.
