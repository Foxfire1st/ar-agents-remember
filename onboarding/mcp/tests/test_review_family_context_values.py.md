# mcp/tests/test_review_family_context_values.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_family_context_values.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T22:10:00+02:00 |
| lastVerifiedCommitHash | `fdf3e4b6cfe73040d35cbfd4d8b93fd55369e499` |
| lastVerifiedCommitDate | 2026-09-23T22:41:36+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

**The family-context values' own construction rules, exercised as values (ICR-R31@v1).**
`ICR-R31@v1`'s composition is measured over the production entry in
`mcp/tests/test_review_family_context.py`. These cases measure the other half of the same deliverable:
the rules the **values** enforce on any caller, so that the sentences the composition publishes cannot be
built from numbers that contradict them.

**Each case mutates one internally consistent value and shows the construction refusing it** (`:6-11`): a
family remainder with no way to reach it, a membership-row total that is not the sum of the rosters beside
it, a unique member total inflated by counting rows, a truncated roster page presented as a complete one,
and a side that read nothing carrying a roster.

**The honest value these cases mutate is a value fixture, and the module says so.** `_honest_context`
(`:114-210`) builds one internally consistent `ReviewFamilyContext` — it is *never* evidence about the
store, and no case here claims to be one. That boundary is why this module imports no store, no fixture
support and no enclosure: it is the one part of the leaf's case population that is deliberately not a
real-boundary test.

## Code Commentary

### Logic

**Every case departs from the honest value in exactly one way, so a refusal is attributable.** The four
cases and the clause each one exercises:

| Case | Line | The single departure it refuses |
| --- | --- | --- |
| `test_a_context_whose_counts_do_not_describe_its_roster_is_refused` | `:29` | counts that do not describe the entries and rosters beside them — the family counts, and a membership-row total that is not the sum of the rosters carried |
| `test_a_roster_page_may_not_present_a_truncated_roster_as_a_complete_one` | `:50` | a roster page whose completeness, its remainder and its cursor disagree, so a truncated roster could read as the whole one |
| `test_a_side_that_read_nothing_may_not_carry_a_roster` | `:80` | a side that recorded no context carrying members or a member count, which would be read as a measured empty roster |
| `test_a_recorded_side_may_not_name_a_revision_its_family_does_not_record` | `:95` | a recorded side naming a revision the family owner does not record for that snapshot — the fix-round-1 clause that makes an unrecorded selection unreachable |

**The honest fixture is built once and mutated, not re-authored per case.** `_honest_context`
(`:114-210`) assembles a complete, internally consistent context — two sides with their selected
revisions, guarantees and rosters, one shared member reference, and the counts that follow from them — so
each case's assertion is about the *one* clause it breaks rather than about a hand-built inconsistency
that could be refused for several reasons at once. The imports (`:15-27`) are the value types under test
plus `KnowledgeReadCounts` and `pydantic.ValidationError`, and `pytestmark` (`:26`) selects the module's
markers once.

**These cases are the value half of the leaf's bite-proofs.** The production cases prove the composition
builds the right context from real datasets; these prove that a context built wrongly *cannot exist*, which
is what makes the composition's sentences trustworthy to a renderer that receives the value and nothing
else.

### Conventions

The module builds values directly and asserts `ValidationError`; it imports no store, no fixture support
and no fastapi client, so it runs without an enclosure. Each case names the clause it violates in its own
name, and the fixture's field values are chosen so that every clause *other* than the one under test is
satisfied.

### Invariants And Boundaries

- **A value fixture is not evidence about the store.** The module says so itself, and no case here is
  reported as a store measurement; the real-boundary measurement is the sibling module's.
- **A truncated roster can never be presentable as a complete one**, and a side that read nothing carries
  no roster and no count.
- **A recorded side's revision must be one the family owner records**, which is the value-level half of
  the leaf's population fix: even a caller that skipped the composition cannot construct that shape.
- **Boundary: this module is a disclosed part of the leaf's split.** It exists as a separate file so the
  production case module stays smaller; it is registered in `mcp/tests/test-evidence-lanes.toml`'s
  `unit-regression` lane with its siblings.

### Todos

None recorded.

## Docs References

No configured domain documentation could be consulted for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category — its whole body is "No entries
configured yet." — so there is no external or domain source to check and no documentation row is
recorded here.

## Repo-Internal References

Every claim on this card is checkable in the module's own cases and in the validators they exercise. The
two details a reader should carry: **these cases prove the invalid context cannot be constructed at all**,
which is the value-level complement to the composition's production cases; and **a recorded side naming a
revision the family does not record is refused**, which is the value-level half of the leaf's population
fix.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The two halves of the deliverable: the production composition measured in the sibling module, and the value rules measured here, with the honest fixture explicitly not evidence about the store.** | "Each case mutates one internally consistent value and shows the construction refusing it" | mcp/tests/test_review_family_context_values.py:1-13 |
| **Counts that do not describe the entries and rosters beside them.** | `test_a_context_whose_counts_do_not_describe_its_roster_is_refused` | mcp/tests/test_review_family_context_values.py:29-47 |
| **A roster page whose completeness, remainder and cursor disagree, so a truncated roster cannot read as the whole one.** | `test_a_roster_page_may_not_present_a_truncated_roster_as_a_complete_one` | mcp/tests/test_review_family_context_values.py:50-77 |
| A side that recorded no context carrying members or a member count. | `test_a_side_that_read_nothing_may_not_carry_a_roster` | mcp/tests/test_review_family_context_values.py:80-92 |
| **A recorded side naming a revision the family owner does not record — the value-level half of the population fix.** | `test_a_recorded_side_may_not_name_a_revision_its_family_does_not_record` | mcp/tests/test_review_family_context_values.py:95-111 |
| The one internally consistent context every case departs from by exactly one clause. | `_honest_context` | mcp/tests/test_review_family_context_values.py:114-210 |
| **The validator these cases exercise, which requires a recorded side's revision to be one the family owner records.** | `_require_the_state_to_match_what_it_carries` | mcp/src/agents_remember/models/knowledge/review_family_context.py:299-334 |
| The validator refusing a claimed remainder with no way to reach it and counts that do not describe the entries. | `_require_the_family_counts_to_describe_the_entries` | mcp/src/agents_remember/models/knowledge/review_family_context.py:471-526 |
| The validator refusing a truncated roster presented as a complete one. | `_require_the_cursor_and_the_remainder_to_agree` | mcp/src/agents_remember/models/knowledge/review_family_context.py:246-268 |
| The production-entry cases this module is the value half of. | `test_a_selected_invariant_resolves_both_recorded_families_with_their_own_guarantees` | mcp/tests/test_review_family_context.py:284-318 |
| The population cases sharing the same fix round. | `test_the_history_sentence_is_measured_against_the_family_owner` | mcp/tests/test_review_family_context_population.py:241-279 |

## Cross-Repo References

No cross-repository behavior is exercised by these cases. They construct values in memory and assert the
refusals those values' own validators raise; no store, enclosure, network or external system is involved,
so no cross-repo reference row is recorded.

## Update History

- 2026-09-23T22:10:00+02:00 — 260921-ICR-L31 curator (uncommitted change set on `ar/260921-icr-l31`, base `4c000b11c5243e4a8e77c08e87984fff00c1d94b`): created this one-to-one card for the value-construction case module `ICR-R31@v1` introduced alongside the composition's production cases. The stamp basis is honest rather than convenient: the module is untracked at the base commit, so `lastVerifiedCommitHash` names the leaf's base commit, and the verified basis is the working-tree delta on top of it — no commit contains what a stamp would otherwise claim to have verified. The card records the boundary the module itself states: these cases prove that a wrongly built family context **cannot exist**, which is the value-level complement to the production cases that prove the composition builds the right one from real datasets — and the value they mutate is a value fixture, never evidence about the store. Fix round 1 added the fourth case (`test_a_recorded_side_may_not_name_a_revision_its_family_does_not_record`), which is the value-level half of the population fix: a recorded side's selected revision must be one the family owner records for that snapshot, so even a caller that bypassed the composition cannot construct the shape the round-1 verification falsified.
