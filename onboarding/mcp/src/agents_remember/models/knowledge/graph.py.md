# mcp/src/agents_remember/models/knowledge/graph.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The retained exact-membership values and authored realization-role vocabulary consumed by derived-index readers. These are values, not a table owner, writer or authority decision.

## Code Commentary

### Logic

FamilyMemberDraft names member_id, family_revision_id, invariant_revision_id and provenance. FamilyMember adds repository_id and row_digest. InvariantFamilies carries the queried exact invariant revision and stored membership tuple; an empty tuple is an explicit empty answer.

RealizationRole closes primary-authority, enforcement, propagation-persistence, support, presentation, incidental and unclassified. UNCLASSIFIED_ROLE names the last value; a reader does not infer a role or rationale from a path or symbol.

### Invariants And Boundaries

- Membership cites exact revisions, never a floating identity/current pointer. A successor family revision needs its own authored membership set.
- A member draft carries no row seal; the derived-index decoder re-derives the stored member digest.
- Roles are authored claims, not mechanical classifications.
- Text realization entries belong to knowledge_files/sidecars.py and carry anchor, role and rationale. Its own role vocabulary omits incidental; the two Literals are not asserted identical.
- This module performs no I/O, writes no relationship and grants no approval.

### Historical boundary — MIK-R26

RealizationClaimDraft/RealizationClaim and the FamilyMembers/RealizationClaims/AnchorRealizations roster were retired with the canonical database route. Their old write operations and claim codecs surviving in tests are fixture support, not production successors or a second write lane.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References


- The retained membership values name exact revision endpoints. [1]


- The retained authored role Literal has an explicit unclassified value. [2]


- The membership draft and namespace/digest-carrying stored value. [3]


- The retained membership read-result shape. [6]


- Production membership functions read the exact pair or invariant-to-family rows. [7]


- The retained production member codec derives and validates its digest; claim codec is retired. [9]

The requirement this vocabulary's first delivered slice belongs to: requirement packet `KS-R02@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it.

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
