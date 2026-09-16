# mcp/src/agents_remember/memory/knowledge/families.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/families.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `27242ecbefd79f2e8fbc6db32e02013fa8298ba3`|
| lastVerifiedCommitDate | 2026-09-16T08:41:27+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

## Purpose

The family half of the knowledge graph: family identity, its sealed revisions and the family
lineage. A family is a stable subject whose revision carries an authored **joint guarantee** about a
set of invariant revisions that hold together. The guarantee is the family's own text and is never
assembled from its members — a member keeps its exact own obligation, and the two are separate
authored claims a reader must not derive from one another.

This module owns the `family`, `family_revision` and `family_predecessor` tables. It owns no
membership: which invariant revisions a family revision covers is `memberships.py`, because a
membership is its own authored act rather than a field of the guarantee.

## Code Commentary

### Logic

- `create_family` writes the family identity: it resolves the bound namespace, checks the stored
  identity, and inserts or reports. An identity reuse with a **different display label** is
  `duplicate_identity` naming both labels; an identical re-declaration is the `no_change` shape the
  package uses elsewhere.
- `create_family_revision` seals a `FamilyRevisionDraft` through `records.sealed_family_revision_from_draft`
  (a `ValueError` becomes `invalid_payload`), then performs, in order: the identity-reuse check
  (same digest → the stored revision; different digest → `duplicate_identity` with both digests),
  `unknown_family`, `_require_same_family_predecessors`, `_require_acyclic_family`, the revision
  INSERT, the predecessor-edge INSERTs, and `store._require_referential_integrity`.
- `_require_same_family_predecessors` answers two different failures with two different codes: a
  predecessor that exists in no revision is a dangling `invalid_reference`, and a predecessor that
  exists in **another** family is `invalid_reference` naming the expected and observed families.
- `_require_acyclic_family` delegates to `lineage.find_cycle` over `lineage.family_edges`, so the
  family lineage and the invariant lineage share one rule rather than two similar ones. The
  two-branch refusal is `refusals.family_lineage_cycle_refusal`.
- Reads select the canonical columns directly through `connection.fetch_one` and hand the stored row
  to a `records.decode_*` function, which re-derives the payload seal on the way out. There is no
  cache and no in-memory family index.
- `family_id_of_revision` is deliberately narrow: it answers only *which family owns this revision*
  for the predecessor-ownership check and the endpoint check. It is not a membership read.

### Conventions

- Row builders live in `records.py` (`family_row`, `family_revision_row`, `family_predecessor_rows`)
  and their column order must match `schema.CANONICAL_COLUMNS`; this module never spells a column
  list of its own beyond the declared `_FAMILY_*_COLUMNS` / `_INSERT` constants that mirror it.
- Every mutating entry point takes the opened store as its first argument and reuses the store's
  `_exclusive_candidate_lock` and `_within_immediate`; a graph module does not open its own
  transaction.
- Refusals are constructed by `refusals.py` factories and returned as a typed result, never raised
  out of a public operation. `KnowledgeRefused` is an internal control-flow signal caught by the
  operation's own wrapper (`_family_refusal`, `_family_revision_refusal`).

### Invariants And Boundaries

- **A family revision is immutable and its payload is sealed.** The joint guarantee, the origin
  state, the acceptance reference, the provenance and the *sorted* predecessor set are one
  aggregate. Changing the guarantee means authoring a separately identified successor; a membership
  citing the original revision keeps resolving the original text.
- **Family lineage never crosses families.** Predecessors are same-family revision identities, a
  revision must not declare itself as its own predecessor (refused at construction by
  `FamilyRevisionDraft`), and the acyclic rule is evaluated over the post-insert graph **before any
  row is written**.
- **One lock, one transaction per mutation.** A refusal therefore never leaves a partial family,
  revision or edge behind.
- **The guarantee is never derived from the members.** Nothing in this module reads a membership to
  compose or complete a guarantee.
- **Boundary against approval and Git.** This module manufactures no acceptance, resolves no code
  attribution and stores no Git state; the provenance envelope is authored data that arrived on the
  request.
- **Not this module's job.** Anchor storage and resolution (`anchors.py`), membership
  (`memberships.py`), realization claims (`realizations.py`) and the shared relation-endpoint checks
  (`endpoints.py`). Anchor *resolution* is deferred to `KS-R07`; this module only stores what was
  authored.

### Todos

None recorded for this slice. The disclosed `family` identity-trigger asymmetry is recorded in the
route overview rather than here: `family_revision` rows carry a `no-update`/`no-delete` trigger, while
the `family` identity row carries none, so `UPDATE family SET display_label …` and `DELETE FROM
family` on an unreferenced row are not refused by the database. That matches the v1 design, which
covers revision rows and relation payloads only; adding the two triggers changes
`schema_fingerprint()`, which the L5 merge preflight compares, so it belongs to the declared
`ar-knowledge-sqlite/v2` route rather than to this leaf.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two rules this module is shaped by, stated in its own docstring. | "A family revision is immutable and its payload is sealed." | mcp/src/agents_remember/memory/knowledge/families.py:6-8 |
| Family identity creation and its label-conflict refusal. | `create_family`; `_insert_family` | mcp/src/agents_remember/memory/knowledge/families.py:78-95; mcp/src/agents_remember/memory/knowledge/families.py:96-111 |
| The sealed family revision operation and its ordered checks. | `create_family_revision`; `_insert_family_revision` | mcp/src/agents_remember/memory/knowledge/families.py:112-141; mcp/src/agents_remember/memory/knowledge/families.py:142-168 |
| Predecessor ownership, which distinguishes a dangling predecessor from a cross-family one. | `_require_same_family_predecessors` | mcp/src/agents_remember/memory/knowledge/families.py:169-185 |
| The family lineage guard, which reuses the shared rule rather than restating it. | `_require_acyclic_family` | mcp/src/agents_remember/memory/knowledge/families.py:186-203 |
| The narrow ownership read used for predecessor and endpoint checks. | `family_id_of_revision` | mcp/src/agents_remember/memory/knowledge/families.py:233-251 |
| The read surface, including the seal-verifying revision read. | `get_family`; `get_family_revision`; `list_family_revision_ids` | mcp/src/agents_remember/memory/knowledge/families.py:204-214; mcp/src/agents_remember/memory/knowledge/families.py:215-232; mcp/src/agents_remember/memory/knowledge/families.py:252-264 |
| The shared lineage rule this module applies a second time. | `find_cycle`; `family_edges` | mcp/src/agents_remember/memory/knowledge/lineage.py:71-86; mcp/src/agents_remember/memory/knowledge/lineage.py:63-68 |
| The two-branch family lineage refusal and its shared wording. | `family_lineage_cycle_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:265-286 |
| The payload a family revision's digest seals, including the sorted predecessor set. | `canonical_family_revision_payload`; `sealed_family_revision` | mcp/src/agents_remember/models/knowledge/digest.py:71-92; mcp/src/agents_remember/models/knowledge/digest.py:99-102 |
| The vocabulary shapes this module stores. | `FamilyDraft`; `FamilyRevisionDraft`; `FamilyRevision`; `StoredFamilyRevision` | mcp/src/agents_remember/models/knowledge/family.py:35-48; mcp/src/agents_remember/models/knowledge/family.py:58-102; mcp/src/agents_remember/models/knowledge/family.py:105-109; mcp/src/agents_remember/models/knowledge/family.py:112-123 |
| The declared `family`, `family_revision` and `family_predecessor` tables and their indexes. | `family`; `family_revision`; `family_predecessor` | mcp/src/agents_remember/memory/knowledge/schema.py:173-183; mcp/src/agents_remember/memory/knowledge/schema.py:184-201; mcp/src/agents_remember/memory/knowledge/schema.py:202-217 |
| The requirement this module's first delivered slice belongs to. | `KS-R02@v1` | ar-coordination/tasks/agents-remember/260915_knowledge-substrate/requirements/KS-R02-v1-registered-family-and-realization-graph.md |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): created this one-to-one card for the new family module. It records the two rules the module is shaped by (an immutable, payload-sealed family revision whose guarantee is never derived from its members; a family lineage that reuses the one shared acyclic rule instead of restating it), the guarantee-is-not-the-members separation, the narrow `family_id_of_revision` ownership read, and the disclosed `family` identity-trigger asymmetry routed to the `ar-knowledge-sqlite/v2` decision rather than treated as a v1 defect. Verification metadata remains empty until closeout stamps the code commit.
