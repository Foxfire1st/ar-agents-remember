# mcp/tests/test_review_bounded_pagination.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_bounded_pagination.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T00:15:00+02:00 |
| lastVerifiedCommitHash | `870701b43039cd205a8c98e418382729510c3de3` |
| lastVerifiedCommitDate | 2026-09-23T03:12:21+02:00|
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
| The lane marker, the two dataset sizes, and the two page sizes the walks use. | `pytestmark`; `SMALL_EXTRA_CLAIMS`; `LARGE_EXTRA_CLAIMS`; `COMPARISON_PAGE`; `RECORDS_PAGE` | mcp/tests/test_review_bounded_pagination.py:85-105 |
| **The real two-snapshot fixture, built through the public store operations over two real Git trees.** | `PaginationFixture`; `build_pagination_fixture` | mcp/tests/test_review_bounded_pagination.py:109-151; mcp/tests/test_review_bounded_pagination.py:165-211 |
| The composition, the real route and the query builder every page is read through. | `compose_page`; `route_client`; `route_query`; `paged_payload` | mcp/tests/test_review_bounded_pagination.py:214-265 |
| The walk helper and the two independent answer readers the cases compare the published counts with. | `walk_comparison`; `_comparison_answer`; `_returned_item_ids` | mcp/tests/test_review_bounded_pagination.py:268-370 |
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
| The two page refusal codes the transport cases read. | `comparison_page_reset`; `comparison_page_unreadable` | mcp/src/agents_remember/models/knowledge/review.py:149-150 |
| **The lane row and the three exact-scope consumer rows this module's registration produced.** | "unit-regression"; "mcp/tests/test_review_bounded_pagination.py" | mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/test-evidence-lanes.toml:163-163; mcp/tests/evidence-lifecycle.toml:1254-1254; mcp/tests/evidence-lifecycle.toml:1421-1421; mcp/tests/evidence-lifecycle.toml:1462-1462 |

## Cross-Repo References

No cross-repository behavior is exercised in this file. Both snapshots are built in one temporary
repository and the two Git trees borrow each other's object store inside `tmp_path`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
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
