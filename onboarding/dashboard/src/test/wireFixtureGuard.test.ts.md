# dashboard/src/test/wireFixtureGuard.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/wireFixtureGuard.test.ts`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T10:30+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The policy half of the fixture guard. `wireFixtureGuard.ts` is the mechanism; this file supplies the
three things a mechanism cannot supply itself (L18-L39):

1. **The registry** — every site that still does what the rules forbid, with the sentence that earns it.
   Exact (counts, not files) and bidirectional (an entry that stops matching fails too), so a new
   consumer-authored fixture cannot appear silently and an old exemption cannot outlive its reason.
2. **The planted bypasses** — an AST guard written without them has holes; *this leaf proved that twice*.
   Every rule is shown FAILING against a source that must never exist on disk, over a virtual program
   laid on the real tree so planted files import the real wire types.
3. **The vacuity checks** — every rule is conditioned on "is this a wire type?", so a guard whose
   vocabulary came back empty would pass everything in silence.

Its framing sentence is R6: *a test whose fixture is authored by the consumer cannot detect producer
drift.* `contract.test.ts` makes the MIRROR honest; this file makes the FIXTURES honest. Neither is
worth much alone — a perfect mirror nobody is checked against, or fixtures checked against a mirror that
lies.

## Code Commentary

### Logic

**`SANCTIONED_WIRE_SITES`** (L45-L182), keyed `<file> :: <what was written>` so it does not churn on
line moves, in four groups:

- **The decode boundary** (L46-L140) — 24 entries across `data/store.ts`, `data/seatEvents.ts`,
  `data/taskDocuments.ts`, `data/terminal.ts`, `data/terminalOpen.ts`, `data/launchFlow.ts`,
  `data/submitClient.ts`, `data/sessionCapabilities.ts`, `data/capabilityCatalog.ts`,
  `data/conversation/{client,stream}.ts` and `data/conversation-library/client.ts`. Outside the fixture
  surface a cast to a wire type is the client saying "this JSON came from the server and I am trusting
  it" — a different act from a test authoring the server's answer. Listed rather than rewritten because
  narrowing them honestly is a runtime-validation problem, not a fixture one.
- **The mirror's own derivations** (L142-L150) — two casts inside `types/projection.ts`:
  `as StateCountField<S>` (the bucket-name rule's runtime twin, re-narrowing what template concatenation
  widens) and `as LifecycleStateCounts` (`Object.fromEntries` answers a plain record; the KEYS come from
  the vocabulary).
- **The fixture surface's four legitimate casts** (L152-L174) — `servedProjection.ts`'s sanctioned
  narrowing; three brand mints in `fixtures/conversationWire.ts` (`ActivePageCursor`, `ActiveEventCursor`,
  `LibraryConversationKey` — opaque server-issued tokens with no structure to get wrong); and one in
  `topology/model.test.ts` described as *the one deliberate WIDENING* — `State` is a bare `str`
  server-side, so the mirror's closed union is narrower than the wire by construction, and that test
  exists to prove an unlisted member still classifies.
- **Compiler suppressions** (L176-L181) — one entry, `contract.test.ts :: @ts-expect-error`, count **3**,
  reasoned as the inverted pins: each asserts a field the server CANNOT send is absent from the mirror,
  and an unused `@ts-expect-error` is itself a compile error, so they fail the moment a field comes back.

**The sweep over the real tree** (L186-L189) builds the program once and derives `findings` and
`vocabulary` from it.

**`the guard has something to police`** (L195-L258) — the vacuity suite:

- the vocabulary is asserted **non-empty** (`> 100` names) — "an empty vocabulary is not a clean tree, it
  is a guard that has stopped running";
- it is asserted to contain the types the two proven defects lived on:
  `src/types/projection.ts:EngineProcessEdge` (where `refusedPolarity` was invented) and
  `:TaskDocNode` (where `createdAt` was), plus `src/types/event.ts:ObserverEvent` and
  `src/data/conversation/types.ts:ConversationCapabilities`;
- the marker-carrying module set is pinned **exactly** to seven:
  `data/conversation-library/types.ts`, `data/conversation/types.ts`, `types/event.ts`,
  `types/harnessCapabilities.ts`, `types/projection.ts`, `types/terminalCatalog.ts`,
  `types/terminalOpen.ts`;
- every `.ts` file under `src/types/` must declare itself a mirror on its first line;
- `isFixtureSurface` is pinned on eight representative paths, including two that must be `false`
  (`src/data/store.ts`, `src/panels/RailChat.tsx`).

**`no dashboard test asserts against a payload the server cannot produce`** (L260-L282) — the
reconciliation: `unregistered` must be empty (with a failure message telling the author to build the
fixture with `fixtures/wire.ts` or `conversationWire.ts`, annotate it, or `satisfies` it — *do not cast
it*), `spent` and `miscounted` must be empty, and every entry must carry a written reason.

**`PLANTED_FILES`** (L289-L447) — seven virtual modules under `src/__wire_guard_planted__`, numbered
1-15 in their own comments:

| Probe | What it plants |
| --- | --- |
| `casts.test.ts` | the plain cast, the double cast, an import rename, a local alias, `Partial<>`/array/`Record<>` wrappers, `as never`/`as any`/`as unknown as`, `typeof template`, and an unbindable type name |
| `freshness.test.ts` | a spread that loses freshness, `Object.assign` answering an intersection, and `JSON.parse` answering `any` |
| `suppression.test.ts` | a `@ts-expect-error` above a wire-annotated literal |
| `union.test.ts` | the `SubTaskRow` blend as a FRESH literal, the same blend non-fresh, and a property no member declares |
| `helper.ts` + `twoModule.test.ts` | smuggling that happens in another planted module |
| `honest.test.ts` | annotated literal, `satisfies`, `as const`, a DOM mock, a builder call, and both sides of the union on their own |

**`the guard is shown able to fail`** (L462-L578) asserts each rule biting, and two of the assertions are
harness assertions as much as rule ones. The `twoModule` case (L554-L565) exists because a planted file
importing another planted file used to resolve to nothing, degrade to `any`, and trip rule 3 — *the test
passed for the wrong reason*, which is the same as a harness that cannot express the case at all. The
unresolved-name case (L573-L577) asserts `wire-cast: asserts <unresolved>`, because "the guard did not
understand this" must read as a failure.

**`the guard leaves the honest forms alone`** (L580-L587) asserts ZERO findings on `honest.test.ts`. The
comment states the stake: a guard that also flags the fix is a guard that gets deleted — and `satisfies`
and a type annotation both do FULL checking, which is what the whole file exists to force fixtures back
onto.

**`the registry cannot be quietly outgrown`** (L589-L620) unit-tests `reconcileWithRegistry` on
synthetic findings: a site no entry covers, an entry matching nothing, a second occurrence hiding behind
a one-site exemption, and an entry with a blank reason.

### Conventions

- A registry entry is a sentence, not a flag. `unreasoned` fails on a blank one, so "why" is structurally
  required.
- The planted sources are string arrays joined with `\n`, and the suppression probe writes `${"@"}ts-…`
  so the directive exists in the planted TEXT without existing in this file — which is also why the
  guard reads suppressions from comment trivia rather than from raw lines.
- Both directions of the module-set assertion are one `toEqual`, deliberately: a module that LOSES its
  marker silently narrows every rule, and a NEW mirror module fails here too — "which is the moment to
  decide what its fixtures are allowed to do".

### Invariants And Boundaries

- The registry is the only escape hatch, and it escapes by SITE, never by file. Adding an entry is a
  decision with a written justification; growing a count is a new hole.
- The vacuity assertions must stay. Every other assertion in this file is conditioned on a non-empty
  vocabulary.
- `honest.test.ts` must keep returning zero findings. New rules are added against a planted bypass AND
  against the honest set.
- This file asserts; it holds no matching logic. Rule behaviour belongs in `wireFixtureGuard.ts`.

### Todos

**What these assertions do not establish.**

- **The KNOWN GAP is written into the module-set assertion itself** (L216-L224) rather than papered over:
  `data/changeset.ts`, `data/files.ts`, `data/notes.ts`, `data/harnessCatalog.ts` and
  `data/submissionLifecycleClient.ts` declare wire-shaped response types INLINE, beside client-side
  option and handler types (`MasterChangesetOptions`, `FetchLike`, `ListQuery`). They carry no marker,
  are not vocabulary, and **a fixture for those routes is unguarded**. Treating "the header cites a `.py`
  file" as the rule was measured and rejected — it sweeps up the option types too, which are not wire
  shapes, and would make the guard wrong rather than wider. The real fix is to move those response types
  into a marker-carrying module: a refactor of app code, not of fixtures. Note the asymmetry the
  seven-module `toEqual` cannot fix: it catches a module that LOSES its marker, and passes cleanly for
  one that never had one.
- The planted suite proves each rule CAN bite on a constructed source. It does not establish that the
  rules are complete — `wireFixtureGuard.ts`'s own `WHAT THIS DOES NOT COVER` lists five reproduced
  evasions that are not planted here, because they are known to pass.
- The vocabulary threshold is a floor (`> 100`), not a pinned count, so a partial loss of vocabulary
  short of collapse would not fail this assertion.
- The header (L23) still says "read its header for the four rules" where there are five. Stale wording
  worth correcting in the source; the rule set itself is five and is enumerated correctly in the
  mechanism's header.

## Docs References

The registry, the planted bypasses and the honest set are all statements about TypeScript's own
checking: an assertion suppresses excess-property checking, a double assertion suppresses assignability
too, excess-property checking applies only to fresh literals, and an unused `@ts-expect-error` is itself
an error.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Type assertions do not perform a check, and a two-step assertion through `unknown` is the documented way to assert between unrelated types — the two moves probes 1 and 2 plant. | Type Assertions | [TypeScript Handbook — Everyday Types / Type Assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) |
| Excess-property checking applies to fresh object literals only, which is why probe 9's spread-into-a-variable compiles and needs a rule of its own. | Excess Property Checks | [TypeScript Handbook — Object Types / Excess Property Checks](https://www.typescriptlang.org/docs/handbook/2/objects.html#excess-property-checks) |
| An unused `@ts-expect-error` is reported as an error — the property that makes the registry's 3-count suppression entry a live pin rather than a permanent exemption. | `@ts-expect-error` | [TypeScript 3.9 Release Notes — // @ts-expect-error Comments](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-9.html#-ts-expect-error-comments) |
| `satisfies` validates a value against a type without widening it — the honest form the guard must leave alone. | `satisfies` | [TypeScript 4.9 Release Notes — the satisfies Operator](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html#the-satisfies-operator) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The header: the three things the mechanism cannot supply itself, and R6 as the framing. | L18-L39 | [wireFixtureGuard.test.ts](wireFixtureGuard.test.ts) |
| The registry: decode boundary, the mirror's own derivations, the four fixture-surface casts, and the 3-count suppression entry. | L45-L182 | [wireFixtureGuard.test.ts](wireFixtureGuard.test.ts) |
| The vacuity suite: non-empty vocabulary, the two defect types, the exact seven-module set with its KNOWN GAP note, the `src/types/` marker convention, and the fixture-surface classification. | L195-L258 | [wireFixtureGuard.test.ts](wireFixtureGuard.test.ts) |
| The reconciliation over the real tree, with the failure message that names the fix. | L260-L282 | [wireFixtureGuard.test.ts](wireFixtureGuard.test.ts) |
| The seven planted modules, numbered 1-15. | L289-L447 | [wireFixtureGuard.test.ts](wireFixtureGuard.test.ts) |
| Each rule shown biting, including the two-module harness assertion and the unresolved-name fail-closed case. | L462-L578 | [wireFixtureGuard.test.ts](wireFixtureGuard.test.ts) |
| Zero findings on the honest forms. | L580-L587 | [wireFixtureGuard.test.ts](wireFixtureGuard.test.ts) |
| `reconcileWithRegistry` unit-tested in all four directions. | L589-L620 | [wireFixtureGuard.test.ts](wireFixtureGuard.test.ts) |
| The mechanism: the five rules, the discovered vocabulary, the virtual-file program, and the five uncovered evasions. | L1-L75; L484-L587 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |
| `SubTaskRow` and the two `extra="forbid"` models the union probe blends. | L361-L391 | [../types/projection.ts](../types/projection.ts) |
| The two mirror-internal casts the registry sanctions, in context. | L206-L235 | [../types/projection.ts](../types/projection.ts) |
| The sanctioned narrowing the registry names, with its reason. | L34-L43 | [servedProjection.ts](servedProjection.ts) |
| The three brand mints the registry names. | L50-L65 | [fixtures/conversationWire.ts](fixtures/conversationWire.ts) |
| The three `@ts-expect-error` directives the 3-count entry covers. | L501-L523 | [contract.test.ts](contract.test.ts) |
| The deliberate widening in the topology suite: `fromANewerServer` performs the single `as State` the registry sanctions, named once so its two consumers read as a forward-compatibility check rather than as the pattern this guard bans. | L45-L54 | [../topology/model.test.ts](../topology/model.test.ts) |
| KNOWN GAP, live: an inline `HarnessInfo` with no marker — the row a removed fixture gave a `control` field. | L4-L16 | [../data/harnessCatalog.ts](../data/harnessCatalog.ts) |
| KNOWN GAP, live: `WithdrawalResultWire` declares no `bridgeEpoch`, though the sibling batch model does. | L35-L46 | [../data/submissionLifecycleClient.ts](../data/submissionLifecycleClient.ts) |

## Cross-Repo References

No cross-repository boundary. Every scanned root, every registry key and every planted module is inside
`dashboard/` in this repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The sweep is built from `dashboardRoot()` and the in-repo scanned roots; nothing outside this repository is read. | L136; L170-L181 | [wireFixtureGuard.ts](wireFixtureGuard.ts) |

## Update History

- 2026-08-01T10:30+02:00 — 260731-EFA-L4 curator (citation pass): `types/projection.ts` adopted the
  server's state partition (`LIVE_STATES` + `TERMINAL_STATES` composed into `LIFECYCLE_STATES`), moving
  every anchor below it. Re-anchored the two rows citing that file: the union-probe models L324-L354 →
  L361-L391 (`TaskSubTaskRefNode` L368, `SeriesSubTaskNode` L380, `SubTaskRow` L391); the two sanctioned
  mirror-internal casts L171-L201 → L206-L235 (`as StateCountField<S>` L223, `as LifecycleStateCounts`
  L234, with the types they re-narrow to at L206/L214). Registry keys are `<file> :: <what was written>`
  and did not move, so no body claim changed.

- 2026-08-01T10:00+02:00 — 260731-EFA-L4 curator: created. Records the registry's four groups (including
  the 3-count `@ts-expect-error` entry and the one deliberate widening), the vacuity suite, the seven
  planted modules with the two that are harness assertions rather than rule assertions, the zero-findings
  honest set, and the four-way `reconcileWithRegistry` unit tests. States what the assertions do NOT
  establish: the KNOWN GAP written into the module-set assertion (five unmarked modules whose fixtures
  are unguarded, with the measured-and-rejected alternative rule and the one-directional fail-closedness
  of marker discovery), that planted probes prove biting rather than completeness, that the vocabulary
  check is a floor not a pinned count, and that the header still says "four rules" where there are five.
  Verification metadata pinned to the leaf base `abc7cbcc74921cdcb57a61529445f61641e919e7` until closeout
  stamps the L4 code commit.
