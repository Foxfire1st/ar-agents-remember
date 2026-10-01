# dashboard/src/grammar/Dot.test.tsx

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

Vitest + Testing Library coverage for `Dot`, the one place a lifecycle state or an attention severity
becomes something a developer can see. Three flat properties, and deliberately nothing else:

1. the variant vocabulary equals what the wire can send plus what the queue can rank;
2. every variant renders differently from every other variant **and** from a variant the component
   does not know;
3. every variant carries an ink of its own, so the glyph is redundancy rather than a replacement.

The suite exists because `awaiting-developer` reached this component with no treatment at all — a
hand-copied `KNOWN` list missed it, `variant` resolved to `undefined`, and only the base applied. An
unrecognised variant does not throw and does not render blank; it silently ships looking like the
base. That is why the fallback is carried in the variant list as an extra citizen rather than as a
special case: "distinct from the fallback" and "distinct from each other" are the same requirement.

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

1. *treats exactly the states the wire can send and the severities the queue can rank* — asserts
   `[...DOT_VARIANTS].sort()` equals `[...LIFECYCLE_STATES, "alarm", "warn", "info"].sort()`.
   Asserted in **both** directions: a new lifecycle state with no dot treatment fails, and so does a
   recipe variant nothing can ever send. `DOT_VARIANTS` is read off the recipe, never hand-copied.
2. *renders every state and severity differently from every other, and from a variant it does not
   know* — walks `ALL_VARIANTS` into a `Map<appearance, variant>`, failing with the colliding
   variant's name, and finally asserts `seen.size === ALL_VARIANTS.length`. It also asserts each mark
   has non-empty `textContent`. Colour alone cannot carry this: `blocked`/`alarm`, `running`/`info`
   and `awaiting-developer`/`warn` are three hues each shared by a state and a severity the cockpit's
   left rail shows at the same time, so the glyph is what makes it pass.
3. *gives every variant an ink of its own, so the glyph is redundancy and not a replacement* —
   extracts the first `c_*` class per variant, asserts it exists, and asserts it differs from the
   fallback's. Without this a build that stripped every hue would still pass test 2 on glyphs alone.
   Sharing the base's tone is the one collision that is never safe, because every consumer can reach
   the base — while the base was `amber` that was literally true of `warn`.

### Conventions

The vocabulary is imported from the unit under test (`DOT_VARIANTS`) and from the wire mirror
(`LIFECYCLE_STATES`); this file holds no list of its own. Assertions read the rendered class list
rather than computed styles, because under jsdom the atomic class name is the declaration. `cleanup`
runs in `afterEach` since several helpers render inside loops.

### Invariants And Boundaries

- No stylesheet, no browser, no snapshot. The suite must stay readable as three properties, not as a
  table of expected class names — a snapshot would pass on a wrong-but-stable rendering.
- Animation atoms must stay excluded from the appearance key. Counting them would let a variant
  "differ" only by moving, which is exactly what the Calm toggle and reduced motion erase.
- The fallback stays a member of `ALL_VARIANTS`, never a separate assertion.
- Test 3 must keep asserting colour separately from test 2. Together they say "colour is required and
  the glyph is redundancy"; either one alone permits dropping a channel.
- Scope is the mark's own appearance. Accessible naming lives with the consumers (`LifecycleList`'s
  "Task progress: …" label, `AttentionQueue`'s "Severity: …" image); `Dot` is `aria-hidden`.

### Todos

No open file-local todos.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card is verified from its direct source and the component under test.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

The suite closes over three declarations it does not own: the recipe's variant map, the wire state
vocabulary, and the glyph table. All three are cited so a reader can see why no list is restated here.

- The suite declares `ALL_VARIANTS` with the explicit `FALLBACK` member. [1]
- `markOf` renders one mark and returns the rendered element for assertions. [2]
- `appearanceOf` derives the observable appearance key from the rendered mark. [3]
- The suite asserts the wire/recipe vocabulary equality. [4]
- The suite asserts distinct appearances for every variant and the fallback. [5]
- The suite asserts that every variant carries its own ink. [6]
- `DOT_VARIANTS = dot.variantMap.variant` is the derived vocabulary this suite imports rather than copying. [7]
- `DOT_GLYPHS` is the glyph table used by the dot recipe. [8]
- The `cva` base uses `color: "muted"`. [9]
- The `dot` recipe defines the state/severity color pairs that the glyph tests distinguish. [10]
- `LIFECYCLE_STATES` is the composed lifecycle vocabulary. [11]
- `LIVE_STATES` declares the live lifecycle vocabulary. [12]
- `TERMINAL_STATES` declares the terminal lifecycle vocabulary. [13]
- The effects-off source comment explicitly keeps the rule unlayered so it wins over the effects layer. [14]
- The `html[data-effects="off"]` selector is declared here. [15]
- The effects-off rule disables animation with `!important`. [16]
- The effects-off rule disables transition with `!important`. [17]
- `Cockpit.tsx` renders `AttentionQueue`. [18]
- `Cockpit.tsx` renders `LifecycleList`. [19]

### Cross-Repo References

No meaningful cross-repo references found. The vocabulary mirrors the served lifecycle states, but the
mirror (`types/projection.ts`) is in this repository.

No meaningful cross-repo references found.
