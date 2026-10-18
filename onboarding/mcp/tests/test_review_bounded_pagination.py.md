# mcp/tests/test_review_bounded_pagination.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Pins bounded review walks, exact continuation scope and entry-read laziness — including the
removed records collection's named refusal.

## Code Commentary

Eight test functions cover a complete one-page comparison, long walks without duplication/loss,
partitioned item windows, the removed records collection refused by name on every request form
(`comparison_page_unreadable`, with no channel row rather than a measured zero), never-admitted
records cursors, a moved generation requiring fresh selection, transport page bounds and the entry
read populating its button without fetching record pages.

The fixture builds on shared text-tree populations through the read/diff-scope support modules, which use test-only knowledge_rows_test_support; this module does not import the row constructors directly. Production review/page composition is read back; fixture authoring names are not shipped storage admission. The deleted remainder-test population and former twelve-case coverage account are historical, not assertions supplied by this module.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References


- `test_every_page_of_a_large_comparison_is_reachable_without_duplicate_or_loss` supplies the current fixture or assertion described above. [21]




- `test_a_cursor_from_a_moved_generation_is_refused_with_a_new_generation_action` supplies the current fixture or assertion described above. [23]


- `test_the_entry_read_populates_the_button_without_fetching_record_pages` supplies the current fixture or assertion described above. [24]


- Fixture construction imports the shared diff/read-scope test support and rebuilds its candidate text population; this is not production write admission. [25]


- Test-only RowStore mutates a text tree and rebuilds the derived index; it is not a shipped validating write-admission plane. [26]


- compose_page calls the production review composition and asserts that it answered with a review payload. [27]
- build_pagination_fixture builds the shared diff fixture, adds extra realization paths and returns its candidate fixture. [28]
- The composition, the real route and the query builder every page is read through. [30]
- The walk helper and the two independent answer readers the cases compare the published counts with. [31]
- **A complete comparison is one page: no remainder and no cursor, so a whole selection is never presentable as a truncated one.** [32]
- The large comparison walk reads every page through HTTP and checks the union, counts, scope and terminal cursor without duplicate or loss. [33]
- Item windows partition the comparison population exactly and their rendered claim-row union matches the whole comparison. [34]
- **The packet's failure example: a cursor whose generation moved is refused with the new-generation action, and the response is the first page of the comparison that is there now.** [36]
- **The page-size boundary admitted by the route itself: 64 served, 65 and −1 refused by name with no uncaught request-model error.** [37]
- The entry case asserts unpaged subject review reads at both fixture sizes and independently verifies that driving the entry catalogue calls no comparison or view owner. [39]
- ReviewCollectionPage validates total arithmetic, continuation availability, reset reason and continued-from identity. [40]
- The transport case checks named input refusals and the page-size bound, including 64 admitted and 65 or negative sizes refused. [41]

- The removed records collection is a named refusal on first, unsized, continued and crossed requests. The serialized guard requires the evidence field to be absent, not an empty measured channel. [22]
- PaginationFixture holds shared test-support fixture state and builds its request/resolution; build_pagination_fixture composes that fixture. Neither is shipped public-store write admission. [29]
- One unit-regression membership and seven exact-scope lifecycle artifact records name this module. These source declarations are neither a six-row census nor test execution. [42]
