# mcp/src/agents_remember/application/review_governing_route.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_governing_route.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T19:40:00+02:00 |
| lastVerifiedCommitHash | `dcf35a0e0fc06bccdafd22390b7588b0aea811bc` |
| lastVerifiedCommitDate | 2026-09-22T20:08:58+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The reviewed identity's recorded governing-route association** (`ICR-R08@v1`). A governing route is a
recorded association like a realization and a family membership, and it is the one the comparison's
union does not carry as an item: it is a join row between an identity and a route. This module reads it
for one identity on each snapshot and displays **both recorded sides**, which is the packet's
"associations" clause applied to the route relation.

Three states are kept apart, and each is a fact rather than a default: `recorded` (the snapshot records
the identity and a route governs it, with the route's own id and its recorded path), `ungoverned` (the
snapshot records the identity and no route governs it — it is **not** placed in the repository root and
no route is inferred from the paths its claims name), and `not_recorded` (the snapshot does not record
the identity at all). The route owner answers `None` for both the ungoverned case and the absent one,
so the existence question is asked here, by identity, **before** the route question.

A review with no reviewed identity — a path seed, or the task-context composition — asks about no
identity's route and is answered with no association rather than with a route read for whichever record
the path matched first.

The module is new in `260921-ICR-L8` and exists only in that leaf's uncommitted candidate (branch
`ar/260921-icr-l8`); the verification basis recorded above is the production line at this leaf's base,
`02957762709c9b515b4ff57f7f13524a7c0dfb8d`. Closeout owns the stamp once the code commit exists.

## Code Commentary

### Logic

**`governing_route_movement` is the one entry point and it answers two different questions in order.**
It extracts the reviewed identity from the selector (`_subject_identity`: an identity selector or an
exact revision of one names its identity; a path selector names none and is answered with `None`), then
reads one side per snapshot and builds one movement with both sides, the transition and its statement.
`pairing_basis` is `same_governed_identity`, because both sides *are* one association — the governing
route of the identity this review selected, read on each snapshot — so the movement states why its two
sides are one rather than asserting a movement.

**`_route_side` asks the existence question before the route question.** `_identity_recorded` runs the
route owner's own governed-table question for the identity kind (`_GOVERNED_TABLES`: `invariant` or
`family`, the owner's own table names, so the read asks the question the write answers); when the
identity is not recorded the side is `not_recorded` with a sentence that says so and carries no facts
at all. When it is recorded, `find_governing_route` answers the route question: `None` is `ungoverned`
with its own sentence, and a route id is `recorded` with `route_path_for_id`'s recorded path.

**`_route_transition` names what happened, and `_route_gaps` states what could not be established.**
Two recorded routes that differ are `reassigned`; the same route id on both sides is `unchanged`; a side
whose snapshot does not record the identity at all yields a `route_not_recorded` gap carrying that
side's own sentence. `_route_word` renders one side for the statement, so an ungoverned side reads as
"no governing route" and an absent identity as "no `invariant`/`family` identity recorded" — never as
the repository root and never as the other snapshot's answer.

### Conventions

`__all__` publishes the kind constant and the entry point (`GOVERNING_ROUTE_KIND` is
`Literal["governing_route"]`, the fourth relationship kind the vocabulary admits); the movement it
builds is the same wire type every other association uses (`ReviewRelationshipMovement`). The module
opens no connection of its own — the traversal passes the two snapshots it already opened read-only —
and it writes nothing. Every fact it states comes from the route owner (`find_governing_route`,
`route_path_for_id`) or from its own existence question, and no route is inferred from a path.

### Invariants And Boundaries

- **An ungoverned identity is not a root identity.** `ungoverned` carries `route_id=None` and its own
  sentence; the repository root is never substituted and no path-derived route is guessed.
- **An identity a snapshot does not record is not an identity with no route.** The two are different
  states and neither is filled in from the other snapshot.
- **A path seed asks about no identity.** A review with no reviewed identity displays no route
  association, which is a statement about the question rather than about the repository.
- **The route question is the owner's.** The tables asked are the route owner's own governed-table
  names, and the route's path is read from the owner rather than composed here.
- **Boundaries.** The `route_not_recorded` gap is defensive-only in production reach for this leaf's
  measured path (it needs the reviewed identity absent from one snapshot); mounting the movement in the
  pane is `ICR-R24`'s and the acceptance journey is `ICR-R25`'s.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring and ten
definitions, the route owner it reads through, the traversal that calls it, and the two cases that
measure it.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the three states, of the existence question asked before the route question, and of the path seed that asks about no identity.** | `governing_route_movement` | mcp/src/agents_remember/application/review_governing_route.py:1-21; mcp/src/agents_remember/application/review_governing_route.py:59-93 |
| The published surface: the fourth relationship kind and the one entry point. | `GOVERNING_ROUTE_KIND`; `__all__` | mcp/src/agents_remember/application/review_governing_route.py:36-39; mcp/src/agents_remember/application/review_governing_route.py:41-41 |
| The governed-table names the route owner's own writes answer, so the read asks the question the write answers. | `_GOVERNED_TABLES` | mcp/src/agents_remember/application/review_governing_route.py:45-45 |
| **One side read: the identity kind named by the selector, the existence question first, then the route and its recorded path.** | `_route_side`; `_RouteFacts`; `_route_side_of`; `_identity_recorded` | mcp/src/agents_remember/application/review_governing_route.py:122-158; mcp/src/agents_remember/application/review_governing_route.py:112-119; mcp/src/agents_remember/application/review_governing_route.py:161-183; mcp/src/agents_remember/application/review_governing_route.py:246-255 |
| The selector question: an identity or an exact revision of one names it, a path selector names none. | `_subject_identity` | mcp/src/agents_remember/application/review_governing_route.py:96-109 |
| **The transition and the gap: reassigned when the recorded routes differ, and one gap per side whose snapshot does not record the identity.** | `_route_transition`; `_route_gaps` | mcp/src/agents_remember/application/review_governing_route.py:186-195; mcp/src/agents_remember/application/review_governing_route.py:198-212 |
| The statement of both sides and the word each side is rendered as — never the repository root. | `_route_statement`; `_route_word` | mcp/src/agents_remember/application/review_governing_route.py:215-233; mcp/src/agents_remember/application/review_governing_route.py:236-243 |
| The route owner the association is read through. | `find_governing_route`; `route_path_for_id` | mcp/src/agents_remember/memory/knowledge/routes.py:359-405; mcp/src/agents_remember/memory/knowledge/routes.py:269-282 |
| The traversal that calls this module once per review, and the wire vocabulary the movement fills. | `relationship_movements`; `ReviewRelationshipMovement` | mcp/src/agents_remember/application/review_relationship_movement.py:142-177; mcp/src/agents_remember/models/knowledge/review_relationships.py:258-372 |
| **The cases that measure the route movement: a reassignment displaying both recorded routes, and an identity with no route displayed as ungoverned and never as the root.** | `test_a_governing_route_reassignment_displays_both_recorded_routes`; `test_an_identity_with_no_route_is_displayed_as_ungoverned_and_never_as_the_root` | mcp/tests/test_knowledge_review_relationship_movement.py:803-826; mcp/tests/test_knowledge_review_relationship_movement.py:829-857 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one repository's recorded route
association for an identity inside that repository's namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`, confirmed from the enclosure contract): **created.** The module is new in this leaf (`ICR-R08@v1`) and this is its one-to-one card. It records the route association as a fourth recorded relationship the union does not carry as an item, the three states kept apart (`recorded`/`ungoverned`/`not_recorded`), the existence question asked before the route question because the route owner answers `None` for both of the latter, and the measured boundary that an ungoverned identity is never placed in the repository root. **Basis accounting:** the verification pair above names this leaf's base, the last real commit the reading was taken against; the candidate is named here in the body rather than in a metadata row, and closeout owns the stamp once the code commit exists.
