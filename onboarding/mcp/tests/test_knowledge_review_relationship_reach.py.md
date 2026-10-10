# mcp/tests/test_knowledge_review_relationship_reach.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose
Pins relationship evidence at exact member heads, recorded pairings and qualified rename observations.

## Code Commentary
A member's moved realization is displayed at its own selected head; ambiguous heads remain unresolved. A withdrawal does not deny a relationship the same payload displays, and retained memberships appear once. Pairing states the recorded relation it uses, never an address resemblance. Rename inference distinguishes measured absence from a measurement not made.

Test-only knowledge_rows_test_support family/revision/membership operations construct the input populations. Real review composition supplies the rendered evidence and refusals; the cases do not reinstate the retired family or membership authoring plane.

### Logic
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

### Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring, the
five fixture builders and the seven cases.

- `test_a_member_identities_moved_realization_is_displayed_at_its_own_head` supplies the current fixture or assertion described above. [10]
- `test_a_withdrawal_never_denies_a_relationship_the_same_payload_displays` supplies the current fixture or assertion described above. [11]
- `test_a_pairing_is_qualified_and_an_address_resemblance_never_pairs` supplies the current fixture or assertion described above. [12]
- `test_the_rename_inference_separates_a_measured_absence_from_a_measurement_never_made` supplies the current fixture or assertion described above. [13]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [14]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [15]

- The module's own statement of the five states the ruling turns on, and the candidate-only paths the cases author. [16]
- **The ruling measured: a member identity's movement displayed at its own established head, with the new address displayed and the old one still listed.** [17]
- **The multi-ended line unresolved with its reason and never a denial.** [18]
- **One payload may not contradict itself: the withdrawn rows name the candidate row citing the same revision.** [19]
- The member-wise family pairing, each membership displayed once. [20]
- **Every pairing states the recorded relation it was made on, and an address resemblance never pairs.** [21]
- **The two rename non-pairing states kept apart, and the similarity word present only where Git paired.** [22]
- The sibling case module whose builders this module imports, and the two exact-scope support rows it is registered on. [23]

### Docs References

No Domain Documentation source is configured for this slice.

### Cross-Repo References

No cross-repository behavior is exercised in this file.

No applicable cross-repository source was found.
