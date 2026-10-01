# mcp/src/agents_remember/memory/knowledge/memberships.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The membership relation: **one exact invariant revision in one exact family revision.** A membership
cites revisions rather than identities, so nobody has to guess which statement it was authored
against, and a newer family revision needs its own explicitly authored membership instead of
inheriting one through a moving `current` pointer.

This module owns the `family_member` table — the one canonical stored identity for the statement "this
invariant revision is a member of this family revision". It is also the owner of both read directions
over that table, which is why forward and reverse lookups can be compared by identity rather than
reconciled.

## Code Commentary

### Logic

- `create_family_member` resolves the namespace, takes the candidate lock, and runs one immediate
  transaction whose check order is fixed: build the stored member and its expected row digest;
  an identical re-declaration is `no_change`; the same `member_id` sealing different content is
  `duplicate_identity`; the two endpoints are checked by `endpoints.py`; the same endpoint pair is
  `relationship_constraint`; then the insert and the referential-integrity check. Since `KS-R03` the
  insert is the in-transaction helper `insert_family_member`, which the candidate-change batch
  composes as well.
- `insert_family_member_draft` is the second entry point the batch command uses: it seals an authored
  `FamilyMemberDraft` under the admitted `Authorship` and computes the row digest **here**, so a draft
  that arrived carrying its own envelope cannot make the stored row digest something the caller chose.
  That is the same provenance rule the batch applies to every other command, expressed where the
  member's digest is derived.
- `list_members` (family revision → members) and `list_families_for_invariant_revision` (invariant
  revision → members) select the same table and the same column list. Neither derives anything: both
  return stored `FamilyMember` rows, so the two directions answer with identical `member_id` sets.
- `remove_family_member` requires the row digest the caller expects. A mismatch is
  `stale_precondition` with both digests, so a caller that remembered an older row is told rather
  than obeyed.
- `find_membership_by_pair` is the duplicate-pair probe the insert path consults; it is not a reader
  the application calls to decide whether a relationship exists.

### Conventions

- The declared unique tuple `(repository_id, family_revision_id, invariant_revision_id)` and the
  composite foreign keys are the structural guarantee; the operation's pre-checks exist so the caller
  gets a refusal naming the stored identity instead of a raw constraint failure. Both layers are
  needed and each has its own evidence: the concept pre-check inside the insert refuses the pair by
  name, and the database's own UNIQUE tuple is the backstop when a caller reaches the table another
  way — the batch's mid-batch attribution node disables the pre-check deliberately, so the two
  mechanisms no longer share one node.
- Endpoint existence is never re-implemented here: both checks come from `endpoints.py`, which is the
  single definition of "this endpoint does not exist" for both relation kinds.
- Equality for the `no_change` decision is whole-model equality, so a provenance difference is a
  duplicate rather than a no-op.

### Invariants And Boundaries

- **A membership relates exactly one pair, once.** The unique tuple is declared, and the operation
  pre-checks it, so a second row for the same pair is unrepresentable in practice and reported as
  `relationship_constraint` naming the stored identity.
- **A newer family revision does not inherit memberships.** There is no floating pointer: the relation
  cites `family_revision_id`, and the successor needs its own authored row.
- **No second list.** The reverse read is a query over the same rows, not a separately maintained
  index of semantic facts.
- **Removal never repoints.** A removal takes the row out of the candidate; the earlier dataset keeps
  it, which is what makes a before/after comparison meaningful.
- **One lock, one transaction**, with every check before the first write, so a refusal leaves the
  relation tables exactly as they were. `insert_family_member`, `insert_family_member_draft` and
  `delete_family_member` are the in-transaction halves the batch composes: they assume the caller
  already holds the lock and the transaction, and nothing enforces that.
- **Not this module's job.** Family and family-revision identity (`families.py`), the joint guarantee
  (a property of the family revision, never composed from members), realization claims
  (`realizations.py`), and family *composition* across families, which `KS-R02` defers.

### Todos

None recorded for this slice. Cross-family composition remains explicitly deferred by `KS-R02@v1`
rather than pending work in this module.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The relation this module owns, stated as one exact pair. [1]
- The membership creation operation and its ordered checks. [2]
- The in-transaction insert both the operation and the batch command compose, including the pair pre-check the database's unique tuple backs up. [3]
- The draft-sealing entry point that computes the row digest from the admitted provenance. [4]
- The removal path, whose stale-caller refusal carries both digests. [5]
- The forward read (family revision to members). [6]
- The reverse read (invariant revision to families) over the same rows. [7]
- The duplicate-pair probe the insert path consults. [8]
- The batch command that composes the draft-sealing insert. [9]
- The two nodes that keep the concept guard and the database's own tuple separately proven. [10]
- The single definition of a missing relation endpoint, shared with the claim relation. [11]
- The batch command that composes the draft-sealing insert. [12]
- The two nodes that keep the concept guard and the database's own tuple separately proven. [13]
- The single definition of a missing relation endpoint, shared with the claim relation. [14]
- The row codec and expected-row digest that make the stale-caller refusal possible. [15]
- The vocabulary this module stores and returns. [16]
- The declared `family_member` table, its unique tuple, its index and its no-repoint trigger. [17]
The requirement this module's first delivered slice belongs to: requirement packet `KS-R02@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it.

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
