# dashboard/src/test/fixtures/overrides.ts

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

The override parameter type every builder in `fixtures/wire.ts` and `fixtures/conversationWire.ts`
takes, and the reason it is not a bare `Partial<T>`. Three exports in 69 lines: `RequiredKeys<T>`
(local), `Overrides<O, T>` and `NoOverrides`.

**The defect it closes.** `tsconfig.app.json` does not set `exactOptionalPropertyTypes`, so every
optional slot of a `Partial<T>` also accepts an EXPLICIT `undefined` — and the builders' trailing
`...over` writes it through. `conversationPage({ capabilities: undefined })` therefore compiled, and
answered a page whose REQUIRED `capabilities` was `undefined`: verbatim the defect
`conversationWire.ts`'s header says it fixed (`undefined as unknown as ConversationCapabilities` —
"worse: `capabilities` is REQUIRED, so this fixture stated that a required field is absent"), reachable
again with no cast at all. `lifecycle({ state: undefined })`, `taskDoc({ steps: undefined })` and
`projection({ enclosures: undefined })` are the same move.

Nothing in `wireFixtureGuard.ts` can see any of them, and the source says exactly why (cit:(["no assertion for rule 1"], dashboard/src/test/fixtures/overrides.ts:10-12)): there
is no assertion for rule 1, no suppression for rule 5, and rule 4 measures property NAMES, which are
all present and correct. This is the "a value" hole named in that guard's own
`WHAT THIS DOES NOT COVER` section — closed here at the type level rather than left to the AST sweep.

## Code Commentary

### Logic

- cit:([`RequiredKeys`], dashboard/src/test/fixtures/overrides.ts:46-48): the keys of `T` that carry no `?`. Implemented with the standard
  `-?` + `Record<never, never> extends Pick<T, K>` probe — an optional key makes `Pick<T, K>` satisfiable
  by the empty object, a required one does not.
- cit:([`Overrides`], dashboard/src/test/fixtures/overrides.ts:60-66): `O` intersected with a homomorphic mapped type over `O`'s own keys. For
  each key: if it is NOT a required key of `T`, pass `O[K]` through untouched. If it IS required but its
  declared type genuinely admits `undefined` (`foo: string | undefined`), also pass through. Otherwise
  `Exclude<O[K], undefined>` — which collapses to `never` for a literal `undefined`, and `never` is what
  produces the rejection. The observed diagnostic is
  `Type 'undefined' is not assignable to type 'never'`.
- cit:([`NoOverrides`], dashboard/src/test/fixtures/overrides.ts:69-69): `Record<never, never>`, the default type argument a builder uses when called
  with no argument at all.

The mapped half is homomorphic **on purpose** (documented L54-L58): it preserves `O`'s own optionality
and leaves excess-property checking to the `O extends Partial<T>` constraint at each builder's
declaration site, so a field the mirror does not declare still fails exactly the way it always did.
`fixtureOverrides.test.ts` asserts both halves — four rejections and two surviving excess-property
errors — because a constraint that quietly swallowed excess-property checking would have cost the
builders the property they exist for.

### Conventions

Builders pair the constraint with a widening local: `function lifecycle<O extends Partial<X> = NoOverrides>(overrides?: Overrides<O, X>)`
then `const over: Partial<X> = overrides ?? {}` before spreading. The generic is what binds at the call
site; the local is what makes the spread ordinary.

### Invariants And Boundaries

- The rejection happens at the **CALL SITE**, in whichever tsconfig project the caller sits in. That is
  the property the project-wide flag would not have given for free: it covers `tsconfig.driver.json`'s
  Playwright suites (`e2e`, `e2e-chats`, `e2e-production`, `perf`) and the wire guard's own in-memory
  program, neither of which is `tsconfig.app.json`.
- A required key whose declared type genuinely admits `undefined` must keep passing through. Tightening
  `Exclude<O[K], undefined>` onto every required key would reject shapes the server does send.
- This binds builder parameters only. It is not a decoder, a validator, or a runtime guard — it emits no
  runtime values at all.

### Why Not Just `exactOptionalPropertyTypes`

Recorded in the source (cit:(["222 errors across 71 files"], dashboard/src/test/fixtures/overrides.ts:14-21)) as a measured decision, not a preference. The flag is the general fix
and was measured on this tree: **222 errors across 71 files**, the bulk of them in app code
(`panels/DetailPanel.tsx`, `panels/eventSummary.ts`, `data/submitMachine.ts`,
`data/conversation-library/store.ts`) that this leaf does not own and that has other work in flight.
Turning it on and clearing 222 sites is its own change; turning it on and clearing some of them is worse
than not turning it on. So the narrow fix lives here.

The 222/71 figure is the source's recorded measurement at the time of the change, not a re-derived
number — treat it as provenance for the decision rather than as a current count.

### Todos

**What this does NOT cover.** The header carries three limits (cit:(["WHAT IT DOES NOT COVER"], dashboard/src/test/fixtures/overrides.ts:23-43)). They are the point of the
file, not caveats on it:

1. **The override must be a FRESH literal at the call site.** Widen it through a variable first —
   `const over: Partial<ConversationPage> = { capabilities: undefined }; conversationPage(over);` — and
   `O` infers `Partial<ConversationPage>`, every slot admits `undefined` again, and it compiles.
   `fixtureOverrides.test.ts` asserts that case as a **KNOWN PASS** (its `honest.test.ts` probe, entry
   `k`) rather than leaving it to be discovered. Only `exactOptionalPropertyTypes` closes it.
2. **ONE LEVEL DEEP ONLY.** `conversationCapabilities` takes per-GROUP overrides
   (`{ controls?: Partial<ConversationCapabilities["controls"]> }`), so
   `conversationCapabilities({ controls: { interrupt: undefined } })` still writes `undefined` onto a
   required leaf. Generalizing `Overrides` through a nesting level is a different and fiddlier type; it
   was left rather than half-done.
3. **EVERYTHING OUTSIDE THESE TWO MODULES.** This binds the builders in `fixtures/wire.ts` and
   `fixtures/conversationWire.ts` only. Any other `Partial<WireType>` parameter in the tree — a component
   prop, a store helper, an app-code decoder — still admits an explicit `undefined`, and only the
   project-wide flag would change that.

## Evidence

### Docs References

The mechanism rests on two TypeScript behaviours: `exactOptionalPropertyTypes` (off here) governs
whether `undefined` may be written into an optional slot, and homomorphic mapped types are what let the
constraint preserve `O`'s own optionality while adding a demand over it.

External language references retained for reading only: [TSConfig Reference — exactOptionalPropertyTypes](https://www.typescriptlang.org/tsconfig/#exactOptionalPropertyTypes) and [TypeScript Handbook — Mapped Types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html). These URLs are not repository-relative citation sources.

No repository-relative Domain Documentation source applies; the two external TypeScript references above are retained for reading only.

### Repo-Internal References

- The defect statement: `Partial<T>` admits an explicit `undefined`, the four reachable impossible fixtures, and why no `wireFixtureGuard` rule sees them. [1]
- The measured rejection of `exactOptionalPropertyTypes` (222 errors / 71 files) and the call-site property the narrow fix has instead. [2]
- The three documented limits: fresh-literal-only, one level deep, and only these two modules. [3]
- `RequiredKeys<T>`, `Overrides<O, T>` and `NoOverrides`. [4]
- The proof that all four rejections fire, that excess-property checking survives, and that the widened-variable case is a known pass. [5]
- Consumer: every projection builder takes `Overrides<O, Node>`. [6]
- Consumer: the conversation builders, including the one that is deliberately NOT an `Overrides` (`conversationCapabilities`, per-group and one level deeper). [7]
- The app project's whole `compilerOptions` block — `strict` is on, `resolveJsonModule` is on, and no `exactOptionalPropertyTypes` entry appears anywhere in it. That absence is the config fact this file exists to answer. [8]
- `tsconfig.driver.json` covers the Playwright suites (`e2e`, `e2e-chats`, `e2e-production`, `perf`) and also omits the flag, which is why a call-site constraint reaches further than the flag would have. [9]

### Cross-Repo References

No meaningful cross-repository or external-system boundary is involved; this is a type helper for
in-repo test fixtures.

- Import and boundary review found the same-repository `wire.ts` consumer. [10]
- Import and boundary review found the same-repository `conversationWire.ts` consumer. [11]
