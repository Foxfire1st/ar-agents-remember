# mcp/tests/test_review_family_context_values.py

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
and a side that read nothing carrying a roster. This reopen added the value-level pair that pins the
corrected completion semantics in **both** directions (`:114-163`): a walk the read took in one page must
still carry the whole roster it counts, while the same carried rows on a completed **continued** page are
accepted — the one relaxation the correction makes, pinned so that it cannot become a hole.

**The honest value these cases mutate is a value fixture, and the module says so.** `_honest_context`
(`:166-262`) builds one internally consistent `ReviewFamilyContext` — it is *never* evidence about the
store, and no case here claims to be one. That boundary is why this module imports no store, no fixture
support and no enclosure: it is the one part of the leaf's case population that is deliberately not a
real-boundary test.

## Code Commentary

### Logic

**Every case departs from the honest value in exactly one way, so a refusal is attributable.** The seven
cases and the clause each one exercises:

| Case | Line | The single departure it refuses |
| --- | --- | --- |
| `test_a_context_whose_counts_do_not_describe_its_roster_is_refused` | `:29` | counts that do not describe the entries and rosters beside them — the family counts, and a membership-row total that is not the sum of the rosters carried |
| `test_a_roster_page_may_not_present_a_truncated_roster_as_a_complete_one` | `:50` | a roster page whose completeness, its remainder and its cursor disagree, so a truncated roster could read as the whole one |
| `test_a_side_that_read_nothing_may_not_carry_a_roster` | `:80` | a side that recorded no context carrying members or a member count, which would be read as a measured empty roster |
| `test_a_recorded_side_may_not_name_a_revision_its_family_does_not_record` | `:95` | a recorded side naming a revision the family owner does not record for that snapshot — the fix-round-1 clause that makes an unrecorded selection unreachable |
| `test_a_complete_walk_that_is_one_page_must_carry_the_whole_roster` | `:114` | a complete page that is also the walk's first page carrying **none** of the rows it counts — the truncation the guard exists for, still refused after this reopen's relaxation |
| `test_a_final_page_of_a_multi_page_walk_may_carry_only_its_own_share` | `:128` | **not a refusal:** it pins the correction itself — a completed **continued** page carrying only its own share is accepted, and the same carried rows moved onto a first page are refused |
| `test_a_member_source_may_not_state_a_region_its_observation_does_not_support` | `:167` | a member source whose locator state, locator, ranges and resolution disagree — ranges beside a non-exact resolution, a `resolved` state with no range, `whole_file` claimed for a symbol locator, ranges presented as `unresolved`, a locator with no observed address — and a source missing its stored `role` or `rationale`; the honest `resolved` source and a `not_observed` source are accepted. Unlike the other cases it builds its own honest source dict rather than departing from `_honest_context` |

**The honest fixture is built once and mutated, not re-authored per case.** `_honest_context`
(`:219-315`) assembles a complete, internally consistent context — two sides with their selected
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
  no roster and no count. After this reopen the refusal is **scoped to the walk's own shape**: a page that
  is complete *and* the walk's first page is the whole roster and must carry all of it, while a completed
  **continued** page carries its own share by construction and is accepted. The module pins both
  directions in one case, so a reader cannot mistake the relaxation for a removed guard.
- **A recorded side's revision must be one the family owner records**, which is the value-level half of
  the leaf's population fix: even a caller that skipped the composition cannot construct that shape.
- **Boundary: this module is a disclosed part of the leaf's split.** It exists as a separate file so the
  production case module stays smaller; it is registered in `mcp/tests/test-evidence-lanes.toml`'s
  `unit-regression` lane with its siblings.

### Todos

None recorded.

## Evidence

### Docs References

No configured domain documentation could be consulted for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category — its whole body is "No entries
configured yet." — so there is no external or domain source to check and no documentation row is
recorded here.

### Repo-Internal References

Every claim on this card is checkable in the module's own cases and in the validators they exercise. The
three details a reader should carry: **these cases prove the invalid context cannot be constructed at
all**, which is the value-level complement to the composition's production cases; **a recorded side naming
a revision the family does not record is refused**, which is the value-level half of the leaf's population
fix; and **the corrected roster guard is pinned in both directions here** — a complete page that is the
walk's first page must carry the whole roster, while a completed **continued** page carrying only its own
share is accepted.

- **The two halves of the deliverable: the production composition measured in the sibling module, and the value rules measured here, with the honest fixture explicitly not evidence about the store.** [1]
- **Counts that do not describe the entries and rosters beside them.** [2]
- **A roster page whose completeness, remainder and cursor disagree, so a truncated roster cannot read as the whole one.** [3]
- A side that recorded no context carrying members or a member count. [4]
- **A recorded side naming a revision the family owner does not record — the value-level half of the population fix.** [5]
- **The corrected guard's real subject, still enforced: a complete page that is also the walk's first page carries every row it counts.** [6]
- **The correction itself, pinned with the same carried rows: a completed continued page is accepted, and those rows on a first page are refused, so the relaxation is not a hole.** [7]
- **A member source's locator state, locator, ranges and resolution are one fact, and a source without its stored role or rationale is refused.** [8]
- The validators that case exercises. [9]
- The one internally consistent context every roster-and-count case departs from by exactly one clause. [10]
- **The validator these cases exercise, which requires a recorded side's revision to be one the family owner records and — this reopen's correction — holds only a single-page walk (`complete and state == "first_page"`) to the revision-wide member count.** [11]
- The validator refusing a claimed remainder with no way to reach it and counts that do not describe the entries. [12]
- The validator refusing a truncated roster presented as a complete one. [13]
- The production-entry cases this module is the value half of. [14]
- The population case independently checks authored-head ambiguity and explicitly requested revision history. [15]

### Cross-Repo References

No cross-repository behavior is exercised by these cases. They construct values in memory and assert the
refusals those values' own validators raise; no store, enclosure, network or external system is involved,
so no cross-repo reference row is recorded.
