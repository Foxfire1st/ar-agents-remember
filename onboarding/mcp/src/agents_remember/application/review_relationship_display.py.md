# mcp/src/agents_remember/application/review_relationship_display.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_relationship_display.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T19:40:00+02:00 |
| lastVerifiedCommitHash | `2edad477bcd9127a90e4618d345ce34ef7e6a6d9` |
| lastVerifiedCommitDate | 2026-09-23T00:33:19+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**What one recorded relationship is displayed as** (`ICR-R08@v1`). The traversal module produces the
population; this module renders one relationship of it, and it owns the three things that surround a
movement: **both recorded sides** (each stating which snapshot fact it is), **the authored lineage and
the unresolved states** (a succession, a split, a merge, and one gap per fact the display could not
establish, each with its side, its code and the read's own reason), and **the pane's address view**
(one location per recorded realization side, each carrying the identity both sides sit under and the
movement it belongs to).

The module exists because the packet's required behaviour is a *display* contract: a moved realization
must show both addresses under one preserved identity, a retraction must stay visible with its deleted
file, and a one-sided movement's sentence may only assert what was actually read. Nothing here selects,
ranks or concludes — the recorded facts are rendered as they are, a movement the author's edges do not
connect stays two one-sided movements, and no similarity, version, label or insertion order
participates in any of it.

The module is new in `260921-ICR-L8` and exists only in that leaf's uncommitted candidate (branch
`ar/260921-icr-l8`); the verification basis recorded above is the production line at this leaf's base,
`02957762709c9b515b4ff57f7f13524a7c0dfb8d`. Closeout owns the stamp once the code commit exists.

## Code Commentary

### Logic

**`ContinuationSearch` is why a one-sided sentence can be tested rather than believed.** A movement
with one side states why the other side is not there, and those sentences may only say what was read.
The value carries the candidate relationships the review holds, the rows that cite the exact same
thing, **every revision of the citation's authored lines that was read** and the rows found on them,
and the line's shape — its ends, and the unique head when there is one. The first two verification
rounds failed this leaf on sentences that outran this value, and the third on a sentence that named a
head the value did not establish; every sentence below is now built from it.

**`paired_movement` builds the two-sided movement.** It renders every baseline side, the candidate
side, the transition (`unchanged` when the candidate recorded the same address, role, rationale and
revision; `reassigned` when a non-realization association kept its member revision under a moved
family revision; `moved` otherwise), the authored lineage, the paired gaps and the statement. The
statement names both recorded associations, the identity they sit under, and the **basis sentence** —
the recorded relation the pairing used, read from a table (`_BASIS_SENTENCES`) so a basis added to the
vocabulary is a row rather than another branch. The `authored_successor_head_revision` sentence is
chosen only for a row that *is* the line's uniquely established head; every other line-read row takes
`authored_successor_line_revision`, whose sentence names the line this review read and the revision
the row actually records and says that it is not the line's head.

**`single_sided_movement` keeps the two one-sided facts apart.** A relationship the candidate's
snapshot does not hold at all is `retracted`; one it holds while the declared selection did not reach
it is `outside_selection` and says so in its own sentence — "present but outside the selected scope is
not deletion" as a state of the vocabulary rather than a note a reader has to remember. Its gaps come
from the search value, and the withdrawal statement is a four-state sentence (the same-citation rows
this review read are **named**, the line's rows are named, a non-unique head is stated as unresolved
with its shape, and only a negative the reads establish is asserted).

**`_lineage`/`_withdrawal_lineage` read the author's own edges.** A succession (one revision naming a
predecessor), a split (several recorded successors) and a merge (several recorded predecessors) are
read from the snapshots' own predecessor tables; the lineage statement names every successor the
author recorded, and the withdrawal lineage states what this review read on the line rather than
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
  `ContinuationSearch`; a candidate row citing the same thing is named, a line's rows are named, and a
  negative is asserted only over the revisions that were read.
- **A head is named only when it is one.** The head basis requires the row's own revision to be the
  head ICR-R07's rule establishes; an intermediate descendant and a multi-ended line both take the
  line basis, and a multi-ended line yields `successor_line_unresolved` with its shape.
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
- **Boundaries.** The gaps the production path reaches are `anchor_unresolved`,
  `successor_line_unresolved` and `predecessor_records_no_relationship`; `anchor_unrecorded`,
  `identity_differs`, `identity_not_recorded` and `route_not_recorded` are defensive-only (the store
  the schema admits cannot produce them), so they are not presented as displayed behaviour. Browser
  mounting is `ICR-R24`'s; the A06/A07/A24 journey is `ICR-R25`'s; the family-subject unresolved
  statement side remains `ICR-R09`'s co-owned side.

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
thirty-one definitions, the traversal and read owners it consumes, the wire vocabulary it fills, and
the case modules that measure it.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of what it owns: both sides, the lineage and unresolved states, the address view, and that nothing here selects, ranks or concludes.** | `paired_movement` | mcp/src/agents_remember/application/review_relationship_display.py:1-20; mcp/src/agents_remember/application/review_relationship_display.py:107-139 |
| The published surface: the search value, the two movement builders and the address view. | `__all__` | mcp/src/agents_remember/application/review_relationship_display.py:42-47 |
| **The tested search value a one-sided sentence must be built from.** | `ContinuationSearch` | mcp/src/agents_remember/application/review_relationship_display.py:51-73 |
| **The address view: one location per recorded realization side, deduped by relationship and path, each carrying its movement.** | `source_locations`; `_displayed_sides`; `_location` | mcp/src/agents_remember/application/review_relationship_display.py:76-104; mcp/src/agents_remember/application/review_relationship_display.py:769-788; mcp/src/agents_remember/application/review_relationship_display.py:791-821 |
| **The two-sided movement: both recorded sides, the transition from the recorded facts, the authored lineage, the paired gaps and the statement that names its basis.** | `paired_movement`; `_transition`; `_paired_statement` | mcp/src/agents_remember/application/review_relationship_display.py:107-139; mcp/src/agents_remember/application/review_relationship_display.py:260-283; mcp/src/agents_remember/application/review_relationship_display.py:286-316 |
| **The one-sided movement: retraction and outside-selection are different states, and the sentence states only what the search read.** | `single_sided_movement`; `_outside_selection_statement` | mcp/src/agents_remember/application/review_relationship_display.py:142-174; mcp/src/agents_remember/application/review_relationship_display.py:202-209 |
| The side rendering with the fact it states, and the reason a recorded address is unresolved rather than absent. | `_side_of`; `_side_detail` | mcp/src/agents_remember/application/review_relationship_display.py:177-199; mcp/src/agents_remember/application/review_relationship_display.py:244-257 |
| **The basis table: one recorded relation per basis, with the head basis reserved for a row that is the line's uniquely established head.** | `_basis_sentence`; `_BasisSentence`; `_BASIS_SENTENCES` | mcp/src/agents_remember/application/review_relationship_display.py:319-344; mcp/src/agents_remember/application/review_relationship_display.py:347-351; mcp/src/agents_remember/application/review_relationship_display.py:354-387 |
| **The four-state withdrawal sentence: the same-citation rows named, the line's rows named, a non-unique head stated unresolved, only an established negative asserted.** | `_withdrawal_statement`; `_single_sided_gaps` | mcp/src/agents_remember/application/review_relationship_display.py:398-458; mcp/src/agents_remember/application/review_relationship_display.py:212-241 |
| The authored lineage: succession, split and merge read from the snapshots' own predecessor rows, and the withdrawal lineage that states what was read. | `_lineage`; `_add_succession`; `_add_split`; `_add_merge`; `_withdrawal_lineage`; `_successors`; `_predecessors` | mcp/src/agents_remember/application/review_relationship_display.py:511-532; mcp/src/agents_remember/application/review_relationship_display.py:535-556; mcp/src/agents_remember/application/review_relationship_display.py:559-580; mcp/src/agents_remember/application/review_relationship_display.py:583-602; mcp/src/agents_remember/application/review_relationship_display.py:605-645; mcp/src/agents_remember/application/review_relationship_display.py:495-500; mcp/src/agents_remember/application/review_relationship_display.py:503-508 |
| The gaps one movement states: paired gaps, per-side gaps, the resolved-anchor gap, the identity difference and the recorded predecessor that holds no relationship. | `_paired_gaps`; `_side_gaps`; `_side_gap`; `_identity_gaps`; `_unpaired_predecessor_gaps`; `_identity_unresolved_gap` | mcp/src/agents_remember/application/review_relationship_display.py:648-663; mcp/src/agents_remember/application/review_relationship_display.py:666-681; mcp/src/agents_remember/application/review_relationship_display.py:684-711; mcp/src/agents_remember/application/review_relationship_display.py:714-734; mcp/src/agents_remember/application/review_relationship_display.py:737-763; mcp/src/agents_remember/application/review_relationship_display.py:461-473 |
| **An address is named as the counterpart only when the other side records exactly one.** | `_counterpart_path`; `_other_side`; `_baseline_only` | mcp/src/agents_remember/application/review_relationship_display.py:835-848; mcp/src/agents_remember/application/review_relationship_display.py:851-858; mcp/src/agents_remember/application/review_relationship_display.py:824-832 |
| The wire vocabulary the display fills: the sides and their states, the lineage, the gap with its code and reason, and the movement's validators. | `ReviewRelationshipSide`; `ReviewAuthoredLineage`; `ReviewRelationshipGap`; `ReviewRelationshipMovement` | mcp/src/agents_remember/models/knowledge/review_relationships.py:153-201; mcp/src/agents_remember/models/knowledge/review_relationships.py:204-218; mcp/src/agents_remember/models/knowledge/review_relationships.py:138-150; mcp/src/agents_remember/models/knowledge/review_relationships.py:258-372 |
| The pane row the address view builds, with the movement carried beside the pane's own long-standing fields. | `ReviewSourceLocation`; `ReviewSourcePane` | mcp/src/agents_remember/models/knowledge/review.py:95-95; mcp/src/agents_remember/models/knowledge/review.py:96-96 |
| **The cases that measure the displayed sentences: the split line that names its rows, the multi-ended line that never claims a head, the split that records nothing, the intermediate descendant, and the withdrawal that never denies what the same payload displays.** | `test_a_split_line_that_records_relationships_names_them_and_never_denies`; `test_a_multi_head_line_with_relationships_never_claims_a_unique_head`; `test_a_split_line_that_records_nothing_states_only_what_was_read`; `test_a_relationship_on_an_intermediate_descendant_is_displayed`; `test_a_withdrawal_never_denies_a_relationship_the_same_payload_displays` | mcp/tests/test_knowledge_review_relationship_line.py:211-263; mcp/tests/test_knowledge_review_relationship_line.py:266-291; mcp/tests/test_knowledge_review_relationship_line.py:294-313; mcp/tests/test_knowledge_review_relationship_line.py:316-350; mcp/tests/test_knowledge_review_relationship_reach.py:392-432 |
| The qualification cases: a pairing states the recorded relation it was made on, and an address resemblance never pairs. | `test_a_pairing_states_the_recorded_relation_it_was_made_on`; `test_a_pairing_is_qualified_and_an_address_resemblance_never_pairs` | mcp/tests/test_knowledge_review_relationship_reach.py:472-500; mcp/tests/test_knowledge_review_relationship_reach.py:503-541 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It renders values built from the two
datasets the server resolved and one repository namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`, confirmed from the enclosure contract): **created.** The module is new in this leaf (`ICR-R08@v1`) and this is its one-to-one card. It records the display contract and the three verified correction rounds that shaped it: every one-sided sentence is built from the tested `ContinuationSearch` value (a record the store holds is named, never denied); the head sentence is reserved for a row that **is** the line's uniquely established head, with the line basis carrying the intermediate and multi-ended cases; the lineage sentence states what was read on the line; and the address view carries the movement beside the pane's existing row. It also records the routed `source_locations` consequence — one location per `(relationship_id, path)`, so one old address that is a side of two movements carries only the first movement in that row while the complete set is in `source.relationships` (`ICR-R24` mounts it) — and the reachability truth that separates the reached gaps from the defensive-only codes. **Basis accounting:** the verification pair above names this leaf's base, the last real commit the reading was taken against; the candidate is named here in the body rather than in a metadata row, and closeout owns the stamp once the code commit exists.
