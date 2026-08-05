# mcp/src/agents_remember/memory_quality/style/citations/drafts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/drafts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Describe migration declines and their next action.

## Code Commentary

### Logic

Module-level surface:

- `Subject` (class, lines 112-119) — One document and the source file its own metadata table says it is about.
- `Draft` (class, lines 122-155) — One citation being migrated: where it is, what it states, and why it was refused.
- `TableDraft` (class, lines 158-171) — One superseded table: where its header is, its rows, and the marker a padded row uses.
- `Result` (class, lines 174-194) — What one pass read, converted and declined.

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
| Defines the class `Subject` (lines 112-119) — One document and the source file its own metadata table says it is about.. | `Subject` | mcp/src/agents_remember/memory_quality/style/citations/drafts.py:112-119 |
| Defines the class `Draft` (lines 122-155) — One citation being migrated: where it is, what it states, and why it was refused.. | `Draft` | mcp/src/agents_remember/memory_quality/style/citations/drafts.py:122-155 |
| Defines the class `TableDraft` (lines 158-171) — One superseded table: where its header is, its rows, and the marker a padded row uses.. | `TableDraft` | mcp/src/agents_remember/memory_quality/style/citations/drafts.py:158-171 |
| Defines the class `Result` (lines 174-194) — What one pass read, converted and declined.. | `Result` | mcp/src/agents_remember/memory_quality/style/citations/drafts.py:174-194 |

## Update History

- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive class ranges; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
