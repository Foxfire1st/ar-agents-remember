# mcp/src/agents_remember/application/review_relationship_movement.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The recorded before/after relationship union of one reviewed subject: one value per relationship with both sides.** The traversal is the union both snapshots record, not the candidate's graph read alone; pairing is by the same recorded relationship row and nothing else, and every movement names its `pairing_basis`. The authored-line continuation search is deleted with the predecessor tables (MIK-R74 rule 1): the union is the comparison's selected page, and an association the candidate records under the same relationship row is displayed rather than called withdrawn.

## Code Commentary

`relationship_movements` reads both snapshots under one identity (`RelationshipSources` carries the two snapshots, the reviewed subject, the two bound code trees and the rename-inference seam as one frozen value) and returns one movement per relationship plus the governing-route movements. `_movements` pairs recorded sides by the same recorded row; only what neither side's union items hold is displayed as a one-sided association, with its sentence stating exactly which populations were searched. Each side states which snapshot fact it is — `recorded`, `unresolved`, `ungoverned`, `unavailable` or `not_recorded` — and none is defaulted to another. The rename inference is labelled and proves nothing: it is attached beside a movement and never read by the traversal. Three responsibilities stay in their own modules and are called: recorded relationships, governing route, rename inference.

## Evidence

- One traversal over the union both snapshots record [17]
- Pairing by the same recorded row, one movement per relationship [18]
- The search published for a one-sided sentence [19]
- Same-citation matching without authored lines [20]
- Continuation by recorded rows only [21]
