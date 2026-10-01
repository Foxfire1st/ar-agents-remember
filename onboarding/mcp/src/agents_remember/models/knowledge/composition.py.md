# mcp/src/agents_remember/models/knowledge/composition.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The **composition vocabulary**: the closed command kinds and record tables this leaf adds, the one
registered review scope a traversal policy may widen, the closed direction vocabulary, the value
models a caller supplies for an edge and a policy version, and the reported models the reads and the
projection return.

It is a value-boundary module: it decides what a **half-declared** policy, an edge, a link and an
authored context *are*, and refuses at construction what the store would otherwise have to refuse at
write time. The other half of that validation lives in the tables' own `CHECK` constraints, and the
two exist together on purpose.

## Code Commentary

### Logic

- `COMPOSITION_COMMAND_KINDS` — the closed set of four candidate command kinds this leaf adds:
  `add_family_composition_policy`, `add_family_composition`, `set_family_revision_route` and
  `author_family_explanation_context`.
- `COMPOSITION_WRITABLE_TABLES` — the closed set of six record tables those commands write, exactly
  generation 5's six appended tables.
- **Both are published as named constants rather than inlined into the union literal**, so a case
  that pins the union's membership unions *this leaf's declaration* with the earlier leaves'
  declarations instead of restating the members. That is why the facet suite's re-scoped assertion
  reads `18 + len(COMPOSITION_COMMAND_KINDS)` rather than a new literal: a later leaf appends its own
  named set and nothing has to be re-derived from a count.
- `FamilyCompositionPolicyDraft` and `FamilyCompositionPolicyVersion` — one declared policy version
  as a caller supplies it, and as it is stored. `policy_version_id` (the immutable row identity an
  edge cites) and `declared_version` (the author's own version spelling) are **separate fields**,
  because re-spelling a version is a new version row rather than a repointed reference in every edge
  that cited it.
- `FamilyCompositionDraft` and `FamilyComposition` — the edge. Both endpoints are typed family
  revisions; there is no target-kind column, no target-id column and no `related_to`.
- `FamilyCompositionLink` — the reported link, carrying its direction and the policy version it was
  declared under.
- `FamilyExplanationContext` and `FamilyExplanationContextDraft` — the authored explanatory context
  and its immutable revisions, with `is_first_revision` naming the "no predecessor" idiom (a chain's
  first revision names itself).
- `WidenedScope`, `REGISTERED_REVIEW_SCOPE` and `FOLLOW_DIRECTIONS` — the closed vocabularies. A
  policy may add scope to a **named** scope and nothing else, and a direction is a rule rather than a
  hint: it decides which endpoints a traversal may step through.

### Conventions

- **No value model here carries a content address, a logical digest or a fingerprint.** The context
  in particular declares none, so the prose cannot become a second identity authority.
- **Malformed policies are unrepresentable at the value boundary**: a draft missing its version, its
  direction, its bound or its scope fails construction rather than reaching a store to be refused
  there. The table `CHECK`s are the second, independent half.
- Every model here is a `KnowledgeModel`; the leaf adds no new base type and no new refusal
  vocabulary of its own — the composition refusals are restated through the shipped codes.

### Invariants And Boundaries

- **The vocabulary is closed, and it is closed over named sets.** A caller cannot widen the union by
  spelling a new kind; a new kind is a new named constant an owning leaf publishes.
- **No command kind here can carry a conclusion.** The four kinds author rows; none records a status,
  a seat, a gate or an approval, so nothing in this vocabulary becomes a competing contract.
- **Boundary.** This module declares shape and refusal at the value boundary. It writes nothing,
  reads nothing, and decides nothing about whether a graph is acyclic.

### Todos

None recorded. The registered-review-scope *construction* is a later leaf's; this module publishes
the one scope name such a construction may widen.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The four command kinds, published as a named constant so a later leaf unions its own set rather than restating members.** [1]
- **The six record tables those commands write, exactly generation 5's appended set.** [2]
- **The one registered scope a traversal policy may widen, and nothing else.** [3]
- The closed direction vocabulary, which decides which endpoints a traversal may step through. [4]
- **The value-boundary half of the policy validation: a half-declared policy fails construction.** [5]
- The stored policy version, whose row identity and author spelling are separate fields. [6]
- The reported link, carrying its direction and the policy version it was declared under. [7]
- **The authored context model, which declares no content address, digest or fingerprint of its own.** [8]
- The context draft, whose successor cites a predecessor that must already be stored. [9]
- **The case that proves the union is exactly its own members and the six tables declare no content-address column.** [10]
- **The case that proves every half-declared policy state is refused at the value boundary.** [11]
- **The facet suite's re-scoped assertion, which now unions this leaf's published constant instead of a literal.** [12]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
