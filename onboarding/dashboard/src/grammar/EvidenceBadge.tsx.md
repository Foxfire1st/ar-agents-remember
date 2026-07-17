# dashboard/src/grammar/EvidenceBadge.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/EvidenceBadge.tsx`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `overview.md`                                    |

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

- `EVIDENCE_GLYPHS` (L13-L19): the exported tier→glyph record — the distinctness contract the
  test pins with a Set. Keyed by `EvidenceTier` (declared in `data/sessionCockpitStore.ts`).
- Panda `cva` (L23-L44): tier variants carry podracer token colors — pending `muted`, readback
  `mint`, model-validated `cyan`, defaults `dormant`, refused `alarm`; sizes `row` (0.72rem) and
  `sm` (0.62rem); inline-flex baseline layout, `whiteSpace: nowrap`.
- `EvidenceBadge({ tier, size = "row", showWord = false })` (L46-L69): a `role="img"` span with
  `aria-label` = `` `evidence ${tier}: ${TIER_SENSE[tier]}` `` (the tier word + its sense
  sentence from `data/launchEvidence.TIER_SENSE`), a matching `title`, and
  `data-evidence-tier`/`data-evidence-size` hooks; the glyph span is `aria-hidden` (L65);
  `showWord` additionally renders the tier word VISIBLY (banner usage, L66) — the accessible
  name carries it regardless.

### Invariants And Boundaries

- Five DISTINCT glyphs, always — no two tiers may ever share a mark (pinned by the Set test).
- The tier WORD must survive every size: it lives in the `aria-label`, so truncation or font
  size can never strip the evidence word.
- Render-only: tier assignment is `data/launchEvidence.launchTier`'s job; adding logic here
  (promotion, defaulting) would violate the evidence-honesty split.
- Styling is Panda `cva` in-file — `index.css` untouched (L3 posture).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Glyph record, cva variants, and the badge component. | L13-L69 | [EvidenceBadge.tsx](EvidenceBadge.tsx) |
| The tier machine + `TIER_SENSE` wording the aria-label embeds. | — | [../data/launchEvidence.ts](../data/launchEvidence.ts) |
| The `EvidenceTier` union the props/glyph record key on. | — | [../data/sessionCockpitStore.ts](../data/sessionCockpitStore.ts) |
| Provenance-chip consumer (derived tier, `size="sm"`). | — | [../panels/session-cockpit/HeaderStrip.tsx](../panels/session-cockpit/HeaderStrip.tsx) |
| Inspector consumer (same derivation). | — | [../panels/session-cockpit/SeatInspector.tsx](../panels/session-cockpit/SeatInspector.tsx) |
| Banner consumer (refused tier beside the never-validated pair). | — | [../panels/session-cockpit/FailedLaunchBanner.tsx](../panels/session-cockpit/FailedLaunchBanner.tsx) |
| The jsdom suite pinning distinctness + the word at every size. | L16-L62 | [EvidenceBadge.test.tsx](EvidenceBadge.test.tsx) |

## Update History

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R7 (evidence badge): five distinct glyphs
  (… / ✓ / ◇ / · / ✕), tier word always in the accessible name at every size, glyph aria-hidden,
  sizes row/sm on podracer token colors, optional visible word for banners — render-only, tier
  assignment stays in `data/launchEvidence.ts`. Verification metadata pinned to the leaf base
  until closeout stamps the L3 code commit.
