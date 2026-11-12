# mcp/src/agents_remember/application/review_relationship_display.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**What one recorded relationship is displayed as** (`ICR-R08@v1`). The traversal module produces the
population; this module renders one relationship of it, and it owns the three things that surround a
movement: **both recorded sides** (the current `_side_of` emits `recorded` for a readable anchor and
`unresolved` otherwise; missing identity is a separate gap, not an invented side), **the unresolved states** (one gap per fact the display could not
establish, each with its side, its code and the read's own reason), and **the pane's address view**
(one location per displayed realization side in each movement, each carrying that movement's identity
and movement value; a side shared by movements contributes a location to each).

The module exists because the packet's required behaviour is a *display* contract: a moved realization
must show both addresses under one preserved identity, a retraction must stay visible with its deleted
file, and a one-sided movement's sentence may only assert what was actually read. Nothing here selects,
ranks or concludes — the recorded facts are rendered as they are, and no similarity, version, label or insertion order
participates in any of it.

## Code Commentary

### Logic

**`ContinuationSearch` carries the traversal’s search facts.** Its `candidates` and `same_citation` tuples do not authenticate their own contents. In this display module withdrawal wording reads `same_citation`; outside-selection wording reads the baseline relationship’s coverage. Not every one-sided sentence or gap is computed from the search value.

**`paired_movement` builds the two-sided movement.** It renders every baseline side, the candidate
side, the transition (`added` with no baseline side, otherwise from the recorded facts), the pairing
basis and the statement. The statement names the recorded relation the pairing was made on: two rows
are displayed as one association because of *that* relation, never because their addresses look
alike. The current traversal supplies relationships from the comparison's union page and pairs matching
recorded rows; this builder does not add a separate outside-page qualification.

**`single_sided_movement` keeps the two one-sided facts apart.** A relationship the candidate's
snapshot does not hold at all is `retracted`; one it holds while the declared selection did not reach
it is `outside_selection` and says so in its own sentence — "present but outside the selected scope is
not deletion" as a state of the vocabulary rather than a note a reader has to remember. Its gaps come
from the baseline relationship's side and identity facts. The withdrawal statement uses
`search.same_citation` to name other read rows citing the same thing, or states that none was read;
it does not inspect `search.candidates` directly.

**`source_locations` is the address view, and it is the pane's own long-standing row shape.** One
location per displayed realization side in each movement: the baseline side's location and the candidate's
when they are two recorded relationships or two recorded addresses, and a single location within that
movement when both snapshots recorded the same row at the same address. A side shared by multiple
movements contributes a row to each; there is no cross-movement deduplication. Each location now also carries `invariant_id` (the
preserved identity), `transition`, `recorded_side`, `counterpart_path` (the other side's recorded
address **only when that side records exactly one** — several are listed by the movement and none is
chosen to stand for them) and `movement`. A side whose recorded address could not be read has no
address to list and is not invented: the movement carries that side with its unresolved state and
reason. `_baseline_only` carries the comparison's own coverage as the pane's `before_only`, and
`_location` asserts the two fields the row cannot exist without.

### Conventions

`__all__` publishes exactly four names — `ContinuationSearch`, `paired_movement`,
`single_sided_movement` and `source_locations`; `review_relationship_movement.py` imports and re-exports `source_locations`, so
the pane has one traversal import path and the address view has one implementation. The gap codes and states
come from the wire vocabulary (`models/knowledge/review_relationships.py`); the pane row type comes
from `models/knowledge/review.py`. The module is pure: it reads no store, opens no connection and
writes nothing — every fact it renders arrives in the `RecordedRelationship` values the traversal
built.

### Invariants And Boundaries

- **One-sided wording follows carried facts.** Outside-selection wording uses baseline coverage;
  withdrawal wording uses `ContinuationSearch.same_citation`. The production traversal constructs that
  search from its candidate union relationships. The display does not independently verify the search.
- **Both sides are displayed, and the identity is preserved.** A movement shows every recorded
  baseline side and the candidate side under one identity; two sides naming different identities
  produce an `identity_differs` gap rather than a silent pairing under one of them.
- **Nothing is chosen for the reader.** `counterpart_path` names an address only when the other side
  records exactly one; a movement with several baseline addresses lists them all, and no single
  address stands for the others.
- **The address view preserves each movement's displayed realization sides.** An address shared by
  two movements contributes a location carrying each movement. `_displayed_sides` still omits a
  baseline side matching that movement's after-side relationship and path; sides without paths are
  skipped.

```text
Historical prior address-view boundary, superseded by the current per-movement rows:
- **The address view is one location per `(relationship_id, path)`.** When one old address is a side
  of two movements, that single location row carries only the first movement in stream order; the
  complete set is in `source.relationships`. This is a display consequence of the pane's existing
  row-per-address shape, it is recorded here as a boundary rather than as a second implementation, and
  mounting the full set is `ICR-R24`'s.
```
- **Boundaries.** This display constructs `anchor_unrecorded`, `anchor_unresolved`,
  `identity_not_recorded` and `identity_differs` gaps. The imported wire vocabulary additionally admits
  `route_not_recorded` and `route_unavailable`; their production reachability belongs to the separate
  governing-route owner. Browser
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


- The published surface: the search value, the two movement builders and the address view. [2]


- **The two-sided movement: both recorded sides, the transition from the recorded facts, the pairing basis and the statement that names it.** [5]


- The side rendering with the fact it states, and the reason a recorded address is unresolved rather than absent. [7]


- **The basis sentence: the recorded relation the pairing was made on, spelled out so resemblance never pairs.** [8]


- **The withdrawal statement: what was read is named, and only an established negative is asserted.** [9]


- The gaps one movement states: paired gaps, per-side gaps, the resolved-anchor gap and the identity difference. [11]


- **An address is named as the counterpart only when the other side records exactly one.** [12]


- The wire vocabulary the display fills: the sides and their states, the gap with its code and reason, and the movement's validators. [13]


### Cross-Repo References

No cross-repository behavior is implemented in this file. It renders values built from the two
snapshots the review compares and one repository namespace.

No applicable cross-repository source was found.

- ContinuationSearch is a frozen dataclass carrying candidates and same_citation. Withdrawal wording reads same_citation; outside-selection wording uses the baseline relationship and coverage instead. The traversal constructs the search from candidate union relationships. This value does not validate that its contents were actually read. [3]
- source_locations iterates realization movements and appends a location for every displayed side with a path, without a cross-movement seen set. _displayed_sides preserves before-then-after order and omits baseline sides matching that movement's after-side relationship and path; it does not deduplicate baseline sides against each other. _location preserves the pane fields and carries identity, transition, recorded side, counterpart path and the movement. [4]
- ReviewSourceLocation and ReviewSourcePane are implemented in review_source.py and imported/re-exported by review.py. The location retains address, claim, revision, role, rationale, source identities, resolution, change state, baseline coverage and reached-via fields, plus movement identity, transition, side, counterpart and movement. The pane independently carries inventory, locations and relationships alongside attribution and unresolved fields. These are DTO fields, not a claim that every field is rendered. [14]
- The current traversal owner imports source_locations from review_relationship_display and publishes it through __all__. Its _movements reads both snapshots' union relationships, pairs matching recorded rows, and builds one-sided movements for unmatched baseline sides. The absent old review_relationships.py path does not imply deletion of this behavior. [17]
- The module exposes movement display and address projection without opening a store or choosing the traversal population. Its current _side_of emits recorded or unresolved side states from anchor readability, with missing identity represented separately by a gap. Broader side descriptions in the inherited module docstring are not a claim that this builder emits every wire state. [1]
- single_sided_movement uses the baseline item_coverage to distinguish outside_selection from retracted and derives gaps from that side. Outside-selection wording reads baseline facts; withdrawal wording consumes same_citation from the supplied search. The display does not independently authenticate that search. [6]
- Stored assertions cover exact retraction wording, no invented unique head, outside-union exclusions and naming the same-citation relationship the payload also displays. These complete test bodies were inspected statically; no fresh execution, fixture provenance or review grade is inferred. [15]
- Stored assertions require recorded pairing bases and leave address resemblance unpaired. These complete test bodies were inspected statically; no fresh execution, fixture provenance or review grade is inferred. [16]
