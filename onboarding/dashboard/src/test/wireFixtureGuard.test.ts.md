# dashboard/src/test/wireFixtureGuard.test.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The policy half of the fixture guard. `wireFixtureGuard.ts` is the mechanism; this file supplies the
three things a mechanism cannot supply itself:

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

**`SANCTIONED_WIRE_SITES`**, keyed `<file> :: <what was written>` so it does not churn on
line moves, in four groups:

- **The decode boundary** — 24 entries across `data/store.ts`, `data/seatEvents.ts`,
  `data/taskDocuments.ts`, `data/terminal.ts`, `data/terminalOpen.ts`, `data/launchFlow.ts`,
  `data/submitClient.ts`, `data/sessionCapabilities.ts`, `data/capabilityCatalog.ts`,
  `data/conversation/{client,stream}.ts` and `data/conversation-library/client.ts`. Outside the fixture
  surface a cast to a wire type is the client saying "this JSON came from the server and I am trusting
  it" — a different act from a test authoring the server's answer. Listed rather than rewritten because
  narrowing them honestly is a runtime-validation problem, not a fixture one.
- **The mirror's own derivations** — two casts inside `types/projection.ts`:
  `as StateCountField<S>` (the bucket-name rule's runtime twin, re-narrowing what template concatenation
  widens) and `as LifecycleStateCounts` (`Object.fromEntries` answers a plain record; the KEYS come from
  the vocabulary).
- **The fixture surface's four legitimate casts** — `servedProjection.ts`'s sanctioned
  narrowing; three brand mints in `fixtures/conversationWire.ts` (`ActivePageCursor`, `ActiveEventCursor`,
  `LibraryConversationKey` — opaque server-issued tokens with no structure to get wrong); and one in
  `topology/model.test.ts` described as *the one deliberate WIDENING* — `State` is a bare `str`
  server-side, so the mirror's closed union is narrower than the wire by construction, and that test
  exists to prove an unlisted member still classifies.
- **Compiler suppressions** — one entry, `contract.test.ts :: @ts-expect-error`, count **3**,
  reasoned as the inverted pins: each asserts a field the server CANNOT send is absent from the mirror,
  and an unused `@ts-expect-error` is itself a compile error, so they fail the moment a field comes back.

**The sweep over the real tree** builds the program once and derives `findings` and
`vocabulary` from it.

**`the guard has something to police`** — the vacuity suite:

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
  (`src/data/store.ts`; the removed `src/panels/RailChat.tsx` was the other before MIK-R95).

**`no dashboard test asserts against a payload the server cannot produce`** — the
reconciliation: `unregistered` must be empty (with a failure message telling the author to build the
fixture with `fixtures/wire.ts` or `conversationWire.ts`, annotate it, or `satisfies` it — *do not cast
it*), `spent` and `miscounted` must be empty, and every entry must carry a written reason.

**`PLANTED_FILES`** — seven virtual modules under `src/__wire_guard_planted__`, numbered
1-15 in their own comments:

| Probe | What it plants |
| --- | --- |
| `casts.test.ts` | the plain cast, the double cast, an import rename, a local alias, `Partial<>`/array/`Record<>` wrappers, `as never`/`as any`/`as unknown as`, `typeof template`, and an unbindable type name |
| `freshness.test.ts` | a spread that loses freshness, `Object.assign` answering an intersection, and `JSON.parse` answering `any` |
| `suppression.test.ts` | a `@ts-expect-error` above a wire-annotated literal |
| `union.test.ts` | the `SubTaskRow` blend as a FRESH literal, the same blend non-fresh, and a property no member declares |
| `helper.ts` + `twoModule.test.ts` | smuggling that happens in another planted module |
| `honest.test.ts` | annotated literal, `satisfies`, `as const`, a DOM mock, a builder call, and both sides of the union on their own |

**`the guard is shown able to fail`** asserts each rule biting, and two of the assertions are
harness assertions as much as rule ones. The `twoModule` case exists because a planted file
importing another planted file used to resolve to nothing, degrade to `any`, and trip rule 3 — *the test
passed for the wrong reason*, which is the same as a harness that cannot express the case at all. The
unresolved-name case asserts `wire-cast: asserts <unresolved>`, because "the guard did not
understand this" must read as a failure.

**`the guard leaves the honest forms alone`** asserts ZERO findings on `honest.test.ts`. The
comment states the stake: a guard that also flags the fix is a guard that gets deleted — and `satisfies`
and a type annotation both do FULL checking, which is what the whole file exists to force fixtures back
onto.

**`the registry cannot be quietly outgrown`** unit-tests `reconcileWithRegistry` on
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

- **The KNOWN GAP is written into the module-set assertion itself** rather than papered over:
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

## Evidence

### Docs References

The registry, the planted bypasses and the honest set are all statements about TypeScript's own
checking: an assertion suppresses excess-property checking, a double assertion suppresses assignability
too, excess-property checking applies only to fresh literals, and an unused `@ts-expect-error` is itself
an error.

No external documentation is used for this bounded card.

### Repo-Internal References

- The framing and three responsibilities the mechanism cannot supply itself. [1]
- The sanctioned-site registry and its four groups. [2]
- The real-tree sweep derives its discovered vocabulary with `wireTypeNames(program, ROOT)`. [3]
- The vacuity suite's fixture-surface checks. [4]
- The reconciliation over the real tree. [5]
- The virtual planted modules and honest forms. [6]
- Each rule shown biting, including cross-module and unresolved-name cases. [7]
- Zero findings on the honest forms. [8]
- The registry reconciliation unit cases. [9]
- The five-rule mechanism and discovered vocabulary. [10]
- The guard's documented uncovered-evasions section names `ElementAccessExpression`. [11]
- `SubTaskRow` is the union of `TaskSubTaskRefNode` and `SeriesSubTaskNode`. [12]
- The `StateCountField` mirror-internal cast. [13]
- The `LifecycleStateCounts` mirror-internal cast. [14]
- The sanctioned narrowing the registry names. [15]
- The `ActivePageCursor` brand mint. [16]
- The `ActiveEventCursor` brand mint. [17]
- The `LibraryConversationKey` brand mint. [18]
- The contract uses @ts-expect-error to assert that master references cannot have createdAt. [19]
- The contract uses @ts-expect-error to assert that series rows cannot have linkedLifecycleId. [20]
- The contract test suppresses the carried `refusedPolarity` property. [21]
- The deliberate widening in the topology suite. [22]
- KNOWN GAP, live: the inline `HarnessInfo` response shape is outside the marker vocabulary. [23]
- KNOWN GAP, live: `WithdrawalResultWire` is outside the marker vocabulary. [24]

### Cross-Repo References

No cross-repository boundary. Every scanned root, every registry key and every planted module is inside
`dashboard/` in this repository.

- The sweep is built from the in-repo dashboard root and scanned source files; nothing outside this repository is read. [25]
