# mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T01:15+02:00 |
| lastVerifiedCommitHash | `709dd07671b07d85ac49eaf3b77f4609b1e5fc5f` |
| lastVerifiedCommitDate | 2026-09-04T00:53:17+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Owns the deterministic anchor-to-range projection transaction (CCR-R10). When a claim's exact
anchor resolves uniquely in the frozen source-index snapshot, this module projects the claim's
current path/range mechanically from the shared exact-name oracle (symbol_index.locate and
Sightings.unique, language extents, and the source-index snapshot) and binds snapshot id, prior
claim digest, anchor, resolved extent, new document digest, and repair-tool version inside one
byte-level edit transaction with an explicit generated no-content-impact Update History bullet.
Every other case - multiple definitions, multiple unparsed occurrences, parsed mention-only
anchors, renames, deletions, malformed claims, stale snapshots, and conflicting writes - refuses
deterministically and routes to the existing actionable finding path. No similarity, filename,
or prose search authority is introduced, no old range is accepted as a fallback, and canonical
Markdown stays the sole memory content.

## Code Commentary

### Logic

Module-level surface (decorator-inclusive ranges):

- `now_utc` (function, lines 44-46) - The projection timestamp source, injectable so a replay is byte-for-byte.
- `ResolvedExtentInfo` (class, lines 49-61) - One anchor's resolved extent as the oracle chose it, ready to bind; `written` renders `path:start-end`.
- `Projection` (class, lines 64-104) - One deterministic anchor-to-range rewrite with its full binding, plus `to_dict` for the fixer payload.
- `ProjectionDecline` (class, lines 107-113) - Why one claim stayed on the curator path instead of being projected.
- `history_section_line` (function, lines 116-126) - The 1-based line of the Update History heading, or `None` when a document has no canonical section.
- `history_bullet` (function, lines 129-150) - The generated no-content-impact bullet, newest-first by construction, stamped with a full offset-bearing ISO 8601 datetime and the explicit `No content impact:` marker.
- `ProjectionRequest` (class, lines 153-164) - The transaction envelope: one claim, its read, and the frozen generation.
- `plan_projection` (function, lines 167-218) - One claim's deterministic projection, or the concrete refusal (`projection_no_resolved_extent` / `projection_conflicting_write`); `was` is read from the live source cell and the prior digest binds exactly the bytes the rewrite replaces.
- `verify_unchanged` (function, lines 221-227) - The transaction precondition: the cell still holds what the plan bound.
- `conflicting_write_decline` (function, lines 230-238) - The refusal when the cell changed between planning and staging.
- `history_edit` (function, lines 241-249) - One edit inserting every generated bullet directly under the heading, newest-first by construction.
- `document_digest` (function, lines 252-255) - SHA-256 of the exact bytes the batch would write to the document.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to
this module. The fixer drives this module (``fixer.Staging`` and ``fixer._decide``); resolution
semantics stay with the shared oracle in ``repair``/``source_index``/``symbol_index`` so a second
citation authority can never emerge here.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- A mechanically moved range is never an untraced body edit: it always stages the generated
  no-content-impact bullet in the same edit batch when the document has an Update History section.
- A document without the canonical Update History section gets a bound projection but no invented
  bullet (no structural section is fabricated from a range rewrite).
- Refusals are deterministic and never accept the old range as a fallback.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the injectable UTC clock `now_utc` (lines 44-46) - the single timestamp source for projection bullets. | `now_utc` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:44-46 |
| Defines the dataclass `ResolvedExtentInfo` (lines 49-61) - one anchor's oracle-chosen extent, with `written` rendering `path:start-end`. | `ResolvedExtentInfo` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:49-61 |
| Defines the dataclass `Projection` (lines 64-104) - one deterministic rewrite with its complete binding (document, line, anchors, was/now, resolved extents, snapshot id, prior claim digest, new document digest, history bullet, stamp, version). | `Projection` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:64-104 |
| Defines the dataclass `ProjectionDecline` (lines 107-113) - why one claim stayed on the curator path. | `ProjectionDecline` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:107-113 |
| Defines the function `history_section_line` (lines 116-126) - the 1-based Update History heading line, or `None` when absent. | `history_section_line` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:116-126 |
| Defines the function `history_bullet` (lines 129-150) - the generated no-content-impact bullet with an offset-bearing ISO stamp and explicit `No content impact:` marker. | `history_bullet` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:129-150 |
| Defines the dataclass `ProjectionRequest` (lines 153-164) - the transaction envelope (lines, site, relative path, claim, repair outcome, repository index, clock, history line). | `ProjectionRequest` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:153-164 |
| Defines the function `plan_projection` (lines 167-218) - one claim's deterministic projection or the concrete refusal. | `plan_projection` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:167-218 |
| Defines the function `verify_unchanged` (lines 221-227) - the write-time precondition that the cell still holds the planned bytes. | `verify_unchanged` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:221-227 |
| Defines the function `conflicting_write_decline` (lines 230-238) - the refusal for a cell changed between planning and staging. | `conflicting_write_decline` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:230-238 |
| Defines the function `history_edit` (lines 241-249) - the heading-element replacement that inserts generated bullets newest-first at the top of the section. | `history_edit` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:241-249 |
| Defines the function `document_digest` (lines 252-255) - SHA-256 of the exact bytes the batch would write. | `document_digest` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:252-255 |
| The fixer drives projection staging through `Staging` and `_decide`. | `Staging`; `_decide` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:244-250; mcp/src/agents_remember/memory_quality/style/citations/fixer.py:332-398 |

## Update History

- 2026-09-04T01:15+02:00 - 260831-CCR-L10 Gate-5 memory pass: created this file-level
  onboarding card for the new deterministic anchor-to-range projection module (CCR-R10) delivered
  in code commit 709dd076; anchors and ranges derived from the current worktree source and pinned
  to that commit.
