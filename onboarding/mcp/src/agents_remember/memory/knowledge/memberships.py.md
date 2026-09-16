# mcp/src/agents_remember/memory/knowledge/memberships.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/memberships.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `27242ecbefd79f2e8fbc6db32e02013fa8298ba3`|
| lastVerifiedCommitDate | 2026-09-16T08:41:27+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

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
  `relationship_constraint`; then the insert and the referential-integrity check.
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
  gets a refusal naming the stored identity instead of a raw constraint failure.
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
  relation tables exactly as they were.
- **Not this module's job.** Family and family-revision identity (`families.py`), the joint guarantee
  (a property of the family revision, never composed from members), realization claims
  (`realizations.py`), and family *composition* across families, which `KS-R02` defers.

### Todos

None recorded for this slice. Cross-family composition remains explicitly deferred by `KS-R02@v1`
rather than pending work in this module.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The relation this module owns, stated as one exact pair. | "one exact invariant revision in one exact family revision" | mcp/src/agents_remember/memory/knowledge/memberships.py:1-1 |
| The membership creation operation and its ordered checks. | `create_family_member`; `_insert_member` | mcp/src/agents_remember/memory/knowledge/memberships.py:59-80; mcp/src/agents_remember/memory/knowledge/memberships.py:81-122 |
| The removal path, whose stale-caller refusal carries both digests. | `remove_family_member`; `_delete_member` | mcp/src/agents_remember/memory/knowledge/memberships.py:123-144; mcp/src/agents_remember/memory/knowledge/memberships.py:145-175 |
| The forward read (family revision to members). | `list_members` | mcp/src/agents_remember/memory/knowledge/memberships.py:201-215 |
| The reverse read (invariant revision to families) over the same rows. | `list_families_for_invariant_revision` | mcp/src/agents_remember/memory/knowledge/memberships.py:216-232 |
| The duplicate-pair probe the insert path consults. | `find_membership_by_pair` | mcp/src/agents_remember/memory/knowledge/memberships.py:187-200 |
| The single definition of a missing relation endpoint, shared with the claim relation. | `require_family_revision_endpoint`; `require_invariant_revision_endpoint` | mcp/src/agents_remember/memory/knowledge/endpoints.py:25-40; mcp/src/agents_remember/memory/knowledge/endpoints.py:42-56 |
| The row codec and expected-row digest that make the stale-caller refusal possible. | `member_row`; `member_row_digest`; `decode_member_row` | mcp/src/agents_remember/memory/knowledge/records.py:382-391; mcp/src/agents_remember/memory/knowledge/records.py:392-412; mcp/src/agents_remember/memory/knowledge/records.py:413-428 |
| The vocabulary this module stores and returns. | `FamilyMemberDraft`; `FamilyMember`; `FamilyMembers`; `InvariantFamilies` | mcp/src/agents_remember/models/knowledge/graph.py:49-56; mcp/src/agents_remember/models/knowledge/graph.py:58-63; mcp/src/agents_remember/models/knowledge/graph.py:96-102; mcp/src/agents_remember/models/knowledge/graph.py:104-109 |
| The declared `family_member` table, its unique tuple, its index and its no-repoint trigger. | `family_member`; `family_member_invariant_revision`; `family_member_no_repoint` | mcp/src/agents_remember/memory/knowledge/schema.py:231-247; mcp/src/agents_remember/memory/knowledge/schema.py:277-278; mcp/src/agents_remember/memory/knowledge/schema.py:341-345 |
| The requirement this module's first delivered slice belongs to. | `KS-R02@v1` | ar-coordination/tasks/agents-remember/260915_knowledge-substrate/requirements/KS-R02-v1-registered-family-and-realization-graph.md |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): created this one-to-one card for the new membership module. It records the no-floating-pointer rule (a membership cites an exact family revision, so a successor needs its own authored row), the exactly-once pair guarantee split between the declared unique tuple and the operation's pre-check, the stale-caller removal contract, the shared endpoint owner, and the fact that the reverse read is a query over the same rows rather than a second relation list. Verification metadata remains empty until closeout stamps the code commit.
