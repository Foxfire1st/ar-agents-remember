# mcp/src/agents_remember/memory/knowledge/compositions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/compositions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:10+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25`|
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l17` uncommitted source; base `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The **authored composition edge** between two exact family revisions, the **canonical owning route**
of a family *revision*, and the **authored explanatory context** with its append-only revision chain.
One module, three authored acts, all of them writes into generation 5's six tables.

The module owns the write path and the reads that answer "what did somebody author here". It does
**not** own the traversal policy (`composition_policies.py`), the declared-policy walk
(`composition_traversal.py`), the Family projection (`family_view.py`) or the cycle rule
(`lineages.py` supplies edges to the shared rule in `lineage.py`). That split is by protected
property, not by size: the edge, the route and the context share one preconditions-and-receipts
shape, while the policy and the traversal are different questions asked about the same edges.

**The edge is authored, never inferred.** There is no code here that derives a relationship from a
display label, a folder or path ancestry, a prefix, a symbol, a shared member, a shared anchor or a
prose sentence. Two endpoints are typed columns with repository-scoped composite foreign keys to
`family_revision(repository_id, revision_id)`, so a wrong endpoint kind is *unrepresentable* rather
than merely rejected, and there is deliberately no polymorphic `(target_kind, target_id)` column and
no `related_to` for an unchecked identity to land in.

## Code Commentary

### Logic

- `insert_composition` — the one write of an edge. It resolves both endpoints against the stored
  family revisions, refuses an endpoint this namespace does not hold **before any row is written and
  with the offending identity named**, and then inserts under the declared unique tuple. The
  duplicate lookup runs first, so a second bare edge is refused with a typed refusal before either
  partial unique index is reached.
- `find_composition_by_pair` and `composition_links_of_revision` — the two reads of the edge. The
  second returns every link of one revision *in declared order*, and it reports **both** rows when one
  pair carries two different declared policies: two separately authored meanings are two rows, and
  neither is silently preferred.
- `insert_family_revision_route` — records the canonical owning route of the revision aggregate.
  `require_route_endpoint` validates that the route is authored in this namespace, so a route that
  does not exist refuses **before** the association is written. This is the *revision* altitude, a
  different fact from generation 2's identity-level `family_route`.
- `owning_route_of_family_revision` — returns the recorded route, or `None` for the explicit
  **ungoverned** state. It never defaults to the repository root, to the identity's own route, or to
  a route derived from where the members live.
- `insert_context_revision`, `get_context_revision`, `context_of_family_revision` — the authored
  explanatory context. Its subject is bound exactly (both the family identity and the family
  revision), a successor's predecessor must already be stored, and `get_context_revision` is the read
  that returns the **earlier** text after a successor appends. The context is separable from the
  seal: no column here could hold a joint guarantee, and editing the context never rewrites one.
- `composition_row_digest`, `owning_route_row_digest`, `context_row_digest` — the row digests the
  receipt surfaces compare by value. They identify **authored rows**, not content: the context
  itself carries no content address, no logical fingerprint and no digest of its own.

### Conventions

- Every write goes through the batch path, and every modelled failure is returned as a typed
  `KnowledgeRefusal`, never raised as a bare exception for a caller to interpret.
- Authorship travels as an encoded provenance envelope on every row; a row with no provenance is not
  representable.
- Immutability is enforced twice on purpose: the operation's preconditions return the typed refusal,
  and generation 5's triggers raise `immutable_revision:` so a changeset, a repair script or a future
  code path that forgot the rule still cannot repoint or delete a row.

### Invariants And Boundaries

- **An authored row is immutable.** There is no update and no delete path here; a correction is a
  **new** edge, a new route record or a newly identified context revision. The earlier text survives
  the correction.
- **One pair under one declared policy version is stored once.** A second *policy* over the same pair
  is a second row and is reported as such. The unique tuple is two partial unique indexes rather than
  one table `UNIQUE`, because a table constraint over the nullable `policy_id` would not enforce
  uniqueness for `NULL`s.
- **The context is not a hiding place for an obligation.** A condition read as context is a review
  finding, and no read here performs that reading; the boundary is stated in the module and in
  `models/knowledge/composition.py`.
- **No row here carries task status, seat ownership, a lifecycle gate or approval authority**, so
  nothing in this module becomes an independently editable competing contract.
- **Boundary.** This module writes and reads authored rows. It does not decide whether the composition
  graph is acyclic — that is the shared rule's job, fed by `lineages.composition_edges` — and it does
  not walk edges under a policy.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one composition-edge write, which resolves both endpoints and names the offending identity in its refusal. | `insert_composition` | mcp/src/agents_remember/memory/knowledge/compositions.py:120-120 |
| **The duplicate lookup that refuses a second row for the same declared tuple before either partial unique index is reached.** | `find_composition_by_pair` | mcp/src/agents_remember/memory/knowledge/compositions.py:244-244 |
| **The read that reports every stored link of one revision in declared order, including two policies over one pair.** | `composition_links_of_revision` | mcp/src/agents_remember/memory/knowledge/compositions.py:279-279 |
| The revision-altitude owning-route write, which refuses a route this namespace does not hold. | `insert_family_revision_route` | mcp/src/agents_remember/memory/knowledge/compositions.py:334-334 |
| **The owning-route read that returns the explicit ungoverned state rather than inferring a route.** | `owning_route_of_family_revision` | mcp/src/agents_remember/memory/knowledge/compositions.py:392-392 |
| The context write, whose subject is bound to the exact family revision and whose predecessor must already be stored. | `insert_context_revision` | mcp/src/agents_remember/memory/knowledge/compositions.py:417-417 |
| **The read that returns the earlier context text after a successor appends.** | `get_context_revision` | mcp/src/agents_remember/memory/knowledge/compositions.py:618-618 |
| The read the projection uses for one revision's recorded context. | `context_of_family_revision` | mcp/src/agents_remember/memory/knowledge/compositions.py:642-642 |
| The edge fingerprint the receipt surface compares, which is an authored-row identity and not a content address on the context. | `_edge_fingerprint` | mcp/src/agents_remember/memory/knowledge/compositions.py:768-768 |
| **The case that drives three tables past the write path and proves no update and no delete exists.** | "test_an_authored_edge_a_policy_and_a_context_are_immutable_at_the_database" | mcp/tests/test_knowledge_family_composition.py:606-606 |
| **The case that proves both policy rows over one pair are reported and neither is preferred.** | "test_one_pair_under_one_policy_is_stored_once_and_a_second_policy_is_a_second_edge" | mcp/tests/test_knowledge_family_composition.py:550-550 |
| The case that proves a recorded route governs and the ungoverned state is reported rather than filled. | "test_a_recorded_route_governs_and_the_ungoverned_state_is_reported_not_filled" | mcp/tests/test_knowledge_family_composition.py:705-705 |
| The case that proves the context is bound to the exact revision and a successor appends without rewriting the guarantee. | "test_a_context_is_bound_to_the_exact_revision_and_a_successor_appends" | mcp/tests/test_knowledge_family_composition.py:787-787 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_an_authored_edge_a_policy_and_a_context_are_immutable_at_the_database" repointed to mcp/tests/test_knowledge_family_composition.py:606-606. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_one_pair_under_one_policy_is_stored_once_and_a_second_policy_is_a_second_edge" repointed to mcp/tests/test_knowledge_family_composition.py:550-550. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_recorded_route_governs_and_the_ungoverned_state_is_reported_not_filled" repointed to mcp/tests/test_knowledge_family_composition.py:705-705. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_context_is_bound_to_the_exact_revision_and_a_successor_appends" repointed to mcp/tests/test_knowledge_family_composition.py:787-787. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_a_context_is_bound_to_the_exact_revision_and_a_successor_appends" repointed to mcp/tests/test_knowledge_family_composition.py:762-762. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_an_authored_edge_a_policy_and_a_context_are_immutable_at_the_database" repointed to mcp/tests/test_knowledge_family_composition.py:581-581. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_one_pair_under_one_policy_is_stored_once_and_a_second_policy_is_a_second_edge" repointed to mcp/tests/test_knowledge_family_composition.py:525-525. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_a_recorded_route_governs_and_the_ungoverned_state_is_reported_not_filled" repointed to mcp/tests/test_knowledge_family_composition.py:680-680. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_a_context_is_bound_to_the_exact_revision_and_a_successor_appends" repointed to mcp/tests/test_knowledge_family_composition.py:759-759. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T06:30:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read each of this card's reopened claims against the construct as the merged line now stands, confirmed the cited range is current, and retired 4 generated projection bullet(s) by hand** — `test_a_context_is_bound_to_the_exact_revision_and_a_successor_appends`, `test_a_recorded_route_governs_and_the_ungoverned_state_is_reported_not_filled`, `test_an_authored_edge_a_policy_and_a_context_are_immutable_at_the_database`, `test_one_pair_under_one_policy_is_stored_once_and_a_second_policy_is_a_second_edge`. A mechanically projected range is unverified evidence, which is exactly why the check kept these claims reopened until an agent had read the construct they point at; the claims' wording is retained because each states what the construct does, and the ranges are the declarations the claims are about. Verification metadata advances to the merged base commit `15fe8678`.

- 2026-09-18T04:10:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): created this one-to-one card for the composition write module. It records that the edge is **authored and never inferred**, that a wrong endpoint kind is unrepresentable rather than merely rejected, that the module reports `None` for the explicit **ungoverned** state instead of deriving a route from where the members live, and that a correction is a new authored row rather than an update or a delete. It records the one-pair/two-policies decision (both rows reported, neither preferred) and the two partial unique indexes that enforce the declared tuple because a table `UNIQUE` over a nullable column would not stop a second bare edge. Verification metadata is the leaf's base commit `e963a01c`: the code commit does not exist yet and closeout owns that stamp.
