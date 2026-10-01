# mcp/src/agents_remember/memory/knowledge/families.py

## Governing Overview

[memory route overview](../overview.md)

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
  package uses elsewhere. Since `KS-R03` the insert itself is `insert_family`, which refuses **any**
  stored identity under the requested id, and that is the helper the candidate-change batch composes:
  a caller-authored identity is never an upsert.
- `create_family_revision` seals a `FamilyRevisionDraft` through `records.sealed_family_revision_from_draft`
  (a `ValueError` becomes `invalid_payload`), decides the identical-repeat answer itself (same digest →
  the stored revision; different digest → `duplicate_identity` with both digests) and delegates the
  write to `insert_family_revision`, which performs, in order: owning-identity availability, the
  identity-reuse refusal, `_require_same_family_predecessors`, `_require_acyclic_family`, the revision
  INSERT, the predecessor-edge INSERTs, and `store.require_referential_integrity`.
- `_require_same_family_predecessors` answers two different failures with two different codes: a
  predecessor that exists in no revision is a dangling `invalid_reference`, and a predecessor that
  exists in **another** family is `invalid_reference` naming the expected and observed families. It
  takes the batch's declared `pending` identities, so a predecessor another command in the same batch
  creates is admitted from the declaration — the batch validates the completed graph before it writes
  and re-proves both graphs after.
- `_require_acyclic_family` delegates to `lineage.find_cycle` over `lineage.family_edges`, so the
  family lineage and the invariant lineage share one rule rather than two similar ones. The
  two-branch refusal is `refusals.family_lineage_cycle_refusal`. A batch's *declared* edges are judged
  by that same shared rule through `lineage.declared_cycle`, called from
  `batch_preconditions._require_declared_acyclic` — not by a second rule grown here.
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
  `exclusive_candidate_lock` and `within_immediate`; a graph module does not open its own
  transaction. `insert_family` and `insert_family_revision` are the **in-transaction** halves: they
  write through `store.write` and assume the caller already holds both the lock and the transaction,
  which is what lets the candidate-change batch compose them without nesting a second
  `BEGIN IMMEDIATE` or re-taking the lock.
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
  revision or edge behind. The published `insert_*` helpers assume that transaction; a caller that
  invokes one outside a transaction would write an autocommitted row silently, and nothing in this
  module enforces otherwise.
- **A batch's declarations are validated over the completed graph.** A family revision may declare a
  predecessor any command in the same batch creates, wherever that command sits in the sequence; the
  position of the creating command does not matter, and the completed-graph pass refuses a cycle among
  the batch's own revisions by name before any row is written.
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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The two rules this module is shaped by, stated in its own docstring. [1]
- Family identity creation and its label-conflict refusal. [2]
- The in-transaction family identity insert the batch command composes. [3]
- The sealed family revision operation, which decides the repeat answer and delegates the write. [4]
- The in-transaction aggregate insert, including the deferral of the immediate foreign-key check to the batch's own pass. [5]
- Predecessor ownership, which distinguishes a dangling predecessor from a cross-family one and admits the batch's declarations. [6]
- The family lineage guard, which reuses the shared rule rather than restating it. [7]
- The narrow ownership read used for predecessor and endpoint checks. [8]
- The read surface, including the seal-verifying revision read. [9]
- The shared lineage rule this module applies a second time, and the batch-aware caller that hands it the declared edges. [10]
- The two-branch family lineage refusal and its shared wording. [11]
- The payload a family revision's digest seals, including the sorted predecessor set. [12]
- The vocabulary shapes this module stores. [13]
- The declared `family`, `family_revision` and `family_predecessor` tables and their indexes. [14]
The requirement this module's first delivered slice belongs to: requirement packet `KS-R02@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it.

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
