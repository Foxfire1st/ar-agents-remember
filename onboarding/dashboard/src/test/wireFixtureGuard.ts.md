# dashboard/src/test/wireFixtureGuard.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/wireFixtureGuard.ts`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T09:50+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The mechanism behind `wireFixtureGuard.test.ts`: an AST + type-checker sweep over the whole dashboard
tree answering one question — *can a test assert against a payload the server could never send?*

**Why a guard and not just `tsc`.** TypeScript already refuses an impossible field on a wire-typed
object literal; `{ refusedPolarity: "amber" } satisfies EngineProcessEdge` does not compile. The leak is
that a fixture can OPT OUT, and every opt-out is one token long. The header lists seven (L9-L16):
`as EngineProcessEdge`; `as unknown as LifecycleProjection`; `as never` / `as any`;
`// @ts-expect-error`; `const raw = {…}; use(raw)` (a literal loses FRESHNESS in a variable, and
excess-property checking only applies to fresh literals); `Object.assign(base, {…})` (the result is an
intersection, which is assignable); `use(JSON.parse(text))` (`any` assigns to anything). **The last
three are not assertions at all and no ban on `as` can see them** — all three were confirmed against
this repo's TypeScript before the file was written. Hence five rules, four of which exist because
banning `as` alone is not enough.

If `contract.test.ts` makes the MIRROR honest, this makes the FIXTURES honest. Neither is worth much
alone: a perfect mirror nobody is checked against, or fixtures checked against a mirror that lies.

## Code Commentary

### Logic

**Vocabulary discovery, never a list.** `MIRROR_MARKER` (L108) is
`/^\s*\/\/\s*(TypeScript|Browser) mirror of\b/` and it is tested against the **first line only**
(`declaresItselfAMirror`, L110-L112). `isWireModule` (L114-L116) is that marker OR a path under
`src/types/`. `WireVocabulary`'s constructor (L241-L262) collects every export of every wire module
whose symbol flags include `Interface | TypeAlias | Enum`. `wireTypeNames` (L461-L482) is the same walk
exported as `<relative>:<Name>` strings so the guard's own test can refuse a vacuous run.

**Fixture surface.** `isFixtureSurface` (L118-L132): `*.test.ts(x)` / `*.spec.ts(x)`, anything matching
`fixture(s)?` as a file or a directory, everything under `src/test/` and `src/dev/`, any `e2e*/` root,
and `perf/`. `src/dev/` is in it because gallery fixtures are hydrated straight into the store.

**Program construction.** `SCANNED_ROOTS` (L136) is `src`, `e2e`, `e2e-production`, `e2e-chats`, `perf`.
`GUARD_COMPILER_OPTIONS` (L138-L149) is strict, bundler resolution, `resolveJsonModule` — and
deliberately does NOT set `exactOptionalPropertyTypes`, which is what makes `fixtureOverrides.test.ts`'s
assertions meaningful. `dashboardRoot()` (L170-L173) resolves from `import.meta.url`, not the process
cwd.

`buildProgramWithVirtualFiles` (L183-L230) lays in-memory files over the real tree so planted sources
can import the REAL wire types. It overrides `getSourceFile`, `fileExists`, `readFile` **and
`directoryExists`** — the last one is load-bearing and the comment says why (L192-L197): bundler
resolution asks `directoryExists` before looking inside a folder, and the planted directory is not on
disk, so without it a planted file importing another planted file fails to resolve, degrades to `any`,
and rule 3 fires for the wrong reason. It also pulls the wire modules in explicitly (L224-L229), because
a virtual file that never imports them would leave the vocabulary empty and every rule vacuous.

**Type resolution.** `mentionedByTypeNode` (L282-L335) walks a written type ANNOTATION, unaliasing
imports and local `type X = …` indirection and descending into arrays, unions and type arguments — so
`Partial<TaskDocNode>`, `LifecycleProjection[]`, `Record<string, Analytics>` and `typeof someWireValue`
all answer. Two deliberate behaviours: `as const` is skipped by name (it can only NARROW a literal), and
a name the checker cannot bind returns `UNRESOLVED` (L239) rather than `null` — "the guard did not
understand this" must read as a failure, not a pass. `mentionedByType` (L337-L357) does the same for a
resolved contextual type, which has no syntax.

**`wireSlotTarget`** (L359-L394) is the union-aware half. It strips `undefined`/`null`, reads each
remaining member through `wireObject` (L396-L410, which unwraps a single-argument alias such as
`Partial<TaskDocNode>` and bails on anything with an index signature), and **answers with EVERY member**.
That is the point: TypeScript's excess-property check against a non-discriminated union only requires
each property to exist in SOME member, so `SubTaskRow = TaskSubTaskRefNode | SeriesSubTaskNode` accepts a
row bearing `linkedLifecycleId` (only the first declares it) AND `createdAt` (only the second does) — a
blend of two `extra="forbid"` server models neither could send. **That pair is this leaf's own defect
reproduced as a type**, and `types/projection.ts` carries the comment explaining the collapse that caused
it. Conservative in the other direction: one member the guard cannot name abandons the whole slot rather
than measuring against half a union.

**The five rules**, in `collectWireFixtureFindings` (L484-L587):

| # | `WireFixtureRule` | What it catches | Scope |
| --- | --- | --- | --- |
| 1 | `wire-cast` | an assertion that NAMES a wire type — directly, renamed on import, behind a local alias, or inside a generic | every scanned file |
| 2 | `wire-position-cast` | an assertion naming no wire type (`as never`, `as any`, `as unknown`) landing in a wire-typed slot | fixture surface |
| 3 | `wire-any-value` | an `any`-typed value reaching a wire slot — `JSON.parse`, an untyped helper, a `: any` local | fixture surface |
| 4 | `wire-excess-property` | a shape the slot could never hold: a property no member declares (on a NON-fresh value), or a blend no SINGLE union member declares | fixture surface |
| 5 | `compiler-suppression` | a `@ts-expect-error` / `@ts-ignore` in a fixture file | fixture surface |

Rule 1 runs everywhere because a builder that casts in app code is a fixture too. Rules 2-5 run on the
fixture surface only: outside it, a cast to a wire type is the decode boundary saying "I am trusting the
server", a different and legitimate act, and those sites are registry-listed rather than rewritten.

Two details worth keeping. **Fresh object literals are skipped except against a union** (L534-L542) —
checking a fresh literal is `tsc`'s own job, and the union is exactly where `tsc` stops doing it
properly. And **suppressions are read as TOKENS, not lines** (`directiveLines`, L424-L452, with
`DIRECTIVE` at L459 mirroring TypeScript's own `commentDirectiveRegEx`): `contract.test.ts` discusses
`@ts-expect-error` in prose three times without using it, and this guard's own test file carries planted
directives inside template literals. A line-wise regex calls both a suppression; comment trivia sees
neither.

**`excessPropertyVerdict`** (L609-L658) returns either (a) the properties NO member declares, or (b) on a
union, the "blend" no single member declares, with a message naming the mutually exclusive shapes. It
reads an INTERSECTION on purpose — `Object.assign(node, {…})` answers `Wire & {…}`, assignable to the
wire type — and declines a union VALUE, an `any`/`unknown`, or a value with its own index signature.

**`reconcileWithRegistry`** (L673-L693) returns four lists: `unregistered` (a site no entry covers),
`spent` (an entry matching nothing), `miscounted` (an entry whose occurrence count moved), `unreasoned`
(an entry with no written reason). It counts occurrences per key rather than listing files, so a second
cast in an already-listed file fails and an exemption cannot outlive its reason.

### Conventions

- Finding keys are `<file> :: <what was written>` — stable under line moves, so the registry does not
  churn on every edit while the COUNT still catches a second occurrence.
- Fail-closed by design: an unresolvable type name is a finding, an empty vocabulary is asserted against
  in the test, and a planted-bypass suite proves each rule can bite.

### Invariants And Boundaries

- **The vocabulary is discovered, never listed.** Adding a mirror module means writing the house marker
  on its first line; nothing here should grow a hard-coded type list.
- The marker is matched on the FIRST LINE only. A module that moves its marker down a line silently
  leaves the vocabulary.
- `GUARD_COMPILER_OPTIONS` must keep omitting `exactOptionalPropertyTypes`; `fixtureOverrides.test.ts`
  borrows this program specifically because the flag is off.
- This module is a library. It performs no assertions and owns no policy — the registry, the planted
  bypasses and the vacuity checks all live in `wireFixtureGuard.test.ts`.

### Todos

**WHAT THIS DOES NOT COVER** — reproduced from the header (L39-L75), which records it "so the next
reader knows the SHAPE of what is uncovered rather than inferring completeness from a clean run". Each
was reproduced against this tree; none is fixed.

1. **Rule 4 reads four node kinds.** `Identifier`, `CallExpression`, `PropertyAccessExpression`, and
   (for the union case only) `ObjectLiteralExpression` — see `isCandidateForExcessCheck` (L594-L601).
   `ElementAccessExpression` (`rows[0]`) escapes, and so do `AwaitExpression`, `NewExpression` and
   `NonNullExpression` (`rows.at(0)!`). **This is the widest of the holes**, because array indexing and
   `await` are the two most idiomatic fixture accessors in this suite: `const row = rows[0]` reaching a
   wire slot is unread today, and so is `sink(await built())`.
2. **A generic helper defeats rules 1 and 4 together.** `function make<T>(shape: object): T { return
   shape as T; }` names no wire type at the assertion (rule 1 sees a type PARAMETER, not vocabulary), and
   `make<LifecycleProjection>({ … })` answers the wire type exactly, so rule 4 has no undeclared property
   to weigh. One helper re-opens every evasion the five rules close.
3. **A new UNMARKED mirror module is invisible.** The discovery mechanism is fail-closed in one direction
   only: a mirror that LOSES its marker fails the test's seven-module assertion loudly, while one that
   never carried a marker never appears — **and that assertion still passes**. Live instances today:
   `data/harnessCatalog.ts`, `data/submissionLifecycleClient.ts`, `data/changeset.ts`, `data/files.ts`,
   `data/notes.ts`. Each declares wire-shaped response types INLINE beside client-side option and handler
   types, so **fixtures for those routes are unguarded**. Both of the impossible fixtures this leaf
   removed — a `control` on the harness catalog row and a `bridgeEpoch` on `WithdrawalResultWire` — lived
   in exactly this blind spot. Widening the rule to "the header cites a `.py` file" was measured and
   rejected: it sweeps up the option types too, which are not wire shapes, and would make the guard wrong
   rather than wider. The real fix is to move those response types into a marker-carrying module — a
   refactor of app code, not of fixtures.
4. **Type predicates and assertion functions narrow with no `as` anywhere.**
   `function isPage(v: unknown): v is ConversationPage { return true; }` and
   `function assertPage(v: unknown): asserts v is ConversationPage {}` both put an arbitrary value into a
   wire slot carrying a wire type, with nothing syntactic to ban and nothing structural to compare.
5. **A value, not a name.** Every rule here measures property NAMES. An override whose names are all
   correct and whose VALUE is `undefined` on a field the server always sends is invisible to all five —
   `conversationPage({ capabilities: undefined })` asserts nothing, suppresses nothing and declares
   nothing undeclared. `exactOptionalPropertyTypes` is the general answer and is NOT set on this project
   (measured: 222 errors across 71 files); the builders carry the constraint themselves instead
   (`fixtures/overrides.ts`, proven by `fixtureOverrides.test.ts`).

## Docs References

The sweep is written against the TypeScript compiler API, and three specific language behaviours are
what the rules exist to compensate for: excess-property checking applies only to *fresh* object
literals, it is weakened against a non-discriminated union, and `any` is assignable to everything.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `ts.createProgram`, `ts.CompilerHost` overrides and `TypeChecker` navigation are the documented API this sweep is built on. | Using the Compiler API | [TypeScript Wiki — Using the Compiler API](https://github.com/microsoft/TypeScript/wiki/Using-the-Compiler-API) |
| Excess-property checking applies to *fresh* object literal types and is lost once the literal is assigned to a variable — the behaviour rule 4 extends to non-fresh values. | Excess Property Checks | [TypeScript Handbook — Object Types / Excess Property Checks](https://www.typescriptlang.org/docs/handbook/2/objects.html#excess-property-checks) |
| A type assertion may not be used to check a value, and `any` is assignable to every type — the two properties rules 1-3 exist to police. | Type Assertions; any | [TypeScript Handbook — Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The header: seven one-token opt-outs, why three of them carry no assertion at all, what makes the sweep fail-closed, and the rule scopes. | L1-L37 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |
| `WHAT THIS DOES NOT COVER`, items 1-5. | L39-L75 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |
| `MIRROR_MARKER`, `declaresItselfAMirror`, `isWireModule` — the discovered vocabulary. | L105-L116 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |
| `isFixtureSurface` — the surface rules 2-5 are strict on. | L118-L132 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |
| `GUARD_COMPILER_OPTIONS` (strict, bundler, `resolveJsonModule`, and no `exactOptionalPropertyTypes`). | L136-L149 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |
| `buildProgramWithVirtualFiles`, including the `directoryExists` override without which a two-module planted case silently degrades to `any`. | L183-L230 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |
| `mentionedByTypeNode` / `mentionedByType`, and `UNRESOLVED` as a finding rather than a skip. | L238-L239; L282-L357 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |
| `wireSlotTarget` answering a union with every member, with the `SubTaskRow` worked example. | L359-L410 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |
| `collectWireFixtureFindings` — the five rules, and the fresh-literal exception that keeps rule 4 from second-guessing `tsc`. | L484-L587 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |
| `isCandidateForExcessCheck` — the four node kinds, which is the exact shape of gap 1. | L589-L601 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |
| `directiveLines` + `DIRECTIVE` — suppressions read as comment trivia, not raw lines. | L424-L459 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |
| `excessPropertyVerdict` — undeclared properties, and the union blend no single member declares. | L603-L658 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |
| `reconcileWithRegistry` — unregistered / spent / miscounted / unreasoned. | L660-L693 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |
| The registry, planted bypasses and vacuity checks this module deliberately does not own. | L41-L182; L284-L447 | [wireFixtureGuard.test.ts](wireFixtureGuard.test.ts) |
| `SubTaskRow` and the two `extra="forbid"` models whose collapse the union rule reproduces. | L324-L354 | [../types/projection.ts](../types/projection.ts) |
| Gap 3, live: the first line is a "Same-origin client for …" header, not a `mirror of` marker, so nothing this module declares enters the vocabulary. | L1 | [../data/changeset.ts](../data/changeset.ts) |
| Same, for the read-only files API client. | L1 | [../data/files.ts](../data/files.ts) |
| Same, for the coordination-notes API client. | L1 | [../data/notes.ts](../data/notes.ts) |
| Gap 3 with a proven cost: `HarnessInfo` is declared inline (id/name/detected only) beside the client-side `HarnessCatalogErrorKind`/`HarnessCatalogRead`, with no marker — and fixtures adding a `control` field to that row lived unguarded until this leaf removed them. | L4-L16 | [../data/harnessCatalog.ts](../data/harnessCatalog.ts) |
| The other proven cost: `WithdrawalResultWire` declares no `bridgeEpoch` (the sibling `SubmissionStatusBatchWire` does), and the fixture that gave it one was invisible to the guard. | L35-L46 | [../data/submissionLifecycleClient.ts](../data/submissionLifecycleClient.ts) |
| Gap 5's answer: the call-site constraint the builders carry instead of the project-wide flag. | L23-L69 | [fixtures/overrides.ts](fixtures/overrides.ts) |

## Cross-Repo References

No cross-repository boundary. The sweep runs entirely over `dashboard/` sources in this repository; the
"wire" it polices is a Python↔TypeScript seam inside `agents-remember`, and the TypeScript compiler is a
devDependency rather than a system boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The scanned roots are all inside `dashboard/`; nothing outside this repository is read. | L136; L151-L177 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |

## Update History

- 2026-08-01T09:50+02:00 — 260731-EFA-L4 curator: created. Records the seven one-token opt-outs that
  make `tsc` alone insufficient, the five rules and their scopes, the DISCOVERED (never listed) mirror
  vocabulary, `wireSlotTarget`'s every-member union handling with the `SubTaskRow` case that reproduces
  this leaf's own defect, the token-level suppression scan, and the counting bidirectional registry
  reconciliation. Reproduces all five `WHAT THIS DOES NOT COVER` items in substance — rule 4's four node
  kinds (and the `ElementAccessExpression` / `AwaitExpression` / `NewExpression` / `NonNullExpression`
  blind spots), the generic helper that defeats rules 1 and 4 together, the invisible unmarked mirror
  module with its five live instances and the two impossible fixtures that lived there, type predicates
  and assertion functions, and the value-vs-name limit. Verification metadata pinned to the leaf base
  `abc7cbcc74921cdcb57a61529445f61641e919e7` until closeout stamps the L4 code commit.
