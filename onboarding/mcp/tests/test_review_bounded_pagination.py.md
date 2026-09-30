# mcp/tests/test_review_bounded_pagination.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_bounded_pagination.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:13:03+02:00 |
| lastVerifiedCommitHash | `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` |
| lastVerifiedCommitDate | 2026-09-30T03:31:21+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The **bounded-pagination cases** for `ICR-R10@v1`: every page reachable, no page invented, and a stale
cursor refused. Twelve cases drive the **real** composition over **real** two-snapshot fixtures built by
the public store operations and read the pages back through the **real HTTP transport** the dashboard
uses.

Nothing here re-implements a comparison, a view, a cursor or a count: the numbers asserted are the
owners' own numbers, and the cursor carried from one call to the next is the owner's own token. The
module's docstring names the load-bearing properties one case each — a whole comparison is one page; a
large population is reachable page by page; a cursor for a moved generation is refused; the entry read
is a catalogue rather than a record fetch — and the card below records what each case is *for*.

## Code Commentary

### Logic

**Two dataset sizes, and the large one is real.** `PaginationFixture` builds a baseline snapshot, a
candidate copied from it and then curated through the store, and two real committed Git trees that
borrow each other's object store so one repository names both sides. `SMALL_EXTRA_CLAIMS` (0) and
`LARGE_EXTRA_CLAIMS` (90) are the only difference between the two sizes, so the walk is exercised over
a population large enough to page seven times without inventing a fixture that the production path
would not accept.

**Each page is read through the route, not through the composition directly.** `route_client` builds
the real app, `route_query` builds the query the dashboard builds, and `paged_payload` reads one page
back. The page's own `returned` is cross-checked against the comparison owner's independent answer for
the same request, so the published counts are the owner's rather than a re-derivation of them.

**A page that reports a remainder must name the way to reach it, and the cases assert the negative
too.** `test_a_records_remainder_never_names_a_cursor_that_cannot_reach_it` proves the comparison's
cursor is *refused* as a records page before asserting that the note names the request that does reach
the remainder; `test_the_whole_review_never_states_a_remainder_without_the_way_to_reach_it` checks the
named request really reaches the whole population. Both exist because the two are different facts and
one sentence used to carry both.

**The two transport-level refusals are pinned where the reader meets them.** The page-size boundary is
refused by the route itself in its own vocabulary (64 served; 65 and −1 refused by name, with no
uncaught request-model error), and a foreign cursor is reported as the wrong collection rather than as a
moved generation — the two directions are measured separately, because collapsing them would tell a
reader to open a new comparison when nothing had moved.

**The entry case is a negative measurement.** `test_the_entry_read_populates_the_button_without_fetching_record_pages`
replaces the comparison and the view with recorders that raise, then drives the real entry operation,
so "paging the catalogue does not fetch record pages" is measured rather than argued.

**One case deliberately does not assert page attribution of a rendered location row.** The item windows
partition exactly, every rendered row belongs to the population, and the union of the pages' rendered
rows equals the rows the unpaged read renders — but a location row may name a claim whose item arrives
on another page, because `ICR-R08@v1`'s traversal resolves the recorded relationship *line* from the
store. The case states that boundary in its own docstring instead of asserting a property the design
does not have.

### Conventions

- `pytestmark = pytest.mark.evidence_unit` keeps this a hermetic unit module; everything it needs is
  built under `tmp_path`, and no live coordination tree, network or service is touched.
- Every case builds its own fixture through the public store operations; the two real Git trees are the
  only Git objects and they are created under `tmp_path`.
- Cursors are opaque strings throughout: the cases assert the value the server published is the value
  the next request carried, and none of them parses or constructs one.

### Invariants And Boundaries

- **No assertion mirrors the implementation.** Every count is compared with the owner's own answer for
  the same request, and every page is read through the route.
- The `ICR-R08`/`ICR-R24` boundary above is recorded, not silently narrowed.
- Not covered here: a real-browser journey (`ICR-R24`/`ICR-R25` own the cockpit and browser half of
  A16), and a generation move racing an in-flight page request.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the four load-bearing properties and of what it does not re-derive.** | `compose_review` | mcp/tests/test_review_bounded_pagination.py:1-23; mcp/tests/test_review_bounded_pagination.py:35-35 |
| The lane marker, the two dataset sizes, and the two page sizes the walks use. | `pytestmark`; `SMALL_EXTRA_CLAIMS`; `LARGE_EXTRA_CLAIMS`; `COMPARISON_PAGE`; `RECORDS_PAGE` | mcp/tests/test_review_bounded_pagination.py:85-85; mcp/tests/test_review_bounded_pagination.py:94-95; mcp/tests/test_review_bounded_pagination.py:100-101 |
| **The real two-snapshot fixture, built through the public store operations over two real Git trees.** | `PaginationFixture`; `build_pagination_fixture` | mcp/tests/test_review_bounded_pagination.py:108-151; mcp/tests/test_review_bounded_pagination.py:165-211 |
| The composition, the real route and the query builder every page is read through. | `compose_page`; `route_client`; `route_query`; `paged_payload` | mcp/tests/test_review_bounded_pagination.py:214-229; mcp/tests/test_review_bounded_pagination.py:232-241; mcp/tests/test_review_bounded_pagination.py:244-258; mcp/tests/test_review_bounded_pagination.py:261-265 |
| The walk helper and the two independent answer readers the cases compare the published counts with. | `walk_comparison`; `_comparison_answer`; `_returned_item_ids` | mcp/tests/test_review_bounded_pagination.py:268-315; mcp/tests/test_review_bounded_pagination.py:326-338; mcp/tests/test_review_bounded_pagination.py:341-370 |
| **A complete comparison is one page: no remainder and no cursor, so a whole selection is never presentable as a truncated one.** | "test_a_complete_comparison_is_one_page_with_no_remainder_and_no_cursor" | mcp/tests/test_review_bounded_pagination.py:373-386 |
| **The large walk: every page through HTTP, the union the comparison's own total exactly once, each page's counts adding up, the scope beside the counts.** | "test_every_page_of_a_large_comparison_is_reachable_without_duplicate_or_loss" | mcp/tests/test_review_bounded_pagination.py:389-426 |
| **The item windows partition exactly and no rendered row is lost — with page attribution of a location row deliberately not asserted (`ICR-R08` resolves the line).** | "test_the_item_windows_partition_exactly_and_paging_loses_no_rendered_row" | mcp/tests/test_review_bounded_pagination.py:429-488 |
| The records collection publishes its own bounds and a cursor that is a different document from the comparison's. | "test_the_records_collection_publishes_its_own_bounds_and_cursor" | mcp/tests/test_review_bounded_pagination.py:509-532 |
| **The records walk: four pages, the same union property, no duplicate and no loss.** | "test_every_page_of_a_large_records_selection_is_reachable_without_duplicate_or_loss" | mcp/tests/test_review_bounded_pagination.py:535-562 |
| **The packet's failure example: a cursor whose generation moved is refused with the new-generation action, and the response is the first page of the comparison that is there now.** | "test_a_cursor_from_a_moved_generation_is_refused_with_a_new_generation_action" | mcp/tests/test_review_bounded_pagination.py:565-603 |
| **The page-size boundary admitted by the route itself: 64 served, 65 and −1 refused by name with no uncaught request-model error.** | "test_the_transport_names_the_input_it_refused_and_bounds_the_page_it_applies" | mcp/tests/test_review_bounded_pagination.py:606-689 |
| **A foreign cursor reported as the wrong collection rather than as a moved generation.** | "test_a_foreign_cursor_is_reported_as_the_wrong_collection_not_a_moved_generation" | mcp/tests/test_review_bounded_pagination.py:692-724 |
| **A records remainder never names a cursor that cannot reach it, proved by presenting that cursor and reading the refusal.** | "test_a_records_remainder_never_names_a_cursor_that_cannot_reach_it" | mcp/tests/test_review_bounded_pagination.py:727-765 |
| The refused records cursor stated with its code, both identities and a live first page of that collection. | "test_a_refused_records_cursor_states_its_code_identities_and_a_live_first_page" | mcp/tests/test_review_bounded_pagination.py:768-804 |
| **The whole review states no remainder without the way to reach it, and the named request really reaches the population.** | "test_the_whole_review_never_states_a_remainder_without_the_way_to_reach_it" | mcp/tests/test_review_bounded_pagination.py:807-838 |
| **The entry stays a catalogue: driving it calls no comparison and no view, and its body carries no page at either dataset size.** | "test_the_entry_read_populates_the_button_without_fetching_record_pages" | mcp/tests/test_review_bounded_pagination.py:841-878 |
| The page arithmetic under test, and the page value whose constructor refuses a remainder without a cursor. | `comparison_page`; `records_page`; `reset_comparison_page`; `ReviewCollectionPage` | mcp/src/agents_remember/application/review_pagination.py:202-305; mcp/src/agents_remember/models/knowledge/review.py:366-440 |
| The two page refusal codes the transport cases read. | `comparison_page_reset`; `comparison_page_unreadable` | mcp/src/agents_remember/models/knowledge/review.py:157-158; mcp/src/agents_remember/models/knowledge/review.py:152-162 |
| **The lane row and the three exact-scope consumer rows this module's registration produced.** | "unit-regression"; "mcp/tests/test_review_bounded_pagination.py" | mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/test-evidence-lanes.toml:209-209 |

## Cross-Repo References

No cross-repository behavior is exercised in this file. Both snapshots are built in one temporary
repository and the two Git trees borrow each other's object store inside `tmp_path`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; MIK-R13 inserted one `unit-regression` row at `test-evidence-lanes.toml:121`, so citation ranges into later lane rows were projected by the installed `memory-citations --fix` or, for multi-anchor rows it declined, re-pointed by the exact base-to-staged line shift (+1 at or after `:121`; each such row was byte-identical to memory HEAD).
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; MIK-R01 moved lines in `test-evidence-lanes.toml`, so citation ranges into it were projected by the installed `memory-citations --fix` or, for multi-anchor rows it declined, re-pointed by the exact base-to-staged line shift (each such row was byte-identical to memory HEAD).
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; L06 inserted one `unit-regression` row at `test-evidence-lanes.toml:69`, so its citations to later lane rows moved down one line. The multi-anchor lane rows the fixer declined were re-pointed by that exact +1 shift, and each was checked to hold its anchors in the shifted ranges; any other moved row was re-pointed by the installed fixer, which records its own bullet. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R11's changes, were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R02's changes (or normalised by the installed fixer in the same pass), were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): No content impact: citation-only repair. Ranges into `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R30's line insertions (or normalised by the installed fixer in the same pass), were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-working line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R03 added one row at `:112` of `test-evidence-lanes.toml`, moving every later row down one line, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). The fixer also normalised passing ranges in rows that cite files this leaf did not change; those ranges are measurement-true. No claim, anchor or source file of this card changed.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R08 moved lines in `test-evidence-lanes.toml`, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). No claim, anchor or source file of this card changed.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`mcp/tests/test-evidence-lanes.toml`) were re-pointed by the exact base-to-working line map (multi-anchor rows the installed fixer declined); no claim wording changed. No verification stamp was advanced.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`test-evidence-lanes.toml`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): No content impact: this card's source is unchanged; its citations into `mcp/tests/test-evidence-lanes.toml` moved by this leaf's two-line `unit-regression` insertion at `:107-108` and were re-pointed (by the installed anchor-range projection where it could, otherwise by exact base-to-working line mapping). Each re-pointed row cites the same lane line it cited at base; no claim wording changed and no verification stamp was advanced.
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): **No content impact** — citation-only repair. MIK-R20 inserts two `unit-regression` rows at `mcp/tests/test-evidence-lanes.toml:102-103`, which moves every later lane row down by two lines; this card's lane-row citations were re-pointed by that exact shift (by base-to-working line mapping where the installed fixer declined a multi-anchor row), their claims unchanged. No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`test-evidence-lanes.toml`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`application/published_intent.py`, `mcp/tools/knowledge.py`, `mcp/registration/knowledge.py`, `models/tools/knowledge_responses.py`, `cli/__main__.py`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed by the installed fixer or, for the multi-anchor rows it declined, by exact base-to-working line mapping; a per-document `memory-citations` check then reported 0 findings. No claim wording changed.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): No content impact: citation-only re-measure. This card cites `mcp/tests/test-evidence-lanes.toml`, where MIK-R22's two `unit-regression` rows (`:99-100`) moved every later row down two lines. Ranges were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact line shift, and a per-document check then reported 0 findings. The claims were re-read and are unchanged. No verification stamp was advanced.
- 2026-09-29T06:00:00+02:00 — 260928-MIK-L07 curator (uncommitted change set on `ar/260928-mik-l07`, code base `45fe37749b388de348d16ced50c28c03490dce64` plus the working-tree delta): No content impact: MIK-R07 inserts one `unit-regression` row at `mcp/tests/test-evidence-lanes.toml:98`, so this card's rows citing lane lines below it were re-pointed one line down (by the installed anchor-range projection or, where it declined a multi-anchor row, by an exact one-line shift confirmed by every anchor resolving in the current file). Claim wording unchanged. No stamp advanced.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): No content impact: the lane-row citation re-measured after MIK-R21's two-line insertion into `test-evidence-lanes.toml`. Claim meaning unchanged; no stamp advanced.
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 1 citation into `mcp/tests/test-evidence-lanes.toml` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T23:11:42+02:00 — 260921-ICR-L56 curator (candidate tree `0dabc51f68b613546ec971657726b97828afb69a` over code base `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`): No content impact: re-pointed 1 citation into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_read_anchor_memo.py` row at `:173`; each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T20:07:41+02:00 — 260921-ICR-L55 curator: No content impact: re-pointed 1 citation into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_notes_listing.py` row at `:162` (candidate tree `c77a4346480db6674dd760f974e8b24079d8f755` over code base `e66f1f3894116e0bb37b49f178d8bfcb130a7e28`). Each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): No content impact: citation ranges into files this leaf changed (`dashboard/src/data/review.ts`, `dashboard/src/panels/review/SourceContent.test.tsx`, `mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_knowledge_review_source_content.py`) were re-pointed to where the same anchors now sit, each row checked valid at the base, invalid at the candidate, and valid after the base-to-candidate line mapping; claim wording unchanged. No stamp advanced.

- 2026-09-27T05:43:38+00:00 — Curator-authored re-citation of 1 investigated L41 source-linked claim(s). Each named registration or declaration was selected individually after the composite guarded projection declined. Prior explanation, refusal evidence, generated history and real verification stamps are preserved.

- 2026-09-27T00:34:45Z — L39: No content impact: resolved the affected registry/instruction/overview reference rows against their exact current named anchors after the scoped source changes. Existing factual meaning, verification stamps and earlier history are preserved.

- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **citation re-anchoring and history only; no claim wording changed and no row deleted.** This leaf's change set moved the lines several of this card's rows cite — `mcp/src/agents_remember/application/knowledge_curator_ingest.py` grew 3587 → 3861 while `mcp/tests/test-evidence-lanes.toml` gained one `unit-regression` row and `mcp/tests/evidence-lifecycle.toml` gained two consumer rows, each shifting every row below it — so every affected range was re-derived against the candidate's own bytes rather than shifted by a remembered delta and re-anchored to the construct it names. Nothing in the body above was deleted to clear a finding, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-23T00:15:00+02:00 — 260921-ICR-L10 curator: **created.** The module is new in this leaf
  (`ICR-R10@v1`) and this is its one-to-one card. It records the properties the twelve cases protect
  (a complete comparison is one page; the walk loses nothing and repeats nothing; a moved cursor is
  refused with the new-generation action; the entry fetches no record page), the two facts a reader
  would otherwise have to rediscover — the fixture is built from two real Git trees through the public
  store operations, so the counts asserted are the owners' own — and the one boundary the case states
  rather than asserts: a rendered location row's page attribution belongs to `ICR-R08@v1`, which
  resolves the recorded relationship line from the store. The card also records this module's
  registration: **one** `unit-regression` lane row at `mcp/tests/test-evidence-lanes.toml:163` and
  **three** exact-scope consumer rows in `mcp/tests/evidence-lifecycle.toml`, which is what re-pinned
  `LIFECYCLE_CATALOG_SHA256` to `b4d4a7f9…` in this leaf. **Stamp accounting:** the verification pair
  names the **production line at this leaf's base** `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`
  (2026-09-22T20:08:58+02:00); the module itself is **uncommitted**, so no commit contains the bytes a
  stamp would claim to have verified and closeout owns the real stamp.
