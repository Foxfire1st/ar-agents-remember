# mcp/src/agents_remember/models/knowledge/composition.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/composition.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:24+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b`|
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l17` uncommitted source; base `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The four command kinds, published as a named constant so a later leaf unions its own set rather than restating members.** | `COMPOSITION_COMMAND_KINDS` | mcp/src/agents_remember/models/knowledge/composition.py:62-62 |
| **The six record tables those commands write, exactly generation 5's appended set.** | `COMPOSITION_WRITABLE_TABLES` | mcp/src/agents_remember/models/knowledge/composition.py:71-71 |
| **The one registered scope a traversal policy may widen, and nothing else.** | `REGISTERED_REVIEW_SCOPE` | mcp/src/agents_remember/models/knowledge/composition.py:45-45 |
| The closed direction vocabulary, which decides which endpoints a traversal may step through. | `FOLLOW_DIRECTIONS` | mcp/src/agents_remember/models/knowledge/composition.py:51-51 |
| **The value-boundary half of the policy validation: a half-declared policy fails construction.** | `FamilyCompositionPolicyDraft` | mcp/src/agents_remember/models/knowledge/composition.py:83-83 |
| The stored policy version, whose row identity and author spelling are separate fields. | `FamilyCompositionPolicyVersion` | mcp/src/agents_remember/models/knowledge/composition.py:110-110 |
| The reported link, carrying its direction and the policy version it was declared under. | `FamilyCompositionLink` | mcp/src/agents_remember/models/knowledge/composition.py:179-179 |
| **The authored context model, which declares no content address, digest or fingerprint of its own.** | `FamilyExplanationContext` | mcp/src/agents_remember/models/knowledge/composition.py:206-206 |
| The context draft, whose successor cites a predecessor that must already be stored. | `FamilyExplanationContextDraft` | mcp/src/agents_remember/models/knowledge/composition.py:244-244 |
| **The case that proves the union is exactly its own members and the six tables declare no content-address column.** | "test_the_composition_commands_are_the_closed_unions_own_members" | mcp/tests/test_knowledge_family_composition.py:244-244 |
| **The case that proves every half-declared policy state is refused at the value boundary.** | "test_the_declared_policy_shape_refuses_every_half_declared_state" | mcp/tests/test_knowledge_family_composition.py:282-282 |
| **The facet suite's re-scoped assertion, which now unions this leaf's published constant instead of a literal.** | "test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables" | mcp/tests/test_knowledge_facets.py:901-901 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables" repointed to mcp/tests/test_knowledge_facets.py:901-901. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables" repointed to mcp/tests/test_knowledge_facets.py:866-866. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_the_composition_commands_are_the_closed_unions_own_members" repointed to mcp/tests/test_knowledge_family_composition.py:244-244. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_the_declared_policy_shape_refuses_every_half_declared_state" repointed to mcp/tests/test_knowledge_family_composition.py:282-282. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables" repointed to mcp/tests/test_knowledge_facets.py:824-824. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T06:30:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read each of this card's reopened claims against the construct as the merged line now stands, confirmed the cited range is current, and retired 2 generated projection bullet(s) by hand** — `test_the_composition_commands_are_the_closed_unions_own_members`, `test_the_declared_policy_shape_refuses_every_half_declared_state`. A mechanically projected range is unverified evidence, which is exactly why the check kept these claims reopened until an agent had read the construct they point at; the claims' wording is retained because each states what the construct does, and the ranges are the declarations the claims are about. Verification metadata advances to the merged base commit `15fe8678`.

- 2026-09-18T06:09:03+00:00: Generated citation repair: "test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables" repointed to mcp/tests/test_knowledge_facets.py:816-816. No content impact: mechanical anchor-range projection bound to citation source snapshot 014df62463362d92ea768ade7d81f0ca0b615347d5c6feed94e130d80244a24d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T06:06:32+00:00: Generated citation repair: "test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables" repointed to mcp/tests/test_knowledge_facets.py:817-817. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T04:24:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): created this one-to-one card for the composition vocabulary. It records why the four command kinds and six writable tables are **published named constants** rather than literals — so a case pins membership by unioning declarations, which is what the facet suite's re-scoped assertion now does — and it records the value-boundary half of the two-place policy validation. It records that no value model here carries a content address, that the one registered scope is the only thing a policy may widen, and that the two shipped `Literal` unions gained this leaf's members (`create_composition` and `set_family_revision_route`, and the read operation `follow_family_composition`). Verification metadata is the leaf's base commit `e963a01c`: the code commit does not exist yet and closeout owns that stamp.
