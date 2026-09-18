# mcp/tests/test_knowledge_relation_rules.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_relation_rules.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `2dcacb27446ecbaba01b69ee32e2ac40a1713b09` |
| lastVerifiedCommitDate | 2026-09-18T17:26:34+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

Focused behaviour of the relation writes — anchors, memberships and realization claims. Each case
protects one consequential operation or failure: an endpoint the database **and** the operation both
constrain, a pair that may be related only once, an identity reuse that must not replace a stored
relation, a new anchor that must roll back with the claim that carried it, a removal that must name the
row it expects, and the database-level triggers that keep a stored relation from being re-pointed.
Constructor validation is **not** re-tested here.

## Code Commentary

### Logic

- The endpoint cases are the atomicity proof: a membership naming a missing family revision or
  invariant revision, and a realization naming a missing anchor, each refuse with the endpoint named
  and leave the whole-database `table_counts` unchanged.
- `test_a_new_anchor_and_its_claim_are_one_transaction` is the anchored-transaction node: the anchor is
  written before the claim's own duplicate checks, so the case that refuses afterwards must show **no**
  anchor row left behind. The review independently reproduced this by orphan probe rather than
  trusting the node.
- `test_the_same_endpoint_pair_is_related_only_once` and
  `test_a_reused_relation_identity_with_other_endpoints_refuses` cover the two distinct identity
  failures: the pair is `relationship_constraint`, the reused identity is `duplicate_identity`.
- `test_a_realization_role_is_authored_vocabulary` protects the "role is a claim, not an observation"
  rule at the model boundary.
- `test_an_explicit_removal_requires_the_row_the_caller_expects` is the stale-caller contract, and
  `test_a_cited_anchor_cannot_be_removed_and_an_uncited_one_can` is the anchor-lifetime contract.
- `test_relation_payloads_refuse_an_in_place_rewrite` and
  `test_foreign_keys_are_enforced_on_the_relation_tables` test the database's own enforcement, not the
  operation's pre-checks.
- `test_graph_operations_refuse_another_repository_namespace` sweeps the namespace boundary, and
  `test_the_application_seam_authors_a_graph_through_an_admitted_destination` drives the composed path
  (admit → create → reopen → read) rather than the store directly.

### Conventions

- This is the one graph module that imports the application seam, so the composed path is exercised
  somewhere; the other two go through the store so a failure is attributable to one layer.
- Cases that need a request shape the public builders do not produce construct it locally from the
  fixture's constants rather than adding a permissive builder to the shared support module.
- Every refusal case asserts the refusal code **and** the unchanged row counts, because a code alone
  does not prove nothing was written.

### Invariants And Boundaries

- **A relation is written once or not at all.** The atomicity cases are the executable form of that
  claim; the anchored-claim case is the only one where a row is deliberately written before a later
  check.
- **The endpoint kind is unrepresentable when wrong**, which is why the wrong-kind cases refuse at the
  database layer as well as through the operation's check.
- **A graph-valid relation is still only a claim.** No case asserts that a stored claim makes a
  statement true, and none should.
- **Boundary.** This module owns relation-write behaviour. Family-revision rules are
  `test_knowledge_family_revision.py`, the read contract is `test_knowledge_graph_reads.py`, and the
  payload seals are `test_knowledge_revision_seals.py`.

### Todos

None recorded for this slice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The scope statement: operation and failure behaviour, not constructor validation. | "Constructor validation is not re-tested here." | mcp/tests/test_knowledge_relation_rules.py:7-7 |
| The anchored-claim atomicity node. | "test_a_new_anchor_and_its_claim_are_one_transaction" | mcp/tests/test_knowledge_relation_rules.py:77-117 |
| The two endpoint-refusal nodes that prove nothing was written. | "test_a_membership_endpoint_that_does_not_exist_refuses_and_writes_nothing"; "test_a_realization_of_a_missing_anchor_refuses_and_writes_nothing" | mcp/tests/test_knowledge_relation_rules.py:118-159; mcp/tests/test_knowledge_relation_rules.py:160-187 |
| The pair-uniqueness and the identity-reuse nodes. | "test_the_same_endpoint_pair_is_related_only_once"; "test_a_reused_relation_identity_with_other_endpoints_refuses" | mcp/tests/test_knowledge_relation_rules.py:188-232; mcp/tests/test_knowledge_relation_rules.py:233-262 |
| The authored-role node. | "test_a_realization_role_is_authored_vocabulary" | mcp/tests/test_knowledge_relation_rules.py:263-304 |
| The stale-caller removal and anchor-lifetime nodes. | "test_an_explicit_removal_requires_the_row_the_caller_expects"; "test_a_cited_anchor_cannot_be_removed_and_an_uncited_one_can" | mcp/tests/test_knowledge_relation_rules.py:305-363; mcp/tests/test_knowledge_relation_rules.py:364-413 |
| The database-enforcement nodes: payload rewrite refusal and foreign keys. | "test_relation_payloads_refuse_an_in_place_rewrite"; "test_foreign_keys_are_enforced_on_the_relation_tables" | mcp/tests/test_knowledge_relation_rules.py:414-441; mcp/tests/test_knowledge_relation_rules.py:442-472 |
| The namespace sweep and the composed application-seam node. | "test_graph_operations_refuse_another_repository_namespace"; "test_the_application_seam_authors_a_graph_through_an_admitted_destination" | mcp/tests/test_knowledge_relation_rules.py:473-565; mcp/tests/test_knowledge_relation_rules.py:566-680 |
| The production modules under test. | `create_source_anchor`; `create_family_member`; `create_realization_claim` | mcp/src/agents_remember/memory/knowledge/anchors.py:49-68; mcp/src/agents_remember/memory/knowledge/memberships.py:88-107; mcp/src/agents_remember/memory/knowledge/realizations.py:61-81 |
| The application seam this module is the only test importer of. | `create_knowledge_family`; `create_knowledge_family_member`; `create_knowledge_realization_claim` | mcp/src/agents_remember/application/knowledge.py:423-438; mcp/src/agents_remember/application/knowledge.py:471-486; mcp/src/agents_remember/application/knowledge.py:495-510 |
| The unit-regression lane row this module is registered by. | "mcp/tests/test_knowledge_relation_rules.py" | mcp/tests/test-evidence-lanes.toml:106-106 |
|  The fixture contract that names this module as an exact consumer. | "contract:knowledge-identity-branching-fixture" | mcp/tests/evidence-lifecycle.toml:1187-1187  |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:knowledge-identity-branching-fixture" repointed to mcp/tests/evidence-lifecycle.toml:1187-1187. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_relation_rules.py" repointed to mcp/tests/test-evidence-lanes.toml:106-106. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_knowledge_relation_rules.py" repointed to mcp/tests/test-evidence-lanes.toml:104-104. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_relation_rules.py" repointed to mcp/tests/test-evidence-lanes.toml:102-102. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-identity-branching-fixture" repointed to mcp/tests/evidence-lifecycle.toml:1183-1183. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_relation_rules.py" repointed to mcp/tests/test-evidence-lanes.toml:89-89. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 7 generated projection bullet(s) by hand while resolving the memory sync** — `mcp/tests/test_knowledge_relation_rules.py`, `create_knowledge_family`, `create_knowledge_family_member`, `create_knowledge_realization_claim`, `create_source_anchor`, `create_family_member`, `create_realization_claim`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 5 generated projection bullet(s) by hand** — `mcp/tests/test_knowledge_relation_rules.py`, `create_knowledge_family`, `create_knowledge_family_member`, `create_knowledge_realization_claim`, `create_source_anchor`, `create_family_member`, `create_realization_claim`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_knowledge_relation_rules.py"` → `mcp/tests/test-evidence-lanes.toml:84-84`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-17T08:11:27+00:00 — 260915-KS-L9 curator (memory-quality closure): re-read every reopened claim in this card against code commit `c22beb0121946c0637e113ec4cf29da29fd4aec7` and advanced the verification stamp to that commit, which closeout re-stamps. A generated citation repair had already rewritten these ranges mechanically, so each was re-read rather than trusted: the range was checked against the current definition of the construct the claim is about, and the wording still holds. Extents chosen: `create_source_anchor`; `create_family_member`; `create_realization_claim` at mcp/src/agents_remember/memory/knowledge/anchors.py:49-68; mcp/src/agents_remember/memory/knowledge/memberships.py:88-107; mcp/src/agents_remember/memory/knowledge/realizations.py:61-81.

- 2026-09-17T08:11:27+00:00 — 260915-KS-L9 curator (memory-quality closure): re-read every reopened claim in this card against code commit `c22beb0121946c0637e113ec4cf29da29fd4aec7` and advanced the verification stamp to that commit, which closeout re-stamps. A generated citation repair had already rewritten these ranges mechanically, so each was re-read rather than trusted: the range was checked against the current definition of the construct the claim is about, and the wording still holds. Extents chosen: `create_source_anchor`; `create_family_member`; `create_realization_claim` at mcp/src/agents_remember/memory/knowledge/anchors.py:49-68; mcp/src/agents_remember/memory/knowledge/memberships.py:88-107; mcp/src/agents_remember/memory/knowledge/realizations.py:61-81.

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `create_knowledge_family_member` in the row 99 of this card from mcp/src/agents_remember/application/knowledge.py:495-497 to mcp/src/agents_remember/application/knowledge.py:86, the extent of the construct the claim is about (the checker named line(s) [86, 471] as its live location); re-pointed `create_knowledge_realization_claim` in the row 99 of this card from mcp/src/agents_remember/application/knowledge.py:86 to mcp/src/agents_remember/application/knowledge.py:88, the extent of the construct the claim is about (the checker named line(s) [88, 495] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `create_knowledge_family_member` in the row 99 of this card from mcp/src/agents_remember/application/knowledge.py:423-425 to mcp/src/agents_remember/application/knowledge.py:471-473, the extent of the construct the claim is about (the checker named line(s) [86, 471] as its live location); re-pointed `create_knowledge_realization_claim` in the row 99 of this card from mcp/src/agents_remember/application/knowledge.py:471-473 to mcp/src/agents_remember/application/knowledge.py:495-497, the extent of the construct the claim is about (the checker named line(s) [88, 495] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `create_knowledge_family_member` in the row 99 of this card from mcp/src/agents_remember/application/knowledge.py:495-497 to mcp/src/agents_remember/application/knowledge.py:471-473, the extent of the construct the claim is about (the checker named line(s) [86, 471] as its live location); re-pointed `create_knowledge_family` in the row 99 of this card from mcp/src/agents_remember/application/knowledge.py:471-473 to mcp/src/agents_remember/application/knowledge.py:423-425, the extent of the construct the claim is about (the checker named line(s) [85, 423] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-read the reopened claim in the row 98 of this card against the current code: its anchor still resolves inside the cited range, so the wording holds and the stamp advances

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/src/agents_remember/application/knowledge.py:423-425 in the row 99 of this card; the repetition added no pooled evidence

- 2026-09-16T06:24:00+00:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): created this one-to-one card for the new relation-rules test module. It records the atomicity claim its endpoint and anchored-claim cases carry (a refusal leaves the whole-database counts unchanged), the separation between the pair-uniqueness and identity-reuse failures, the database-level enforcement nodes that are distinct from the operation's own pre-checks, and the fact that this is the only graph module driving the composed application seam. Verification metadata remains empty until closeout stamps the code commit.
