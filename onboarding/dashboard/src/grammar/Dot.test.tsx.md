# dashboard/src/grammar/Dot.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/Dot.test.tsx`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T10:30+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                    |

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

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card is verified from its direct source and the component under test.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

The suite closes over three declarations it does not own: the recipe's variant map, the wire state
vocabulary, and the glyph table. All three are cited so a reader can see why no list is restated here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite declares `ALL_VARIANTS` with the explicit `FALLBACK` member. | `ALL_VARIANTS` | dashboard/src/grammar/Dot.test.tsx:17-17 |
| `markOf` renders one mark and returns the rendered element for assertions. | `markOf` | dashboard/src/grammar/Dot.test.tsx:19-24 |
| `appearanceOf` derives the observable appearance key from the rendered mark. | `appearanceOf` | dashboard/src/grammar/Dot.test.tsx:35-42 |
| The suite asserts the wire/recipe vocabulary equality. | "treats exactly the states" | dashboard/src/grammar/Dot.test.tsx:45-51 |
| The suite asserts distinct appearances for every variant and the fallback. | "renders every state" | dashboard/src/grammar/Dot.test.tsx:53-70 |
| The suite asserts that every variant carries its own ink. | "gives every variant an ink" | dashboard/src/grammar/Dot.test.tsx:72-87 |
| `DOT_VARIANTS = dot.variantMap.variant` is the derived vocabulary this suite imports rather than copying. | `DOT_VARIANTS` | dashboard/src/grammar/Dot.tsx:92-92 |
| `DOT_GLYPHS` is the glyph table used by the dot recipe. | `DOT_GLYPHS` | dashboard/src/grammar/Dot.tsx:104-114 |
| The `cva` base uses `color: "muted"`. | "color: \"muted\"" | dashboard/src/grammar/Dot.tsx:37-37 |
| The `dot` recipe defines the state/severity color pairs that the glyph tests distinguish. | `dot` | dashboard/src/grammar/Dot.tsx:23-87 |
| `LIFECYCLE_STATES` is the composed lifecycle vocabulary. | `LIFECYCLE_STATES` | dashboard/src/types/projection.ts:13-13 |
| `LIVE_STATES` declares the live lifecycle vocabulary. | `LIVE_STATES` | dashboard/src/types/projection.ts:9-9 |
| `TERMINAL_STATES` declares the terminal lifecycle vocabulary. | `TERMINAL_STATES` | dashboard/src/types/projection.ts:11-11 |
| The effects-off source comment explicitly keeps the rule unlayered so it wins over the effects layer. | "Unlayered + !important so it always wins over the effects layer." | dashboard/src/index.css:136-137 |
| The `html[data-effects="off"]` selector is declared here. | "html[data-effects=\"off\"] *," | dashboard/src/index.css:138-138 |
| The effects-off rule disables animation with `!important`. | "animation: none" | dashboard/src/index.css:141-141 |
| The effects-off rule disables transition with `!important`. | "transition: none" | dashboard/src/index.css:142-142 |
| `Cockpit.tsx` renders `AttentionQueue`. | "<AttentionQueue" | dashboard/src/cockpit/Cockpit.tsx:638-638 |
| `Cockpit.tsx` renders `LifecycleList`. | "<LifecycleList" | dashboard/src/cockpit/Cockpit.tsx:639-639 |

## Cross-Repo References

No meaningful cross-repo references found. The vocabulary mirrors the served lifecycle states, but the
mirror (`types/projection.ts`) is in this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T15:56:39+02:00 — 260731-EFA-L6 S18-B10 curator: closed same-reviewer residuals D7 and D9 by binding the color-pair claim to the `dot` recipe extent and splitting the unlayered source-comment predicate from the literal selector declaration; rechecked this card through the locked exact-document fixer/check.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-08-01T10:30+02:00 — 260731-EFA-L4 curator (citation pass): `types/projection.ts` adopted the
  server's state partition (`LIVE_STATES` + `TERMINAL_STATES` composed into `LIFECYCLE_STATES`), moving
  every anchor below it. Re-anchored the one row citing that file: `LIFECYCLE_STATES` L21-L30 → L42-L59,
  which spans both halves and the composed tuple. The equality assertion still imports the one tuple, so
  no claim in the body changed.
- 2026-08-01T09:46+02:00 — 260731-EFA-L4 curator: created. New suite pinning three flat properties of
  `Dot` — vocabulary equality against `LIFECYCLE_STATES` in both directions, every variant plus the
  fallback rendering distinguishably (with animation atoms excluded, so motion cannot stand in for
  identity), and every variant carrying its own `c_*` ink so a hue-stripped build cannot pass on
  glyphs alone. Verification metadata pinned to the leaf base (`abc7cbc`); the source file is still
  uncommitted and closeout stamps the code commit.
