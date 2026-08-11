# mcp/src/agents_remember/serving/conversation/library/errors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/errors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T15:20+02:00 |
| lastVerifiedCommitHash |  `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

Defines the leaf-local typed error family for the native conversation library so every routine
refusal maps to one precise HTTP status (the reviewer O4 obligation: no raw 500s) while the
parallel L1 leaf never collides with a shared error module.

## Code Commentary

### Logic

Declares `ConversationLibraryError` over the shared `AgentsRememberError` base, then one
subclass per refusal class: unknown harness, invalid cursor/key, catalog generation drift,
stale native identity, unknown native conversation, capability-disabled (carrying the exact
capability state), store/helper failure, open request conflict, unknown open request, and a
full open ledger. `LibraryScopeError` subclasses the shared `AuthorityError` so scope escapes
surface as authority violations.

### Conventions

Every error subclasses the shared `agents_remember.errors` family so existing
`except ValueError` handlers keep working. The leaf keeps its own module instead of editing
shared `errors.py` so parallel leaves stay collision-free.

### Invariants And Boundaries

- `LibraryCapabilityError` always carries the exact `capability_state` for fail-closed 422
  copy; the feature stays visible and never claims invented parity.
- `LibraryScopeError` must remain an `AuthorityError` so the route table's subclass-before-base
  ordering keeps scope escapes on 403.
- No error may carry raw native stderr, secret, or path detail beyond allow-listed copy.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this internal error family.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The route module maps every member of this family to one precise status; the shared error base
keeps existing handlers compatible.

| Finding | Anchor | Source |
| --- | --- | --- |
| The route table maps each family member subclass-before-base to one exact HTTP status. | "def _error_response(exc: Exception) -> JSONResponse:"; "_ERROR_STATUS_TABLE: tuple[tuple[type[Exception], str, int], ...] = ("; "LIBRARY_RESPONSES: dict" | mcp/src/agents_remember/serving/conversation/library/api.py:278-312; mcp/src/agents_remember/serving/conversation/response_contract.py:131-142 |
| The shared base types this family subclasses keep `except ValueError` handlers working. | `ConversationLibraryError`; `LibraryScopeError` | mcp/src/agents_remember/serving/conversation/library/errors.py:15-16; mcp/src/agents_remember/serving/conversation/library/errors.py:23-24 |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local error module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-11T15:20+02:00 — Replaced generic error/table names with their exact declarations and
  removed the import-only citation that did not own response semantics.
- 2026-08-03T10:50+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 4 assigned citation findings (2 missing anchors and 2 malformed sources); final scoped check is clean.

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the leaf-local typed error family
  sidecar. Verification is blank until closeout commits and stamps the new source.
