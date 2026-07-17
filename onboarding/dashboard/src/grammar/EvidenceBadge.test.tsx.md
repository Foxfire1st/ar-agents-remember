# dashboard/src/grammar/EvidenceBadge.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/EvidenceBadge.test.tsx`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

jsdom suite for the EvidenceBadge grammar primitive (260715-FEUI-L3 R7) — pins the two contracts
that make the badge honest at any size: five DISTINCT glyphs (no two tiers share a mark) and the
tier WORD present in the ACCESSIBLE name at every size, so truncation or font size can never
strip the evidence word.

## Code Commentary

### Logic

- **Glyph distinctness** (L17-L20): maps all five tiers through `EVIDENCE_GLYPHS` and asserts
  `new Set(...).size === 5` — a dropped or duplicated glyph fails loudly.
- **Leaf-doc glyph anatomy** (L22-L28): pins the exact marks — `✓` readback / `◇`
  model-validated / `·` defaults / `✕` refused / `…` pending (provenance-in-flight, never a
  verification mark).
- **Word at EVERY size** (L30-L41): renders all five tiers × both sizes (`row`, `sm`) and
  asserts `data-evidence-size` plus the tier word inside `aria-label`.
- **Glyph aria-hidden** (L43-L48): the mark is `aria-hidden`; the `role="img"` wrapper carries
  the accessible content.
- **`showWord`** (L50-L53): the visible tier word renders for banner usage.
- **Token colors** (L55-L61): refused wears `c_alarm`, readback `c_mint` (Panda class
  assertions).

### Conventions

Plain `@testing-library/react` render + `cleanup` per test; iterates `TIERS`/`SIZES` arrays typed
against the production unions so a vocabulary change breaks the suite at compile time. Test-only.

### Invariants And Boundaries

The distinctness Set and the word-at-every-size loop are the regression net for R7's
"tiers never collapse" rule — they must keep failing if a glyph is reused or the aria-label ever
drops the tier word.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component + glyph record under test. | L13-L69 | [EvidenceBadge.tsx](EvidenceBadge.tsx) |
| The `EvidenceTier` union the tier list types against. | — | [../data/sessionCockpitStore.ts](../data/sessionCockpitStore.ts) |

## Update History

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R7: glyph Set-distinctness, exact glyph
  anatomy, tier word in the accessible name at both sizes for all five tiers, aria-hidden mark,
  visible `showWord`, and token-color classes. Verification metadata pinned to the leaf base
  until closeout stamps the L3 code commit.
