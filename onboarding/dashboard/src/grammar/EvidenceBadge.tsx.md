# dashboard/src/grammar/EvidenceBadge.tsx

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

The **launch-evidence badge** (260715-FEUI-L3 R7) — the ONE grammar primitive rendering the five
evidence tiers, with five DISTINCT glyphs so tiers never collapse at ambient sizes: `…` pending
(in-flight provenance, deliberately not a verification mark), `✓` readback (OK echo), `◇`
model-validated (diamond validated), `·` defaults (dot), `✕` refused. The tier WORD is ALWAYS
present in the accessible name at every size (the glyph alone is aria-hidden). Assignment comes
from `data/launchEvidence.launchTier` — this component only renders, it never decides. Consumed
by the HeaderStrip provenance chip, SeatInspector, and FailedLaunchBanner.

## Code Commentary

### Logic

- cit:([`EVIDENCE_GLYPHS`], dashboard/src/grammar/EvidenceBadge.tsx:13-19): the exported tier→glyph record — the distinctness contract the
  test pins with a Set. Keyed by `EvidenceTier` (declared in `data/sessionCockpitStore.ts`).
- cit:([`cva`], dashboard/src/grammar/EvidenceBadge.tsx:23-44): Panda tier variants carry podracer token colors — pending `muted`, readback
  `mint`, model-validated `cyan`, defaults `dormant`, refused `alarm`; sizes `row` (0.72rem) and
  `sm` (0.62rem); inline-flex baseline layout, `whiteSpace: nowrap`.
- cit:([`EvidenceBadge`], dashboard/src/grammar/EvidenceBadge.tsx:46-69): a `role="img"` span with
  `aria-label` = `` `evidence ${tier}: ${TIER_SENSE[tier]}` `` (the tier word + its sense
  sentence from `data/launchEvidence.TIER_SENSE`), a matching `title`, and
  `data-evidence-tier`/`data-evidence-size` hooks; the glyph span is `aria-hidden`;
  `showWord` additionally renders the tier word VISIBLY (banner usage) — the accessible
  name carries it regardless.

### Invariants And Boundaries

- Five DISTINCT glyphs, always — no two tiers may ever share a mark (pinned by the Set test).
- The tier WORD must survive every size: it lives in the `aria-label`, so truncation or font
  size can never strip the evidence word.
- Render-only: tier assignment is `data/launchEvidence.launchTier`'s job; adding logic here
  (promotion, defaulting) would violate the evidence-honesty split.
- Styling is Panda `cva` in-file — `index.css` untouched (L3 posture).

## Evidence

### Repo-Internal References

- Glyph record, cva variants, and the badge component. [1]
- The tier machine + `TIER_SENSE` wording the aria-label embeds. [2]
- The `EvidenceTier` union the props/glyph record key on. [3]
- Provenance-chip consumer (derived tier, `size="sm"`). [4]
- Inspector consumer (same derivation). [5]
- Banner consumer (refused tier beside the never-validated pair). [6]
- The jsdom suite pinning distinctness + the word at every size. [7]
