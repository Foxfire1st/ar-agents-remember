# mcp/tests/test_review_family_context_population.py

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

Exercises the family revision population and bounded readback through real text trees, application composition and HTTP continuation.

## Code Commentary

### Logic

One family recording several revisions — memberless successor heads, withdrawn-and-rerecorded
rosters, explicit history beside an ambiguous head — is not a shape a text tree can express
(rule 3), so those cases name their removal rather than asserting it. What the text topology still
measures: a recorded memberless family on both sides, a member joining or leaving a recorded
roster, the measured zero against the absent family, and the sparse walk preserving its
population — all pinned through the same production composition.

The new-member case records the sibling member in the direct family's roster without moving the
family revision. The removed-member case proves the old membership no longer pins the family
context. `_assert_primary_unchanged` checks revision selection, statements, conditions, the whole
evidence pane and the complete source inventory across those family-only changes.

### Conventions

Keep the existing comparison, family, roster and source/evidence owners. This module introduces no alternate store, selection policy or publication authority.

### Invariants And Boundaries

- A recorded memberless family stays recorded, not absent — distinct from the measured zero and from the absent family.
- A new primary invariant is genuinely before-absent without making its existing family before-absent.
- A removed member does not pin family context to its retained predecessor.
- Fixtures and passing tests are bounded verification, not published project intent or installed product acceptance.

### Todos

No unrelated repair is assigned to this file.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

The operative contract is defined by the repository sources below.

### Repo-Internal References

These current owners and cases establish the stated behavior.


- A recorded memberless family retains its guarantee and measured empty roster. [2]


- A new member retains the family's existing before counterpart. [4]


- A retained predecessor membership cannot pin the family after selection. [5]


- Primary knowledge, evidence and complete source inventory stay independent. [6]


- Sparse pages preserve the recorded population and primary panes through real HTTP walks. [7]
