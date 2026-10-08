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

`InvariantRevision` is the complete authored aggregate: `repository_id`, `invariant_id`, `revision_id` (all UUID
pattern), `display_version`, `statement`, `applicability`, `conditions`, `exclusions`, `state_at_origin`,
`acceptance_ref`, `provenance`, `predecessors` and `payload_digest` (SHA-256 pattern).

Validators: `_require_nonblank_authored_text` strips `display_version`/`statement`/`applicability` and refuses a
blank; `_require_nonblank_clauses` strips clause entries, refuses a blank and **preserves order**, because the
order is the author's and the digest covers it; `_require_unique_predecessors` refuses a repeated revision
identity; and the after-validator `_require_self_consistent_acceptance` enforces the self-predecessor rule and
delegates the accepted/proposed rule to `base.require_consistent_acceptance` — an `accepted` origin needs a
nonempty `acceptance_ref`, and a `proposed` origin must not carry one. The two `ValueError` messages are unchanged
by the extraction; the rule moved so the family revision aggregate applies one owner's version instead of a
second copy.

StoredInvariantRevision wraps the decoded revision and its sorted predecessor tuple. The index row decoder constructs that tuple and verifies the aggregate payload digest; this wrapper declares no independent sorted-predecessor after-validator.

### Conventions

`InvariantIdentity` is the stable subject; a revision is one authored statement of it. The friendly display
version belongs to the revision's **label**, not to its identity: two successors of one revision may both display
`v2`, and that is a supported state rather than an identity conflict.

### Invariants And Boundaries

- Immutability is by construction: the digest seals the whole semantic payload including the sorted predecessor
  set, so a stored revision identifies exactly one authored aggregate.
- `conditions`/`exclusions` are tuples whose empty value is a recorded "none", never a missing value.
- Proposal is distinct from acceptance: `state_at_origin` is authored data, and the store manufactures no
  acceptance and exposes no promotion operation.
- InvariantRevision declares the aggregate; digest functions define its seal, and the index row decoder verifies it on read. store.py reads exact revisions and exposes no revision writer. The former insert-only canonical database operation was retired by MIK-R26.
- **The accepted/proposed rule is shared, not owned here.** It lives in `base.py` because both revision
  aggregates apply it at construction; a third revision kind must call it rather than restate it.
- **No change to this model's behaviour was made by the graph leaf.** The extraction is behaviour-preserving, and
  the revision's field set, validators and digest participation are unchanged.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The invariant identity shape, its nonblank display label and the row digest a label edit names. [1]
- The complete revision aggregate and its validators, including the self-predecessor rule. [2]
- The shared accepted/proposed rule this validator now delegates to. [3]
- The read-back shape that pins the sorted predecessor set. [4]
- The stored `invariant_revision` table this aggregate is written to, with its immutability triggers. [5]

- The current exact revision read and decoder verify a retained aggregate rather than writing it. [6]

The requirement packet whose normative property this model encodes: requirement packet `KS-R01@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it.

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
