# mcp/tests/test_review_delivered_comparison.py

## Governing Overview

[Owning route overview](../../overview.md)

## Purpose

Measure a landed leaf's review: it opens the pair the leaf delivered, keeps earlier comparisons as history, and refuses what it cannot establish.

## Code Commentary

The module builds a real task enclosure, code repository and memory repository through the shipped test world, removes the worktrees where a landed leaf has none, and calls the production resolver. Cases cover the composed regression (a stale last record over the delivered pair), a replayed landing that differs from the closeout's code commit, an exact delivered record older than the last record, a matching last record that keeps its number, a delivery Git cannot produce, a leaf that records no delivery, the notice line, a closeout with no memory cell, a recorded tree id, an unconverted delivery, a failed required conversion, a numbered leaf-wide read, and create-only publication in two directions.

The cases that go through the resolver assert the production answer's identity fields — commits, trees, numbers, sides and refusal codes — rather than a private helper's return shape, while the cases that call `publish_comparison_record` directly assert its own answers: `True`/`False` and the bytes it left.

## Invariants And Boundaries

The cases exercise the production resolver over isolated repositories and a disposable task enclosure; they never read or mutate the developer's coordination records. They prove the properties named by MIK-R195 rules 1-5 for those shapes, not a whole-catalogue certification.

## Evidence

- A leaf whose last record predates its delivery opens the four delivered sides and keeps the earlier record. [1]
- A replayed landing's commit is the code candidate. [2]
- An exact delivered record older than the last record is reused at its own number. [3]
- A matching last record is the delivered default and keeps its number. [4]
- A delivery Git cannot produce is named and never replaced. [5]
- A leaf that records no delivery keeps its recorded default. [6]
- The line says which pair was delivered. [7]
- A closeout without its memory cell refuses and publishes nothing. [8]
- A recorded tree id is not a delivered commit. [9]
- An unconverted delivery opens the legacy-unavailable review. [10]
- A required conversion that fails is refused, not read as an empty base. [11]
- A numbered leaf-wide read records no comparison. [12]
- Publishing a record never replaces one that exists. [13]
- An injected publication loss is refused: with `publish_comparison_record` forced to `False` the record is refused as `reviewer_busy` with `offending_input` `2` while the leaf's records remain `[1]`, so no staged pair occupies number 2 (`test_review_delivered_comparison.py:509-529`). [14]
