# mcp/src/agents_remember/models/knowledge/graph.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/graph.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `27242ecbefd79f2e8fbc6db32e02013fa8298ba3`|
| lastVerifiedCommitDate | 2026-09-16T08:41:27+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

## Purpose

The relation half of the knowledge graph: the membership and realization-claim vocabulary plus the
read models both directions answer with. Two relations carry the graph, and each is stored exactly
once:

- a **family membership** relates one exact family revision to one exact invariant revision;
- a **realization claim** relates one exact invariant revision to one source anchor and carries the
  author's role and rationale.

This module defines values, not rows. It performs no I/O, owns no table and raises no refusal: the
storage owners are `memory/knowledge/memberships.py` and `memory/knowledge/realizations.py`.

## Code Commentary

### Logic

- `FamilyMemberDraft` is the authored membership (`member_id`, `family_revision_id`,
  `invariant_revision_id`, `provenance`); `FamilyMember` adds the bound `repository_id` and the
  expected `row_digest`.
- `RealizationClaimDraft` is the authored claim (`claim_id`, `invariant_revision_id`, `role`,
  `rationale`) with a non-blank rationale validator. **The anchor endpoint is deliberately absent**:
  it is supplied by the request that carries the draft, because naming an existing anchor and
  recording a new one in the same transaction are different inputs, and folding both into the draft
  would erase that distinction.
- `RealizationClaim` adds `repository_id`, `anchor_id`, `provenance` and `row_digest`.
- `RealizationRole` is the closed authored vocabulary — `primary-authority`, `enforcement`,
  `propagation-persistence`, `support`, `presentation`, `incidental`, `unclassified` — and
  `UNCLASSIFIED_ROLE` names the last one so a caller does not hard-code the string.
- The four read models at the bottom (`FamilyMembers`, `InvariantFamilies`, `RealizationClaims`,
  `AnchorRealizations`) each carry their query's endpoint identity plus a tuple of stored rows. They
  are the shapes the two directions return, which is why they can be compared by identity.

### Conventions

- Read models are named for the question they answer, not for the table: `InvariantFamilies` is "the
  memberships that place this invariant revision in families", `AnchorRealizations` is "the claims
  that cite this anchor".
- Every named tuple defaults to `()` rather than being required, so an empty result is a value rather
  than an error.
- The role's leading and trailing members are this repository's addition to the design's list: a
  missing role must be representable as "not classified" rather than silently defaulted to a real one.

### Invariants And Boundaries

- **A role is a claim about this relationship, never a machine observation.** The closed vocabulary
  exists so a reader can render a role without inventing one; nothing in the read path infers or
  fills a role.
- **Drafts carry no seal.** `FamilyMemberDraft` and `RealizationClaimDraft` have no `row_digest` field,
  so a caller cannot present a row whose digest belongs to different content; the store computes it
  through `records.member_row_digest` / `records.claim_row_digest`.
- **Revisions, not identities.** The membership cites `family_revision_id` and
  `invariant_revision_id`, so nobody has to guess which statement a membership was authored against
  and a newer family revision needs its own explicitly authored membership.
- **Boundary.** No operation, no table, no SQL, no refusal code. The relation operations, their
  endpoint checks and their uniqueness enforcement live in `memory/knowledge/`.
- **Not this module's job.** Family revision identity (`family.py`), the locator and source-identity
  union (`source.py`), the request/result and refusal vocabulary (`result.py`).

### Todos

None recorded for this slice. `UNCLASSIFIED_ROLE` is a declared affordance with no production reader
yet; it exists so an author who does not know a role can say so, and a later consumer may read it
without this module having to change.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two relations this module's vocabulary carries, and the no-second-list rule. | "There is no second, separately maintained list of semantic facts" | mcp/src/agents_remember/models/knowledge/graph.py:14-17 |
| The closed authored role vocabulary and the explicit not-classified member. | `RealizationRole`; `UNCLASSIFIED_ROLE` | mcp/src/agents_remember/models/knowledge/graph.py:36-44; mcp/src/agents_remember/models/knowledge/graph.py:46-46 |
| The membership draft and its stored, digest-carrying form. | `FamilyMemberDraft`; `FamilyMember` | mcp/src/agents_remember/models/knowledge/graph.py:49-56; mcp/src/agents_remember/models/knowledge/graph.py:58-63 |
| The claim draft, with its anchor endpoint deliberately held by the request instead. | `RealizationClaimDraft` | mcp/src/agents_remember/models/knowledge/graph.py:65-85 |
| The stored claim, including its anchor and expected row digest. | `RealizationClaim` | mcp/src/agents_remember/models/knowledge/graph.py:87-94 |
| The four read models, one pair per relation direction. | `FamilyMembers`; `InvariantFamilies`; `RealizationClaims`; `AnchorRealizations` | mcp/src/agents_remember/models/knowledge/graph.py:96-102; mcp/src/agents_remember/models/knowledge/graph.py:104-109; mcp/src/agents_remember/models/knowledge/graph.py:112-118; mcp/src/agents_remember/models/knowledge/graph.py:120-129 |
| The membership operations that store and read these values. | `create_family_member`; `list_members`; `list_families_for_invariant_revision` | mcp/src/agents_remember/memory/knowledge/memberships.py:59-80; mcp/src/agents_remember/memory/knowledge/memberships.py:201-215; mcp/src/agents_remember/memory/knowledge/memberships.py:216-232 |
| The realization operations that store and read these values. | `create_realization_claim`; `list_claims_for_invariant_revision`; `list_claims_for_anchor` | mcp/src/agents_remember/memory/knowledge/realizations.py:61-83; mcp/src/agents_remember/memory/knowledge/realizations.py:238-254; mcp/src/agents_remember/memory/knowledge/realizations.py:255-269 |
| The row codecs and expected-row digests the drafts deliberately omit. | `member_row_digest`; `claim_row_digest` | mcp/src/agents_remember/memory/knowledge/records.py:392-412; mcp/src/agents_remember/memory/knowledge/records.py:441-462 |
| The declared relation tables these values map onto. | `family_member`; `realization_claim` | mcp/src/agents_remember/memory/knowledge/schema.py:231-247; mcp/src/agents_remember/memory/knowledge/schema.py:248-268 |
| The requirement this vocabulary's first delivered slice belongs to. | `KS-R02@v1` | ar-coordination/tasks/agents-remember/260915_knowledge-substrate/requirements/KS-R02-v1-registered-family-and-realization-graph.md |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): created this one-to-one card for the new relation vocabulary. It records the membership-cites-revisions rule, the closed authored role vocabulary with its explicit `unclassified` member, the deliberate absence of the anchor endpoint from the claim draft (naming an anchor and recording one are different inputs), and the drafts-carry-no-seal rule that keeps expected-row digests in the store's hands. Verification metadata remains empty until closeout stamps the code commit.
