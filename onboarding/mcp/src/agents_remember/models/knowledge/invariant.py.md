# mcp/src/agents_remember/models/knowledge/invariant.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Invariant identity and the immutable invariant revision aggregate — the two identifiers that make a cited
statement impossible to rewrite in place, and the shape every stored revision is validated against.

## Code Commentary

### Logic

`InvariantDraft` is an invariant identity proposed for a namespace: `invariant_id` (UUID pattern),
`display_label` (bounded, nonblank after stripping) and `label_provenance`. `InvariantIdentity` extends the draft
with `repository_id` and a `row_digest`, which is the expected-row digest a label edit names.

`InvariantRevision` carries repository, invariant and revision identities, the display version, statement, applicability, ordered conditions and exclusions, provenance, predecessors and the payload digest. It also carries the selected tree's derived `state`, outside the payload seal.

Validators: `_require_nonblank_authored_text` strips `display_version`/`statement`/`applicability` and refuses a
blank; `_require_nonblank_clauses` strips clause entries, refuses a blank and **preserves order**, because the
order is the author's and the digest covers it; `_require_unique_predecessors` refuses a repeated revision
identity. The after-validator `_require_no_self_predecessor` refuses a revision that lists itself.

StoredInvariantRevision wraps the decoded revision and its sorted predecessor tuple. The index row decoder constructs that tuple and verifies the aggregate payload digest; this wrapper declares no independent sorted-predecessor after-validator.

### Conventions

`InvariantIdentity` is the stable subject; a revision is one authored statement of it. The friendly display
version belongs to the revision's **label**, not to its identity: two successors of one revision may both display
`v2`, and that is a supported state rather than an identity conflict.

### Invariants And Boundaries

- Immutability is by construction: the digest seals the whole semantic payload including the sorted predecessor
  set, so a stored revision identifies exactly one authored aggregate.
- `conditions`/`exclusions` are tuples whose empty value is a recorded "none", never a missing value.
- The index supplies derived state when reading the revision. A state change leaves the authored payload seal intact.
- InvariantRevision declares the aggregate; digest functions define its seal, and the index row decoder verifies it on read. store.py reads exact revisions and exposes no revision writer. The former insert-only canonical database operation was retired by MIK-R26.


### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The invariant identity shape, its nonblank display label and the row digest a label edit names. [1]

- The invariant revision validates its scoped authored fields and excludes self-predecessors. [2]









The requirement packet whose normative property this model encodes: requirement packet `KS-R01@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it.

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

- The read-back shape that pins the sorted predecessor set. [4]

- The current exact revision read and decoder verify a retained aggregate rather than writing it. [6]

- The stored `invariant_revision` table this aggregate is written to, with its immutability triggers. [5]
