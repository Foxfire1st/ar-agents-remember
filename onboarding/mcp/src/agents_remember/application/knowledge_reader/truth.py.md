# mcp/src/agents_remember/application/knowledge_reader/truth.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The truth views, the census view, the record list and the code view of the knowledge reader (MIK-R29
rules 3 and 4).** A truth view shows one record of the selected tree with every field it records, its
explanation prose (the record's `.md`) when it has one, its outgoing links (its own `links`, a family's
members and routes, what it supersedes) and its incoming links, and its timeline (`timeline.py`). Per kind:

- **invariant:** every normative field, its realizations and proofs each with its MIK-R03 state at the
  selection's code tree, the invariant's own state, its families, and the records linking to it (a decision
  shown whole), and membership history with its owner, kind, closed status, path, row identity, subject, disposition and document;
- **family:** guarantee, members (each with statement and state), routes, every member location grouped by
  path, and MIK-R03's stale members;
- **decision:** `records.decision_document`, the decision in full;
- **incident and every other facet record:** every field as recorded (an incident's cause,
  `cause_uncertainty`, recovery and corrective actions included), with typed links both ways.

The **census view** is MIK-R20's report of each census under `knowledge/census/`; the **record list** is every
record by kind (the dashboard's lookup); the **code view** is one code file at the selection's code tree,
opened at a locator.

## Code Commentary

### Logic

- **The record.** `record_view` returns `None` for an ID the tree does not hold (the entry point answers
  `not-found`). It builds the record summary with its path and whole document, the prose, the outgoing and
  incoming links (`link_document` over `incoming_links`), the kind's own part, and the timeline over the
  history rows about it and the entries that feed it (an invariant's own; a family's members'). Invariant membership-subject rows join that timeline as well as the dedicated membership array.

- **Outgoing links, or why not (F11).** `_links_of` validates the record through its kind's model in
  `RECORD_MODELS` and renders each link with `record_link_target` (and its `alternative` for a decision).
  A record that does not validate, or a kind no model reads, returns the reason; the view then carries
  `outgoingState: unavailable` rather than claiming no outgoing link.
- **States.** `_invariant` and `_family` call `paths.states_at` once each; `_currentness_header` names the code
  tree and, when states could not be computed, the reason.
- **Facets.** Every field but the frame (`schema`, `id`, `links`) is returned as recorded;
  this is the backend projection, while display is owned by the reader's `TruthView`.
- **Census.** `census_view` reads the tree's census files (`files.census_files`) through L20's
  `read_censuses` and `census_reports`. An unknown census ID is `not-found`, checked by membership (not by
  mapping a `KeyError`, F11); a read failure is `unavailable`; census file problems are listed.
- **Code (F3).** `code_view` normalises the path, parses the locator first (`_parse_locator`: a JSON object
  with a string `kind`, otherwise `ReaderRequestError`, which answers 400), reads the text (`files.code_text`,
  which answers `absent`, `binary`, `too-large` or `unavailable` without bytes), and resolves the locator with
  L08's `CodeTrees.resolve` against the recorded blob. A well-formed locator that does not resolve is
  `unresolved` with the reason, not an error; a resolved one gives its line span. The answer names the code
  tree and the file's language (`language_for`, the one line worker B added).

### Paged history without eager reacquisition

`record_view` forwards the continuation to `record_timeline` and supplies
`_record_history` as a callback rather than eagerly querying those timeline rows.
A manifest hit avoids that callback; a miss reads the record's rows and, for an
invariant, its membership-subject rows. The invariant's dedicated membership array
still queries membership history independently in `_invariant`, before the timeline
call. This adds paging and defers the timeline callback; it does not claim that a
whole truth-view request performs no history queries or adds another index-completeness
policy.

### Conventions

- The census is computed per request from the tree's files, as L20 suggested; the index skips
  `knowledge/census/`.
- Decision status is stored and derived; `under_reconsideration` is shown as stored (L14's surfacing is not
  duplicated here).

### Invariants And Boundaries

- **Implementation failure handling is not the same as the cited test controls.** `_links_of`
  returns a reason when no model can read the kind or validation fails, and `record_view` adds
  `outgoingState: unavailable`; the outgoing list can still be empty, but it is accompanied by
  the named failure state. `census_view` returns `unavailable` with a detail on a read exception,
  or `not-found` for an unknown ID; `code_view` returns a locator marked `unresolved` with a detail
  when resolution fails. These are implementation branches, not three controls proved by the
  original pair of named tests. [2] [4] [7] [8]
- **Named assertions:** `test_incident_and_facet_views_show_every_field_and_typed_links_both_ways`
  sets `RECORD_MODELS = {}` and asserts unavailable outgoing links.
  `test_the_census_view_shows_measures_and_each_routes_status_history` checks normal census
  measures/history and `wave-9` as `not-found`; it does not stimulate an unreadable census or
  an unresolved locator. [9]
  A separate existing case, `test_bad_requests_are_400_and_large_or_binary_code_is_a_bounded_notice`,
  sends a JSON object with string kind `line_range` but non-integer `start: "x"` and asserts
  `locator.state == "unresolved"`. That is admission of the outer JSON shape, not a fully valid
  line-range operand; the case asserts neither locator detail nor an unreadable census. [12]
- A decision is shown whole in the invariant's linked records and in its own view (the rule carried from L13).
- Nothing here writes.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- One record's truth view carries its links, kind part and timeline, now forwarding a continuation and lazy history callback. [2]
- Invariant and family parts expose their own currentness, entries and locations; the invariant's dedicated membership array queries history independently of the timeline cache. [5]
- Invariant truth retains its dedicated membership projection, while the timeline callback includes membership-subject rows alongside record history. [10]
- Membership projections carry owner, owner kind, closed flag, path, row ID, subject, disposition and document. [11]
- Family/decision/incident/facet assertions, unavailable outgoing links after removing RECORD_MODELS, and normal census measures/history with an unknown-ID control; not an unreadable-census or unresolved-locator control. [9]
- The separate bad-request/code-size case supplies string kind=line_range and non-integer start="x", asserting unresolved locator state rather than locator detail or an unreadable census. [12]

- The module's own statement of the truth views per kind and the census view. [1]
- The kind's own part, and the entries that feed its timeline. [3]
- Outgoing links, or the reason they could not be read (F11). [4]
- Every record by kind. [6]
- MIK-R20's census report; an unknown census by membership. [7]
- A code file at a locator; a malformed locator is a bad request (F3). [8]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
