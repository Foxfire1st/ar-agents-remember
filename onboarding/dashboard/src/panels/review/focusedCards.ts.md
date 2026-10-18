# dashboard/src/panels/review/focusedCards.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The pure arithmetic of MIK-R31's focused expression cards: grouping by (path, range), MIK-R01 order, counts,
each member's voice, the not-current marks, and how much of a bounded family the cards cover.** It resolves,
searches and guesses nothing: every range comes from the server's MIK-R08 definition 3 resolution
(`ReviewTreeEntry` in `data/reviewTrees.ts`). `ExpressionCards.tsx` renders what it computes.

## Code Commentary

### Logic

- **Grouping (rule 1).** `cardKey` is the kind plus each side's region: `path:start-end` for a resolved side,
  `path:<state>` otherwise. Entries share a card only when both sides are established regions (resolved, or a file
  absent there); an unresolved or unavailable side appends the entry's own ID, because "the same range" is not a
  fact anyone established for it. So two regions of one file keep two cards and two rationales, and several
  members' entries at the same path and range share one card listing each member.
- **Order (MIK-R01 rule 4).** `orderedEntries`: the seed invariant's entries first (the selected member, by
  `invariant_key`), then by invariant ID, realizations before proofs (`KIND_RANK`), path, then entry ID. A card
  takes the position of its first entry (`expressionCards`). The server sorts proofs first within an invariant;
  this order puts them after the realizations.
- **Counts.** `cardCounts` counts cards, `changed`, `unchanged` and `undetermined` apart: an unchanged card is
  excluded from every changed count.
- **Voices (rule 2).** `cardVoice` speaks from the side that records the entry now (after, else before) with that
  side's role, facet and rationale; `missing` is a realization without an authored rationale, which the renderer
  shows as an explicit gap. `revised` carries the before side's different rationale (or facet) for "Revised in this
  leaf".
- **Ranges.** `firstLines` gives each side's first line for a diff gutter that keeps the file's numbering;
  `rangeLabel` prints `L<a>–<b>`, `no file` or the state.
- **Not current (rule 1).** `notCurrent` lists every recorded side whose MIK-R03 state is not `current`, with its
  reason.
- **Scope of a bounded or unreadable roster (review F2, R2-5).** `cardScope` skips `not_recorded` sides, names other
  unread-side details, and collects reasons from a recorded side whose page is explicitly incomplete, whose loaded
  row count is below `members_total`, or whose member content is not `recorded`. Without an entry, missing reasons,
  or any recorded side it returns `undefined`; that return alone is not proof that the family was read completely.
  Otherwise it takes the recorded side with the greatest `members_total` (ties retain `before`), deduplicates its
  loaded `invariant_id ?? member_id` values, caps that count at its own total, and returns the explicit `missing`
  reasons alongside those two counts. It does not combine before/after populations or fetch another page.
- `languageOfPath` maps a path suffix to the highlighting ids `data/review.ts` uses; it styles and decides nothing.

### Conventions

- Pure functions of their arguments; the component owns all state.

### Invariants And Boundaries

- **Design boundary: focused cards group expression regions and keep authored voices above the excerpt; an
  absent rationale remains a gap.** `cardKey`, `expressionCards` and `cardVoice` supply that arithmetic; the
  renderer owns placement. The grouping fixtures check distinct/shared regions, unresolved isolation and order.
  The current mounted `ReviewSurface.gitTrees.test.tsx` family case asserts 12 cards, separate changed/unchanged
  counts and rationale-before-excerpt DOM order. Those are checked-in fixture assertions, not fresh measurements.
  The earlier account of four cards in `review_source_admission.py` is historical fixture provenance, not the
  current mounted case or a new formal-invariant admission.
- **Recorded invariant `INV-VPX81HXV`: bounded linked-source scope is not the whole family.** `cardScope`
  carries the loaded member count and the actual missing reasons; `ExpressionCards.ScopeLine` distinguishes an
  unfinished roster from missing content when the widest side's member count is already complete. The F2 test
  source checks a captured bounded/complete pair and a disjoint-sides variant. A separate case checks unread
  content, an underfilled side and an unreadable memory side when the widest side is fully loaded.
- **Historical accepted note R3-N1 (09:38:03):** the earlier implementation could say "loaded 2 of 2 … load the
  rest" when only the other side was incomplete. That accepted wording note remains provenance, not a description
  of the current `ScopeLine`: current text names missing content instead of promising that continuation fills it.
- Test references describe checked-in fixture assertions, not a test execution or a new CODE/MEMORY grade.

### Todos

No open R3-N1 wording task is asserted here: current source distinguishes its two scope cases. This card does not
certify all consumers, all malformed input shapes or full-family retrieval.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R31@v1` and its rulings
(`31_focused-expression-cards.json`) live outside the code and memory repositories, so they are named here and not
cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement of grouping and order. [1]
- A card: kind, path, change, both sides and its entries. [2]
- The region key; an unresolved or unavailable side keeps its own card. [3]
- MIK-R01 order with the seed first, and one card per key. [4]
- Unchanged excluded from the changed count. [5]
- Each member's voice, with `missing` for an absent rationale. [6]
- Gutter starts, range labels and not-current marks. [7]
- Loaded scope includes explicit missing reasons, deduplicates one widest recorded side and caps its count; undefined alone does not prove full retrieval. [8]
- Checked-in grouping assertions cover distinct regions, shared voices, unresolved isolation, separate change counts and seed ordering; no new execution. [9]
- Bounded/complete and disjoint-side F2 fixtures plus equal-count missing content, an underfilled side and an unreadable-side regression. [10]

- The current mounted family fixture asserts 12 cards with separate changed/unchanged counts and rationale-before-excerpt DOM order; this is source evidence, not a new test run. [11]

### Cross-Repo References

No cross-repository boundary is asserted by this module.
