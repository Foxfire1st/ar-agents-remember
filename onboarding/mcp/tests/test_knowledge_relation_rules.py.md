# mcp/tests/test_knowledge_relation_rules.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The scope statement: operation and failure behaviour, not constructor validation. [1]
- The anchored-claim atomicity node. [2]
- The two endpoint-refusal nodes that prove nothing was written. [3]
- The pair-uniqueness and the identity-reuse nodes. [4]
- The authored-role node. [5]
- The stale-caller removal and anchor-lifetime nodes. [6]
- The database-enforcement nodes: payload rewrite refusal and foreign keys. [7]
- The namespace sweep and the composed application-seam node. [8]
- The production modules under test. [9]
- The application seam this module is the only test importer of. [10]
- The unit-regression lane row this module is registered by. [11]
- The fixture contract that names this module as an exact consumer. [12]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
