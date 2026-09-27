# mcp/tests/test_review_family_context_population.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_family_context_population.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T02:21:35Z |
| lastVerifiedCommitHash | `c8d6ebe2289731c7693eb890b806a2f3490f3e97` |
| lastVerifiedCommitDate | 2026-09-27T04:55:05+02:00|
| governingOverview | `mcp/tests/overview.md` |

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

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The operative contract is defined by the repository sources below. | — | — |

## Repo-Internal References

These current owners and cases establish the stated behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| Competing memberless heads remain ambiguous. | `test_the_canonical_memberless_successor_shape_is_an_ambiguity` | mcp/tests/test_review_family_context_population.py:89-134 |
| A recorded memberless family retains its guarantee and measured empty roster. | `test_a_recorded_family_with_no_members_is_recorded_not_absent` | mcp/tests/test_review_family_context_population.py:160-194 |
| Independent ambiguity and explicit-revision history are both checked. | `test_the_history_sentence_is_measured_against_the_family_owner` | mcp/tests/test_review_family_context_population.py:236-288 |
| A new member retains the family’s existing before counterpart. | `test_a_new_member_keeps_the_existing_familys_before_context` | mcp/tests/test_review_family_context_population.py:321-349 |
| A retained predecessor membership cannot pin the family after selection. | `test_a_removed_member_does_not_pin_family_context_to_its_retained_predecessor` | mcp/tests/test_review_family_context_population.py:352-381 |
| Primary knowledge, evidence and complete source inventory stay independent. | `_assert_primary_unchanged` | mcp/tests/test_review_family_context_population.py:291-300 |
| Sparse pages preserve the recorded population and primary panes through real HTTP walks. | `test_content_and_claim_only_pages_preserve_the_authored_population` | mcp/tests/test_review_family_context_population.py:508-560 |

## Cross-Repo References

No sibling repository defines this file's behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository implementation dependency. | — | — |

## Update History

- 2026-09-27T02:21:35Z — L40: Recorded the new/removed-member regressions and the explicit correction of the old membership-subset ambiguity expectation, preserving the earlier L38 sparse-page coverage. Existing verification stamps and all prior history are preserved; working-source provenance is retained in task notes and actual commit stamping remains closeout-owned.


- 2026-09-27T00:59:43+00:00 — Added exact sparse-page population coverage through the public authorship owners and real HTTP read. Counts derive from unique stored identities; bounded content/claim pages and unchanged primary/source/evidence facts are asserted without a constructed display payload.

- 2026-09-23T22:10:00+02:00 — 260921-ICR-L31 curator (uncommitted change set on `ar/260921-icr-l31`, base `4c000b11c5243e4a8e77c08e87984fff00c1d94b`): created this one-to-one card for the case module fix round 1 added, which measures **the revision population of a family selection** rather than what a context carries. The stamp basis is honest rather than convenient: the module is untracked at the base commit, so `lastVerifiedCommitHash` names the leaf's base commit, and the verified basis is the working-tree delta on top of it — no commit contains what a stamp would otherwise claim to have verified. The card records why these four cases exist and which way each one bites: three of them fail on the pre-fix bytes with the exact wrong values round-1 verification falsified (a memberless successor made invisible so an authored ambiguity read as a `compared` pair naming the superseded revision, a guarantee-bearing memberless family rendered as `no_family_recorded` with its guarantee dropped, and a history sentence printing `0 other recorded revision(s)` while the owner recorded three), while the fourth — the measured zero against an absent family — passes on both byte sets by design because it is the guard against over-correcting. The enclosure, the authored movement and the request helpers are the sibling case module's, imported rather than duplicated.
