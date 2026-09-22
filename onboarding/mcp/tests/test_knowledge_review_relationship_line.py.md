# mcp/tests/test_knowledge_review_relationship_line.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_review_relationship_line.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T19:40:00+02:00 |
| lastVerifiedCommitHash | `dcf35a0e0fc06bccdafd22390b7588b0aea811bc` |
| lastVerifiedCommitDate | 2026-09-22T20:08:58+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The **authored line** case module (`ICR-R08@v1`, second and third verification rounds): the three
shapes the reach cases did not cover, each authored through the public store operations and read back
through the production composition.

- a relationship recorded at an **intermediate** descendant of the citation, with the line's head
  recording nothing — the whole line is read, so the address is displayed;
- a line **split** into two successors that each record a relationship — both are displayed and the
  split lineage names them, instead of a sentence denying what the same movement calls unresolved —
  and the split-only case, where the lineage sentence states the complete negative over the revisions
  that were read;
- a membership moved onto an unselected successor **family** revision holding the same member — read
  through the family-revision membership owner, so the member's new side is displayed and no sibling
  member is presented as this member's record.

## Code Commentary

### Logic

**Three fixtures, each authoring one line shape through the store's own operations.**
`build_split_with_relationships_fixture` authors one citation with two authored successors that each
record a realization claim, `build_intermediate_descendant_fixture` authors a two-step line whose head
records nothing and whose intermediate revision records the claim, and
`build_family_head_membership_fixture` moves a membership onto a successor family revision that keeps
the same member. They import the shared builders (`build_endpoint_fixture`, `author_claim`,
`author_revision`, `remove_claim`, `realization_movements`, `review_of`) from the sibling case modules
and reuse `build_split_head_fixture` from the reach module rather than re-authoring the same topology.

**Five cases, one distinct user operation each:**

- `test_a_split_line_that_records_relationships_names_them_and_never_denies` — the round-2 F1 fix: the
  lineage sentence names both successors, the rows recorded on them are displayed as their own
  movements, and no denial clause is emitted.
- `test_a_multi_head_line_with_relationships_never_claims_a_unique_head` — the round-3 F5 fix: a
  multi-ended line has no head, so neither row's sentence may say "uniquely established head"; each
  names the line that was read and the revision it records.
- `test_a_split_line_that_records_nothing_states_only_what_was_read` — the negative is complete over
  the revisions that were read, and nothing more is claimed.
- `test_a_relationship_on_an_intermediate_descendant_is_displayed` — the round-2 F3 fix: the whole line
  is read, not just its head.
- `test_a_membership_moved_onto_an_unselected_family_revision_is_displayed` — the family side is read
  through the family-revision owner, so the new side is displayed with its pairing basis.

### Conventions

Imports go through the composition and the public store operations, plus the sibling case modules'
builders — which is why the module is registered on both exact-scope consumer rows of
`mcp/tests/evidence-lifecycle.toml` (the Twentieth deliberate re-pin) and has its own `unit-regression`
lane row in `mcp/tests/test-evidence-lanes.toml`. `pytestmark = pytest.mark.evidence_unit` puts it in
the ordinary unit lane. The module's own path constants (`SPLIT_ONE_PATH`, `SPLIT_TWO_PATH`,
`INTERMEDIATE_PATH`) name the candidate-only files the cases author.

### Invariants And Boundaries

- **The whole authored line is read**, so a relationship at an intermediate descendant is displayed and
  a stated negative is complete over the revisions that were read.
- **A head is named only where one exists**: a multi-ended or cyclic line has none, so no sentence may
  claim one, and the row's basis sentence names the line it read and the revision it records.
- **No sentence denies what the same payload displays**, and the family side is read through the owner
  keyed by the family revision, so no sibling member is mis-named.
- **Boundaries.** The ruling's member-head and multi-head *reach* cases live in the reach module; this
  module owns the authored-line consequences; browser mounting is `ICR-R24`'s and the acceptance
  journey `ICR-R25`'s.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring, the
three fixture builders and the five cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the three shapes it owns and of the read-back the cases use. | `build_split_with_relationships_fixture` | mcp/tests/test_knowledge_review_relationship_line.py:1-14; mcp/tests/test_knowledge_review_relationship_line.py:57-99 |
| The fixtures that author an intermediate descendant, a split with relationships on both successors, and a membership moved onto a successor family revision. | `build_intermediate_descendant_fixture`; `build_family_head_membership_fixture` | mcp/tests/test_knowledge_review_relationship_line.py:102-146; mcp/tests/test_knowledge_review_relationship_line.py:149-208 |
| **The split line that names its recorded relationships and never denies them (round-2 F1).** | `test_a_split_line_that_records_relationships_names_them_and_never_denies` | mcp/tests/test_knowledge_review_relationship_line.py:211-263 |
| **The multi-ended line that never claims a unique head (round-3 F5).** | `test_a_multi_head_line_with_relationships_never_claims_a_unique_head` | mcp/tests/test_knowledge_review_relationship_line.py:266-291 |
| The split that records nothing: only what was read is claimed. | `test_a_split_line_that_records_nothing_states_only_what_was_read` | mcp/tests/test_knowledge_review_relationship_line.py:294-313 |
| **The relationship recorded on an intermediate descendant is displayed (round-2 F3).** | `test_a_relationship_on_an_intermediate_descendant_is_displayed` | mcp/tests/test_knowledge_review_relationship_line.py:316-350 |
| The membership moved onto an unselected successor family revision, read through the family-revision owner. | `test_a_membership_moved_onto_an_unselected_family_revision_is_displayed` | mcp/tests/test_knowledge_review_relationship_line.py:353-405 |
| The display sentences these cases pin, and the pairing bases the head rule chooses between. | `_withdrawal_statement`; `_BASIS_SENTENCES`; `_is_line_head` | mcp/src/agents_remember/application/review_relationship_display.py:398-458; mcp/src/agents_remember/application/review_relationship_display.py:354-387; mcp/src/agents_remember/application/review_relationship_movement.py:295-318 |
| The whole-line read and the head rule the cases measure. | `read_line_relationships`; `successor_line` | mcp/src/agents_remember/application/review_recorded_relationships.py:309-339; mcp/src/agents_remember/application/review_recorded_relationships.py:233-292 |
| The sibling case module this one imports its builders from, and the reach fixture it reuses. | `build_split_head_fixture`; `build_movement_fixture` | mcp/tests/test_knowledge_review_relationship_reach.py:117-142; mcp/tests/test_knowledge_review_relationship_movement.py:128-200 |

## Cross-Repo References

No cross-repository behavior is exercised in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`, confirmed from the enclosure contract): **created.** The module is new in this leaf (`ICR-R08@v1`) and this is its one-to-one card. It records the cases the second and third verification rounds required on the authored line: the split whose recorded relationships are named rather than denied, the multi-ended line that never claims a unique head, the split-only negative complete over the revisions read, the intermediate descendant that is displayed because the whole line is read, and the membership moved onto an unselected family revision read through the family owner. It also records the module's governed registration (both `consumer_scope = "exact"` rows in `mcp/tests/evidence-lifecycle.toml`, the Twentieth deliberate re-pin, and its own lane row in `mcp/tests/test-evidence-lanes.toml`). **Basis accounting:** the verification pair above names this leaf's base, the last real commit the reading was taken against; the candidate is named here in the body rather than in a metadata row, and closeout owns the stamp once the code commit exists.
