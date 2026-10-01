# mcp/tests/test_knowledge_review_relationship_reach.py

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring, the
five fixture builders and the seven cases.

- The module's own statement of the five states the ruling turns on, and the candidate-only paths the cases author. [1]
- The fixtures that author each measured shape through the public store operations. [2]
- **The ruling measured: a member identity's movement displayed at its own established head, with the new address displayed and the old one still listed.** [3]
- **The multi-ended line unresolved with its reason and never a denial.** [4]
- **One payload may not contradict itself: the withdrawn rows name the candidate row citing the same revision.** [5]
- The member-wise family pairing, each membership displayed once. [6]
- **Every pairing states the recorded relation it was made on, and an address resemblance never pairs.** [7]
- **The two rename non-pairing states kept apart, and the similarity word present only where Git paired.** [8]
- The sibling case module whose builders this module imports, and the two exact-scope support rows it is registered on. [9]

### Cross-Repo References

No cross-repository behavior is exercised in this file.

No applicable cross-repository source was found.
