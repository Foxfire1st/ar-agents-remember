# mcp/src/agents_remember/models/knowledge/review_tree_entries.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review_tree_entries.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:22:59+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

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

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R31@v1` lives outside the code and memory
repositories, so it is named here and not cited as a row.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the per-side states, the locator fallback and the excerpt rule. | "are different facts and are never merged"; "is shown once" | mcp/src/agents_remember/models/knowledge/review_tree_entries.py:1-33 |
| The published names. | `__all__` | mcp/src/agents_remember/models/knowledge/review_tree_entries.py:49-56 |
| The four range states, the three change states and the excerpt bounds. | `ReviewEntryRangeState`; `ReviewEntryChange`; `EXCERPT_MAX_LINES`; `EXCERPT_MAX_CHARACTERS` | mcp/src/agents_remember/models/knowledge/review_tree_entries.py:58-61 |
| One entry on one side. | `ReviewTreeEntrySide` | mcp/src/agents_remember/models/knowledge/review_tree_entries.py:64-81 |
| One entry on both sides, joined to a member by `invariant_key`. | `ReviewTreeEntry` | mcp/src/agents_remember/models/knowledge/review_tree_entries.py:84-98 |
| The tree view's field that carries the entries. | `ReviewTreesResult` | mcp/src/agents_remember/models/knowledge/review_trees.py:242-264 |
| The client mirror of this shape. | `ReviewTreeEntrySide`; `ReviewTreeEntry` | dashboard/src/data/reviewTrees.ts:193-211; dashboard/src/data/reviewTrees.ts:213-222 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:22:59+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`): No content impact: this card's own source is unchanged. MIK-R32 moved lines in `mcp/src/agents_remember/models/knowledge/review_trees.py`, so the citation rows into them that moved were re-pointed by the installed fixer (run once; its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; every re-pointed row was byte-identical to memory HEAD beforehand and was checked to hold its anchors in the new range. No verification stamp was advanced.
- 2026-09-30T09:59:20+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): created this card for the new model MIK-R31 adds. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
