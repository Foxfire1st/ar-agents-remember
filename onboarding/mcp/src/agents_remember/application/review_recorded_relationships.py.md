# mcp/src/agents_remember/application/review_recorded_relationships.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_recorded_relationships.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T19:40:00+02:00 |
| lastVerifiedCommitHash | `dcf35a0e0fc06bccdafd22390b7588b0aea811bc` |
| lastVerifiedCommitDate | 2026-09-22T20:08:58+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The relationships one snapshot's union items record, read from that snapshot** (`ICR-R08@v1`). The
traversal that displays the recorded before/after union needs three facts per side, and this module
owns all three: the shipped comparison's own union items (each carrying the side payload that selected
it), the identity each association revision belongs to — read from the snapshot's own revision rows,
because the selection read does not project it — and the snapshot's own authored predecessor edges.

It also owns the **reach** the master's ruling established: a relationship's own authored line, read
through the shipped owners. A read selects the revision a relationship cites and not the revisions
that succeeded it, so an association an author re-recorded onto a successor revision is recorded in
the snapshot while being outside the comparison's page. `successor_line` states one revision's
authored successor line — its ends, and the unique head when there is one — by **ICR-R07@v1's own head
rule** (`revision_heads`, called rather than re-derived), and `read_line_relationships` reads the
relationships recorded at **every** revision of that line, so a row read here carries the same
observation vocabulary as a selected one and a negative about a line can be complete.

Nothing here selects, pairs or concludes. The module is new in `260921-ICR-L8` and exists only in that
leaf's uncommitted candidate (branch `ar/260921-icr-l8`); the verification basis recorded above is the
production line at this leaf's base, `02957762709c9b515b4ff57f7f13524a7c0dfb8d`. Closeout owns the
stamp once the code commit exists.

## Code Commentary

### Logic

**`recorded_snapshot` holds one snapshot's own edges beside its file and connection.** The edge reader
is ICR-R07's `read_snapshot_edges`, called rather than re-implemented: it reads both predecessor
tables of one snapshot through its own read-only connection, which is the one implementation of "the
authored old/new relations this snapshot records".

**`successor_line` is the head rule, and it keeps three outcomes apart.** No recorded successor at all
is `state="none"` with a sentence saying the revision is the end of its own authored line; exactly one
revision of the line that no other revision names as its predecessor is `state="established"` with its
`head_revision_id`; several such revisions (a split that never rejoins) and none (a cycle) are both
`state="unresolved"`, each with the sentence that says which shape it is and, for a split, **every**
candidate end. A caller that cannot name a head therefore states the reason instead of denying that a
relationship is recorded — the correction the second and third verification rounds required.
`authored_descendants` walks the snapshot's own `(successor, predecessor)` edges outwards and visits
each revision once, so a cycle in a corrupted graph cannot spin; `authored_ancestor`/`authored_successor`
are the same walk in predicate form, the strict one being the form a pairing asks for.

**`read_snapshot_relationships` reads one snapshot's union items as recorded sides.** Only the three
relationship kinds are read (`_RELATIONSHIP_KINDS`: realization, membership, advertised frontier link —
a revision item is not a relationship, it is one of the two things a relationship relates), and each
side is read through `_relationship` with the identity index resolved first (`_identity_index` reads
the invariant and family revision rows of exactly the revisions the payloads name, so the identity
displayed is the one the snapshot records rather than one inferred from the item's shape).

**`read_line_relationships` is the reach, and it reads the whole line.** Each kind is read by the owner
that owns it: realizations through `fetch_realizations_for_invariants` with the same anchor seam a
selected row uses (`head_anchor_resolver`, built from that side's own dataset identity and bound tree),
and family memberships through `fetch_memberships_of_families_full`, the owner keyed by the **family**
revision. A membership's member side is a line of invariant revisions too, so both of its lines are
read and a membership recorded on either is found. `RelationshipLine` carries the kind with the ids
because the kind is what selects the read owner — asking the invariant-revision owner for a family
revision is how a whole branch of this reach came to read nothing (the second round's F2 finding).

**A row read on a line carries its own origin and the identity of its revision.** `origin` is
`selection` for a side of the comparison's own union item and `successor_head` for a row read on an
authored line outside the page; both are recorded facts of the same snapshot, and the display states
the difference rather than blurring it. `_line_realization` and `_line_membership` resolve the
association's identity from the snapshot's own revision row, and a row whose anchor the read could not
resolve keeps `anchor_readable=False` with the reason, exactly as a selected row does.

**`recorded_change_state` carries the comparison's own statement verbatim.** It is the moved-out
`_change_state`: `not_selected` when the union item carries no source observation, `changed` when the
observation changed or the change is source-only, `unchanged` otherwise. Nothing here re-derives it.

### Conventions

`__all__` publishes thirteen names — the two read dataclasses and the edge/line vocabulary plus the
readers the traversal and the route module consume (`authored_ancestor`, `authored_successor`,
`head_anchor_resolver`, `read_line_relationships`, `read_snapshot_relationships`,
`recorded_change_state`, `recorded_snapshot`, `side_payload`, `successor_line`). `RecordedSnapshot`,
`RecordedRelationship`, `RecordedIdentityIndex`, `SuccessorLine` and `RelationshipLine` are frozen
dataclasses, not wire shapes. The module reads: it opens no connection of its own (the caller passes
one), writes nothing, and calls the shipped read owners and ICR-R07's head rule instead of declaring a
second implementation of either.

### Invariants And Boundaries

- **The identity is read, never guessed.** An association's identity comes from the snapshot's own
  revision rows; a row read at a successor head resolves the same way, because the movement is
  displayed *under* that identity.
- **The line's head is ICR-R07's, and an unresolved line states its reason.** No second head rule
  exists here, and a multi-ended or cyclic line is `unresolved` with its shape and its candidate ends.
- **The whole line is read.** A relationship recorded at an intermediate descendant is displayed, and
  a negative the display states is complete over the revisions that were read.
- **The owner is chosen by the kind of revision, not by convenience.** Realizations read by invariant
  revision; memberships by family revision *and* by member revision; a sibling membership holding a
  different member is never this association's record.
- **Boundaries.** Pairing, transitions and display sentences belong to the traversal and display
  modules; the comparison's own selection, coverage and change state are carried, never recomputed;
  Git rename detection is `review_rename_inference.py`'s and is not consulted here.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring and
twenty-three definitions, the shipped read owners and ICR-R07 rule it calls, the traversal that
consumes it, and the cases that measure the reach.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the three facts it owns and of the reach: the page is not the store, the whole line is read, and the owner is chosen by the kind of revision.** | `successor_line` | mcp/src/agents_remember/application/review_recorded_relationships.py:1-59; mcp/src/agents_remember/application/review_recorded_relationships.py:233-292 |
| The published surface: the read values and the readers the traversal and route modules consume. | `__all__` | mcp/src/agents_remember/application/review_recorded_relationships.py:61-75 |
| One snapshot as this traversal reads it: its side name, its file, its connection and its own authored edges. | `RecordedSnapshot`; `recorded_snapshot`; `read_snapshot_edges` | mcp/src/agents_remember/application/review_recorded_relationships.py:95-101; mcp/src/agents_remember/application/review_recorded_relationships.py:145-160; mcp/src/agents_remember/application/review_revision_comparison.py:97-110 |
| **One recorded side, with the origin that says which read produced it and the identity its revision belongs to.** | `RecordedRelationship`; `RecordedIdentityIndex` | mcp/src/agents_remember/application/review_recorded_relationships.py:105-134; mcp/src/agents_remember/application/review_recorded_relationships.py:138-142 |
| **The head rule: no successor, one established head, or an unresolved line with its shape and its candidate ends — never a denial that a relationship is recorded.** | `SuccessorLine`; `successor_line`; `revision_heads` | mcp/src/agents_remember/application/review_recorded_relationships.py:164-178; mcp/src/agents_remember/application/review_recorded_relationships.py:233-292; mcp/src/agents_remember/application/review_revision_comparison.py:81-94 |
| The authored walk: every descendant, visited once, and the ancestor/successor predicates the pairing uses. | `authored_descendants`; `authored_ancestor`; `authored_successor` | mcp/src/agents_remember/application/review_recorded_relationships.py:181-198; mcp/src/agents_remember/application/review_recorded_relationships.py:201-217; mcp/src/agents_remember/application/review_recorded_relationships.py:220-230 |
| **The line read: the kind selects the owner, realizations by invariant revision and memberships by family revision, and the whole line is read.** | `RelationshipLine`; `read_line_relationships`; `fetch_realizations_for_invariants`; `fetch_memberships_of_families_full` | mcp/src/agents_remember/application/review_recorded_relationships.py:296-306; mcp/src/agents_remember/application/review_recorded_relationships.py:309-339; mcp/src/agents_remember/memory/knowledge/read_queries.py:263-297; mcp/src/agents_remember/memory/knowledge/read_queries.py:153-175 |
| The anchor seam one side's exact code tree asks for, so a line-read row carries the same resolution vocabulary as a selected one. | `head_anchor_resolver` | mcp/src/agents_remember/application/review_recorded_relationships.py:342-359 |
| One realization and one membership read on a successor line, each resolving its identity from the snapshot's own revision row. | `_line_realization`; `_line_membership`; `_revision_identity` | mcp/src/agents_remember/application/review_recorded_relationships.py:376-409; mcp/src/agents_remember/application/review_recorded_relationships.py:412-449; mcp/src/agents_remember/application/review_recorded_relationships.py:362-373 |
| **The union-item read: the three relationship kinds, the identity index built from the snapshot's own revision rows, and the payload read as one recorded side.** | `read_snapshot_relationships`; `_identity_index`; `_relationship`; `side_payload` | mcp/src/agents_remember/application/review_recorded_relationships.py:458-475; mcp/src/agents_remember/application/review_recorded_relationships.py:478-518; mcp/src/agents_remember/application/review_recorded_relationships.py:521-561; mcp/src/agents_remember/application/review_recorded_relationships.py:452-455; mcp/src/agents_remember/application/review_recorded_relationships.py:87-91 |
| The comparison's own statement about a claim's source observation, carried verbatim. | `recorded_change_state` | mcp/src/agents_remember/application/review_recorded_relationships.py:593-603 |
| The traversal that consumes this module and the member-wise pairing rule built on its predicates. | `relationship_movements`; `_line_relationships`; `_replaced` | mcp/src/agents_remember/application/review_relationship_movement.py:142-177; mcp/src/agents_remember/application/review_relationship_movement.py:227-274; mcp/src/agents_remember/application/review_relationship_movement.py:544-580 |
| **The cases that measure the reach: the member identity's movement at its own head, the multi-ended line unresolved and never denied, the family head read through the family owner with no sibling mis-named, and a membership moved onto an unselected family revision.** | `test_a_member_identities_moved_realization_is_displayed_at_its_own_head`; `test_a_member_line_with_no_single_head_is_unresolved_and_never_denied`; `test_a_family_revision_that_keeps_its_members_displays_each_membership_once`; `test_a_membership_moved_onto_an_unselected_family_revision_is_displayed` | mcp/tests/test_knowledge_review_relationship_reach.py:305-357; mcp/tests/test_knowledge_review_relationship_reach.py:360-389; mcp/tests/test_knowledge_review_relationship_reach.py:435-469; mcp/tests/test_knowledge_review_relationship_line.py:353-405 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one repository's two datasets
through their own owners and carries no identity beyond that repository namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`, confirmed from the enclosure contract): **created.** The module is new in this leaf (`ICR-R08@v1`) and this is its one-to-one card. It records the read contract and the master's ruling as implemented: the identity of every association revision is read from the snapshot's own rows; the head of an authored line is ICR-R07's rule, called rather than re-derived; the **whole** line is read (the third round's F3), so an intermediate descendant is found and a negative is complete over what was read; and the family side is read through the family-revision owner while a membership contributes both of its lines (the second round's F2). It also records that a row read outside the comparison's page carries its own origin, and that the comparison's change state is carried verbatim by `recorded_change_state`. **Basis accounting:** the verification pair above names this leaf's base, the last real commit the reading was taken against; the candidate is named here in the body rather than in a metadata row, and closeout owns the stamp once the code commit exists.
