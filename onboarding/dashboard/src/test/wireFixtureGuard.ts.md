# dashboard/src/test/wireFixtureGuard.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/wireFixtureGuard.ts`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T09:50+02:00                           |
| lastVerifiedCommitHash | `dc03c64a91947cee470622c560c516854eec86b5`       |
| lastVerifiedCommitDate | 2026-08-30T17:41:53+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The mechanism behind `wireFixtureGuard.test.ts`: an AST + type-checker sweep over the whole dashboard
tree answering one question — *can a test assert against a payload the server could never send?*

**Why a guard and not just `tsc`.** TypeScript already refuses an impossible field on a wire-typed
object literal; `{ refusedPolarity: "amber" } satisfies EngineProcessEdge` does not compile. The leak is
that a fixture can OPT OUT, and every opt-out is one token long. The header lists seven cit:(["as unknown as LifecycleProjection"], dashboard/src/test/wireFixtureGuard.ts:10-10):
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

**Vocabulary discovery, never a list.** cit:([`MIRROR_MARKER`], dashboard/src/test/wireFixtureGuard.ts:108-108) is
`/^\s*\/\/\s*(TypeScript|Browser) mirror of\b/` and it is tested against the **first line only**
cit:([`declaresItselfAMirror`], dashboard/src/test/wireFixtureGuard.ts:110-112). cit:([`isWireModule`], dashboard/src/test/wireFixtureGuard.ts:114-116) is that marker OR a path under
`src/types/`. `WireVocabulary`'s constructor cit:([`WireVocabulary`], dashboard/src/test/wireFixtureGuard.ts:241-411) collects every export of every wire module
whose symbol flags include `Interface | TypeAlias | Enum`. cit:([`wireTypeNames`], dashboard/src/test/wireFixtureGuard.ts:466-482) is the same walk
exported as `<relative>:<Name>` strings so the guard's own test can refuse a vacuous run.

**Fixture surface.** cit:([`isFixtureSurface`], dashboard/src/test/wireFixtureGuard.ts:123-132): `*.test.ts(x)` / `*.spec.ts(x)`, anything matching
`fixture(s)?` as a file or a directory, everything under `src/test/` and `src/dev/`, any `e2e*/` root,
and `perf/`. `src/dev/` is in it because gallery fixtures are hydrated straight into the store.

**Program construction.** cit:([`SCANNED_ROOTS`], dashboard/src/test/wireFixtureGuard.ts:136-136) is `src`, `e2e`, `e2e-production`, `e2e-chats`, `perf`.
cit:([`GUARD_COMPILER_OPTIONS`], dashboard/src/test/wireFixtureGuard.ts:138-149) is strict, bundler resolution, `resolveJsonModule` — and
deliberately does NOT set `exactOptionalPropertyTypes`, which is what makes `fixtureOverrides.test.ts`'s
assertions meaningful. cit:([`dashboardRoot`], dashboard/src/test/wireFixtureGuard.ts:171-173) resolves from `import.meta.url`, not the process
cwd.

cit:([`buildProgramWithVirtualFiles`], dashboard/src/test/wireFixtureGuard.ts:188-230) lays in-memory files over the real tree so planted sources
can import the REAL wire types. It overrides `getSourceFile`, `fileExists`, `readFile` **and
`directoryExists`** — the last one is load-bearing and the comment says why cit:([`buildProgramWithVirtualFiles`], dashboard/src/test/wireFixtureGuard.ts:188-230): bundler
resolution asks `directoryExists` before looking inside a folder, and the planted directory is not on
disk, so without it a planted file importing another planted file fails to resolve, degrades to `any`,
and rule 3 fires for the wrong reason. It also pulls the wire modules in explicitly cit:([`wireModules`], dashboard/src/test/wireFixtureGuard.ts:226-228), because
a virtual file that never imports them would leave the vocabulary empty and every rule vacuous.

**Type resolution.** cit:([`mentionedByTypeNode`], dashboard/src/test/wireFixtureGuard.ts:289-335) walks a written type ANNOTATION, unaliasing
imports and local `type X = …` indirection and descending into arrays, unions and type arguments — so
`Partial<TaskDocNode>`, `LifecycleProjection[]`, `Record<string, Analytics>` and `typeof someWireValue`
all answer. Two deliberate behaviours: `as const` is skipped by name (it can only NARROW a literal), and
a name the checker cannot bind returns cit:([`UNRESOLVED`], dashboard/src/test/wireFixtureGuard.ts:239-239) rather than `null` — "the guard did not
understand this" must read as a failure, not a pass. cit:([`mentionedByType`], dashboard/src/test/wireFixtureGuard.ts:338-357) does the same for a
resolved contextual type, which has no syntax.

**`wireSlotTarget`** cit:([`wireSlotTarget`], dashboard/src/test/wireFixtureGuard.ts:376-394) is the union-aware half. It strips `undefined`/`null`, reads each
remaining member through `wireObject` cit:([`wireObject`], dashboard/src/test/wireFixtureGuard.ts:397-410) (which unwraps a single-argument alias such as
`Partial<TaskDocNode>` and bails on anything with an index signature), and **answers with EVERY member**.
That is the point: TypeScript's excess-property check against a non-discriminated union only requires
each property to exist in SOME member, so `SubTaskRow = TaskSubTaskRefNode | SeriesSubTaskNode` accepts a
row bearing `linkedLifecycleId` (only the first declares it) AND `createdAt` (only the second does) — a
blend of two `extra="forbid"` server models neither could send. **That pair is this leaf's own defect
reproduced as a type**, and `types/projection.ts` carries the comment explaining the collapse that caused
it. Conservative in the other direction: one member the guard cannot name abandons the whole slot rather
than measuring against half a union.

**The five rules**, in cit:([`collectWireFixtureFindings`], dashboard/src/test/wireFixtureGuard.ts:484-587):

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

Two details worth keeping. **Fresh object literals are skipped except against a union** cit:([`fresh`], dashboard/src/test/wireFixtureGuard.ts:541-541) —
checking a fresh literal is `tsc`'s own job, and the union is exactly where `tsc` stops doing it
properly. And **suppressions are read as TOKENS, not lines** cit:([`directiveLines`, `DIRECTIVE`], dashboard/src/test/wireFixtureGuard.ts:434-452; dashboard/src/test/wireFixtureGuard.ts:459-459) (mirroring TypeScript's own `commentDirectiveRegEx`): `contract.test.ts` discusses
`@ts-expect-error` in prose three times without using it, and this guard's own test file carries planted
directives inside template literals. A line-wise regex calls both a suppression; comment trivia sees
neither.

**`excessPropertyVerdict`** cit:([`excessPropertyVerdict`], dashboard/src/test/wireFixtureGuard.ts:609-658) returns either (a) the properties NO member declares, or (b) on a
union, the "blend" no single member declares, with a message naming the mutually exclusive shapes. It
reads an INTERSECTION on purpose — `Object.assign(node, {…})` answers `Wire & {…}`, assignable to the
wire type — and declines a union VALUE, an `any`/`unknown`, or a value with its own index signature.

**`reconcileWithRegistry`** cit:([`reconcileWithRegistry`], dashboard/src/test/wireFixtureGuard.ts:673-693) returns four lists: `unregistered` (a site no entry covers),
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

**WHAT THIS DOES NOT COVER** cit:(["WHAT THIS DOES NOT COVER"], dashboard/src/test/wireFixtureGuard.ts:39-39) — reproduced from the header, which records it "so the next
reader knows the SHAPE of what is uncovered rather than inferring completeness from a clean run". Each
was reproduced against this tree; none is fixed.

1. **Rule 4 reads four node kinds.** `Identifier`, `CallExpression`, `PropertyAccessExpression`, and
   (for the union case only) `ObjectLiteralExpression` — see cit:([`isCandidateForExcessCheck`], dashboard/src/test/wireFixtureGuard.ts:594-601).
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

External language references retained for reading only: [TypeScript Wiki — Using the Compiler API](https://github.com/microsoft/TypeScript/wiki/Using-the-Compiler-API), [TypeScript Handbook — Object Types / Excess Property Checks](https://www.typescriptlang.org/docs/handbook/2/objects.html#excess-property-checks), and [TypeScript Handbook — Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions). These URLs are not repository-relative citation sources.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The header: seven one-token opt-outs, why three of them carry no assertion at all, what makes the sweep fail-closed, and the rule scopes. | "as unknown as LifecycleProjection" | dashboard/src/test/wireFixtureGuard.ts:10-10 |
| `WHAT THIS DOES NOT COVER`, items 1-5. | "WHAT THIS DOES NOT COVER" | dashboard/src/test/wireFixtureGuard.ts:39-39 |
| `MIRROR_MARKER`, `declaresItselfAMirror`, `isWireModule` — the discovered vocabulary. | `MIRROR_MARKER`; `declaresItselfAMirror`; `isWireModule` | dashboard/src/test/wireFixtureGuard.ts:108-108; dashboard/src/test/wireFixtureGuard.ts:110-112; dashboard/src/test/wireFixtureGuard.ts:114-116 |
| `isFixtureSurface` — the surface rules 2-5 are strict on. | `isFixtureSurface` | dashboard/src/test/wireFixtureGuard.ts:123-132 |
| `GUARD_COMPILER_OPTIONS` (strict, bundler, `resolveJsonModule`, and no `exactOptionalPropertyTypes`). | `GUARD_COMPILER_OPTIONS` | dashboard/src/test/wireFixtureGuard.ts:138-149 |
| `buildProgramWithVirtualFiles`, including the `directoryExists` override without which a two-module planted case silently degrades to `any`. | `buildProgramWithVirtualFiles` | dashboard/src/test/wireFixtureGuard.ts:188-230 |
| `mentionedByTypeNode` / `mentionedByType`, and `UNRESOLVED` as a finding rather than a skip. | `mentionedByTypeNode`; `mentionedByType`; `UNRESOLVED` | dashboard/src/test/wireFixtureGuard.ts:239-239; dashboard/src/test/wireFixtureGuard.ts:289-335; dashboard/src/test/wireFixtureGuard.ts:338-357 |
| `wireSlotTarget` answering a union with every member, with the `SubTaskRow` worked example. | `wireSlotTarget`; `SubTaskRow` | dashboard/src/test/wireFixtureGuard.ts:366-366; dashboard/src/test/wireFixtureGuard.ts:376-394 |
| `collectWireFixtureFindings` — the five rules, and the fresh-literal exception that keeps rule 4 from second-guessing `tsc`. | `collectWireFixtureFindings` | dashboard/src/test/wireFixtureGuard.ts:484-587 |
| `isCandidateForExcessCheck` — the four node kinds, which is the exact shape of gap 1. | `isCandidateForExcessCheck` | dashboard/src/test/wireFixtureGuard.ts:594-601 |
| `directiveLines` + `DIRECTIVE` — suppressions read as comment trivia, not raw lines. | `directiveLines`; `DIRECTIVE` | dashboard/src/test/wireFixtureGuard.ts:434-452; dashboard/src/test/wireFixtureGuard.ts:459-459 |
| `excessPropertyVerdict` — undeclared properties, and the union blend no single member declares. | `excessPropertyVerdict` | dashboard/src/test/wireFixtureGuard.ts:609-658 |
| `reconcileWithRegistry` — unregistered / spent / miscounted / unreasoned. | `reconcileWithRegistry` | dashboard/src/test/wireFixtureGuard.ts:673-693 |
| The registry, planted bypasses and vacuity checks this module deliberately does not own. | `SANCTIONED_WIRE_SITES` | dashboard/src/test/wireFixtureGuard.test.ts:51-188 |
| `SubTaskRow` and the two `extra="forbid"` models whose collapse the union rule reproduces. | `SubTaskRow` | dashboard/src/types/projection.ts:815-815 |
| Gap 3, live: the first line is a "Same-origin client for …" header, not a `mirror of` marker, so nothing this module declares enters the vocabulary. | `ChangedFile` | dashboard/src/data/changeset.ts:12-18 |
| Same, for the read-only files API client. | `RepoCatalogEntry` | dashboard/src/data/files.ts:22-26 |
| Same, for the coordination-notes API client. | `NoteEntry` | dashboard/src/data/notes.ts:10-15 |
| Gap 3 with a proven cost: `HarnessInfo` is declared inline (id/name/detected only) beside the client-side `HarnessCatalogErrorKind`/`HarnessCatalogRead`, with no marker — and fixtures adding a `control` field to that row lived unguarded until this leaf removed them. | `HarnessInfo` | dashboard/src/data/harnessCatalog.ts:5-9 |
| The other proven cost: `WithdrawalResultWire` declares no `bridgeEpoch` (the sibling `SubmissionStatusBatchWire` does), and the fixture that gave it one was invisible to the guard. | `WithdrawalResultWire` | dashboard/src/data/submissionLifecycleClient.ts:40-46 |
| Gap 5's answer: the call-site constraint the builders carry instead of the project-wide flag. | `Overrides` | dashboard/src/test/fixtures/overrides.ts:60-66 |

## Cross-Repo References

No cross-repository boundary. The sweep runs entirely over `dashboard/` sources in this repository; the
"wire" it polices is a Python↔TypeScript seam inside `agents-remember`, and the TypeScript compiler is a
devDependency rather than a system boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The scanned roots are all inside `dashboard/`; nothing outside this repository is read. | `SCANNED_ROOTS` | dashboard/src/test/wireFixtureGuard.ts:136-136 |

## Update History
- 2026-09-05T06:24:16+00:00: Generated citation repair: `SubTaskRow` repointed to dashboard/src/types/projection.ts:815-815. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-20T10:45+02:00 — 260815-DAG-L12 curator: re-anchored citation range(s) to current source after the L12 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: corrected 1 citation range: `SubTaskRow` is declared at types/projection.ts L515 (was L505). All other rows and prose citations were already resolved. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 49 mechanical citation findings, including 9 legacy prose references and 20 repo-internal rows. The three external TypeScript URLs were retained as ordinary reading links outside citation tables; all repository rows now use exact anchors and plain repo-relative sources.

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
