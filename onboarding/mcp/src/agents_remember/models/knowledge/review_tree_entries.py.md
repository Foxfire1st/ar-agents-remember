# mcp/src/agents_remember/models/knowledge/review_tree_entries.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The wire shape of one realization or proof entry located on both code sides of a tree comparison (MIK-R31).**
A focused expression card needs, per entry, what the landed dataset payload does not carry for a tree comparison:
the entry's text ID and kind, its authored role and rationale (a realization) or facet (a proof), and the range
its locator resolves to on each code side by the MIK-R08 definition 3 rule. This module fixes that shape;
`application/review_tree_entries.py` fills it, and `ReviewTreesResult.entries` carries it on the wire.

## Code Commentary

### Logic

- **`ReviewTreeEntry`** is one entry ID of K_B or K_C: `id`, `kind` (`realization` or `proof`), `invariant` (the
  text ID), `invariant_key` (the identity the landed review payload addresses the invariant by, the index
  projection's name-based UUID, so a renderer joins an entry to a family member by value and never by a display
  label), `before` (code base B), `after` (code candidate C) and `change`.
- **`ReviewTreeEntrySide`** is the entry on one side:
  - `recorded` says whether that side's memory tree holds the entry (K_B for `before`, K_C for `after`), so an
    added or retired entry is named rather than inferred; it is `None` when that memory tree could not be read.
  - `state` (`ReviewEntryRangeState`) is `resolved` (a range and its content identity), `unresolved` (the locator
    does not resolve there; `reason` says why and no range is guessed), `absent` (no regular file at the path) or
    `unavailable` (the side could not be read; `reason` names what).
  - `blob`, `start_line`, `end_line`, `content`: the resolved range and its content identity.
  - `excerpt` and `excerpt_truncated`: the range's text from the side's exact blob, bounded by `EXCERPT_MAX_LINES`
    (400) and `EXCERPT_MAX_CHARACTERS` (48,000).
  - `role`, `rationale` or `facet`: the side's own authored fields; `currentness` and `currentness_reason`: the
    side's MIK-R03 entry state, present only where the side records the entry.
- **`ReviewEntryChange`**: `changed`, `unchanged` or `undetermined` (either side has no resolved range, so a card is
  never counted as changed or unchanged by guess). An `unchanged` entry carries its excerpt on the `after` side only.

### Conventions

- `KnowledgeModel` fields bounded by the shared limits (`PATH_MAX_LENGTH`, `REFERENCE_MAX_LENGTH`,
  `PROSE_MAX_LENGTH`, `GIT_OBJECT_PATTERN`); the wire keys are snake_case like the rest of the tree view.

### Invariants And Boundaries

- `absent` and `unavailable` are different facts and are never merged (MIK-R31 Failure and Recovery Behavior).
- The model carries only authored text; it has no field for renderer-written explanation (MIK-R31 rule 2).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R31@v1` lives outside the code and memory
repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement of the per-side states, the locator fallback and the excerpt rule. [1]
- The published names. [2]
- The four range states, the three change states and the excerpt bounds. [3]
- One entry on one side. [4]
- One entry on both sides, joined to a member by `invariant_key`. [5]
- The tree view's field that carries the entries. [6]
- The client mirror of this shape. [7]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
