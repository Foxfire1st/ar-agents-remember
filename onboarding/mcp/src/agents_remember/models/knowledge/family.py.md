# mcp/src/agents_remember/models/knowledge/family.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Family identity and immutable revision values. A family's joint guarantee is authored independently of its members' obligations; members never supply or rewrite that guarantee.

## Code Commentary

### Logic

The draft/stored value split keeps a caller-supplied payload digest out of revision authoring. The decoded revision carries its seal and checked sorted predecessor set. Construction refuses inconsistent acceptance, duplicate predecessors and self-predecessors.

### Invariants And Boundaries

A changed guarantee names a successor revision; an earlier membership keeps the exact revision it cites. This module performs no I/O. `memory/knowledge/families.py` only reads values from the memory tree's derived index. Canonical family creation, revision encoding and draft-sealing APIs are retired; fixture writers are not production successors.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The separation between the family guarantee and its members' obligations. [1]
- The identity draft and its stored, digest-carrying form. [2]
- The authored aggregate before sealing, with its digest deliberately absent. [3]
- The sealed revision and its stored read shape. [4]
- The shared accepted/proposed rule this aggregate applies at construction. [5]
- The payload this revision's digest seals, including the sorted predecessor set. [6]

- The retained family revision decoder verifies the sealed aggregate and sorted predecessors. [7]


- The production reader retrieves family identities and exact sealed revisions from the derived index; it writes nothing. [8]

- The declared `family` and `family_revision` tables these values map onto. [9]
The requirement this vocabulary's first delivered slice belongs to: requirement packet `KS-R02@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it.

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
