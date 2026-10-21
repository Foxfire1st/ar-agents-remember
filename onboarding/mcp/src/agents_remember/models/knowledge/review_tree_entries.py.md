# mcp/src/agents_remember/models/knowledge/review_tree_entries.py

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Define each realization/proof card’s before/after code location, authored fields, currentness, excerpt and optional after-side memory values.

## Code Commentary

One ReviewTreeEntry carries its text id/kind, invariant text id plus projection key, before/after sides and changed/unchanged/undetermined comparison. The application producer fills it; this model performs no range resolution.

A side distinguishes recorded true/false from unknown and resolved/unresolved/absent/unavailable range state. It carries path/blob/range/content, reason, authored realization role/rationale or proof facet, and currentness only where that side records the entry. A supplied symbol names a symbol locator; line-range/file locators have no inferred symbol.

Excerpts come from the exact side blob, capped at 400 lines/48,000 characters with truncation explicit. An unchanged entry needs its excerpt only after; the locator fallback can still show an added/retired entry’s named code on the opposite side. Missing resolution never guesses change status.

Optional ReviewEntryMemory names the after-side path and four values: distinct invariants with a realization there, incoming invariant/family-member links, whether a live invariant lacks proof, and open path weaknesses. Counts are nonnegative. If those values could not be read, memory stays absent and the result’s entry_memory owner names why.

## Invariants And Boundaries

Absent code and an unreadable side are different facts. The model carries authored text and measured fields without renderer-written explanation, authenticating reads or creating a new invariant. Shared field bounds and snake_case wire names remain in use.

## Evidence

- Per-side fields include explicit range/currentness states and optional locator symbol. [8]
- The four after-side memory values have a path and nonnegative counts. [9]
- One entry joins to its invariant by key and optionally carries its memory values. [10]
- The source declares exact-side locator/excerpt and absence semantics. [11]
