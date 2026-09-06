# mcp/src/agents_remember/serving/conversation/library/scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The cursor suite proves the narrow-only scope semantics and the digest binding; the null-byte
route regression is pinned at the ASGI layer.

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical library scope confines the requested path and refuses invalid or escaping input. | `canonical_library_scope` | mcp/src/agents_remember/serving/conversation/library/scope.py:30-71 |
| Canonical library scope confines the requested path and refuses invalid or escaping input. | `canonical_library_scope` | mcp/src/agents_remember/serving/conversation/library/scope.py:30-71 |
| The query digest binds harness, canonical scope and sort. | `query_digest` | mcp/src/agents_remember/serving/conversation/library/scope.py:74-87 |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local scope authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 6 initial citation findings (3 anchor, 0 prose, 3 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the canonical scope authority
  sidecar. Verification is blank until closeout commits and stamps the new source.
