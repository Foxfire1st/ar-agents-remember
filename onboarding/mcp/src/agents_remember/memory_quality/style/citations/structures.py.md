# mcp/src/agents_remember/memory_quality/style/citations/structures.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/structures.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Structural identities for the construct an anchored range denotes.

## Code Commentary

### Logic

Module-level surface:

- `StructuralView` (class, lines 24-98) — One parsed source revision, reused for every anchor resolved inside it.
- `fingerprint` (function, lines 101-108) — Uncached convenience entry point for callers resolving one construct.
- `_span` (function, lines 111-114)
- `_tokens` (function, lines 117-126) — A syntax token stream with comments and layout absent but operators retained.
- `_digest` (function, lines 129-131)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `StructuralView` (lines 24-98) — One parsed source revision, reused for every anchor resolved inside it.. | `StructuralView` | mcp/src/agents_remember/memory_quality/style/citations/structures.py:24-98 |
| Defines the function `fingerprint` (lines 101-108) — Uncached convenience entry point for callers resolving one construct.. | `fingerprint` | mcp/src/agents_remember/memory_quality/style/citations/structures.py:101-108 |
| Defines the function `_span` (lines 111-114). | `_span` | mcp/src/agents_remember/memory_quality/style/citations/structures.py:111-114 |
| Defines the function `_tokens` (lines 117-126) — A syntax token stream with comments and layout absent but operators retained.. | `_tokens` | mcp/src/agents_remember/memory_quality/style/citations/structures.py:117-126 |
| Defines the function `_digest` (lines 129-131). | `_digest` | mcp/src/agents_remember/memory_quality/style/citations/structures.py:129-131 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
