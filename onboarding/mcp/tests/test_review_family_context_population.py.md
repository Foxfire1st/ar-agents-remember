# mcp/tests/test_review_family_context_population.py

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

Exercises the independent family revision population and bounded readback through real authored stores, application composition and HTTP continuation. Its selected-member cases separate primary invariant absence or removal from the family’s independently recorded counterpart.

## Code Commentary

### Logic

The canonical memberless-head and recorded-empty-family cases keep ambiguity, genuine absence and measured empty roster distinct. Family revision populations and history are checked against the family owner’s own stored lists.

The history case now treats a competing memberless head as genuine ambiguity even when only another head contains the selected invariant. It checks the complete retained population and both sides’ candidate head guarantees, with no selected guarantee on an unresolved side. A separate exact-family-revision request retains the named old revision and checks the complete recorded history. The prior membership-subset expectation was deliberately corrected rather than retained as a compatibility mode.

The new-member case authors a candidate-only invariant and an existing family’s successor retaining exact old siblings plus that member. The primary before statement stays absent, while family before/after guarantees and rosters are both present. The removed-member case authors a successor omitting the selected member and proves that the old after-side predecessor membership still exists; this prevents an empty-counterpart-only fix from passing.

`_assert_primary_unchanged` checks revision selection, before/after statement and conditions, the entire evidence pane and the complete source inventory across those family-only changes. Existing sparse HTTP page walks retain exact member/claim coverage, page bounds and primary panes across continuation; repeated member contexts are not counted as distinct memberships.

### Conventions

Keep the existing comparison, family, authored-head, roster and source/evidence owners. This module's role is documented by its own source and the concrete references below; it introduces no alternate store, selection policy or publication authority.

### Invariants And Boundaries

- The family owner’s independent recorded population includes memberless heads and revisions not containing the selected invariant.
- A new primary invariant is genuinely before-absent without making its existing family before-absent.
- A removed member does not make an old stored predecessor the family’s current head.
- Exact revision selection and authored ambiguity are preserved independently of primary invariant selection.
- Fixtures and passing tests are bounded verification, not published project intent or installed product acceptance.

### Todos

No unrelated repair is assigned to this file. Installed product evidence and historical assessment loading remain separately reported outcomes, not conclusions of these source references.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

The operative contract is defined by the repository sources below.

### Repo-Internal References

These current owners and cases establish the stated behavior.

- Competing memberless heads remain ambiguous. [1]
- A recorded memberless family retains its guarantee and measured empty roster. [2]
- Independent ambiguity and explicit-revision history are both checked. [3]
- A new member retains the family’s existing before counterpart. [4]
- A retained predecessor membership cannot pin the family after selection. [5]
- Primary knowledge, evidence and complete source inventory stay independent. [6]
- Sparse pages preserve the recorded population and primary panes through real HTTP walks. [7]

### Cross-Repo References

No sibling repository defines this file's behavior.

No meaningful cross-repository implementation dependency.
