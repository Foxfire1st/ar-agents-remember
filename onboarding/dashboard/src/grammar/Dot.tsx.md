# dashboard/src/grammar/Dot.tsx

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

`Dot` is the one-monospace-cell attention severity mark: alarm, warn or info, with distinct glyphs and ink. Task stage/activity marks and words belong to pageParts/pageStyles, not this severity primitive.

## Code Commentary

### Logic

A Panda `cva` with a `variant` map plus three module constants.

The base is muted for an unclassified value. alarm uses alarm ink, warn amber and info cyan; each known severity also has its own glyph.

`DOT_GLYPHS` is total over DotVariant: alarm ▲, warn △ and info i. UNKNOWN_DOT_GLYPH is ?. Distinct shape remains readable in the task column beside the separate task-status grammar.

**The known-set is derived, not copied.** `export const DOT_VARIANTS = dot.variantMap.variant` reads
the keys off the recipe; `KNOWN` is a `ReadonlySet<string>` built from it and `DotVariant` is
`(typeof DOT_VARIANTS)[number]`. A second hand-maintained list is exactly what let
`awaiting-developer` reach this component and render **colourless** — it missed the copy, `variant`
resolved to `undefined`, and only the base applied.





Motion adds no identity: alarm can pulse, but reduced motion and Calm suppress animation while the severity glyph and ink stay complete.

The free string variant tolerates unknown values by rendering the muted base and ? rather than throwing or borrowing a known severity.

### Conventions

Vocabulary is derived from the single declaration that defines it (`dot.variantMap.variant`), never
restated. Any per-variant table is typed `Record<DotVariant, …>` so it stays total. The base is a
real treatment (`muted` + `?`), not an accident: it must never borrow a live variant's colour, and it
is the reason `Dot.test.tsx` treats the fallback as an independently distinguishable case rather than a special case.

### Invariants And Boundaries

- Presentational and `aria-hidden`. The mark is redundant with the label its consumers render beside
  it (the AttentionQueue Severity image), so
  announcing it would be noise.
- **Colour is required of every variant; the glyph is redundancy, not a replacement.** A build that
  stripped every hue must not pass — `Dot.test.tsx` asserts every variant carries a `c_*` class of
  its own.
- **No variant may share the base's tone.** Every consumer can reach the base, so that one collision
  is never safe; unknown severities must stay distinguishable.
- Motion may only add to a treatment that is already complete without it.
- The `pulse` keyframe is the shared global one in `index.css`, freezing under the
  Calm toggle (`?effects=off` / `html[data-effects="off"]`).
- The base sizing (`width: 1ch`, `textAlign: center`, `flexShrink: 0`, `userSelect: none`) keeps every
  variant in the same column, so a state change never reflows a rail row and a selection drag does
  not pick up the glyph.

### Todos

The earlier `panels/session-cockpit/StateDot.tsx` colour follow-up is retired: that source no longer exists. The current `Dot` severity recipe uses alarm, amber and cyan tokens; task status rendering belongs to `detail-panel/pageParts`, not the removed StateDot.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. The WCAG 2.3.1 flash-threshold constraint the `pulse` keyframe is written
against is recorded in the source comment rather than in an external reference this card could cite.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

The severity vocabulary and treatments are independent of native task stage/activity.



- The `cva` recipe, `DOT_VARIANTS`/`KNOWN`/`DotVariant`, the total `DOT_GLYPHS`, `UNKNOWN_DOT_GLYPH`, and the component. [1]



- The unlayered `html[data-effects="off"]` rule that nulls `animation`/`transition` with `!important` — why motion can never carry identity here. [4]






- `AttentionQueue` passes the raw `q.severity`. [7]





### Cross-Repo References

No cross-repository implementation claim. The local severity vocabulary is distinct from task status.

No meaningful cross-repo references found.
