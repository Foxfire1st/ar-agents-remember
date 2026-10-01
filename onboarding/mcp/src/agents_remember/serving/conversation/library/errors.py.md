# mcp/src/agents_remember/serving/conversation/library/errors.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this internal error family.

No configured domain documentation was available.

### Repo-Internal References

The route module maps every member of this family to one precise status; the shared error base
keeps existing handlers compatible.

- The route table maps each family member subclass-before-base to one exact HTTP status. [1]
- The shared base types this family subclasses keep `except ValueError` handlers working. [2]

### Cross-Repo References

No meaningful cross-repo boundary exists for this local error module.

No meaningful cross-repo references found.
