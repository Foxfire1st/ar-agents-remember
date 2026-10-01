# mcp/src/agents_remember/memory_quality/style/citations/drafts.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Describe migration declines and their next action.

`ACTIONS` is the curator-facing remediation table: every decline code names one reason the citation
cannot be converted without invention and supplies the edit that clears it. `TIERS` overrides the
default curator tier for the few codes that need a developer. Since 260831-LOCR-L33 the three
continuity-refusal codes raised by `repair._retarget` — `repair.ANCHOR_LEFT_LIVE_FILE`,
`repair.ANCHOR_CONTINUITY_UNPROVEN`, and `repair.ANCHOR_KIND_CHANGED` — each have an `ACTIONS` row
and are **deliberately left out of `TIERS`**, so `Draft.refuse`'s
`TIERS.get(code, work_order.CURATOR_TIER)` gives them the default curator tier. They are work a
curator does by reading the claim and re-citing where its fact now lives; none of them is a
developer decision.

## Code Commentary

### Logic

Module-level surface:

- `ACTIONS` (mapping, lines 31-127) — One remediation sentence per decline code; a code with no row cannot be refused.
- `TIERS` (mapping, line 129) — The tier override. Only `repair.ANCHOR_ABSENT` is present, because an anchor found nowhere may mean the claim changed and can require tier-3 review; everything else takes `work_order.CURATOR_TIER`.
- `Subject` (class, lines 132-139) — One document and the source file its own metadata table says it is about.
- `Draft` (class, lines 142-175) — One citation being migrated: where it is, what it states, and why it was refused. `refuse` records the `work_order.Item` and resolves the tier through `TIERS.get(code, work_order.CURATOR_TIER)`, which is the mechanism that gives an unlisted code the curator tier.
- `TableDraft` (class, lines 178-191) — One superseded table: where its header is, its rows, and the marker a padded row uses.
- `Result` (class, lines 194-214) — What one pass read, converted and declined.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- **A new decline code needs an `ACTIONS` row or it cannot be refused.** Leaving a code out of
  `TIERS` is not an omission — it is how a code takes the default curator tier.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- The curator-facing remediation for every decline code, including the three continuity refusals. [1]
- Only the anchor-found-nowhere code overrides the default curator tier. [2]
- Defines the class `Subject` (lines 132-139) — One document and the source file its own metadata table says it is about.. [3]
- Defines the class `Draft` (lines 142-175) — One citation being migrated: where it is, what it states, and why it was refused.. [4]
- Defines the class `TableDraft` (lines 178-191) — One superseded table: where its header is, its rows, and the marker a padded row uses.. [5]
- Defines the class `Result` (lines 194-214) — What one pass read, converted and declined.. [6]
- The refusal recorder resolves an unlisted code to the default curator tier. [7]
- The tier constants the override resolves against. [8]
