# dashboard/src/grammar/Dot.test.tsx

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

Attention-severity Dot assertions only; task stage/activity marks belong to row/page owners.

1. DOT_VARIANTS equals alarm/warn/info.
2. Every severity and fallback differ without animation.
3. Each declared variant has ink distinct from fallback, independently of its glyph.

Fallback remains in ALL_VARIANTS. Lifecycle vocabulary equality is retired; no replacement task-state list belongs in this suite.

## Code Commentary

### Logic

`ALL_VARIANTS = [...DOT_VARIANTS, FALLBACK]` where `FALLBACK = "__no-such-variant__"`. `markOf`
renders one `<Dot>` and returns `container.firstElementChild`, throwing if the component rendered
nothing.

`appearanceOf(mark)` is the observable the second test compares. jsdom applies no stylesheet, so a
computed style would be useless — but Panda's atomic class names **are** the declarations (`c_amber`,
`anim-n_pulseSlow`), so the class list is what actually ships. It returns
`` `${textContent} ${sortedClassTokens}` `` with every token containing `anim` filtered out. Dropping
the animation atoms is the load-bearing choice: motion is additive in `Dot`, so a pair whose only
difference is that one of them moves is a pair that looks identical to anyone with the Calm toggle on
or `prefers-reduced-motion` set.

Three `it`s:

Vocabulary equals alarm/warn/info. Appearance keys exclude animation, require nonempty glyphs and reject pairwise collisions including fallback. Ink is independently required and differs from fallback; these are class/glyph assertions, not computed CSS.

### Conventions

DOT_VARIANTS comes from the recipe; no LIFECYCLE_STATES import remains. Tests inspect atomic classes under jsdom and clean up looped renders.

### Invariants And Boundaries

- No browser, stylesheet or snapshot proof.
- Animation cannot be the only distinction; Calm/reduced motion removes it.
- Fallback stays in ALL_VARIANTS and ink remains independent of glyph assertions.
- Dot is aria-hidden; severity naming belongs to consumers, task marks to row/page owners.

### Todos

No open file-local todos.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card is verified from its direct source and the component under test.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

The local recipe and glyph table govern severity marks, not a lifecycle vocabulary.

- The suite declares `ALL_VARIANTS` with the explicit `FALLBACK` member. [1]
- `markOf` renders one mark and returns the rendered element for assertions. [2]
- `appearanceOf` derives the observable appearance key from the rendered mark. [3]
- The vocabulary assertion requires exactly alarm/warn/info. [4]
- The suite asserts distinct appearances for every variant and the fallback. [5]
- The suite asserts that every variant carries its own ink. [6]
- `DOT_VARIANTS = dot.variantMap.variant` is the derived vocabulary this suite imports rather than copying. [7]
- `DOT_GLYPHS` is the glyph table used by the dot recipe. [8]
- The `cva` base uses `color: "muted"`. [9]
- The recipe defines attention-severity appearances, not task lifecycle marks. [10]



- The effects-off source comment explicitly keeps the rule unlayered so it wins over the effects layer. [14]
- The `html[data-effects="off"]` selector is declared here. [15]
- The effects-off rule disables animation with `!important`. [16]
- The effects-off rule disables transition with `!important`. [17]
- `Cockpit.tsx` renders `AttentionQueue`. [18]
- `Cockpit.tsx` renders `LifecycleList`. [19]

### Cross-Repo References

No cross-repository behavior is exercised; these are local severity-mark assertions, not lifecycle-wire coverage.

No meaningful cross-repo references found.
