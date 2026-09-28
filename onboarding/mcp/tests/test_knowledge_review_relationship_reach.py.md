# mcp/tests/test_knowledge_review_relationship_reach.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_review_relationship_reach.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T19:40:00+02:00 |
| lastVerifiedCommitHash | `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` |
| lastVerifiedCommitDate | 2026-09-29T00:17:28+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The **reach** case module (`ICR-R08@v1`'s fix round): the five states the master's ruling turns on,
each authored through the public store operations and read back through the production composition.
They live beside the packet's own cases in `test_knowledge_review_relationship_movement.py`, which this
module imports its builders from rather than duplicating them.

The measured states are: a **member** identity's realization re-authored onto a successor revision the
comparison's page never selects (the review must read the relationship at the head of the citation's
authored successor line, through ICR-R07's own head rule, and display one movement with both
addresses); a member line whose head is **not unique** (unresolved *with its reason*, and no sentence
may claim that nothing is recorded); a citation the candidate **re-records** under a new row with no
authored edge (the withdrawn rows name that row instead of denying it, because one payload may not
contradict itself about the store); a family revision that **keeps its members** (memberships pair
member-wise, so each is displayed once and named a reassignment); and a fresh row at the **same
address** as a moved realization (an address resemblance never pairs, and a movement that does pair
states the recorded relation it used).

## Code Commentary

### Logic

**Each fixture authors exactly the shape its case measures, through the store's own operations.**
`build_member_move_fixture` re-records a member identity's realization onto a successor revision,
`build_split_head_fixture` authors a citation whose authored line ends in two revisions,
`build_same_citation_fixture` adds a candidate row citing the *same* revision at a new address with no
authored edge, `build_family_same_members_fixture` moves a family revision while keeping two member
revisions, and `build_pairing_qualification_fixture` places a fresh row at the very address a moved
realization names. All five use the shared endpoint enclosure and the public store operations
(`families`, `memberships`, `FamilyMemberRequest`, `FamilyRevisionRequest`) — no case hand-writes a
payload.

**Seven cases, one distinct user operation each:**

- `test_a_member_identities_moved_realization_is_displayed_at_its_own_head` — the ruling: the new
  address is displayed, the old one stays listed, both under one identity, with the head-selection
  owner named as the pairing basis.
- `test_a_member_line_with_no_single_head_is_unresolved_and_never_denied` — the multi-ended line yields
  `successor_line_unresolved` with its reason and asserts no negative.
- `test_a_withdrawal_never_denies_a_relationship_the_same_payload_displays` — the withdrawn rows
  *name* the candidate row citing the same revision (V1), so one payload cannot contradict itself.
- `test_a_family_revision_that_keeps_its_members_displays_each_membership_once` — member-wise pairing
  (V3): each membership displayed once, `reassigned`, and no sibling mis-named.
- `test_a_pairing_states_the_recorded_relation_it_was_made_on` — every paired movement carries a typed
  `pairing_basis` and a sentence naming the recorded relation (V4).
- `test_a_pairing_is_qualified_and_an_address_resemblance_never_pairs` — a fresh row at the movement's
  own address is its own addition, not a continuation.
- `test_the_rename_inference_separates_a_measured_absence_from_a_measurement_never_made` — `not_paired`
  and `unavailable` are different states, and only the measured pairing carries a similarity word.

**The inference cases use the module's own seam.** The last case builds the observation values directly
through `RenameObservations`/`_with_inference`, because the state that must be measured is the one a
substituted probe produces — a real Git failure shares the branch but is not what is measured here.

### Conventions

Imports go through the composition and the public store operations, plus the sibling case module's
builders (`build_endpoint_fixture`, `author_claim`, `author_revision`, `remove_claim`,
`realization_movements`, `review_of`, `ClaimDraft`) — which is why the module is registered on both
exact-scope consumer rows of `mcp/tests/evidence-lifecycle.toml` (the Nineteenth deliberate re-pin) and
has its own `unit-regression` lane row in `mcp/tests/test-evidence-lanes.toml`.
`pytestmark = pytest.mark.evidence_unit` puts it in the ordinary unit lane. The private helpers it
imports from the rename module (`RENAME_INFERENCE_COMMAND`, `_with_inference`) are that module's own
seam and are used only to build one labelled value.

### Invariants And Boundaries

- **The ruling is measured, not asserted**: a relationship recorded outside the comparison's page is
  displayed with both addresses, and a line that cannot be resolved to one head is stated unresolved
  with its reason rather than denied.
- **Member-wise pairing is what keeps a family display honest**: a sibling membership holding a
  different member is never this association's record.
- **Every pairing states its recorded basis**, and an address resemblance never pairs.
- **Boundaries.** The authored-line cases (intermediate descendants, splits) are
  `test_knowledge_review_relationship_line.py`'s; the packet's own cases are the movement module's;
  browser mounting is `ICR-R24`'s and the acceptance journey `ICR-R25`'s.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring, the
five fixture builders and the seven cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the five states the ruling turns on, and the candidate-only paths the cases author. | `MEMBER_MOVED_PATH`; `SAME_CITATION_PATH` | mcp/tests/test_knowledge_review_relationship_reach.py:1-21; mcp/tests/test_knowledge_review_relationship_reach.py:68-71 |
| The fixtures that author each measured shape through the public store operations. | `build_member_move_fixture`; `build_split_head_fixture`; `build_same_citation_fixture`; `build_family_same_members_fixture`; `build_pairing_qualification_fixture` | mcp/tests/test_knowledge_review_relationship_reach.py:74-114; mcp/tests/test_knowledge_review_relationship_reach.py:117-142; mcp/tests/test_knowledge_review_relationship_reach.py:145-175; mcp/tests/test_knowledge_review_relationship_reach.py:178-237; mcp/tests/test_knowledge_review_relationship_reach.py:240-302 |
| **The ruling measured: a member identity's movement displayed at its own established head, with the new address displayed and the old one still listed.** | `test_a_member_identities_moved_realization_is_displayed_at_its_own_head` | mcp/tests/test_knowledge_review_relationship_reach.py:305-357 |
| **The multi-ended line unresolved with its reason and never a denial.** | `test_a_member_line_with_no_single_head_is_unresolved_and_never_denied` | mcp/tests/test_knowledge_review_relationship_reach.py:360-389 |
| **One payload may not contradict itself: the withdrawn rows name the candidate row citing the same revision.** | `test_a_withdrawal_never_denies_a_relationship_the_same_payload_displays` | mcp/tests/test_knowledge_review_relationship_reach.py:392-432 |
| The member-wise family pairing, each membership displayed once. | `test_a_family_revision_that_keeps_its_members_displays_each_membership_once` | mcp/tests/test_knowledge_review_relationship_reach.py:435-469 |
| **Every pairing states the recorded relation it was made on, and an address resemblance never pairs.** | `test_a_pairing_states_the_recorded_relation_it_was_made_on`; `test_a_pairing_is_qualified_and_an_address_resemblance_never_pairs` | mcp/tests/test_knowledge_review_relationship_reach.py:472-500; mcp/tests/test_knowledge_review_relationship_reach.py:503-541 |
| **The two rename non-pairing states kept apart, and the similarity word present only where Git paired.** | `test_the_rename_inference_separates_a_measured_absence_from_a_measurement_never_made`; `_inference_for`; `RenameObservations` | mcp/tests/test_knowledge_review_relationship_reach.py:544-591; mcp/src/agents_remember/application/review_rename_inference.py:238-288; mcp/src/agents_remember/application/review_rename_inference.py:77-88 |
| The sibling case module whose builders this module imports, and the two exact-scope support rows it is registered on. | `build_movement_fixture`; `build_endpoint_fixture` | mcp/tests/test_knowledge_review_relationship_movement.py:128-200; mcp/tests/test_knowledge_review_source_endpoints.py:202-234 |

## Cross-Repo References

No cross-repository behavior is exercised in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 1 citation into `mcp/tests/test_knowledge_review_source_endpoints.py` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`, confirmed from the enclosure contract): **created.** The module is new in this leaf (`ICR-R08@v1`) and this is its one-to-one card. It records the fix-round cases the master's ruling required on this packet — the member identity read at its own established head, the multi-ended line unresolved and never denied, the withdrawal that names the row it does not deny, member-wise family pairing, the stated pairing basis, the address resemblance that never pairs, and the two rename non-pairing states — plus the module's governed registration (both `consumer_scope = "exact"` rows in `mcp/tests/evidence-lifecycle.toml`, the Nineteenth deliberate re-pin, and its own lane row in `mcp/tests/test-evidence-lanes.toml`). **Basis accounting:** the verification pair above names this leaf's base, the last real commit the reading was taken against; the candidate is named here in the body rather than in a metadata row, and closeout owns the stamp once the code commit exists.
