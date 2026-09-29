# mcp/src/agents_remember/memory_quality/knowledge_census/measures.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_census/measures.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The Doc12 measures over census claims (MIK-R20 rule 4).** `Counts.of(claims)` places each in-cohort
claim (`applicability: assessable`) in `T`, `F`, `U` or `P` and counts `non_claim` and
`historical_non_applicable` beside the cohort; `compute_measures(counts)` returns the six declared
measures in Doc12's order. No measure is folded into a score.

## Code Commentary

### Logic

- `Counts.total` is `N`, defined as `T + F + U + P` (the Preservation Boundary).
- Measures: verified truth share `T/N`; correctness among resolved claims `T/(T+F)`, always rendered with
  `U` and `P` as context; contradiction share `F/N`; assessment completion `(T+F+U)/N`; relevant truth
  coverage `C/K` and realization coverage, both "not applicable (no reference inventory)" because no
  census file declares a reference inventory yet.
- `_ratio` makes a zero denominator `not_applicable` with the reason "zero denominator"; `Measure.value`
  is `None` then.
- `Measure.render` always prints the counts: "73.8% (31 of 42)", or "not applicable (zero denominator:
  0 of 0)".

### Conventions

- `to_document` forms feed the report's JSON and the reader's census view (MIK-R29).

### Invariants And Boundaries

- A zero denominator is reported as not applicable, never as a perfect score, and a percentage is never shown without its counts.
- Out-of-cohort claims neither vanish nor dilute a share.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The counts, the measure and the arithmetic.

| Finding | Anchor | Source |
| --- | --- | --- |
| `N` is the sum of the four cells; out-of-cohort claims are counted beside it. | `Counts` | mcp/src/agents_remember/memory_quality/knowledge_census/measures.py:33-83 |
| A measure has a value only when its denominator is not zero, and renders with counts. | `Measure` | mcp/src/agents_remember/memory_quality/knowledge_census/measures.py:86-122 |
| A zero denominator is not applicable. | `_ratio` | mcp/src/agents_remember/memory_quality/knowledge_census/measures.py:125-130 |
| The six measures in Doc12's order. | `compute_measures` | mcp/src/agents_remember/memory_quality/knowledge_census/measures.py:137-160 |
| The conforming example's strings, with counts. | `test_the_measures_of_the_conforming_example_carry_their_counts` | mcp/tests/test_knowledge_census_report.py:42-55 |
| Zero denominators, never a perfect score. | `test_a_zero_denominator_is_not_applicable_never_a_perfect_score` | mcp/tests/test_knowledge_census_report.py:58-72 |
| The cohort, and the latest assessment governs. | `test_the_cohort_is_the_assessable_claims_and_the_latest_assessment_governs` | mcp/tests/test_knowledge_census_report.py:75-95 |

## Cross-Repo References

No meaningful cross-repo references found: the package reads one memory tree's bytes, handed in by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): created this card for the new file MIK-R20 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
