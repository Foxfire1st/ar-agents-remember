# mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Manifest and POSIX identity values for a citation source snapshot.

## Code Commentary

### Logic

Module-level surface:

- `SourceIndexManifestError` (class, lines 18-19) — A source-index manifest is obsolete or malformed.
- `canonical_hash` (function, lines 22-24) — Whether ``value`` is one canonical SHA-256 spelling.
- `_bounded_integer` (function, lines 27-30)
- `_canonical_root` (function, lines 33-43)
- `ReadyGeneration` (class, lines 47-133) — Constant-size authority that makes one database generation queryable.
- `Identity` (class, lines 137-182) — POSIX metadata used as the cheap trigger for authoritative content hashing.
- `SourceFile` (class, lines 186-203) — One indexed file's path, current metadata, and authoritative content digest.
- `TreeState` (class, lines 207-211) — Every relevant directory entry and readable-file candidate in deterministic order.
- `Manifest` (class, lines 215-256) — The atomic metadata companion for one immutable database generation.
- `Validation` (class, lines 260-265) — Whether a generation is current, content-stale, or metadata-equivalent.

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
| Defines the class `SourceIndexManifestError` (lines 18-19) — A source-index manifest is obsolete or malformed.. | `SourceIndexManifestError` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:18-19 |
| Defines the function `canonical_hash` (lines 22-24) — Whether ``value`` is one canonical SHA-256 spelling.. | `canonical_hash` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:22-24 |
| Defines the function `_bounded_integer` (lines 27-30). | `_bounded_integer` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:27-30 |
| Defines the function `_canonical_root` (lines 33-43). | `_canonical_root` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:33-43 |
| Defines the class `ReadyGeneration` (lines 47-133) — Constant-size authority that makes one database generation queryable.. | `ReadyGeneration` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:47-133 |
| Defines the class `Identity` (lines 137-182) — POSIX metadata used as the cheap trigger for authoritative content hashing.. | `Identity` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:137-182 |
| Defines the class `SourceFile` (lines 186-203) — One indexed file's path, current metadata, and authoritative content digest.. | `SourceFile` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:186-203 |
| Defines the class `TreeState` (lines 207-211) — Every relevant directory entry and readable-file candidate in deterministic order.. | `TreeState` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:207-211 |
| Defines the class `Manifest` (lines 215-256) — The atomic metadata companion for one immutable database generation.. | `Manifest` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:215-256 |
| Defines the class `Validation` (lines 260-265) — Whether a generation is current, content-stale, or metadata-equivalent.. | `Validation` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:260-265 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
