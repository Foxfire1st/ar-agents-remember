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

The fixture builds on shared text-tree populations through the read/diff-scope support modules, which use test-only knowledge_rows_test_support; this module does not import the row constructors directly. Production review/page composition is read back; fixture authoring names are not shipped storage admission.

## Retained Full-Card Audit Context

The following distinct accounts are retained from memory base `81cfe4a8`. Dates, source coordinates, counts, outcomes and ownership describe that recorded epoch. They add no fresh execution, mutation result or acceptance. Historical numeric reference labels are custody text and do not select live sidecar anchors.

### Removed remainder population

> The deleted remainder-test population and former twelve-case coverage account are historical, not assertions supplied by this module.

Current source coverage remains the eight-function account above; the former population is retained as retirement context.

### Prior fifth-freeze anchor-retirement receipt

> - Retired at the fifth freeze d59c3493: mcp/tests/evidence-lifecycle.toml:588-588 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:841-841 - the bytes it recorded now occur 5 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:1216-1216 - the bytes it recorded now occur 4 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2265-2265 - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2824-2824 - the bytes it recorded now occur 7 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:125-661 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit eb0b0e98596d07e4e206e7936c20f86d8123e401; mcp/tests/evidence-lifecycle.toml:662-746 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 2f699606998a68c42994b9cc102cd22d56cfae37; mcp/tests/evidence-lifecycle.toml:1552-2083 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 8b0254263c6998b1d4814b2e97c1bd231d39350f; mcp/tests/evidence-lifecycle.toml:2793-2830 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 20624f979e2b89067a3e42019c9611a8e18ff848; mcp/tests/evidence-lifecycle.toml:2391-2475 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 2f699606998a68c42994b9cc102cd22d56cfae37; mcp/tests/evidence-lifecycle.toml:2845-2897 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit b52adc8bc0564f6328d3543e48998e9235f1e417; mcp/tests/evidence-lifecycle.toml:2419-2456 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit de5a7adbb21b2f6f22c3ced0eed9dd7189fe93c7. Retired means the anchor no longer stands, not that the cited subject was deleted.

All match counts, coordinates and removal commits in this receipt describe the recorded fifth freeze. They do not claim current selectors or deletion of the cited subjects.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References


- `test_every_page_of_a_large_comparison_is_reachable_without_duplicate_or_loss` supplies the current fixture or assertion described above. [21]




- `test_a_cursor_from_a_moved_generation_is_refused_with_a_new_generation_action` supplies the current fixture or assertion described above. [23]



- `test_the_entry_read_populates_the_button_without_fetching_record_pages` supplies the current fixture or assertion described above. [24]





- The fixture imports diff and read-scope test helpers. It rebuilds the candidate text population with the successor claim and added realization paths. [25]





- Test-only RowStore mutates a text tree and rebuilds the derived index; it is not a shipped validating write-admission plane. [26]



- compose_page calls the production review composition and asserts that it answered with a review payload. [27]

- build_pagination_fixture builds the shared diff fixture, adds extra realization paths and returns its candidate fixture. [28]



- The HTTP walk builds queries for the registered route, whose port invokes production composition. The direct walk invokes composition through compose_page. [30]




- The cursor walk checks each published cumulative count against a separate call to the comparison owner for the same request. It also reads the page item IDs from that owner. [31]


- **A complete comparison is one page: no remainder and no cursor, so a whole selection is never presentable as a truncated one.** [32]
- The large comparison walk reads every page through HTTP and checks the union, counts, scope and terminal cursor without duplicate or loss. [33]
- Item windows partition the comparison population exactly and their rendered claim-row union matches the whole comparison. [34]
- A stale cursor returns a reset with the new-generation action and differing identities. The reset has no continued-from cursor and hands back a cursor that continues the moved comparison. [36]
- **The page-size boundary admitted by the route itself: 64 served, 65 and −1 refused by name with no uncaught request-model error.** [37]


- At both fixture sizes the unpaged subject read has no page. The larger entry catalogue then returns its subject count without calling the patched comparison or view functions. [39]


- ReviewCollectionPage validates total arithmetic, continuation availability, reset reason and continued-from identity. [40]
- The transport case checks named input refusals and the page-size bound, including 64 admitted and 65 or negative sizes refused. [41]


- The first, unsized, continued and crossed requests for the removed records collection return the named refusal. The crossed request’s model dump omits evidence. [22]

- PaginationFixture holds shared test-support fixture state and builds its request/resolution; build_pagination_fixture composes that fixture. Neither is shipped public-store write admission. [29]




- The lane manifest registers this module in unit-regression. Seven lifecycle artifact consumer declarations also name it. [42]
