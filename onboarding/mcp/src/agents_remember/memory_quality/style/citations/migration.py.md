# mcp/src/agents_remember/memory_quality/style/citations/migration.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Migrate superseded citation tables and prose to the anchored format.

Since 260831-LOCR-L33 the pass also carries the verification provenance a cross-file relocation has
to prove itself against: `Pass.histories` is one `provenance.Histories` over the code and memory
roots, and `Pass.continuity(document)` resolves and memoizes one document's `repair.Continuity` from
its own `lastVerifiedCommitHash`. `place` feeds that continuity into `repair.plan`, so a migration
that would follow an exact name to a different file must prove the anchor existed in a cited file at
the stamp with the same extent kind — the same rule the tree-wide `--fix` pass uses, from one owner.

**On this route the continuity half of that rule cannot fire, and the wiring is kept anyway.** The
earlier `source_unresolvable` refusal in `row_paths`/`plan_row` means every path reaching `place`
still resolves, so the only refusal this entry point can produce is `anchor_left_live_file`; see the
invariant below, which records why the argument must not be deleted as dead code.

## Code Commentary

### Logic

Module-level surface:

- `Pass` (class, lines 63-86) — The document pass and immutable source generation every reader below needs. `__post_init__` builds `provenance.Histories` over the pass's code/memory roots; `continuity(document)` resolves that document's `repair.Continuity` at most once per pass through `repair.continuity_for`.
- `subject_of` (function, lines 89-100) — The card's declared path and repository -- what its own links are written against.
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
- `place` (function, lines 415-447) — The generated Source list for one draft, or ``None`` when it was declined. It feeds the pass's per-document continuity into `repair.plan`, so a cross-file relocation must prove continuity here exactly as it must in the tree-wide fixer.
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
- **A migration relocates under the same continuity rule as the tree-wide fixer.** `Pass.continuity`
  resolves each document's provenance once and `place` hands it to `repair.plan`; the scoped
  exclusion the fixer makes deliberately (`_scoped_citation` passing `None`) has no analogue here
  because migration's `place` is the only relocation decision on this route.
- **The continuity branches are UNREACHABLE from this entry point by construction, and that is
  deliberate on both sides.** `row_paths` resolves every Source Path against both trees and
  `plan_row` refuses one that names no existing file with the earlier, fail-closed
  `source_unresolvable` **before placement is ever considered**. So every `draft.paths` entry handed
  to `place` still resolves, `repair.plan`'s `live` set is therefore never empty, and the resolver
  can only ever answer **`anchor_left_live_file`**: `anchor_continuity_unproven` and the successful
  relocation cannot fire on this path. **Do not delete the continuity argument as dead code and do
  not loosen `row_paths` to make those branches fire** — the wiring becomes live the moment anything
  upstream loosens, and admitting unresolvable rows into placement only so a later branch can refuse
  them again is strictly worse. The seam test in `test_citation_document_transaction.py` pins both
  branches through the gate for exactly that future. Verified statically and experimentally.
- **The continuity cache is keyed by document path**, so a multi-claim document resolves its stamp
  once and every claim in it is judged against the same verification tree.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `Pass` (lines 63-86) — The document pass, now carrying `provenance.Histories` and a per-document continuity cache.. [1]
- Defines the function `subject_of` (lines 76-87) — The card's declared path and repository -- what its own links are written against.. [2]
- Defines the function `row_anchors` (lines 90-102) — The anchors a row STATES, or the code to decline under when it states none.. [3]
- Defines the function `row_paths` (lines 105-120) — Every path this Source cell resolves to, or the code to decline under.. [4]
- Defines the function `verified` (lines 123-128) — The old range, but only where one file is cited and every anchor is proven inside it.. [5]
- Defines the function `_not_in_range_detail` (lines 131-152) — Report the anchor's actual lines in the cited file without guessing another file.. [6]
- Defines the function `plan_row` (lines 155-177) — One old row (finding, citations, source) read into a draft.. [7]
- Defines the function `_is_note` (lines 180-192) — Whether the Citations cell holds prose that converting the row would DISCARD.. [8]
- Defines the function `_anchor_detail` (lines 195-199). [9]
- Defines the function `plan_table` (lines 202-225) — One superseded table, every row read. A placeholder row carries ``None`` for its draft.. [10]
- Defines the function `_plan_cells` (lines 228-247) — A row is the table's empty state, a claim citing no file, or something to convert.. [11]
- Defines the function `_cell` (lines 250-251). [12]
- Defines the function `_superseded` (lines 254-255). [13]
- Defines the function `read_document` (lines 258-273) — Every superseded construct in one document, read once. No file is opened twice.. [14]
- Defines the function `prose_sites` (lines 284-301) — ``(start, end, anchor text)`` for each superseded citation written on this one line.. [15]
- Defines the function `_bare_sites` (lines 304-312) — ``(L126-L173)`` with nothing beside it. A single number is this repository's leaf shorthand as often as a line and is not claimed, exactly as the check does not claim it. [16]
- Defines the function `plan_prose` (lines 315-336) — Every superseded prose citation in one document that sits on a single line.. [17]
- Defines the function `_is_wrapped_tail` (lines 339-352) — Whether this bare range is the second line of an anchored construct that wrapped.. [18]
- Defines the function `_unreachable` (lines 355-358) — Count joined-paragraph citation sites the per-line rewrite cannot reach.. [19]
- Defines the function `_plan_prose_site` (lines 361-393) — Plan one prose citation against the card's declared path.. [20]
- Defines the function `place` (lines 415-447) — The generated Source list for one draft, or ``None`` when it was declined; it consults the pass's continuity before a cross-file relocation.. [21]
- Defines the class `_Sightings` (lines 434-443) — The located anchors, answering NOWHERE for one that was never looked for.. [22]
- Defines the function `_written` (lines 446-452) — How a synthetic citation names itself in a refusal message.. [23]
- Defines the function `_generated` (lines 455-471) — The repair's sources, rejected whole if any cited file yielded no range of its own.. [24]
- Defines the function `_scoped` (lines 474-496) — Select the range when generation narrows a verified span.. [25]
- Defines the function `_narrowed` (lines 499-506) — Whether every generated range is shorter than the multi-line span it came from.. [26]
- Defines the function `_mention_only` (lines 509-523) — Whether every extent behind this range is a MENTION rather than a declaration.. [27]
- Defines the function `anchor_cell` (lines 526-527). [28]
- Defines the function `parser_dependent` (lines 530-539) — Whether this draft's RANGE came from a parse rather than from literal matching.. [29]
- Defines the function `unparsed_target` (lines 542-544) — Whether any cited file is one the extent layer cannot parse today.. [30]

## 260918-TSIP-L6 `ok` Answers Whether The Call Did What It Set Out To Do

`payload` (`:767-833`) no longer folds three facts into `ok` (`T64`). The old expression was
`not result.declined and not result.remaining and not dry_run`, which made a **preview** report
`ok: false` for a plan it had produced completely — while its sibling `citation_fix` answers
`ok: true` on the equivalent preview of the same family, so the two previews contradicted each
other and a caller could not tell "nothing to migrate" from "the operation did not happen".

`ok` now means *did this call do what it set out to do* — `not blocked`, where
`blocked = bool(result.declined) or (not dry_run and bool(result.remaining))`. The two facts that
used to be folded in are declared separately: `state` (`"refused"` when something was declined,
`"planned"` on a dry run, `"converted"` on a write) and `outcome` (`"planned"` / `"converted"`).
`remaining` is a **post-write** measurement — `migrate_onboarding_root` fills it only on the
non-dry branch — so a dry run must not read it; reading it while previewing would answer
`ok: false, state: "planned"`, which is `T64`'s symptom returning through the other fact the old
expression folded in. The truth table, including that dry-run-with-`remaining` row, is pinned by
`mcp/tests/test_response_address_binding.py:225-291`.
