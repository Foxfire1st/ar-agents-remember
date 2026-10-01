# mcp/src/agents_remember/serving/conversation/library/scope.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this internal scope authority.

No configured domain documentation was available.

### Repo-Internal References

The cursor suite proves the narrow-only scope semantics and the digest binding; the null-byte
route regression is pinned at the ASGI layer.

- Canonical library scope confines the requested path and refuses invalid or escaping input. [1]
- Canonical library scope confines the requested path and refuses invalid or escaping input. [2]
- The query digest binds harness, canonical scope and sort. [3]

### Cross-Repo References

No meaningful cross-repo boundary exists for this local scope authority.

No meaningful cross-repo references found.
