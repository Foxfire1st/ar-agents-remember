# dashboard/src/grammar/Dot.tsx

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

`Dot` is the status mark: **one monospace cell** carrying either a lifecycle state
(`running`/`paused`/`blocked`/`awaiting-developer`/`completed`/`abandoned`) or an attention severity
(`alarm`/`warn`/`info`). Note 08 ("state by colour, never chrome") still rules the channel — colour
is the fastest read and it deliberately *groups* related facts — but nine variants plus a base cannot
be separated by the palette's seven tones, so each variant also carries a distinguishing **glyph**.

## Code Commentary

### Logic

A Panda `cva` with a `variant` map plus three module constants.

**Colour is the channel.** The base is `color: "muted"` — the palette's "we could not classify this"
tone. Variants: `running`/`info` cyan; `completed` mint; `blocked`/`alarm` alarm; `awaiting-developer`
and `warn` amber; `abandoned` dormant; `paused` a muted amber mixed in-file.

**The glyph is what separates the pairs colour groups.** `DOT_GLYPHS: Record<DotVariant, string>` is
total over the variant type, so a variant added to the recipe without a mark is a type error rather
than a dot that silently reads as some other state. The marks are `running ●`, `paused ◐`,
`blocked ×`, `awaiting-developer ◆`, `completed ✓`, `abandoned ○`, `alarm ▲`, `warn △`, `info i`,
with `UNKNOWN_DOT_GLYPH = "?"` for anything unrecognised. They are chosen for shape difference at
rail size out of blocks a monospace face carries (Basic Latin, Latin-1 Supplement, Geometric Shapes,
Dingbats). `Cockpit.tsx` renders the `awaiting-developer` and `warn` panels as siblings in one
always-visible rail, so without the mark a handoff and a queue warning are the same dot at a glance.

**The known-set is derived, not copied.** `export const DOT_VARIANTS = dot.variantMap.variant` reads
the keys off the recipe; `KNOWN` is a `ReadonlySet<string>` built from it and `DotVariant` is
`(typeof DOT_VARIANTS)[number]`. A second hand-maintained list is exactly what let
`awaiting-developer` reach this component and render **colourless** — it missed the copy, `variant`
resolved to `undefined`, and only the base applied.

**`paused` no longer looks dead.** `paused` and `abandoned` were both `bg_dormant` with no other
difference, sitting on adjacent rows of the same list — a lifecycle a developer can resume looked
identical to one that is over. `dormant` is the terminal tone (the session grammar spends it on
landed/retired/exited) so it stays with `abandoned`; `paused` takes a muted amber, the tone the
session grammar already rules for `waiting`.

**The mix is `in oklab`, deliberately.** `color-mix` interpolates polar hue along the *shorter* arc,
and amber (h 75) → muted (h 250) is 175° — just under the half turn — so an `in oklch` mix runs
through h 145 and renders **green**, a hand's breadth from `mint`. Measured in Chromium against the
built stylesheet (the only place it shows): OKLCH computes `oklch(0.772 0.104 145)`, OKLAB computes
`oklch(0.772 0.088 75)`.

**Motion is additive, never an identity.** `blocked`/`alarm` carry the shared `pulse` (≤3 flashes/s,
WCAG 2.3.1); `awaiting-developer` carries a slow `pulseSlow` breathe, never the fault strobe. All
three add `_motionReduce: { animation: "none" }`, so `prefers-reduced-motion` reaches the same
resting state the Calm toggle already forced. Motion cannot carry state here: `html[data-effects="off"]`
nulls every animation from an unlayered `!important` rule in `index.css`, so a state whose only
difference is that it moves has no difference at all for a large share of users.

The component still takes a free `variant: string` (`LifecycleList` passes `lifecycle.state` through
untouched), so an unrecognised variant does not throw — it renders the base tone and `?`.

### Conventions

Vocabulary is derived from the single declaration that defines it (`dot.variantMap.variant`), never
restated. Any per-variant table is typed `Record<DotVariant, …>` so it stays total. The base is a
real treatment (`muted` + `?`), not an accident: it must never borrow a live variant's colour, and it
is the reason `Dot.test.tsx` treats the fallback as a tenth citizen rather than a special case.

### Invariants And Boundaries

- Presentational and `aria-hidden`. The mark is redundant with the label its consumers render beside
  it (`LifecycleList`'s "Task progress: …" span, `AttentionQueue`'s "Severity: …" image), so
  announcing it would be noise.
- **Colour is required of every variant; the glyph is redundancy, not a replacement.** A build that
  stripped every hue must not pass — `Dot.test.tsx` asserts every variant carries a `c_*` class of
  its own.
- **No variant may share the base's tone.** Every consumer can reach the base, so that one collision
  is never safe; it is literally how `awaiting-developer` shipped looking like nothing special.
- Motion may only add to a treatment that is already complete without it.
- The `pulse` and `pulseSlow` keyframes are the shared global ones in `index.css`, freezing under the
  Calm toggle (`?effects=off` / `html[data-effects="off"]`).
- The base sizing (`width: 1ch`, `textAlign: center`, `flexShrink: 0`, `userSelect: none`) keeps every
  variant in the same column, so a state change never reflows a rail row and a selection drag does
  not pick up the glyph.

### Todos

`panels/session-cockpit/StateDot.tsx` mixes its own `mutedAmber` in `oklch` and therefore renders the
same unintended green described above. It is pre-existing and outside this leaf's file set — reported
here, not fixed.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. The WCAG 2.3.1 flash-threshold constraint the `pulse` keyframe is written
against is recorded in the source comment rather than in an external reference this card could cite.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

The dot is where a wire state becomes something visible, so the vocabulary it must cover is cited
alongside the treatments it applies.

- The `cva` recipe, `DOT_VARIANTS`/`KNOWN`/`DotVariant`, the total `DOT_GLYPHS`, `UNKNOWN_DOT_GLYPH`, and the component. [1]
- The shared `pulse` keyframe used by `blocked`/`alarm`, documented as ≤3 flashes/s under WCAG 2.3.1. [2]
- The `pulseSlow` keyframe used by `awaiting-developer` — the developer's 2026-07-16 ruling that the cockpit state pulse is a slow ease-in-out, never `steps()` blinking. [3]
- The unlayered `html[data-effects="off"]` rule that nulls `animation`/`transition` with `!important` — why motion can never carry identity here. [4]
- `LIFECYCLE_STATES` — the six states `DOT_VARIANTS` must cover; `Dot.test.tsx` asserts the two lists agree in both directions. The names are declared on the two halves (`LIVE_STATES` L42, `TERMINAL_STATES` L48) and composed at L59. [5]
- `LifecycleList` passes `lifecycle.state` through untouched as `item.variant` and renders the "Task progress: …" label beside the dot. [6]
- `AttentionQueue` passes the raw `q.severity`. [7]
- `Cockpit.tsx` renders `AttentionQueue` and `LifecycleList` as siblings in one always-visible rail — the reason an `awaiting-developer` state and a `warn` severity are on screen together. [8]
- The three flat properties this component is held to: vocabulary equality, every variant distinguishable from every other and from the fallback, and every variant carrying its own ink. [9]

### Cross-Repo References

No meaningful cross-repo references found. The variant vocabulary mirrors the served lifecycle states,
but the mirror itself lives in `types/projection.ts` inside this repository.

No meaningful cross-repo references found.
