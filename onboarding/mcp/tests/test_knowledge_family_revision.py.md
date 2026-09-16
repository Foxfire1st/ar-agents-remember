# mcp/tests/test_knowledge_family_revision.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_family_revision.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `27242ecbefd79f2e8fbc6db32e02013fa8298ba3`|
| lastVerifiedCommitDate | 2026-09-16T08:41:27+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The scope statement: operation and failure behaviour, not constructor validation. | "Constructor validation is not re-tested here." | mcp/tests/test_knowledge_family_revision.py:6-6 |
| The membership-resolves-its-guarantee node, which is the requirement's demonstration. | "test_a_family_membership_keeps_resolving_the_guarantee_it_was_authored_against" | mcp/tests/test_knowledge_family_revision.py:53-88 |
| The in-place guarantee rewrite refusal. | "test_an_in_place_family_guarantee_change_is_refused" | mcp/tests/test_knowledge_family_revision.py:89-129 |
| The seal-verifying read and the field-isolating digest node. | "test_reading_a_family_revision_verifies_its_payload_seal"; "test_a_family_revision_digest_seals_its_predecessor_set" | mcp/tests/test_knowledge_family_revision.py:130-149; mcp/tests/test_knowledge_family_revision.py:150-183 |
| The two predecessor refusals, each naming its endpoint. | "test_a_family_revision_of_an_unknown_family_refuses"; "test_a_family_predecessor_from_another_family_refuses_with_the_named_endpoint"; "test_a_dangling_family_predecessor_refuses_without_leaving_a_row" | mcp/tests/test_knowledge_family_revision.py:184-205; mcp/tests/test_knowledge_family_revision.py:206-237; mcp/tests/test_knowledge_family_revision.py:238-265 |
| The node that proves the family graph applies the same lineage rule as the invariant graph. | "test_the_family_lineage_rule_matches_the_invariant_rule" | mcp/tests/test_knowledge_family_revision.py:266-324 |
| The two-branch wording node. | "test_both_family_lineage_branches_are_worded_for_the_branch_they_describe" | mcp/tests/test_knowledge_family_revision.py:325-348 |
| The support builders this module consumes. | `FamilySeed`; `family_draft`; `sealed_family`; `insert_raw_family_revision`; `insert_raw_family_edge`; `table_counts` | mcp/tests/knowledge_graph_test_support.py:65-74; mcp/tests/knowledge_graph_test_support.py:121-135; mcp/tests/knowledge_graph_test_support.py:136-145; mcp/tests/knowledge_graph_test_support.py:185-190; mcp/tests/knowledge_graph_test_support.py:191-201; mcp/tests/knowledge_graph_test_support.py:176-184 |
| The production module under test. | `create_family`; `create_family_revision`; `get_family_revision`; `family_id_of_revision` | mcp/src/agents_remember/memory/knowledge/families.py:78-95; mcp/src/agents_remember/memory/knowledge/families.py:112-141; mcp/src/agents_remember/memory/knowledge/families.py:215-232; mcp/src/agents_remember/memory/knowledge/families.py:233-251 |
| The unit-regression lane row this module is registered by. | "mcp/tests/test_knowledge_family_revision.py" | mcp/tests/test-evidence-lanes.toml:67-67 |
| The fixture contract that names this module as an exact consumer. | `knowledge-identity-branching-fixture` | mcp/tests/evidence-lifecycle.toml:1031-1052 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): created this one-to-one card for the new family-revision test module. It records the requirement's own falsifier node (a membership citing F1 still resolves G1 after a successor exists), the field-isolating status of the repaired digest node and why it had to be repaired (sealed finding `260915-KS-L2-RV-1`), and the two-branch lineage wording contract. Verification metadata remains empty until closeout stamps the code commit.
