# mcp/src/agents_remember/application/review_governing_route.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Read the reviewed identity's governing-route associations from text. A family's declared route set supplies one association per route, never a joined list disguised as one route.

## Code Commentary

### Logic

`governing_route_movements` reads the identity and route declarations on both snapshots. `_read_side` separates a declared route, a recorded identity with no route, an absent identity and an unread declaration. Families use projected `ix_route` declarations; invariants declare no route and remain ungoverned.

A route on both sides is unchanged; a route only one side declares while the other has different routes is added/retracted. A side with no route contributes its state. Unread declarations are unavailable with their gap and never become ungoverned or unchanged.

### Invariants And Boundaries

No root route is inferred for an ungoverned identity. Path-only review asks about no identity's route. Resemblance supplies no association. The retired scalar canonical join is not read or recreated.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring and ten
definitions, the route owner it reads through, the traversal that calls it, and the two cases that
measure it.

- **The module's own statement of the three states, of the existence question asked before the route question, and of the path seed that asks about no identity.** [1]
- The published surface: the fourth relationship kind and the one entry point. [2]
- The governed-table names the route owner's own writes answer, so the read asks the question the write answers. [3]
- **One side read: the identity kind named by the selector, the existence question first, then the route and its recorded path.** [4]
- The selector question: an identity or an exact revision of one names it, a path selector names none. [5]
- **The transition and the gap: reassigned when the recorded routes differ, and one gap per side whose snapshot does not record the identity.** [6]
- The statement of both sides and the word each side is rendered as — never the repository root. [7]
- The traversal that calls this module once per review, and the wire vocabulary the movement fills. [9]

- Text route sets yield one association per route and unread declarations are never ungoverned. [10]


### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one repository's recorded route
association for an identity inside that repository's namespace.

No applicable cross-repository source was found.
