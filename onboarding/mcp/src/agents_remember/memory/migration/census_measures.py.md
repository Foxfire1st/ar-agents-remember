# mcp/src/agents_remember/memory/migration/census_measures.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/migration/census_measures.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `2dcacb27446ecbaba01b69ee32e2ac40a1713b09`|
| lastVerifiedCommitDate |  2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

`Doc12`'s truth-coverage apparatus as arithmetic, and deliberately small: the accounting
`N = T + F + U + P`, the six measures, and the four-axis slices. What matters is the separation it
keeps, because every prohibition in the packet is a prohibition on collapsing one of these cells into
another. `N` is a claim count over **assessable** claims, and the eligibility rule is stated once here
and used by every comparison: an observation enters the cohort exactly when its record kind is
`census_claim`, its `applicability` is `assessable` and it carries a claim text. `T`, `F` and `U` come
from a curator's authored assessment and from nothing else — there is no code path from an import
outcome to any of the three, and `unassessed` is derivable only as "no assessment exists". `K` is
never read here: the coverage measure takes a denominator as an argument and reports
`not_measurable` without one, because a `K` this module could compute would come from the corpus being
measured, which is what `Doc12:110` forbids outright. The six measures are reported together and never
composed into one number, a zero denominator is `not_applicable` with its counts beside it rather than
a perfect score, and every ratio that could be read as a verdict is paired with the counts that
qualify it.

## Code Commentary

### Logic

**One eligibility rule, stated once and applied three functions down.** `claim_enters_cohort` is the
predicate `CR21-4` requires: the applicability must equal `COHORT_APPLICABILITY` and the claim text
must not be blank. `claim_kind` is deliberately not part of the test — `unclassified` is a reportable
state that counts as unresolved, and a claim a curator classified as historical still enters the
cohort, because what keeps it out of the truth measures is its applicability and its assessment, not
its kind. `slice_claims` re-applies the same predicate rather than trusting its caller, so a slice can
never include a claim the global accounting excluded.

**The separation is a value that closes on itself.** `Separation` carries the four cells plus the two
out-of-cohort counts, and `__post_init__` raises when `total != supported + contradicted + unresolved +
pending`, so a separation whose own cells disagree cannot exist. `cell_counts` gives the four cells
by name, so a report never has to remember the field order. `separation_of` builds one from an
iterable of cell names by counting into the declared `CELL_NAMES`, and takes `non_claim` and
`historical` as separate keyword counts — the two pieces `Doc12:95` requires carry an explicit
disposition rather than vanishing, because a count that appears nowhere is indistinguishable from one
that vanished.

**The cell a claim is in is read out of its stored relations, and the derivation lives elsewhere.**
`assessment_cell` is the whole mapping as one function: no assessment or a `None` disposition is `P`,
`no_concern_found` is `T`, `concern_found` is `F`, and everything else — including a recorded
`unresolved` — is `U`. `unassessed` is the only status it can derive, and it derives it from the
*absence* of an assessment rather than from anything an import did. `cell_of` reads the same rule out
of a stored claim: it collects the claims' evidence relations' `assessment_disposition` values, drops
the `None`s, returns `P` when nothing is recorded, `F` when any recorded value is `concern_found`, `U`
when any is `unresolved`, and `T` otherwise — so `assessed` with no disposition recorded reports `U`
rather than being assumed supported, because an unread verdict is not evidence of truth. The two
functions state the rule twice, and neither calls the other.

**One comparison key, and the original text is what is stored.** `ClaimOccurrence.key_for` reduces a
claim text to `" ".join(text.split()).casefold()`; `unique_occurrence_counts` counts occurrences per
key and returns both totals plus a `repeats` mapping filtered to the keys with more than one
occurrence and sorted by key. `UniqueOccurrenceCounts.__post_init__` refuses an occurrence count below
the unique count, because a unique claim with no occurrence is not a state this census can produce,
and the class docstring states why both are always reported: counting only occurrences inflates, and
counting only uniques hides the incorrect local occurrence and the missing second realization.

**Six measures, always six, each with the counts that qualify it.** `compute_measures` returns one
`Measure` per `MEASURE_NAMES` entry in the doc's own order, including the ones it cannot compute, so a
missing measure is visible as a missing measure rather than as an absent row. `_ratio` returns a
`computed` measure, or `not_applicable` with the note that "a zero denominator means not applicable or
not yet measurable, not a perfect score" when the denominator is zero. `_coverage_measure` returns
`not_measurable` when either side is `None`, with the reason stated in the measure itself: the coverage
denominator cannot come from the corpus being measured, so it stays unmeasured rather than
approximated. The correctness measure's note interpolates the unresolved and pending counts, so the
`T / (T + F)` figure cannot be reported without the two counts `Doc12:100` requires accompany it.

**`Measure.value` refuses rather than defaulting.** It returns `None` unless the state is `computed`
*and* the denominator is truthy, so `not_applicable` and `not_measurable` have no number at all; the
packet's refusal of an automatic perfect score is therefore a property of the value accessor, not of
each caller. `render` follows it: a valueless measure renders as its state and note, a computed one as
`numerator/denominator = value` at six decimals, never as a bare percentage. `CensusReport.render`
emits the baseline pair, the accounting line, the out-of-cohort line, both occurrence counts, the six
measures, then the slices in `SLICE_AXES` order. `CensusReport.measure` raises `KeyError` naming the
reported set for a name the report does not carry; `slice_axis` selects one axis's slices.

**The slices carry the same four-way accounting, keyed by a recorded association.** `slice_claims`
groups the cohort by `keys_of` and falls back to `_unrecorded_key(axis)` for a claim the mapping does
not key, rather than dropping it — a breakdown that silently omitted what it could not key would
report a coverage the corpus does not have. `_unrecorded_key` returns the bare
`CONSEQUENCE_UNRECORDED` for the consequence axis and `f"{axis}:unrecorded"` for the others. Each
slice's separation is built from its members' cells, and its counts come from
`unique_occurrence_counts` over the occurrences that were supplied for those members, so a slice
carries unique and occurrence totals as well as the cells.

**The two count helpers that keep a hidden bucket visible.** `inventory_counts` counts rows by parse
`outcome` and separately by `inventory_state` under an `inventory_state:` prefix, sorted by key, so an
absent surface is a counted bucket rather than an omission. `disposition_counts` counts by
`disposition_kind` and exists to keep `unmapped` visible: `KS-R21@v1` §2.2 makes it a named state
appearing in the census's dispositions, so a report showing only imported and dispositioned counts
would hide exactly the artifacts the importer refused to place. `claim_kind_counts` pre-seeds
`unclassified` plus the four `CLASSIFIED_CLAIM_KINDS`, so a kind with no members still appears at
zero. `inventory_counts` and `disposition_counts` sort their keys; `claim_kind_counts` returns the
seeded order.

### Conventions

Everything here is a frozen dataclass over the imported record vocabulary, and no model is declared
twice: `CensusClaim`, `CensusInventoryRow`, `CensusDispositionKind` and the two closed vocabularies
`CLASSIFIED_CLAIM_KINDS` and `COHORT_APPLICABILITY` all come from `models/knowledge/census.py`. The
four closed vocabularies this module does own are declared as a `Literal` alias paired with a runtime
tuple of the same members — `CellName`/`CELL_NAMES`, `MeasureName`/`MEASURE_NAMES`,
`SliceAxis`/`SLICE_AXES` — which is what lets a measure name a cell and a report iterate the declared
order without a second spelling. Single-value literals are constants rather than inline strings where
a second site exists (`CONSEQUENCE_UNRECORDED`). Private helpers are underscore-prefixed (`_ratio`,
`_coverage_measure`, `_unrecorded_key`), the module declares **no `__all__`**, and every failure is a
raised `ValueError` inside a frozen dataclass's `__post_init__` or a `KeyError` from a lookup — there
is no boolean "valid" flag anywhere. The report's own render and the measure's render are the only
string formatting in the file, and both are deterministic.

### Invariants And Boundaries

- **`K` is never computed here.** `compute_measures` is given the reference inventory's size and the
  represented-truths count, or it is given `None`; there is no branch that could derive a denominator
  from anything this module holds, and the unmeasured state carries its own reason.
- **No measure becomes one score.** The six are returned together as a tuple in the doc's order, and
  `CensusReport.render` prints them as six lines; there is no composite index, no weighting and no
  aggregate field anywhere in the report.
- **A zero denominator is not a perfect score.** `_ratio` returns `not_applicable` and `Measure.value`
  returns `None` for it, so a `0/0` cannot render as `1.0` or as `0.0`.
- **`T`, `F` and `U` are only ever read, never derived from an outcome.** The only mapping from an
  assessment state to a cell is `assessment_cell` and `cell_of`, and both read a curator's authored
  disposition; a claim with no assessment is `P` in both.
- **The cohort rule is one predicate.** `claim_enters_cohort` is the single statement of eligibility
  and `slice_claims` calls it rather than restating it, so global and sliced accounting cannot
  disagree about who is in `N`.
- **The accounting closes or it does not exist.** `Separation.__post_init__` refuses a total that does
  not equal `T + F + U + P`, so an unbalanced separation cannot be constructed by any caller.
- **Nothing is dropped for being unkeyable.** A claim with no recorded key on an axis lands under that
  axis's unrecorded key, and the two out-of-cohort buckets are reported beside `N` rather than inside
  it, so neither an unkeyed claim nor a `non_claim` piece disappears from the report.
- **Both occurrence counts travel together.** `UniqueOccurrenceCounts` carries uniques, occurrences
  and the repeats mapping as one value and refuses an occurrence count below the unique count, so no
  displayed coverage figure can be computed from occurrences alone.
- **This module reads no store and holds no state.** It is pure arithmetic over values passed in: no
  connection, no path, no cache and no mutation of its arguments.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

This module owns the census's arithmetic and the vocabularies the report is expressed in: the four
cells, the six measure names and the four slice axes. The rows below cite each declared vocabulary,
the eligibility predicate, the separation that refuses to disagree with itself, the assessment-to-cell
mapping in both of its forms, the occurrence counting, the six measures with their refusal states, and
the slice and count helpers that keep unkeyed and unplaced facts visible.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the accounting as one separation, with the eligibility rule, the authored-only truth cells and the never-read `K` stated in one place. | `Separation`; `Measure` | mcp/src/agents_remember/memory/migration/census_measures.py:1-26; mcp/src/agents_remember/memory/migration/census_measures.py:80-95; mcp/src/agents_remember/memory/migration/census_measures.py:116-144 |
| The four cells of the accounting as one closed vocabulary, named rather than lettered at each use site. | `CellName`; `CELL_NAMES` | mcp/src/agents_remember/memory/migration/census_measures.py:42-46 |
| The six measure names, declared in `Doc12:99-104`'s own order so that a measure the report cannot compute is still a visible entry. | `MeasureName`; `MEASURE_NAMES` | mcp/src/agents_remember/memory/migration/census_measures.py:48-66 |
| The four slice axes `Doc12:118` names, each documented as a recorded association rather than a derived one, and the consequence axis's own value for "not recorded" so an unattributed mass is a breakdown line instead of a silent omission. | `SliceAxis`; `SLICE_AXES`; `CONSEQUENCE_UNRECORDED` | mcp/src/agents_remember/memory/migration/census_measures.py:68-72; mcp/src/agents_remember/memory/migration/census_measures.py:74-77 |
| The separation value with the two out-of-cohort counts `Doc12:95` requires carry an explicit disposition, the four cells available by name, and the `__post_init__` check that refuses a total its cells do not sum to. | `Separation`; `non_claim`; `historical_non_applicable`; `cell_counts` | mcp/src/agents_remember/memory/migration/census_measures.py:80-95; mcp/src/agents_remember/memory/migration/census_measures.py:97-102; mcp/src/agents_remember/memory/migration/census_measures.py:104-113 |
| The measure's three states, its counts and note, and its rendering with the counts beside the ratio and never as a bare percentage. | `Measure`; `render` | mcp/src/agents_remember/memory/migration/census_measures.py:116-144 |
| One occurrence per extracted claim, with the normalised comparison key that decides a repeat while the original text stays what is reported. | `ClaimOccurrence`; `key_for` | mcp/src/agents_remember/memory/migration/census_measures.py:147-167 |
| Both counts `Doc12:112` requires, always together, with the refusal of an occurrence count below the unique count. | `UniqueOccurrenceCounts` | mcp/src/agents_remember/memory/migration/census_measures.py:170-188 |
| The whole census output and its slice record: the baseline pair, the separation, the six measures, both counts, the inventory counts, and `Doc12:118`'s reason slices are mandatory output rather than an optional breakdown. | `CensusReport`; `SliceReport` | mcp/src/agents_remember/memory/migration/census_measures.py:191-204; mcp/src/agents_remember/memory/migration/census_measures.py:207-219 |
| The two accessors that refuse to guess: a measure name the report does not carry raises naming the reported set, and one axis's slices are selected from the recorded slice list. | `measure`; `slice_axis`; `MEASURE_NAMES` | mcp/src/agents_remember/memory/migration/census_measures.py:220-231 |
| The report rendering: facts as lines, measures together, six measures and never one composite score. | `render` | mcp/src/agents_remember/memory/migration/census_measures.py:233-262 |
| The eligibility rule `CR21-4` requires be stated, as one predicate with `claim_kind` deliberately outside the test, and the closed applicability value it compares against. | `claim_enters_cohort`; `COHORT_APPLICABILITY` | mcp/src/agents_remember/memory/migration/census_measures.py:265-277; mcp/src/agents_remember/models/knowledge/census.py:100-103 |
| The assessment-to-cell mapping in both of its forms: the four cases, whose `None` case makes a claim with no assessment `P`, and the read of a claim's stored evidence relations, where an unread verdict is `U` rather than assumed support. | `assessment_cell`; `cell_of` | mcp/src/agents_remember/memory/migration/census_measures.py:280-299; mcp/src/agents_remember/memory/migration/census_measures.py:487-507 |
| The two arithmetic builders: the separation built from an iterable of cells with the out-of-cohort counts passed separately, and the occurrence count whose repeats mapping keeps only genuine repeats. | `separation_of`; `unique_occurrence_counts` | mcp/src/agents_remember/memory/migration/census_measures.py:302-318; mcp/src/agents_remember/memory/migration/census_measures.py:321-331 |
| The zero-denominator refusal — `not_applicable` with the reason recorded rather than a zero or a one — and the six measures in the doc's order, with the correctness figure's note carrying the unresolved and unassessed counts that must accompany it, and the coverage pair that stays `not_measurable` rather than inventing the denominator it was not given. | `_ratio`; `compute_measures`; `_coverage_measure` | mcp/src/agents_remember/memory/migration/census_measures.py:334-347; mcp/src/agents_remember/memory/migration/census_measures.py:350-419; mcp/src/agents_remember/memory/migration/census_measures.py:422-439 |
| Slicing the cohort by recorded keys, with an unkeyed claim landing under its axis's unrecorded key instead of being dropped. | `slice_claims`; `_unrecorded_key` | mcp/src/agents_remember/memory/migration/census_measures.py:442-478; mcp/src/agents_remember/memory/migration/census_measures.py:481-484 |
| The three count helpers that keep a bucket visible: inventory rows by parse outcome and state, the claim kinds pre-seeded with `unclassified` and the four classified kinds, and the migration dispositions including `unmapped`. | `inventory_counts`; `claim_kind_counts`; `disposition_counts` | mcp/src/agents_remember/memory/migration/census_measures.py:510-543 |
| The closed vocabularies this module reads rather than restates, and the evidence relation whose optional authored disposition is the only source of a truth cell. | `CENSUS_CLAIM_KINDS`; `CENSUS_DISPOSITION_KINDS`; `CensusClaimEvidence` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:85-99; mcp/src/agents_remember/models/knowledge/census.py:239-257 |
## Cross-Repo References

No cross-repository behavior is implemented in this file. It is arithmetic over values its caller
passes in — cells, counts, a denominator and a set of occurrences — and reads no store, no path and no
remote, so nothing here reaches another repository, another dataset or a remote.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): created this one-to-one card for the census's arithmetic module. It records the separation `N = T + F + U + P` as a value that refuses to disagree with itself in `__post_init__`, with the two out-of-cohort counts `non_claim` and `historical_non_applicable` reported beside `N` rather than inside it. It records the single eligibility predicate `claim_enters_cohort`, its deliberate exclusion of `claim_kind`, and the fact that `slice_claims` re-applies it so global and sliced accounting cannot diverge. It records the assessment-to-cell mapping in its two forms — `assessment_cell`'s four cases and `cell_of`'s read of the stored evidence relations — where a claim with no assessment is `P` and an unread verdict is `U` rather than assumed support. It records the six measure names in the doc's order, `_ratio`'s zero-denominator refusal as `not_applicable`, `_coverage_measure`'s `not_measurable` when no independently reviewed denominator was supplied, and `Measure.value`'s refusal to return a number for either state. It records the comparison key `key_for` and the both-counts-together rule, the four slice axes with the recorded-only association rule and the unrecorded-key fallback, and the three count helpers that keep `unmapped`, `absent` and a zero-member kind visible. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
