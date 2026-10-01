# mcp/tests/test_knowledge_review_relationship_line.py

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring, the
three fixture builders and the five cases.

- The module's own statement of the three shapes it owns and of the read-back the cases use. [1]
- The fixtures that author an intermediate descendant, a split with relationships on both successors, and a membership moved onto a successor family revision. [2]
- **The split line that names its recorded relationships and never denies them (round-2 F1).** [3]
- **The multi-ended line that never claims a unique head (round-3 F5).** [4]
- The split that records nothing: only what was read is claimed. [5]
- **The relationship recorded on an intermediate descendant is displayed (round-2 F3).** [6]
- The membership moved onto an unselected successor family revision, read through the family-revision owner. [7]
- The display sentences these cases pin, and the pairing bases the head rule chooses between. [8]
- The whole-line read and the head rule the cases measure. [9]
- The sibling case module this one imports its builders from, and the reach fixture it reuses. [10]

### Cross-Repo References

No cross-repository behavior is exercised in this file.

No applicable cross-repository source was found.
