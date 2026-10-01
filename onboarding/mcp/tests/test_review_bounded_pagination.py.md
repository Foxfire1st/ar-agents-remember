# mcp/tests/test_review_bounded_pagination.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The module's own statement of the four load-bearing properties and of what it does not re-derive.** [1]
- The lane marker, the two dataset sizes, and the two page sizes the walks use. [2]
- **The real two-snapshot fixture, built through the public store operations over two real Git trees.** [3]
- The composition, the real route and the query builder every page is read through. [4]
- The walk helper and the two independent answer readers the cases compare the published counts with. [5]
- **A complete comparison is one page: no remainder and no cursor, so a whole selection is never presentable as a truncated one.** [6]
- **The large walk: every page through HTTP, the union the comparison's own total exactly once, each page's counts adding up, the scope beside the counts.** [7]
- **The item windows partition exactly and no rendered row is lost — with page attribution of a location row deliberately not asserted (`ICR-R08` resolves the line).** [8]
- The records collection publishes its own bounds and a cursor that is a different document from the comparison's. [9]
- **The records walk: four pages, the same union property, no duplicate and no loss.** [10]
- **The packet's failure example: a cursor whose generation moved is refused with the new-generation action, and the response is the first page of the comparison that is there now.** [11]
- **The page-size boundary admitted by the route itself: 64 served, 65 and −1 refused by name with no uncaught request-model error.** [12]
- **A foreign cursor reported as the wrong collection rather than as a moved generation.** [13]
- **A records remainder never names a cursor that cannot reach it, proved by presenting that cursor and reading the refusal.** [14]
- The refused records cursor stated with its code, both identities and a live first page of that collection. [15]
- **The whole review states no remainder without the way to reach it, and the named request really reaches the population.** [16]
- **The entry stays a catalogue: driving it calls no comparison and no view, and its body carries no page at either dataset size.** [17]
- The page arithmetic under test, and the page value whose constructor refuses a remainder without a cursor. [18]
- The two page refusal codes the transport cases read. [19]
- **The lane row and the three exact-scope consumer rows this module's registration produced.** [20]

### Cross-Repo References

No cross-repository behavior is exercised in this file. Both snapshots are built in one temporary
repository and the two Git trees borrow each other's object store inside `tmp_path`.

No meaningful cross-repo references found.
