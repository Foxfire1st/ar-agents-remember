# dashboard/src/grammar/EvidenceBadge.test.tsx

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

jsdom suite for the EvidenceBadge grammar primitive (260715-FEUI-L3 R7) — pins the two contracts
that make the badge honest at any size: five DISTINCT glyphs (no two tiers share a mark) and the
tier WORD present in the ACCESSIBLE name at every size, so truncation or font size can never
strip the evidence word.

## Code Commentary

### Logic

- **Glyph distinctness** (cit:([`EVIDENCE_GLYPHS`], dashboard/src/grammar/EvidenceBadge.tsx:13-19)): maps all five tiers through `EVIDENCE_GLYPHS` and asserts
  `new Set(...).size === 5` — a dropped or duplicated glyph fails loudly.
- **Leaf-doc glyph anatomy** (cit:([`EVIDENCE_GLYPHS`], dashboard/src/grammar/EvidenceBadge.tsx:13-19)): pins the exact marks — `✓` readback / `◇`
  model-validated / `·` defaults / `✕` refused / `…` pending (provenance-in-flight, never a
  verification mark).
- **Word at EVERY size** (cit:(["data-evidence-size"], dashboard/src/grammar/EvidenceBadge.test.tsx:35-35)): renders all five tiers × both sizes (`row`, `sm`) and
  asserts `data-evidence-size` plus the tier word inside `aria-label`.
- **Glyph aria-hidden** (cit:(["aria-hidden='true'"], dashboard/src/grammar/EvidenceBadge.test.tsx:45-45)): the mark is `aria-hidden`; the `role="img"` wrapper carries
  the accessible content.
- **`showWord`** (cit:(["showWord renders the tier word visibly (banner usage)"], dashboard/src/grammar/EvidenceBadge.test.tsx:50-53)): the visible tier word renders for banner usage.
- **Token colors** (cit:(["c_alarm", "c_mint"], dashboard/src/grammar/EvidenceBadge.test.tsx:57-57; dashboard/src/grammar/EvidenceBadge.test.tsx:60-60)): refused wears `c_alarm`, readback `c_mint` (Panda class
  assertions).

### Conventions

Plain `@testing-library/react` render + `cleanup` per test; iterates `TIERS`/`SIZES` arrays typed
against the production unions so a vocabulary change breaks the suite at compile time. Test-only.

### Invariants And Boundaries

The distinctness Set and the word-at-every-size loop are the regression net for R7's
"tiers never collapse" rule — they must keep failing if a glyph is reused or the aria-label ever
drops the tier word.

## Evidence

### Repo-Internal References

- The component + glyph record under test. [1]
- The `EvidenceTier` union the tier list types against. [2]
