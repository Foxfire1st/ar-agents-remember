# mcp/src/agents_remember/models/knowledge/review_relationships.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The closed vocabulary for recorded before/after relationship movements. Both recorded sides and their identity travel together; any missing fact carries its own named gap.

## Code Commentary

### Logic

`ReviewRelationshipSide` distinguishes `recorded`, `absent`, `unresolved`, `ungoverned`, `unavailable` and `not_recorded`. A recorded identity with no route, unread route declarations and an identity absent from the snapshot are different facts. `route_unavailable` keeps an unread declaration visible instead of converting it into ungoverned.

The movement validates its transition against its sides, requires a recorded pairing basis for paired sides and names an identity gap when identity could not be established. Authored split, merge and successor relations carry their exact recorded revisions. Git rename detection remains a labelled inference, never proof of invariant movement.

### Invariants And Boundaries

The models declare values, not storage or verdicts. No similarity supplies a pairing, no unavailable fact becomes measured absence, and no ungoverned identity is placed in the repository root. Text family route sets are rendered one route per association.

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

- The production movement cases retain moved and withdrawn realizations and distinguish each declared route from an unread route side. [12]


### Cross-Repo References

No cross-repository behavior is implemented in this file. It is a value vocabulary for one repository's
review payload and carries no identity beyond that namespace.

No applicable cross-repository source was found.
