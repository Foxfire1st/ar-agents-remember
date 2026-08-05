# dashboard/src/grammar/EvidenceBadge.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/EvidenceBadge.tsx`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Glyph record, cva variants, and the badge component. | `EvidenceBadge` | dashboard/src/grammar/EvidenceBadge.tsx:46-69 |
| The tier machine + `TIER_SENSE` wording the aria-label embeds. | `TIER_SENSE` | dashboard/src/data/launchEvidence.ts:44-51 |
| The `EvidenceTier` union the props/glyph record key on. | `EvidenceTier` | dashboard/src/data/sessionCockpitStore.ts:18-18 |
| Provenance-chip consumer (derived tier, `size="sm"`). | `HeaderStrip` | dashboard/src/panels/session-cockpit/HeaderStrip.tsx:88-169 |
| Inspector consumer (same derivation). | `SeatInspector` | dashboard/src/panels/session-cockpit/SeatInspector.tsx:60-161 |
| Banner consumer (refused tier beside the never-validated pair). | `FailedLaunchBanner` | dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:70-182 |
| The jsdom suite pinning distinctness + the word at every size. | "the tier WORD is present in the accessible name at EVERY size" | dashboard/src/grammar/EvidenceBadge.test.tsx:30-41 |

## Update History
- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 5 repository-reference citations and normalized 1 prose citation (5/5 anchored and sourced; scoped citation check clean).

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R7 (evidence badge): five distinct glyphs
  (… / ✓ / ◇ / · / ✕), tier word always in the accessible name at every size, glyph aria-hidden,
  sizes row/sm on podracer token colors, optional visible word for banners — render-only, tier
  assignment stays in `data/launchEvidence.ts`. Verification metadata pinned to the leaf base
  until closeout stamps the L3 code commit.
