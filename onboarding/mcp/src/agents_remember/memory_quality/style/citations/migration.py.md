# mcp/src/agents_remember/memory_quality/style/citations/migration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/migration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Migrate superseded citation tables and prose to the anchored format.

## Code Commentary

### Logic

Module-level surface:

- `Pass` (class, lines 61-73) — The document pass and immutable source generation every reader below needs.
- `subject_of` (function, lines 76-87) — The card's declared path and repository -- what its own links are written against.
- `row_anchors` (function, lines 90-102) — The anchors a row STATES, or the code to decline under when it states none.
- `row_paths` (function, lines 105-120) — Every path this Source cell resolves to, or the code to decline under.
- `verified` (function, lines 123-128) — The old range, but only where one file is cited and every anchor is proven inside it.
- `_not_in_range_detail` (function, lines 131-152) — Report the anchor's actual lines in the cited file without guessing another file.
- `plan_row` (function, lines 155-177) — One old row (finding, citations, source) read into a draft.
- `_is_note` (function, lines 180-192) — Whether the Citations cell holds prose that converting the row would DISCARD.
- `_anchor_detail` (function, lines 195-199)
- `plan_table` (function, lines 202-225) — One superseded table, every row read. A placeholder row carries ``None`` for its draft.
- `_plan_cells` (function, lines 228-247) — A row is the table's empty state, a claim citing no file, or something to convert.
- `_cell` (function, lines 250-251)
- `_superseded` (function, lines 254-255)
- `read_document` (function, lines 258-273) — Every superseded construct in one document, read once. No file is opened twice.
- `prose_sites` (function, lines 284-301) — ``(start, end, anchor text)`` for each superseded citation written on this one line.
- `_bare_sites` (function, lines 304-312) — A bare parenthesized two-endpoint range with nothing beside it. A single number is this repository's leaf shorthand as often as a line and is not claimed, exactly as the check does not claim it.
- `plan_prose` (function, lines 315-336) — Every superseded prose citation in one document that sits on a single line.
- `_is_wrapped_tail` (function, lines 339-352) — Whether this bare range is the second line of an anchored construct that wrapped.
- `_unreachable` (function, lines 355-358) — Count joined-paragraph citation sites the per-line rewrite cannot reach.
- `_plan_prose_site` (function, lines 361-393) — Plan one prose citation against the card's declared path.
- `place` (function, lines 401-431) — The generated Source list for one draft, or ``None`` when it was declined.
- `_Sightings` (class, lines 434-443) — The located anchors, answering NOWHERE for one that was never looked for.
- `_written` (function, lines 446-452) — How a synthetic citation names itself in a refusal message.
- `_generated` (function, lines 455-471) — The repair's sources, rejected whole if any cited file yielded no range of its own.
- `_scoped` (function, lines 474-496) — Select the range when generation narrows a verified span.
- `_narrowed` (function, lines 499-506) — Whether every generated range is shorter than the multi-line span it came from.
- `_mention_only` (function, lines 509-523) — Whether every extent behind this range is a MENTION rather than a declaration.
- `anchor_cell` (function, lines 526-527)
- `parser_dependent` (function, lines 530-539) — Whether this draft's RANGE came from a parse rather than from literal matching.
- `unparsed_target` (function, lines 542-544) — Whether any cited file is one the extent layer cannot parse today.
- `_provenance` (function, lines 547-554) — Which of the three ways this draft's range was found, counted apart.
- `table_edits` (function, lines 557-571) — The whole table in the new shape: header, delimiter, and every body row.
- `_row` (function, lines 574-585) — One body row at the new width: converted, padded, or carrying its own old evidence.
- `_declined` (function, lines 588-593) — The refusal this draft recorded, counted on the way past.
- `_row_source` (function, lines 596-599)
- `prose_text` (function, lines 602-612) — ``cit:([anchors], sources)`` for one prose citation, on ONE line by construction.
- `live_drafts` (function, lines 615-620) — Every draft still eligible to convert -- nothing about the row itself refused it.
- `anchors_to_locate` (function, lines 623-635) — Only the anchors NO cited file holds -- the ones the tiebreaker will search for.
- `_held_by_a_cited_file` (function, lines 638-643)
- `migrate_onboarding_root` (function, lines 646-697) — Convert every superseded citation in the memory tree, and report what it would not.

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
| Defines the class `Pass` (lines 61-73) — The document pass and immutable source generation every reader below needs.. | `Pass` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:61-73 |
| Defines the function `subject_of` (lines 76-87) — The card's declared path and repository -- what its own links are written against.. | `subject_of` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:76-87 |
| Defines the function `row_anchors` (lines 90-102) — The anchors a row STATES, or the code to decline under when it states none.. | `row_anchors` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:90-102 |
| Defines the function `row_paths` (lines 105-120) — Every path this Source cell resolves to, or the code to decline under.. | `row_paths` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:105-120 |
| Defines the function `verified` (lines 123-128) — The old range, but only where one file is cited and every anchor is proven inside it.. | `verified` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:123-128 |
| Defines the function `_not_in_range_detail` (lines 131-152) — Report the anchor's actual lines in the cited file without guessing another file.. | `_not_in_range_detail` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:131-152 |
| Defines the function `plan_row` (lines 155-177) — One old row (finding, citations, source) read into a draft.. | `plan_row` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:155-177 |
| Defines the function `_is_note` (lines 180-192) — Whether the Citations cell holds prose that converting the row would DISCARD.. | `_is_note` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:180-192 |
| Defines the function `_anchor_detail` (lines 195-199). | `_anchor_detail` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:195-199 |
| Defines the function `plan_table` (lines 202-225) — One superseded table, every row read. A placeholder row carries ``None`` for its draft.. | `plan_table` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:202-225 |
| Defines the function `_plan_cells` (lines 228-247) — A row is the table's empty state, a claim citing no file, or something to convert.. | `_plan_cells` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:228-247 |
| Defines the function `_cell` (lines 250-251). | `_cell` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:250-251 |
| Defines the function `_superseded` (lines 254-255). | `_superseded` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:254-255 |
| Defines the function `read_document` (lines 258-273) — Every superseded construct in one document, read once. No file is opened twice.. | `read_document` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:258-273 |
| Defines the function `prose_sites` (lines 284-301) — ``(start, end, anchor text)`` for each superseded citation written on this one line.. | `prose_sites` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:284-301 |
| Defines the function `_bare_sites` (lines 304-312) — ``(L126-L173)`` with nothing beside it. A single number is this repository's leaf shorthand as often as a line and is not claimed, exactly as the check does not claim it. | `_bare_sites` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:304-312 |
| Defines the function `plan_prose` (lines 315-336) — Every superseded prose citation in one document that sits on a single line.. | `plan_prose` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:315-336 |
| Defines the function `_is_wrapped_tail` (lines 339-352) — Whether this bare range is the second line of an anchored construct that wrapped.. | `_is_wrapped_tail` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:339-352 |
| Defines the function `_unreachable` (lines 355-358) — Count joined-paragraph citation sites the per-line rewrite cannot reach.. | `_unreachable` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:355-358 |
| Defines the function `_plan_prose_site` (lines 361-393) — Plan one prose citation against the card's declared path.. | `_plan_prose_site` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:361-393 |
| Defines the function `place` (lines 401-431) — The generated Source list for one draft, or ``None`` when it was declined.. | `place` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:401-431 |
| Defines the class `_Sightings` (lines 434-443) — The located anchors, answering NOWHERE for one that was never looked for.. | `_Sightings` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:434-443 |
| Defines the function `_written` (lines 446-452) — How a synthetic citation names itself in a refusal message.. | `_written` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:446-452 |
| Defines the function `_generated` (lines 455-471) — The repair's sources, rejected whole if any cited file yielded no range of its own.. | `_generated` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:455-471 |
| Defines the function `_scoped` (lines 474-496) — Select the range when generation narrows a verified span.. | `_scoped` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:474-496 |
| Defines the function `_narrowed` (lines 499-506) — Whether every generated range is shorter than the multi-line span it came from.. | `_narrowed` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:499-506 |
| Defines the function `_mention_only` (lines 509-523) — Whether every extent behind this range is a MENTION rather than a declaration.. | `_mention_only` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:509-523 |
| Defines the function `anchor_cell` (lines 526-527). | `anchor_cell` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:526-527 |
| Defines the function `parser_dependent` (lines 530-539) — Whether this draft's RANGE came from a parse rather than from literal matching.. | `parser_dependent` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:530-539 |
| Defines the function `unparsed_target` (lines 542-544) — Whether any cited file is one the extent layer cannot parse today.. | `unparsed_target` | mcp/src/agents_remember/memory_quality/style/citations/migration.py:542-544 |

## Update History

- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the `Pass` range with the scoped fixer's generated decorator-inclusive extent, reworded the `_bare_sites` Logic bullet out of the superseded prose-citation spelling (the literal example remains in the table row), and completed its description against the source docstring; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
