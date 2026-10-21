# mcp/src/agents_remember/models/knowledge/review_intent_summary.py

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Define authored-intent plus/minus counts, partial/unavailable outcomes and the comparison number those counts describe.

## Code Commentary

Added and removed count after-only and before-only invariant/guarantee head revisions; any statement/status/acceptance/version-only successor contributes once on each side. Pure realization/membership changes stay in their own typed counts. ReviewIntentCounts validates that declared added/removed totals equal those two component sums.

ReviewIntentSummaryResult carries task context and one declared outcome. Unavailable requires a refusal and no counts; counted/partial require counts and no refusal; partial is equivalent to unresolved>0. These constructor checks constrain the supplied shape and arithmetic, not whether a producer actually read/authenticated the comparison.

Optional attribution and nonnegative unexplained_open remain separate from authored-intent totals and outside that outcome validator. A tree producer attaches lane attribution plus a stored-open count; matching complete stored work and decidable unexplained-item gate verdicts are required for that auxiliary count, otherwise it remains absent rather than zero. Dataset comparisons carry no tree attribution.

The optional nonnegative comparison field identifies the recorded tree comparison counted. It is absent when there is no tree comparison or resolution failed; it is a label for the selected result, not an instruction to switch a source.

## Invariants And Boundaries

This module selects and compares nothing. Missing knowledge cannot become measured +0/−0, and independent attribution/stored-open fields cannot be added to statement totals. A present comparison number alone does not authenticate its underlying reads.

## Evidence

- Declared head-count totals equal invariant/guarantee parts and keep relationship-only counts separate. [9]
- Outcome validation and optional attribution/open/comparison fields retain independent meanings. [10]
- The tree producer attaches its number and separate lane/stored-open facts. [11]
- Stored-open counts require complete bound work and no undecided relevant verdict. [12]
