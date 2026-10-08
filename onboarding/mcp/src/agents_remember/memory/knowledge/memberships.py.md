# mcp/src/agents_remember/memory/knowledge/memberships.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Membership reads over the derived index: one exact invariant revision in one exact family revision. The relation cites revisions rather than floating identities; a newer family revision has its own authored membership set rather than inheriting an older revision's rows.

## Code Commentary

### Logic

find_membership_by_pair reads the one stored membership for the named exact endpoint pair. list_families_for_invariant_revision reads the memberships placing one invariant revision in families, ordered by member_id, and returns InvariantFamilies. Both select the same declared columns and decode each row through records.decode_member_row.

### Invariants And Boundaries

- The declared endpoint tuple and foreign keys preserve exact revision membership and endpoint kind.
- These functions read stored relationships and infer no family from paths, labels or obligation similarity.
- The module creates, removes and repoints no membership. It exposes no forward list_members operation.
- Family guarantee text is owned by family revisions, not composed from these rows.

### Historical boundary — MIK-R26

create_family_member, draft-sealing/insert helpers, remove_family_member, list_members and candidate lock/transaction composition belonged to canonical database writing and were retired. The file authoring route owns membership changes; this module reads the resulting derived index.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References


- Membership is one exact invariant revision in one exact family revision. [1]


- The retained invariant-to-family read returns stored memberships in stable order. [7]


- The exact endpoint-pair lookup reads the stored membership. [8]


- The retained member-row digest and decoder; member_row was not a current symbol. [15]


- The retained membership draft, stored member and invariant-to-family result values. [16]

The requirement this module's first delivered slice belongs to: requirement packet `KS-R02@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it.

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
