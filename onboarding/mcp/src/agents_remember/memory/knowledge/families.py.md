# mcp/src/agents_remember/memory/knowledge/families.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Family identity and sealed family-revision reads over a memory tree's derived index. A family revision carries its own authored joint guarantee, distinct from the obligations of its exact member revisions. A guarantee is never assembled from memberships.

## Code Commentary

### Logic

get_family reads one family identity or returns None. get_family_revision reads the exact revision row together with its stored predecessor set and passes the aggregate to records.decode_family_revision_row, which verifies its payload seal. list_family_revision_ids enumerates the family's retained revision identities in stable order; _family_predecessors reads that exact revision's predecessor edges.

### Invariants And Boundaries

- Reading a revision verifies its guarantee, origin state, acceptance reference, provenance and predecessor set as one sealed aggregate.
- Memberships are separate authored relations; these readers do not derive or complete a guarantee from members.
- These functions only read through the supplied opened store. They create no family, revision or lineage edge and manufacture no acceptance or Git state.
- The derived-index table declarations remain separate from the text-file authoring route.

### Historical boundary — MIK-R26

The canonical database's create_family, create_family_revision, insert helpers, ownership/acyclic guards and mutation wrappers were retired. The file writer authors family records now; this module reads the resulting derived index. Earlier mutation checks and schema-trigger observations describe that retired database route, not current family-writing capability.

### Logic

- Reads select the canonical columns directly through `connection.fetch_one` and hand the stored row
  to a `records.decode_*` function, which re-derives the payload seal on the way out. There is no
  cache and no in-memory family index.

### Invariants And Boundaries

- **A family revision is immutable and its payload is sealed.** The joint guarantee, the origin
  state, the acceptance reference, the provenance and the *sorted* predecessor set are one
  aggregate. Changing the guarantee means authoring a separately identified successor; a membership
  citing the original revision keeps resolving the original text.
- **The guarantee is never derived from the members.** Nothing in this module reads a membership to
  compose or complete a guarantee.
- **Boundary against approval and Git.** This module manufactures no acceptance, resolves no code
  attribution and stores no Git state; the provenance envelope is authored data that arrived on the
  request.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References


- Families are authored joint guarantees; these functions only read the derived index. [1]


- The retained family identity, exact revision and revision enumeration reads. [9]


- The family revision payload mapping and digest include the sorted predecessor set. [12]


- The retained family revision value shapes. [13]

The requirement this module's first delivered slice belongs to: requirement packet `KS-R02@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it.

- - The two rules this module is shaped by, stated in its own docstring. [14]
- - The read surface, including the seal-verifying revision read. [15]
- - The payload a family revision's digest seals, including the sorted predecessor set. [16]
- - The declared `family`, `family_revision` and `family_predecessor` tables and their indexes. [17]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
