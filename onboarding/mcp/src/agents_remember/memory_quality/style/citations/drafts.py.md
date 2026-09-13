# mcp/src/agents_remember/memory_quality/style/citations/drafts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/drafts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `723fd2f1becc130d85d7a6b285b93115be0df852` |
| lastVerifiedCommitDate | 2026-09-13T02:07:03+02:00|
| governingOverview | `../../overview.md` |

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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| The curator-facing remediation for every decline code, including the three continuity refusals. | `ACTIONS` | mcp/src/agents_remember/memory_quality/style/citations/drafts.py:31-127 |
| Only the anchor-found-nowhere code overrides the default curator tier. | `TIERS` | mcp/src/agents_remember/memory_quality/style/citations/drafts.py:129-129 |
| Defines the class `Subject` (lines 132-139) — One document and the source file its own metadata table says it is about.. | `Subject` | mcp/src/agents_remember/memory_quality/style/citations/drafts.py:132-139 |
| Defines the class `Draft` (lines 142-175) — One citation being migrated: where it is, what it states, and why it was refused.. | `Draft` | mcp/src/agents_remember/memory_quality/style/citations/drafts.py:142-175 |
| Defines the class `TableDraft` (lines 178-191) — One superseded table: where its header is, its rows, and the marker a padded row uses.. | `TableDraft` | mcp/src/agents_remember/memory_quality/style/citations/drafts.py:178-191 |
| Defines the class `Result` (lines 194-214) — What one pass read, converted and declined.. | `Result` | mcp/src/agents_remember/memory_quality/style/citations/drafts.py:194-214 |
| The refusal recorder resolves an unlisted code to the default curator tier. | "    def refuse(" | mcp/src/agents_remember/memory_quality/style/citations/drafts.py:158-175 |
| The tier constants the override resolves against. | `CURATOR_TIER`; `DEVELOPER_TIER` | mcp/src/agents_remember/memory_quality/style/citations/work_order.py:13-14 |

## Update History

- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: added the `ACTIONS` rows for the three new
  continuity-refusal codes (`anchor_left_live_file`, `anchor_continuity_unproven`,
  `anchor_kind_changed`) and recorded the deliberate choice to leave all three out of `TIERS`, so
  `Draft.refuse`'s `TIERS.get(code, work_order.CURATOR_TIER)` gives them the default curator tier —
  each is work a curator does by reading the claim and re-citing where its fact now lives. Recorded
  that a new decline code needs an `ACTIONS` row or it cannot be refused, and corrected every
  module-surface range. Verification metadata remains closeout-owned; no acceptance claim.

- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive class ranges; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
