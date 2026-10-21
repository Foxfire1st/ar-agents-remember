# mcp/src/agents_remember/application/review_tree_entries.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Build focused realization/proof cards for named invariants on both pinned code sides, including exact excerpts, locator symbol and after-index memory values.

## Code Commentary

tree_entries reads each memory side for the requested invariant text keys, unions entry ids and sorts by invariant, kind, path and id. It returns CardEntries, containing entries plus the after-memory read state. The after side opens its index once, enumerates entries and measures memory values while that same index stays open.

Each card takes its own side entry or, for location only, the other side locator. recorded is unknown when a memory side cannot be read; authored realization role/rationale or proof facet and currentness come only from the side own entry. Empty authored text remains absent. symbol copies a nonblank symbol-locator name and is never inferred for file or line-range locators.

After-side memory values use the after entry when present, otherwise the before entry location. They count distinct invariant realizations at that path, incoming invariant/family-member links, live invariants lacking proof and open weaknesses. The path realization and incoming-link reads are reused within this one open index. Available state retains complete/partial status; APSW/index/I/O failures yield unavailable with a bounded reason and no values, while the entries remain answerable.

Placement distinguishes code unavailable, path absent, resolved and unresolved. Only symbol, line_range and file locators are supported; missing grammar is unresolved and an unavailable recorded blob for a line locator is unavailable. _unsupported and resolution share the same guarded read, so Git/CodeRead failures become named unavailable states instead of escaping through the probe.

The excerpt slices the pinned side blob, not the locator recorded blob, at the resolved span. It keeps at most 400 lines and 48,000 characters and marks a cut; non-UTF-8 or unreadable excerpt bytes produce a reason rather than replacement text. Two resolved content identities determine unchanged/changed; resolved against absent is changed; other combinations are undetermined. Unchanged text is carried only after.

PLACEMENTS keeps at most 8,192 observation-key answers, including a resolution miss; exceptions are not cached and are read again. The leaf-wide owner does not request every excerpt: this remains an on-demand card read. The prior 637 KB leaf-wide and 38,264-byte focused measurements are historical motivation, not newly run evidence.

## Invariants And Boundaries

Nothing is written, re-anchored or judged. An unreadable memory side is not an absent entry, and a missing file is not an unreadable code tree. The locator recorded blob maps a line range only; the exact pinned side blob supplies text. Successful location does not guarantee excerpt readability or memory-value availability, and no renderer-authored explanation replaces entry prose.

## Evidence

- The focused result includes entries and explicit after-memory state from one index opening. [12]
- Memory measurements share the after index and fail independently with a bounded unavailable reason. [13]
- Each card preserves own-side authored/currentness values, carries the locator symbol and derives change conservatively. [14]
- Pinned code placement and exact bounded excerpts keep absence/read failure distinct. [15]
- The observation-key cache stores answers only; unsupported locators and failed resolution keep named outcomes. [16]
- The placement memo is bounded at 8192 entries. [17]
