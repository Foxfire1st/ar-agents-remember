# mcp/tests/test_review_family_context_population.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_family_context_population.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T00:59:43+00:00 |
| lastVerifiedCommitHash | `a5bec6c3b3b413cd3066d0e8d302b4854d1b513a` |
| lastVerifiedCommitDate | 2026-09-27T03:38:17+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

**The family revision population and exact bounded-page population, and the states they decide.** The composition's cases in `mcp/tests/test_review_family_context.py` measure what one family
context *carries*; these four measure the **population that decides it**, which is where this leaf's one
real defect lived: the revision population of a family selection must be the family owner's own revision
list, because a family revision that cites no member is still a revision of that family. Deriving the
population from membership-bearing read rows instead made a memberless head invisible — and that is the
repository's own canonical ambiguity shape, and the normal intermediate state of a curator who authors a
family revision before its memberships.

**Three of the four cases fail on the pre-fix bytes; the fourth is the guard against over-correcting.**
That asymmetry is the module's design, and it is what makes these cases a bite-proof rather than a
restatement of the fix: the pre-fix run printed exactly the three wrong values the round-1 verification
falsified, and the fourth case fails only if the fix turns a genuinely absent family into an empty one.

**The enclosure, the authored movement and the request helpers are the sibling case module's, imported
rather than duplicated** (`:22-26`) — the pattern this test tree already uses for shared fixtures. This
module builds no fixture of its own beyond the three authors below.

## Code Commentary

### Logic

`recorded_population` obtains expected exact membership/revision and claim sets from the authorship owners. `walk_responses` follows the real HTTP route's published cursors at a fixed bound. The sparse-page case uses page sizes one and two, asserts content-only and claim-only updates, exact whole-walk sets and unchanged primary knowledge, evidence, comparison and complete inventory. Repeated sparse member contexts are expected; raw row sums are not unique membership counts.

**Each case drives one population question through the production read and asserts the state it
decides.** The table is the module's own list, with what each case protects.

| Case | Line | What it protects |
| --- | --- | --- |
| `test_the_canonical_memberless_successor_shape_is_an_ambiguity` | `:94` | the canonical shape — two legitimate successors of one predecessor, neither citing a member — is an **ambiguous** authored ambiguity: every head an inspectable candidate and **no** revision chosen, never a `compared` pair naming the superseded revision |
| `test_a_recorded_family_with_no_members_is_recorded_not_absent` | `:165` | a family the snapshot records with an authored guarantee and **no** membership rows is `recorded`, carrying its guarantee and a *measured* empty roster, not `no_family_recorded` |
| `test_the_history_sentence_is_measured_against_the_family_owner` | `:241` | the selection's history sentence is measured against the family owner, so a revision no membership reached is still counted as recorded history rather than reported as zero |
| `test_the_measured_zero_and_the_absent_family_stay_distinct` | `:311` | a family **no** snapshot records is still the measured zero — the over-correction guard, which passes on both byte sets by design |

**The read helpers name each side's own recorded list, which is the fact the cases turn on.**
`recorded_revisions` (`:66-75`) reads the family owner's own revision list for a side, `family_selection`
(`:78-84`) builds the review request for a family selector, and `family_context` (`:87-91`) selects that
family's context out of the payload — so a case asserts against the owner's list and the composed
context, never against a copied number.

**The authors build exactly the shapes the pre-fix bytes got wrong.**
`_author_memberless_successor` (`:142-153`) authors one successor family revision that cites no member,
`_author_memberless_successors` (`:156-162`) authors the canonical pair,
`_author_recorded_empty_family` (`:202-238`) authors a family revision with a guarantee and no
memberships at all (with its label and guarantee taken from the module's own constants, `:62-63`), and
`_withdraw_parent_membership` (`:282-308`) drives the shape the history sentence got wrong — the parent's
membership withdrawn on the candidate with a memberless successor added, which the pre-fix bytes
reported as `0 other recorded revision(s)` while the owner recorded three.

### Conventions

The module imports its enclosure, its authored movement and its request helpers from the sibling case
module rather than rebuilding them (`:28-56`), selects its markers once with `pytestmark` (`:58`), and
keeps the two authored strings it needs at module level (`:62-63`). `pytest.raises`-free: every case
asserts a composed state, because the failure it protects against is a wrong *value*, not an exception.

### Invariants And Boundaries

- **A memberless family revision is a revision of its family.** Every case here exists because that one
  sentence was false in the pre-fix composition.
- **The measured zero and the recorded-empty family are different facts.** The fourth case is the guard:
  a family neither snapshot records stays `no_family_recorded` (and a family neither records is refused
  by the comparison before a context exists), so the fix cannot convert a genuinely absent family into an
  empty one.
- **The ambiguity case asserts a refusal to choose.** Several legitimate heads stay several, and no
  guarantee is presented as the family's own on that selection.
- **Boundary:** the original cases protect revision-selection population; the sparse-page case also protects the exact member/claim population transported over the real application and HTTP path. Rendered behavior remains the dashboard tests' responsibility.

### Todos

None recorded.

## Docs References

No configured domain documentation could be consulted for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category — its whole body is "No entries
configured yet." — so there is no external or domain source to check and no documentation row is
recorded here.

## Repo-Internal References

Every claim on this card is checkable in the module's own cases and in the shape the production
composition builds. The three details a reader should carry: **the family owner's own revision list is
the population, so a memberless revision is a head**; **a family recorded with a guarantee and no
members is `recorded` with a measured empty roster**, not a measured zero; and **the fourth case is the
over-correction guard**, which distinguishes the measured zero from an absent family.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The defect these cases came from, the one case each they pin, and the fact that three of the four fail on the pre-fix bytes.** | "The composition's cases in" | mcp/tests/test_review_family_context_population.py:1-26 |
| The family owner's own recorded revision list for one side. | `recorded_revisions` | mcp/tests/test_review_family_context_population.py:69-78 |
| The review request built for a family selector. | `family_selection` | mcp/tests/test_review_family_context_population.py:81-87 |
| One family's context selected out of the payload. | `family_context` | mcp/tests/test_review_family_context_population.py:90-94 |
| **The canonical memberless-successor shape held as an authored ambiguity with every head inspectable and no revision chosen.** | `test_the_canonical_memberless_successor_shape_is_an_ambiguity` | mcp/tests/test_review_family_context_population.py:97-142 |
| The author of one memberless successor family revision. | `_author_memberless_successor` | mcp/tests/test_review_family_context_population.py:145-156 |
| The canonical pair of memberless successors. | `_author_memberless_successors` | mcp/tests/test_review_family_context_population.py:159-165 |
| **A recorded family with an authored guarantee and no members held as `recorded` with a measured empty roster.** | `test_a_recorded_family_with_no_members_is_recorded_not_absent` | mcp/tests/test_review_family_context_population.py:168-202 |
| The author of a guarantee-bearing family revision with no memberships. | `_author_recorded_empty_family` | mcp/tests/test_review_family_context_population.py:205-241 |
| **The history sentence measured against the family owner rather than the selected population.** | `test_the_history_sentence_is_measured_against_the_family_owner` | mcp/tests/test_review_family_context_population.py:244-282 |
| The withdrawn parent membership with a memberless successor added — the shape printing `0 other recorded revision(s)` before the fix. | `_withdraw_parent_membership` | mcp/tests/test_review_family_context_population.py:285-311 |
| **The over-correction guard: a family no snapshot records stays the measured zero.** | `test_the_measured_zero_and_the_absent_family_stay_distinct` | mcp/tests/test_review_family_context_population.py:314-346 |
| **The fix these cases pin: a family selection's population is every revision the family owner records.** | `_applicable_family` | mcp/src/agents_remember/application/review_family_context.py:538-562 |
| **The history sentence the third case measures, read from the family owner on both snapshots.** | `_selection_sentence` | mcp/src/agents_remember/application/review_family_context.py:768-803 |
| The sibling case module whose enclosure and helpers this module imports. | `build_family_scenario` | mcp/tests/test_review_family_context.py:134-165 |
| The composition cases this module complements rather than repeats. | `test_an_ambiguous_family_lineage_names_its_candidates_and_chooses_no_revision` | mcp/tests/test_review_family_context.py:523-563 |

## Cross-Repo References

No cross-repository behavior is exercised by these cases. The enclosure and the two knowledge datasets
belong to this repository's own fixture support and to the leaf enclosure the resolution selected; no
remote, credential, network or external system is involved, so no cross-repo reference row is recorded.

## Update History

- 2026-09-27T00:59:43+00:00 — Added exact sparse-page population coverage through the public authorship owners and real HTTP read. Counts derive from unique stored identities; bounded content/claim pages and unchanged primary/source/evidence facts are asserted without a constructed display payload.

- 2026-09-23T22:10:00+02:00 — 260921-ICR-L31 curator (uncommitted change set on `ar/260921-icr-l31`, base `4c000b11c5243e4a8e77c08e87984fff00c1d94b`): created this one-to-one card for the case module fix round 1 added, which measures **the revision population of a family selection** rather than what a context carries. The stamp basis is honest rather than convenient: the module is untracked at the base commit, so `lastVerifiedCommitHash` names the leaf's base commit, and the verified basis is the working-tree delta on top of it — no commit contains what a stamp would otherwise claim to have verified. The card records why these four cases exist and which way each one bites: three of them fail on the pre-fix bytes with the exact wrong values round-1 verification falsified (a memberless successor made invisible so an authored ambiguity read as a `compared` pair naming the superseded revision, a guarantee-bearing memberless family rendered as `no_family_recorded` with its guarantee dropped, and a history sentence printing `0 other recorded revision(s)` while the owner recorded three), while the fourth — the measured zero against an absent family — passes on both byte sets by design because it is the guard against over-correcting. The enclosure, the authored movement and the request helpers are the sibling case module's, imported rather than duplicated.
