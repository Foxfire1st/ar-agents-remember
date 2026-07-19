# mcp/src/agents_remember/serving/conversation/library/scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

Derives the server-side canonical allowed project scope for every library call: a requested
`cwd` may narrow the caller's authorized workspace scope but can never grant a new
native-history scope, and every cursor/key binds the resulting harness + scope + sort query
digest.

## Code Commentary

### Logic

`canonical_library_scope` resolves the workspace root, defaults the scope to that root, and
otherwise resolves the requested cwd strictly (following symlinks) and rejects anything that is
unresolvable, not a directory, or outside the root with `LibraryScopeError` — never clamped or
guessed. `query_digest` builds the unkeyed canonical digest of the (harness, scope,
`last-activity-desc` sort) triple; `clamp_limit` enforces one bounded page-size rule for every
library route.

### Conventions

`LIBRARY_SORT = "last-activity-desc"` is the only normalized list ordering this leaf supports
(native recency). Scope resolution failures are typed authority violations, not validation
errors.

### Invariants And Boundaries

- Narrow-only: a requested cwd must resolve to an existing directory inside the canonical root;
  traversal, symlink escape, cross-repo, and prefix-sibling requests fail closed.
- `ValueError` from `Path.resolve` (embedded null bytes and other malformed input) surfaces as
  the typed scope refusal, never a raw 500 (review F2 / O4).
- The query digest binds harness + canonical scope + sort, so cursors minted under one triple
  can never page another.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this internal scope authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The cursor suite proves the narrow-only scope semantics and the digest binding; the null-byte
route regression is pinned at the ASGI layer.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical scope defaults to the root, narrows inside it, and rejects traversal/symlink/cross-scope escapes. | L137-L173 | [test_conversation_library_cursor.py](agents-remember/mcp/tests/test_conversation_library_cursor.py) |
| A null-byte cwd maps to the typed 403 scope refusal on the production route. | L352-L362 | [test_conversation_library_api.py](agents-remember/mcp/tests/test_conversation_library_api.py) |
| The query digest binds harness, scope, and sort into every minted scope. | L131-L136 | [test_conversation_library_cursor.py](agents-remember/mcp/tests/test_conversation_library_cursor.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local scope authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the canonical scope authority
  sidecar. Verification is blank until closeout commits and stamps the new source.
