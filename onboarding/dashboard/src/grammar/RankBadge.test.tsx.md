# dashboard/src/grammar/RankBadge.test.tsx

## Retired source — not a current contract

The rank-chevron primitive and its anatomy/size tests were removed together after the consumer census. This suite no longer proves a current renderer; hierarchy, marks and selection are covered by the current lifecycle-list suites. See [current hierarchy suite](../panels/lifecycle-list/hierarchy.test.tsx.md).

The original explanation and numbered evidence below are retained as historical provenance only; they authorize no current import or renderer.

<details>
<summary>Historical removed-source account</summary>


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

## Evidence

### Repo-Internal References

- The orchestration-tier test renders the command pip and three chevrons, then asserts the filled pip and stroked chevrons. [1]

</details>
