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

### Conventions

- The declared unique tuple `(repository_id, family_revision_id, invariant_revision_id)` and the
  composite foreign keys are the structural guarantee.

### Invariants And Boundaries

- **A membership relates exactly one pair, once.** The unique tuple is declared, so a second row for the same pair is unrepresentable in practice.

- **A newer family revision does not inherit memberships.** There is no floating pointer: the relation
  cites `family_revision_id`, and the successor needs its own authored row.

- **No second list.** The reverse read is a query over the same rows, not a separately maintained
  index of semantic facts.

- **Not this module's job.** Family and family-revision identity (`families.py`), the joint guarantee
  (a property of the family revision, never composed from members), and family *composition* across families, which `KS-R02` defers.

### Todos

### Todos

None recorded for this slice. Cross-family composition remains explicitly deferred by `KS-R02@v1`
rather than pending work in this module.

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

- - The relation this module owns, stated as one exact pair. [17]
- - The reverse read (invariant revision to families) over the same rows. [18]

- - The declared `family_member` table, its unique tuple, its index and its no-repoint trigger. [19]


### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
