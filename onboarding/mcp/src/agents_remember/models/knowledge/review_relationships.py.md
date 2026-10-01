# mcp/src/agents_remember/models/knowledge/review_relationships.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The wire vocabulary of one recorded relationship** (`ICR-R08@v1`): the values the review surface's
source pane carries beside its locations, so a reader sees an association rather than two unrelated
addresses. It owns the vocabulary as **one two-sided fact**, and the shape enforces the packet's rules
rather than trusting a renderer to keep them:

- **A relationship is displayed with both sides.** `ReviewRelationshipMovement` carries every recorded
  side the two snapshots hold for one association, so a realization moved from A to B is one value
  showing A and B — and the `before` collection is a tuple because the recorded facts can be
  many-to-one.
- **The canonical identity is carried, and its absence is a stated gap.** `record_kind`/`record_id`
  name the invariant or family the association sits under; a movement that could not establish one must
  carry an `identity_not_recorded` gap, so a blank can never read as an identity that is not there.
- **A state is never blank.** Every side states which snapshot fact it is: `recorded`, `unresolved`,
  `ungoverned` or `not_recorded`, each with the sentence that says so, and the last two are deliberately
  different facts.
- **A pairing names its recorded basis.** A two-sided movement must carry `pairing_basis`, whose values
  are all recorded relations (the same row, the same member under a moved family revision, an authored
  successor step) and never a similarity.
- **A rename is an inference with its own label, never a movement.**
  `ReviewRenameInference.basis` can only be `git_rename_detection`, its state separates a measured
  pairing, a measured non-pairing and an unmeasured inference, and its statement says it is not proof
  that an invariant moved.

The module is new in `260921-ICR-L8` and exists only in that leaf's uncommitted candidate (branch
`ar/260921-icr-l8`); the verification basis recorded above is the production line at this leaf's base,
`02957762709c9b515b4ff57f7f13524a7c0dfb8d`. Closeout owns the stamp once the code commit exists.

## Code Commentary

### Logic

**Five closed unions and one single-member literal are the vocabulary's declarations.**
`ReviewRelationshipKind` is the four kinds the union holds (three are union items the comparison
selects; `governing_route` is the reviewed identity's own join row), `ReviewRelationshipSideName` is
`before`/`after`, `ReviewRelationshipState` is the five side states, `ReviewRelationshipTransition` is
the six movements, `AuthoredLineageKind` is the three authored relations, `ReviewRelationshipGapCode`
is the seven reasons a display could not establish a fact, and `ReviewPairingBasis` is the eight
recorded relations a pairing may name. `RENAME_INFERENCE_KIND` and `RenameInferenceState` carry the
rename vocabulary, and `RENAME_INFERENCE_KIND`'s literal has one member so no caller can record a
rename of its own as though a tool had measured it.

**`ReviewRelationshipGap` is the packet's Failure And Recovery Behavior as a value.** One fact the
display could not establish, named with its side, the field it is about, the code that names the reason
and the sentence that states it — so an unresolved old or new anchor stays *visible* instead of the
association being dropped or rendered as though it had no second side. The seven codes are
`anchor_unrecorded`, `anchor_unresolved`, `identity_not_recorded`, `identity_differs`,
`predecessor_records_no_relationship`, `successor_line_unresolved` and `route_not_recorded`; the
production path reaches the resolved-anchor, successor-line and unrecorded-predecessor reasons, while
the others are the value layer's defensive vocabulary for a graph the schema does not currently admit.

**`ReviewRelationshipSide` is one snapshot's recorded fact, and its validator refuses a blank
identity.** Fields are what *that* snapshot recorded: the relationship row's own identity, the address
and role its author wrote, the identity and revision the association cites, the resolution the read
reached against that snapshot's code tree, and `item_coverage` — the shipped comparison's own statement
about the union item this side came from — which makes "this side exists only on the baseline" a
carried fact rather than a second derivation. `detail` is required, because every side states which
fact it is, including the states that are not a relationship at all. `recorded` is a claim about a
stored row, so the validator refuses a `recorded` side that carries no relationship id.

**`ReviewAuthoredLineage` is the author's own edge and nothing else.** A succession, a split or a merge,
with `related_revision_ids` holding **every** other revision of that relation, so a split is displayed
with all of the successors its author recorded rather than with the one a pairing happened to pick. The
vocabulary has no field a similarity score could be recorded in.

**`ReviewRenameInference` can only be Git's detection.** Its validator keeps a pairing and its state one
fact (an `inferred` state carries the pair; a state that reports no pairing carries no paths) and
refuses a similarity word on an `unavailable` state, because a score beside an unmeasured inference
would read as a measurement of the two trees that was never made.

**`ReviewRelationshipMovement` is the movement itself, with four validators.** The transition must match
its sides (an `added` movement has one after side and no before side; `retracted`/`outside_selection`
have exactly one before side; a two-sided transition has both), every gap must name a displayed side
(the absence of a whole side is the transition, not a gap), a paired movement must name its
`pairing_basis` (and a one-sided movement must name none), and a movement with no `record_id` must
carry the `identity_not_recorded` gap that explains it.

### Conventions

`__all__` publishes the eleven vocabulary names (the unions, the gap, the side, the lineage, the rename
inference and the movement). Every model is a `KnowledgeModel` (the package's pydantic base) with
bounded string fields (`REFERENCE_MAX_LENGTH`, `PATH_MAX_LENGTH`, `LABEL_MAX_LENGTH`,
`PROSE_MAX_LENGTH`), and every rule above is a `model_validator(mode="after")` rather than a renderer's
convention. The module defines no record kind, reads no store and writes nothing; the review vocabulary
module (`models/knowledge/review.py`) re-exports these names in its own `__all__`, so the payload's
public spellings stay where they were.

### Invariants And Boundaries

- **Both sides, or the transition says why not.** A movement is either two-sided (with a stated basis)
  or one-sided with the transition that names the fact (`added`, `retracted`, `outside_selection`).
- **A state is never blank and an identity is never invented.** Every side (`recorded`, `unresolved`,
  `ungoverned`, `not_recorded`) and every movement (`record_kind`/`record_id` plus a gap when the
  identity could not be established) states itself.
- **Nothing here concludes.** There is no field for a verdict, a severity, a score, a similarity, an
  attribution or a causal claim; lineage is the author's own predecessor edge and the rename inference
  is labelled as an inference.
- **The rename value proves nothing.** Its statement says so in the value itself, and no side, identity
  or association is built from it.
- **Reachability, stated precisely.** The production path reaches `anchor_unresolved`,
  `successor_line_unresolved` and `predecessor_records_no_relationship`, plus the transition
  `outside_selection` and the state `ungoverned`; `anchor_unrecorded`, `identity_differs`,
  `identity_not_recorded` and `route_not_recorded` are defensive-only. The whole code set is not
  presented as displayed behaviour.
- **Boundaries.** The display sentences and the pairing rules are the application modules'; mounting
  these values in the browser pane is `ICR-R24`'s and the acceptance journey is `ICR-R25`'s.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring and
fourteen definitions, the application modules that fill these values, the review vocabulary that
re-exports them, and the cases that measure the shape through the production composition.

- **The module's own statement of the five rules its shape enforces: both sides, the carried identity, no blank state, the labelled authored lineage, and the rename as an inference.** [1]
- The published vocabulary. [2]
- The four relationship kinds, the two side names, the five side states, the six transitions, the three lineage kinds and the seven gap codes. [3]
- **The eight recorded relations a pairing may name, and the single-member rename basis.** [4]
- **The unresolved fact as a value: its side, its field, its code and its sentence.** [5]
- **One snapshot's recorded side, with the validator that refuses a recorded side carrying no relationship identity.** [6]
- The author's own edge with every related revision, and the absence of any field a similarity could occupy. [7]
- **The labelled rename inference, with the validator that ties a pairing to its state and refuses a similarity word on an unmeasured inference.** [8]
- **The movement's four validators: the transition must match its sides, a gap must name a displayed side, a pairing must state its basis, and an absent identity must state itself.** [9]
- The application module that builds the movements, and the display module that renders them. [10]
- The review vocabulary that re-exports these names and gains the two new fields on the pane row. [11]
- **The cases that measure the vocabulary through the production composition: the moved realization under one identity, the withdrawn realization, and the ungoverned identity that is never the root.** [12]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It is a value vocabulary for one repository's
review payload and carries no identity beyond that namespace.

No applicable cross-repository source was found.
