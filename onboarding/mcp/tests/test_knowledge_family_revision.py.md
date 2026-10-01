# mcp/tests/test_knowledge_family_revision.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Focused behaviour of family identity and the immutable family revision aggregate. Each case protects
one consequential operation or failure: a guarantee that must not change behind an existing revision, a
lineage that must refuse a cross-family or dangling predecessor, the wider lineage rule that refuses a
candidate beneath a stored cycle, and the payload seal that makes a stored guarantee the one its
identity names. Constructor validation is **not** re-tested here.

## Code Commentary

### Logic

- The guarantee cases are the requirement's own falsifier: `test_a_family_membership_keeps_resolving_the_guarantee_it_was_authored_against`
  creates F1/G1, a successor F2/G2 and a second same-label successor, then reopens the database and
  shows the membership citing F1 still resolves G1's text. `test_an_in_place_family_guarantee_change_is_refused`
  proves the database refuses the rewrite rather than only the operation.
- `test_a_family_revision_digest_seals_its_predecessor_set` is the field-isolating node for the family
  payload: both seeds hold **every other sealed field equal**, and the assertion is that the two seals
  differ. It was repaired in the fix-verification round to isolate the predecessor set — the round-1
  version's seeds also differed in `revision_id`/`display_version`, so the assertion held for a reason
  other than the field it named (sealed finding `260915-KS-L2-RV-1`).
- The lineage cases come in both branches: a predecessor from another family and a dangling predecessor
  are `invalid_reference` with the named endpoint, and
  `test_the_family_lineage_rule_matches_the_invariant_rule` drives the **same** rule the invariant
  graph uses, which is why it is the registered evidence node for the shared support module.
- `test_both_family_lineage_branches_are_worded_for_the_branch_they_describe` protects the wording
  contract: the descending branch must not claim self-reachability.

### Conventions

- The fixture comes from `knowledge_fixture_test_support` through a `tmp_path`-scoped `fixture`
  function; every case reopens the database rather than reusing an open handle, so "it survives a
  reopen" is the default shape rather than a special case.
- `_revision_request` is the local helper that builds a `FamilyRevisionRequest` from the fixture's
  constants, so a case varies one field instead of restating the request.
- Raw state is created only through `knowledge_graph_test_support`'s two raw writes; nothing here
  writes a row directly.

### Invariants And Boundaries

- **A stored family revision is immutable**, and the two refusals that enforce it are tested at both
  layers: the operation's identity-reuse check and the database's `family_revision_no_update` trigger.
- **A guarantee is never derived from the members.** No case here constructs a guarantee out of member
  obligations, and none should: the two are separate authored claims.
- **The seal covers the predecessor set**, on both payloads; the sibling node for the invariant payload
  lives in `test_knowledge_revision_seals.py` because the mechanism is shared.
- **Boundary.** This module owns family-revision behaviour only. The shared support it uses is
  `knowledge_graph_test_support.py`; membership and claim behaviour is
  `test_knowledge_relation_rules.py`, and the graph read contract is `test_knowledge_graph_reads.py`.

### Todos

None recorded for this slice. The digit-1 node's own repair is recorded in its docstring and in the
route overview rather than as open work.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The scope statement: operation and failure behaviour, not constructor validation. [1]
- The membership-resolves-its-guarantee node, which is the requirement's demonstration. [2]
- The in-place guarantee rewrite refusal. [3]
- The seal-verifying read and the field-isolating digest node. [4]
- The two predecessor refusals, each naming its endpoint. [5]
- The node that proves the family graph applies the same lineage rule as the invariant graph. [6]
- The two-branch wording node. [7]
- The support builders this module consumes. [8]
- The production module under test. [9]
- The unit-regression lane row this module is registered by. [10]
- The fixture contract that names this module as an exact consumer. [11]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
