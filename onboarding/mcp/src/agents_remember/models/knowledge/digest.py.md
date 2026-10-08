# mcp/src/agents_remember/models/knowledge/digest.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The canonical invariant and family revision payload mappings and their SHA-256 digest computations. Each aggregate has its own payload version so the two sealed field sets cannot be mistaken for one another.

## Code Commentary

### Logic

canonical_revision_payload includes the payload version, repository/invariant/revision identities, display version, statement, applicability, ordered conditions and exclusions, origin state, acceptance reference, provenance and sorted predecessors. canonical_family_revision_payload uses the family's own identity and joint guarantee together with the same origin/provenance/predecessor rule. Neither mapping includes its digest.

revision_payload_digest and family_revision_payload_digest hash those exact mappings through kernel.canonical_json.sha256_digest. The predecessor set is sorted because its order is not authored meaning; conditions and exclusions keep their authored order.

### Invariants And Boundaries

- Predecessor edges participate in both payload digests, so changing them changes the aggregate being verified.
- Index row decoders re-derive the digest over decoded rows plus stored predecessor edges and refuse a mismatch.
- Changing the sealed field set requires a different payload version; an existing digest is not silently reinterpreted.
- These functions compute only. They read no store, write no row and manufacture no acceptance.

### Historical boundary — MIK-R26

sealed_revision, sealed_family_revision and the store's draft-sealing writer functions were retired with canonical database mutation. The payload mappings and digest computations remain because derived-index readers verify recorded aggregates; no current sealing/write operation is exported here.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References


- The invariant payload includes authored scope and sorted predecessors while excluding its digest. [1]


- The retained invariant digest computation hashes the canonical mapping. [2]


- The family payload seals its joint guarantee and sorted predecessors. [3]

- The recorded payload versions, separate so one payload's digest cannot be read as the other's. [4]

- Both index revision decoders verify the recorded aggregate seal. [5]


- Index decoders recompute seals on read; draft-sealing writers are retired. [6]

- The node that proves each sealed field is load-bearing rather than incidentally covered. [7]
- The canonical encoder the digest is computed through. [8]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
