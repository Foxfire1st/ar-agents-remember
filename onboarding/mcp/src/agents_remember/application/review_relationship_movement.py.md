# mcp/src/agents_remember/application/review_relationship_movement.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_relationship_movement.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T19:40:00+02:00 |
| lastVerifiedCommitHash | `dcf35a0e0fc06bccdafd22390b7588b0aea811bc` |
| lastVerifiedCommitDate | 2026-09-22T20:08:58+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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
governing-route association, and closes both connections in a `finally` — so one traversal cannot
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
  `outside_selection` and the side state `ungoverned`. `anchor_unrecorded`, `identity_differs`,
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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring and
twenty definitions, the three owners it calls, the vocabulary it fills, the adapter that invokes it,
and the three case modules that measure it.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the contract: the union both snapshots record, one value per relationship, the ruling that the page is not the store, and the unresolved-and-not-denied rule.** | `relationship_movements` | mcp/src/agents_remember/application/review_relationship_movement.py:1-58; mcp/src/agents_remember/application/review_relationship_movement.py:142-177 |
| The published surface: the sources value, the traversal and the re-exported address view. | `__all__` | mcp/src/agents_remember/application/review_relationship_movement.py:101-105 |
| The declared stream order and why the governing route is last. | `_KIND_ORDER` | mcp/src/agents_remember/application/review_relationship_movement.py:107-120 |
| **Everything one traversal reads as one frozen value, because it is one measurement.** | `RelationshipSources` | mcp/src/agents_remember/application/review_relationship_movement.py:123-139 |
| **The one entry point: both snapshots opened read-only and closed in a `finally`, the union traversal, the route movement, and the labelled inference attached last.** | `relationship_movements`; `open_read_only_database`; `recorded_snapshot`; `governing_route_movement`; `with_rename_inferences` | mcp/src/agents_remember/application/review_relationship_movement.py:142-177; mcp/src/agents_remember/application/review_recorded_relationships.py:145-160; mcp/src/agents_remember/application/review_governing_route.py:59-93; mcp/src/agents_remember/application/review_rename_inference.py:155-177; mcp/src/agents_remember/memory/knowledge/connection.py:52-63 |
| **The traversal: candidate sides first, one movement per relationship, the unpaired baseline sides displayed one-sided, the stream in declared order.** | `_movements`; `read_snapshot_relationships`; `paired_movement`; `single_sided_movement`; `_movement_order` | mcp/src/agents_remember/application/review_relationship_movement.py:183-224; mcp/src/agents_remember/application/review_relationship_movement.py:471-480; mcp/src/agents_remember/application/review_relationship_movement.py:107-139; mcp/src/agents_remember/application/review_recorded_relationships.py:458-475; mcp/src/agents_remember/application/review_relationship_display.py:107-139; mcp/src/agents_remember/application/review_relationship_display.py:142-174 |
| **The whole authored line is read, not its head, and rows the page already selected are skipped so a record is displayed once.** | `_line_relationships`; `_ids` | mcp/src/agents_remember/application/review_relationship_movement.py:227-274; mcp/src/agents_remember/application/review_relationship_movement.py:357-360 |
| The citations one baseline side's lines are built from — a realization one invariant revision, a membership its family *and* member revisions. | `_line_citations`; `_lines_of`; `_line_revisions` | mcp/src/agents_remember/application/review_relationship_movement.py:277-292; mcp/src/agents_remember/application/review_relationship_movement.py:321-346; mcp/src/agents_remember/application/review_relationship_movement.py:349-354 |
| **Only a row that *is* the line's uniquely established head may be described as one; an intermediate descendant or a multi-ended line takes the line basis.** | `_is_line_head`; `_pairing_basis`; `successor_line` | mcp/src/agents_remember/application/review_relationship_movement.py:295-318; mcp/src/agents_remember/application/review_relationship_movement.py:439-468; mcp/src/agents_remember/application/review_recorded_relationships.py:233-292 |
| **The tested search value: what was read, what was found on the line, and the shape of the line's ends.** | `_search_of`; `_same_citation` | mcp/src/agents_remember/application/review_relationship_movement.py:363-402; mcp/src/agents_remember/application/review_relationship_movement.py:405-436 |
| **The pairing rules: the same recorded row, or an authored replacement of a withdrawn row; member-wise family pairing; the family edge alone never pairs.** | `_matching`; `_continues`; `_replaced`; `authored_successor` | mcp/src/agents_remember/application/review_relationship_movement.py:491-515; mcp/src/agents_remember/application/review_relationship_movement.py:518-541; mcp/src/agents_remember/application/review_relationship_movement.py:544-580; mcp/src/agents_remember/application/review_recorded_relationships.py:220-230 |
| The adapter's one call: the union traversed from the comparison's own page items and the resolved dataset halves, threaded into the source pane. | `compose_review` | mcp/src/agents_remember/application/knowledge_review.py:300-412 |
| The wire vocabulary the movements fill, with the validators that refuse an unstated pairing, a transition without its sides and an unexplained absent identity. | `ReviewRelationshipMovement`; `ReviewRelationshipSide`; `ReviewPairingBasis`; `ReviewRelationshipGap` | mcp/src/agents_remember/models/knowledge/review_relationships.py:258-372; mcp/src/agents_remember/models/knowledge/review_relationships.py:153-201; mcp/src/agents_remember/models/knowledge/review_relationships.py:126-135; mcp/src/agents_remember/models/knowledge/review_relationships.py:138-150 |
| **The eleven cases that measure the packet's own behaviour: the moved realization, the after-only reading falsified, the withdrawn realization, outside-selection, the labelled rename inference, no fabricated movement, authored split and merge, family reassignment, route reassignment, the ungoverned identity, and the unresolved anchor.** | `test_a_moved_realization_displays_both_recorded_paths_under_one_invariant_identity`; `test_only_the_after_graph_is_read_so_the_old_association_vanishes`; `test_a_withdrawn_realization_stays_visible_with_its_deleted_file_and_its_identity`; `test_a_record_the_other_selection_did_not_reach_is_not_displayed_as_a_deletion`; `test_a_source_rename_is_displayed_as_a_labelled_git_inference`; `test_the_same_rename_with_no_authored_edge_is_a_retraction_and_an_addition`; `test_the_authored_split_and_merge_are_displayed_from_the_candidates_own_edges`; `test_a_family_association_reassigned_to_a_new_revision_displays_both_recorded_sides`; `test_a_governing_route_reassignment_displays_both_recorded_routes`; `test_an_identity_with_no_route_is_displayed_as_ungoverned_and_never_as_the_root`; `test_a_side_that_did_not_resolve_exactly_keeps_its_own_state_and_reason` | mcp/tests/test_knowledge_review_relationship_movement.py:447-494; mcp/tests/test_knowledge_review_relationship_movement.py:497-528; mcp/tests/test_knowledge_review_relationship_movement.py:531-570; mcp/tests/test_knowledge_review_relationship_movement.py:573-601; mcp/tests/test_knowledge_review_relationship_movement.py:607-637; mcp/tests/test_knowledge_review_relationship_movement.py:675-717; mcp/tests/test_knowledge_review_relationship_movement.py:723-753; mcp/tests/test_knowledge_review_relationship_movement.py:759-800; mcp/tests/test_knowledge_review_relationship_movement.py:803-826; mcp/tests/test_knowledge_review_relationship_movement.py:829-857; mcp/tests/test_knowledge_review_relationship_movement.py:860-891 |
| The reach cases the master's ruling required: a member identity's movement at its own established head, a multi-ended line unresolved and never denied, and the address view's qualification. | `test_a_member_identities_moved_realization_is_displayed_at_its_own_head`; `test_a_member_line_with_no_single_head_is_unresolved_and_never_denied`; `test_a_pairing_is_qualified_and_an_address_resemblance_never_pairs` | mcp/tests/test_knowledge_review_relationship_reach.py:305-357; mcp/tests/test_knowledge_review_relationship_reach.py:360-389; mcp/tests/test_knowledge_review_relationship_reach.py:503-541 |
| The authored-line cases of the third round: a split line that records relationships is named and never denied, a multi-ended line never claims a unique head, and an intermediate descendant is displayed. | `test_a_split_line_that_records_relationships_names_them_and_never_denies`; `test_a_multi_head_line_with_relationships_never_claims_a_unique_head`; `test_a_relationship_on_an_intermediate_descendant_is_displayed` | mcp/tests/test_knowledge_review_relationship_line.py:211-263; mcp/tests/test_knowledge_review_relationship_line.py:266-291; mcp/tests/test_knowledge_review_relationship_line.py:316-350 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The traversal reads the two datasets the
server resolved and the two code trees the comparison bound, all inside one repository namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`, confirmed from the enclosure contract): **created.** The module is new in this leaf (`ICR-R08@v1`) and this is its one-to-one card. It records the traversal contract the packet states and the leaf's four adversarial verification rounds hardened: the recorded before/after union rather than the candidate's graph; pairing only by the author's own records with the basis named on every paired movement; the ruling that the union is not bounded by the comparison's selected revision page, implemented by reading the **whole** authored successor line through ICR-R07's head rule and owner-keyed reads; unresolved sides stated with their code and reason and never denied; and the labelled Git rename inference attached after the fact and never read back. It also records the reachability truth measured for this packet — the production path reaches `anchor_unresolved`, `successor_line_unresolved`, `predecessor_records_no_relationship`, the transition `outside_selection` and the state `ungoverned`, while `anchor_unrecorded`, `identity_differs`, `identity_not_recorded` and `route_not_recorded` are defensive-only — and the `source_locations` one-location-per-address consequence routed to `ICR-R24`. **Basis accounting:** the verification pair above names this leaf's base, the last real commit the reading was taken against, because the module exists only in this leaf's uncommitted candidate; the candidate is named here in the body rather than in a metadata row, and closeout owns the stamp once the code commit exists.
