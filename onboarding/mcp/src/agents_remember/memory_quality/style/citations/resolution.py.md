# mcp/src/agents_remember/memory_quality/style/citations/resolution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/resolution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Resolve citation sources against code and memory roots.

## Code Commentary

### Logic

Module-level surface:

- `Trees` (class, lines 28-54) — The two roots a source may name.
- `operation_trees` (function, lines 57-69) — Bind a core operation to either standalone roots or managed application authority.

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
| Defines the class `Trees` (lines 28-54) — The two roots a source may name.. | `Trees` | mcp/src/agents_remember/memory_quality/style/citations/resolution.py:28-54 |
| Defines the function `operation_trees` (lines 57-69) — Bind a core operation to either standalone roots or managed application authority.. | `operation_trees` | mcp/src/agents_remember/memory_quality/style/citations/resolution.py:57-69 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
