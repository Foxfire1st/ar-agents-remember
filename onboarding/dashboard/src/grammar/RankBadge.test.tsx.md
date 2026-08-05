# dashboard/src/grammar/RankBadge.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/RankBadge.test.tsx`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T23:56:06+02:00                           |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`       |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

Vitest render tests for the `RankBadge` insignia primitive (260703-L14). The **glyph anatomy is
the contract** — the developer approved the V4 sketch pinned to exactly these shapes — so the
tests assert structure, not pixels.

## Code Commentary

### Logic

Four cases: (1) the orchestration tier renders four `path`s — a filled command pip
(`style.fill === "currentColor"`, not stroked) over three `stroke="currentColor"` chevrons —
with `data-rank-tier="orchestration"` and `aria-hidden`; (2) the management tier renders exactly
two chevron paths and no pip; (3) the `sm` size shrinks only the rendered `width`/`height`
(16×17 → 13×14) while the `viewBox` stays fixed, with `data-rank-size="sm"` emitted; (4) tier
colour comes from the Panda token classes (`c_gold` vs `c_purple`, read via SVG
`className.baseVal`).

### Invariants And Boundaries

Pure render tests — no store, no backend. The pip assertion reads the inline `style` (that inline
fill is the mechanism that outranks the cva's `& path { fill:none }`), so a refactor that drops it
to a class would fail here and must prove the pip still fills.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The orchestration-tier test renders the command pip and three chevrons, then asserts the filled pip and stroked chevrons. | "renders the orchestration tier as a command pip over three chevrons" | dashboard/src/grammar/RankBadge.test.tsx:12-23 |

## Update History
- 2026-08-04T13:25:51+02:00 — 260731-EFA-L6 S18-B01 same-reviewer semantic-binding repair: narrowed or split the flagged claim to source-clear evidence under the adversarial verdict, then the exact scoped fixer/check passed.

- 2026-07-06T23:56:06+02:00 — 260703-L14 (visual hierarchy + chat grouping): created — pins the V4
  glyph anatomy (pip + 3 chevrons vs 2 chevrons), fixed-viewBox size scaling, and gold/purple tier
  token classes. Verification metadata pinned until closeout stamps the L14 commit.
