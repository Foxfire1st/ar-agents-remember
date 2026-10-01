# mcp/src/agents_remember/memory/knowledge/endpoints.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The endpoint-existence checks shared by the two relation writes. A membership and a realization claim
both name an exact revision, and both must refuse a missing endpoint **with the offending identity
named** before any row is written. One module answers that question so the two operations cannot drift
into reporting different codes for the same failure, and so "the endpoint does not exist" stays a
single definition per endpoint kind.

This module owns no table. It is a two-function contract owner: the shared *question* the relation
modules ask, and the `RelationWrite` vocabulary that names which operation is asking.

## Code Commentary

### Logic

- `require_family_revision_endpoint` asks `families.family_id_of_revision` whether the named family
  revision exists in the bound namespace; when it does not, it raises `KnowledgeRefused` carrying
  `missing_relation_endpoint_refusal`.
- `require_invariant_revision_endpoint` asks `store.get_revision` the same question for the invariant
  half.
- Both refusals carry `endpoint_kind` as the human-readable kind ("family revision", "invariant
  revision"), the declared table, the relation identity and the endpoint identity, so a caller is sent
  to the exact row rather than to the relation in general.
- `RelationWrite` is a closed literal of the two relation operations. It exists so a refusal cannot
  name an operation that does not write relations.

**A sixth endpoint kind, and the strictest of them.** `require_facet_revision_endpoint` is the one operation `add_evidence_claim` adds to `RelationWrite`. It is deliberately stricter than the revision-table lookups beside it: a facet revision is a `record_revision` row whose *owning envelope* carries one of the eight authored-judgment kinds, so a stored revision of a detection record or of another evidence claim is not a facet revision and is refused as the missing endpoint it is — naming the kind the caller asked for and the identity it named — rather than resolving to 'some revision exists'. The module's own docstring records the vocabulary's history: the finding that closed it at two members, the facet leaf that took it to four, and this leaf's addition of `add_evidence_claim`, the one operation that resolves a claim's subject, its evidence anchor and every claimed-coverage endpoint.

### Conventions

- The functions take the opened store as their first argument, exactly like the operations that call
  them, and they never open a transaction of their own — they are called *inside* the caller's
  immediate transaction, before its first write.
- They raise `KnowledgeRefused` rather than returning a result. That is the package's internal
  control-flow signal: the calling operation catches it and converts it into its own typed refusal
  result, so the public surface never exposes an exception.

### Invariants And Boundaries

- **Checks come before any DML.** Both callers run these checks before their first `INSERT`, which is
  what makes "a refused relation writes nothing" true by ordering rather than by rollback.
- **The endpoint kinds are not interchangeable.** A family revision is resolved through the family
  module and an invariant revision through the store; neither can be substituted for the other, and
  the separate functions make that structurally visible.
- **One definition per failure.** The two relation modules do not carry their own "not found" wording
  or their own codes; a change here changes both relations at once, which is the point.
- **Boundary.** This module decides existence, not legality. Whether the *pair* is already related is
  the relation module's own duplicate check, and whether the row matches what the caller expected is
  the removal path's stale-precondition check.

### Todos

None recorded for this slice.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The one-definition-per-endpoint-kind rationale this module exists for. [1]
- The closed relation-operation vocabulary a refusal may name. [2]
- The family-revision endpoint check. [3]
- The invariant-revision endpoint check. [4]
- The refusal these checks raise, with its endpoint kind and identity facts. [5]
- The narrow ownership read that answers the family half. [6]
- The seal-verifying read that answers the invariant half. [7]
- The membership operation that calls both checks before its write. [8]
- The realization operation that calls the invariant check before its write. [9]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
