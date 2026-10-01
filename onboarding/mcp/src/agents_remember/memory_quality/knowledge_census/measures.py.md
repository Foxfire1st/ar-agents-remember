# mcp/src/agents_remember/memory_quality/knowledge_census/measures.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The counts, the measure and the arithmetic.

- `N` is the sum of the four cells; out-of-cohort claims are counted beside it. [1]
- A measure has a value only when its denominator is not zero, and renders with counts. [2]
- A zero denominator is not applicable. [3]
- The six measures in Doc12's order. [4]
- The conforming example's strings, with counts. [5]
- Zero denominators, never a perfect score. [6]
- The cohort, and the latest assessment governs. [7]

### Cross-Repo References

No meaningful cross-repo references found: the package reads one memory tree's bytes, handed in by the caller.

No cross-repo boundary is crossed by this file.
