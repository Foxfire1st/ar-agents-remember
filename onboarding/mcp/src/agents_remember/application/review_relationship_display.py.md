# mcp/src/agents_remember/application/review_relationship_display.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**What one recorded relationship is displayed as** (`ICR-R08@v1`). The traversal module produces the
population; this module renders one relationship of it, and it owns the three things that surround a
movement: **both recorded sides** (each stating which snapshot fact it is — the relationship row and
its address, a row with an unreadable address, an ungoverned identity, or an identity the snapshot
does not record at all), **the unresolved states** (one gap per fact the display could not
establish, each with its side, its code and the read's own reason), and **the pane's address view**
(one location per recorded realization side, each carrying the identity both sides sit under and the
movement it belongs to).

The module exists because the packet's required behaviour is a *display* contract: a moved realization
must show both addresses under one preserved identity, a retraction must stay visible with its deleted
file, and a one-sided movement's sentence may only assert what was actually read. Nothing here selects,
ranks or concludes — the recorded facts are rendered as they are, and no similarity, version, label or insertion order
participates in any of it.

## Code Commentary

### Logic

**`ContinuationSearch` is why a one-sided sentence can be tested rather than believed.** A movement
with one side states why the other side is not there, and those sentences may only say what was read.
The value carries the candidate relationships the review holds and the rows found on what was read;
every sentence below is built from it.

**`paired_movement` builds the two-sided movement.** It renders every baseline side, the candidate
side, the transition (`added` with no baseline side, otherwise from the recorded facts), the pairing
basis and the statement. The statement names the recorded relation the pairing was made on: two rows
are displayed as one association because of *that* relation, never because their addresses look
alike. A candidate row this review read outside its page says so as well, so a reader can tell a
row the comparison selected from one read outside the page.

**`single_sided_movement` keeps the two one-sided facts apart.** A relationship the candidate's
snapshot does not hold at all is `retracted`; one it holds while the declared selection did not reach
it is `outside_selection` and says so in its own sentence — "present but outside the selected scope is
not deletion" as a state of the vocabulary rather than a note a reader has to remember. Its gaps come
from the search value, and the withdrawal statement names what was read rather than
asserting a negative about revisions it did not read.

**`source_locations` is the address view, and it is the pane's own long-standing row shape.** One
location per recorded realization side: the baseline side's location and the candidate's when they are
two recorded relationships or two recorded addresses, and a single location when both snapshots
recorded the same row at the same address. Each location now also carries `invariant_id` (the
preserved identity), `transition`, `recorded_side`, `counterpart_path` (the other side's recorded
address **only when that side records exactly one** — several are listed by the movement and none is
chosen to stand for them) and `movement`. A side whose recorded address could not be read has no
address to list and is not invented: the movement carries that side with its unresolved state and
reason. `_baseline_only` carries the comparison's own coverage as the pane's `before_only`, and
`_location` asserts the two fields the row cannot exist without.

### Conventions

`__all__` publishes exactly four names — `ContinuationSearch`, `paired_movement`,
`single_sided_movement` and `source_locations`; the traversal module re-exports `source_locations` so
the pane has one import path and the address view has one implementation. The gap codes and states
come from the wire vocabulary (`models/knowledge/review_relationships.py`); the pane row type comes
from `models/knowledge/review.py`. The module is pure: it reads no store, opens no connection and
writes nothing — every fact it renders arrives in the `RecordedRelationship` values the traversal
built.

### Invariants And Boundaries

- **A sentence may only say what was read.** Every one-sided sentence is built from
  `ContinuationSearch`, and a negative is asserted only over the revisions that were read.
- **Both sides are displayed, and the identity is preserved.** A movement shows every recorded
  baseline side and the candidate side under one identity; two sides naming different identities
  produce an `identity_differs` gap rather than a silent pairing under one of them.
- **Nothing is chosen for the reader.** `counterpart_path` names an address only when the other side
  records exactly one; a movement with several baseline addresses lists them all, and no single
  address stands for the others.
- **The address view is one location per `(relationship_id, path)`.** When one old address is a side
  of two movements, that single location row carries only the first movement in stream order; the
  complete set is in `source.relationships`. This is a display consequence of the pane's existing
  row-per-address shape, it is recorded here as a boundary rather than as a second implementation, and
  mounting the full set is `ICR-R24`'s.
- **Boundaries.** The gaps the production path reaches are `anchor_unrecorded`,
  `anchor_unresolved`, `identity_not_recorded`, `identity_differs`, `route_not_recorded` and
  `route_unavailable`. Browser
  mounting is `ICR-R24`'s; the A06/A07/A24 journey is `ICR-R25`'s; the family-subject unresolved
  statement side remains `ICR-R09`'s co-owned side.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in source: the module's own docstring and
its definitions, the traversal and read owners it consumes, the wire vocabulary it fills, and
the case modules that measure it.


- **The module's own statement of what it owns: both sides, the unresolved states, the address view, and that nothing here selects, ranks or concludes.** [1]


- The published surface: the search value, the two movement builders and the address view. [2]


- **The tested search value a one-sided sentence must be built from.** [3]


- **The address view: one location per recorded realization side, deduped by relationship and path, each carrying its movement.** [4]


- **The two-sided movement: both recorded sides, the transition from the recorded facts, the pairing basis and the statement that names it.** [5]


- **The one-sided movement: retraction and outside-selection are different states, and the sentence states only what the search read.** [6]


- The side rendering with the fact it states, and the reason a recorded address is unresolved rather than absent. [7]


- **The basis sentence: the recorded relation the pairing was made on, spelled out so resemblance never pairs.** [8]


- **The withdrawal statement: what was read is named, and only an established negative is asserted.** [9]


- The gaps one movement states: paired gaps, per-side gaps, the resolved-anchor gap and the identity difference. [11]


- **An address is named as the counterpart only when the other side records exactly one.** [12]


- The wire vocabulary the display fills: the sides and their states, the gap with its code and reason, and the movement's validators. [13]


- The pane row the address view builds, with the movement carried beside the pane's own long-standing fields. [14]


- The current cases measure retraction without authored-line traversal, no invented unique head, unread further revisions staying outside the union, and withdrawal never denying a relationship the same payload displays. [15]


- The qualification cases: a pairing states the recorded relation it was made on, and an address resemblance never pairs. [16]


### Cross-Repo References

No cross-repository behavior is implemented in this file. It renders values built from the two
snapshots the review compares and one repository namespace.

No applicable cross-repository source was found.
