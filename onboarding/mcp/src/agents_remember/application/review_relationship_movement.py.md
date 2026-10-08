# mcp/src/agents_remember/application/review_relationship_movement.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The **recorded before/after relationship union** of one reviewed subject (`ICR-R08@v1`): the one
traversal that reads what both snapshots record for a realization, a family membership, an advertised
frontier link and the reviewed identity's governing route, and displays each association **with both
of its sides**. It is the direct answer to the packet's non-conforming example — "only the after graph
is read, so the old association vanishes": a realization an author moved from A to B is
`before=(A,)` with `after=B` under one preserved invariant identity, not two unrelated locations.

Three properties are the reason the traversal exists as its own module:

1. **The population is the union the two snapshots record, and the pairing is the author's own
   records.** The union items are the shipped comparison's own page, so a relationship only the
   baseline selected is traversed exactly like one both snapshots hold; the sides are paired by the
   same recorded row or by an authored predecessor edge, never by an address resemblance, a label, a
   version or an insertion order, and every pairing **names the recorded relation it used**
   (`pairing_basis`).
2. **The union is not bounded by the comparison's selected revision page** (the master's ruling on
   this packet). A read selects the revision a relationship cites, not the revisions that succeeded
   it, so an association an author re-recorded onto a successor revision is recorded in the snapshot
   while being outside the page. For every baseline-only side the traversal reads that citation's
   **authored successor line** — every authored descendant, not just its head — through the shipped
   read owners, and it states an association it found there as one movement with both addresses.
3. **An unresolved fact is stated with its reason, never denied.** A line whose ends are several (a
   split that never rejoins) or whose ends are none (a cycle) yields the baseline side displayed as
   it stands plus a gap naming the shape, and the movement's sentence says **what was read** — never
   that no relationship is recorded.

The module is new in `260921-ICR-L8` and exists only in that leaf's uncommitted candidate (branch
`ar/260921-icr-l8`); the verification basis recorded above is the production line at this leaf's base,
`02957762709c9b515b4ff57f7f13524a7c0dfb8d`, because no commit contains the module yet. Closeout owns
the stamp once the code commit exists.

## Code Commentary

### Logic

**`relationship_movements` is the one entry point, and it reads both snapshots under one identity.**
It opens each side's database read-only (`open_read_only_database`), reads that snapshot's own
authored edges through `recorded_snapshot`, traverses the union items, reads the reviewed identity's
governing-route associations through `governing_route_movements`, and closes both connections in a `finally` — so one traversal cannot
read a side under the other snapshot's namespace, and a review that raises cannot leak a database
handle. `RelationshipSources` carries the two snapshots, the reviewed subject, the two bound code
trees and the rename-inference seam as one frozen value, because those are one measurement: a side
read from another snapshot's file, or an inference measured over another pair of trees, would be a
different comparison wearing this one's identity.

**`with_rename_inferences` runs last and only decorates.** The labelled Git inference is attached
*after* the movements exist, over the movements whose recorded addresses differ, and the traversal
never reads it back: no side, identity, transition or association is derived from it.

**`_movements` is the traversal proper.** The candidate's own union is walked first and each of its
relationships is displayed with the baseline sides the author's records connect to it; whatever
baseline side no candidate relationship continues is searched **one step further**, on the authored
successor line, and only what neither read finds is displayed as a one-sided association (a
retraction, or `outside_selection` when the candidate's snapshot holds the row and its declared
selection did not reach it). The stream is then sorted by a declared order — the comparison's own
kind order (revisions, families, memberships, realizations, advertised frontier, then the governing
route last because it is the one association the union does not carry as an item), and inside a kind
the recorded identity, the transition and the displayed addresses — so two runs over the same
snapshots render the same stream.

**`_line_relationships` reads the whole authored line, not its head.** For each baseline-only side it
computes every authored descendant of each citation (`_lines_of`: a realization cites one invariant
revision; a membership cites a family revision **and** a member revision, so it has two lines) and
reads the relationships recorded at every revision of that line, one call per line and per kind,
through the read owner for the kind of revision the line holds. Rows the comparison already selected
are skipped so a record the page holds is never displayed twice; a read the storage owner refuses is
not fatal — the line then records nothing this traversal can display, and the one-sided sentence says
so with its reason, because a review that refused to open would hide every movement it did reach.

**`_pairing_basis` names the relation, and `_is_line_head` keeps one sentence true.** A row read on a
successor line is described as the line's **uniquely established head** only when its own revision is
the head `ICR-R07@v1`'s rule establishes for that line (`successor_line`, called rather than
re-derived); every other line-read row — an intermediate descendant, or a row on a line whose ends are
several — takes the line basis, whose sentence names the line that was read and the revision the row
actually records and says it is not the head. The remaining bases name the recorded relation the
pairing used: the same recorded row selected twice (`same_recorded_relationship`), the same member
revision under a moved family revision (`same_member_revision`), an authored successor step on a
revision or on a member revision, or the family revision an advertised link was recorded against.

**`_continues`/`_replaced` are the pairing rules, and they are deliberately narrow.** Two and only two
things continue a baseline association: the **same recorded relationship row** (both snapshots
selected it, so no edge is needed), or an **authored replacement** where the candidate recorded a new
relationship on a revision whose authored predecessor is the revision the baseline row cited **and**
the baseline row is withdrawn (the candidate records no relationship under that identity any more).
The withdrawal half is what keeps a genuinely new row apart from its surviving siblings. A membership
pairs **member-wise**: the same member revision under a moved family revision is `reassigned`; a
different member continues the association only when the member itself moved along its own authored
line *and* the family revision is the same or a successor — a family edge alone never pairs, which is
how the display stops asserting that one member's association continued another member's row. An
advertised link pairs on the family revision's line, and a realization pairs only on the **strict**
authored-descendant form, so two rows that merely cite the same revision are never one association.

**`_search_of` publishes what a one-sided sentence is allowed to say.** `ContinuationSearch` carries
the candidate relationships the review read, the rows citing the exact same thing (kind-specific:
a realization on its cited revision, a membership on its member revision, an advertised link on its
relationship identity — so a sibling membership holding a different member is never named as this
one), every revision of the citation's lines that was read, the rows found on them, and the line's
shape. A negative stated from anything less than this value is the assertion the first two
verification rounds removed.

### Conventions

`__all__` publishes three names — `RelationshipSources`, `relationship_movements` and the re-exported
`source_locations` (the address view lives in the display module; the pane imports it from here, so
there is one implementation and one import path). `RelationshipSources` is a frozen dataclass, not a
wire shape; the wire vocabulary is `models/knowledge/review_relationships.py`. The module stores
nothing, selects no subject, ranks no relationship and concludes nothing: it opens the two snapshots
read-only, calls ICR-R07's head rule and edge reader, ICR-R04's partition is untouched, and the
comparison's own `coverage`/`change_state`/`reached_via` values are carried rather than recomputed.
The three adjacent responsibilities are their own modules and are called, never re-implemented:
`review_recorded_relationships` (the union items, identity rows and authored edges of one snapshot),
`review_governing_route` (the reviewed identity's route association) and `review_rename_inference`
(the labelled Git inference).

### Invariants And Boundaries

- **One relationship is one value with both sides.** A moved realization is one movement carrying
  every recorded baseline side and the candidate side, under one preserved identity; a withdrawn one
  is one movement with the baseline side and no after side. A pairing always states its basis, and the
  vocabulary refuses a two-sided movement that names none.
- **The union is not the page.** A relationship the candidate's selection did not reach is
  `outside_selection`, never `retracted`, and a row recorded on a successor revision outside the page
  is read and displayed.
- **The pairing is the author's own, and only that.** No similarity, path, label, version or insertion
  order participates; the labelled rename inference is attached beside a movement and is never read
  by the traversal (`review_rename_inference.py`'s own module contract).
- **Every unresolved fact keeps its side, code and reason.** The production path reaches
  `anchor_unresolved` (the read's own resolution detail), `successor_line_unresolved` (a line whose
  ends are several or none) and `predecessor_records_no_relationship` (a candidate row whose recorded
  authored predecessor holds no relationship in the before union), plus the transition
  `outside_selection` and the side states `ungoverned` and `unavailable`; the latter preserves unread route declarations with `route_unavailable`. `anchor_unrecorded`, `identity_differs`,
  `identity_not_recorded` and `route_not_recorded` are **defensive-only**: the value layer keeps them
  for a graph the schema does not currently admit (a claim is fetched with an inner join on its anchor,
  the tree resolver always answers a resolution, the store refuses a cross-identity predecessor edge),
  and no production path reaches them. The whole set is not presented as displayed behaviour.
- **Boundaries.** Mounting `source.relationships` in the browser pane and rendering the labelled
  inference is `ICR-R24`'s; the A06/A07/A24 acceptance journey is `ICR-R25`'s; the dashboard's
  `ReviewSourceLocation`/`ReviewSourcePane` TypeScript mirrors do not carry the new fields yet, so the
  name is a boundary of this leaf and not a claim about the rendered page. The address view's one
  location per `(relationship_id, path)` is the known display consequence recorded below.

### Todos

None recorded. The address-view dedup consequence (`source_locations`, in the display module, keys one
location per recorded relationship and path, so when one old address is a side of two movements that
single location row carries only the first movement in stream order; the complete set is in
`source.relationships`) is routed to `ICR-R24`, which mounts the pane, and is recorded in the
display card's boundaries rather than as work here.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring and
twenty definitions, the three owners it calls, the vocabulary it fills, the adapter that invokes it,
and the three case modules that measure it.

- **The module's own statement of the contract: the union both snapshots record, one value per relationship, the ruling that the page is not the store, and the unresolved-and-not-denied rule.** [1]
- The published surface: the sources value, the traversal and the re-exported address view. [2]
- The declared stream order and why the governing route is last. [3]
- **Everything one traversal reads as one frozen value, because it is one measurement.** [4]

- Both index snapshots feed the authored union and its plural text-route associations. [5]

- **The traversal: candidate sides first, one movement per relationship, the unpaired baseline sides displayed one-sided, the stream in declared order.** [6]
- **The whole authored line is read, not its head, and rows the page already selected are skipped so a record is displayed once.** [7]
- The citations one baseline side's lines are built from — a realization one invariant revision, a membership its family *and* member revisions. [8]
- **Only a row that *is* the line's uniquely established head may be described as one; an intermediate descendant or a multi-ended line takes the line basis.** [9]
- **The tested search value: what was read, what was found on the line, and the shape of the line's ends.** [10]
- **The pairing rules: the same recorded row, or an authored replacement of a withdrawn row; member-wise family pairing; the family edge alone never pairs.** [11]
- The adapter's one call: the union traversed from the comparison's own page items and the resolved dataset halves, threaded into the source pane. [12]
- The wire vocabulary the movements fill, with the validators that refuse an unstated pairing, a transition without its sides and an unexplained absent identity. [13]

- Each text-declared family route is displayed separately; an unread route side is never ungoverned. [14]

- The reach cases the master's ruling required: a member identity's movement at its own established head, a multi-ended line unresolved and never denied, and the address view's qualification. [15]
- The authored-line cases of the third round: a split line that records relationships is named and never denied, a multi-ended line never claims a unique head, and an intermediate descendant is displayed. [16]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The traversal reads the two datasets the
server resolved and the two code trees the comparison bound, all inside one repository namespace.

No applicable cross-repository source was found.
