# dashboard/src/test/fixtures/overrides.ts

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

The override parameter type the retained builders in `fixtures/wire.ts` take, and the reason it is not a bare `Partial<T>`. `RequiredKeys<T>` is local; `Overrides<O,T>` and `NoOverrides` are the two exported types. Source length and obsolete conversation-builder populations are not current API counts.

**The defect it closes.** Without exactOptionalPropertyTypes, optional slots in Partial<T> admit an explicit undefined; the builder spread writes it into the result. `enclosure({repoName:undefined})` therefore constructs an EnclosureNode whose required repoName is undefined, not a conversation page or missing capabilities. The retained taskEntry.stage, taskSummary.steps and projection.enclosures controls are the same required-field move without a cast. Overrides rejects this move at a fresh literal call site; property-name/AST guards alone cannot detect it.

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

Builders pair the constraint with a widening local: `function taskEntry<O extends Partial<X> = NoOverrides>(overrides?: Overrides<O, X>)`
then `const over: Partial<X> = overrides ?? {}` before spreading. The generic is what binds at the call
site; the local is what makes the spread ordinary.

### Invariants And Boundaries

- The rejection happens at the **CALL SITE**, in whichever tsconfig project the caller sits in. That is
  the property the project-wide flag would not have given for free: it covers `tsconfig.driver.json`'s
  retained driver-project consumers and the wire guard's own in-memory
  program, neither of which is the app project. Removed e2e-chats/production suites supply no current coverage.
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

**What this does NOT cover.** The current source documents two limits.

1. **Fresh literals only.** `const over: Partial<TaskEntry> = {stage:undefined}; taskEntry(over);` widens O to `Partial<TaskEntry>`, reopening optional undefined. The retained honest.test.ts probe entry k records this widened-variable residue as a known pass; it is not a conversationPage control. Only the project-wide flag closes that general gap.
2. **Outside wire.ts builders.** This constraint binds the retained fixtures/wire.ts parameters only. Other Partial<WireType> parameters, component props or decoders still admit explicit undefined under their own configuration. The removed conversationWire/conversationCapabilities builders supply no current scope or nested-control guarantee. This mapped type is not recursive validation, and no new nested test coverage is inferred.

## Evidence

### Docs References

The mechanism rests on two TypeScript behaviours: `exactOptionalPropertyTypes` (off here) governs
whether `undefined` may be written into an optional slot, and homomorphic mapped types are what let the
constraint preserve `O`'s own optionality while adding a demand over it.

External language references retained for reading only: [TSConfig Reference — exactOptionalPropertyTypes](https://www.typescriptlang.org/tsconfig/#exactOptionalPropertyTypes) and [TypeScript Handbook — Mapped Types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html). These URLs are not repository-relative citation sources.

No repository-relative Domain Documentation source applies; the two external TypeScript references above are retained for reading only.

### Repo-Internal References

- Partial overrides can erase required task-entry stage, enclosure repoName, task-summary steps or projection enclosures without a cast; the property-name guard does not see this value hole. [1]


- The measured rejection of `exactOptionalPropertyTypes` — 381 errors across 107 files on this tree — and the call-site property the narrow fix has instead.  Anchor: `exactOptionalPropertyTypes` [2]

- Current limits are fresh-literal-only and retained wire.ts builders only; the widened TaskEntry control is a known pass, not a removed conversation/nested builder promise. [3]
- `RequiredKeys<T>`, `Overrides<O, T>` and `NoOverrides`. [4]

- The proof that all four rejections fire, that excess-property checking survives, and that the widened-variable case is a known pass. [5]


- Consumer: every projection builder takes `Overrides<O, Node>`. [6]

- The app project's whole `compilerOptions` block — `strict` is on, `resolveJsonModule` is on, and no `exactOptionalPropertyTypes` entry appears anywhere in it. That absence is the config fact this file exists to answer. [8]

- tsconfig.driver.json currently enables strict driver checks for e2e and playwright.config.ts; its compilerOptions omit exactOptionalPropertyTypes. [9]


### Cross-Repo References

No meaningful cross-repository or external-system boundary is involved; this is a type helper for
in-repo test fixtures.


- Import and boundary review found the same-repository `wire.ts` consumer. [10]
