# dashboard/src/fixtures/snapshot.json

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The dashboard's stand-in for the server: one `WorkspaceProjection` payload, 1,982 lines at the
`260831-LOCR-L17` candidate, shaped like the persisted `latest-state.json`. Four things read it — `test/contract.test.ts` (which measures the
TypeScript mirror against it in three directions), `test/fixtures/wire.ts` (which takes every builder
base from it), and `data/store.test.ts`; `e2e-production/cockpit.production.spec.ts` reads it off disk.

**It is NOT generated.** This file is a hand-maintained sample. The TypeScript mirror it is checked
against is generated and stale-checked from the Pydantic projection schema, so sample coverage and
producer-to-TypeScript provenance are separate claims. `fixtures/wire.ts` draws that boundary:

```text
observer/projection.py schema  --generated + stale-checked-->  types/projection.ts
                                                                ↑ typed fixture builders
                                                                ↕ measured sample coverage
                                                         snapshot.json (manual)
```

So a green sample-coverage build claims that this manual payload exercises the generated mirror.
The projection generator separately binds that mirror to the producer schema, including fields a
sample could miss because their values are currently null or absent.

L14 extends the manual sample with the new sprint structure: the `dependency-aware sprint` task
document carries non-empty `seats` (an identity-bearing active orchestrator + an identity-less
planned strategist) and two typed `masterRef` sub-task rows (both master targets exist in the same
fixture, so the dev-server exercises the sprint → master navigation for real); every other task
document defaults `seats: []`.

L23 extends the manual sample with representative lifecycle-operation rows. The sample carries public progress/result/failure/guidance fields
including public identity/component fingerprints and approval state, but no private operation key
or worker PID, preserving the
producer's private-plane boundary while making the generated dashboard contract measurable.

L17 extends the manual sample with the observer stage's own health reading: a **degraded**
`terminalObserverHealth` row (`generatedAt` 09:01:00, `lastAttemptAt` 09:00:57 so `ageSeconds` is 3.0
against `staleCutoffSeconds` 60.0, `lastSuccessAt` 09:00:17 so `lastSuccessAgeSeconds` is 43.0,
`consecutiveFailureCount` 2 with `initialObservationSucceeded` true). The reading is degraded rather
than healthy because three of the payload's five closed unions are nullable: a payload carrying the
healthy case's nulls could not satisfy a string-vocabulary check at all, so only a non-null reading
can be sampled. The row is arithmetically coherent with the fixture's fabricated `2026-06-14T09:00`
window, and it is what makes the five new `projection.terminalObserverHealth.*` vocabulary paths in
`test/contract.test.ts` non-vacuous.

## Code Commentary

### Logic

The `sim-op-ledger-commit` enclosure sample is removed because `ledger-commit` is no longer
a legal lifecycle phase. Code and memory publication samples remain. The retained
`analytics.ledgers` data represents a downstream consumer projection, so removing the obsolete
Git-operation sample does not remove the ledger from the dashboard fixture.

The current serialized fixture starts with `activeWorktreeGroups` and `analytics`; it also carries
`closeoutQueues`, `enclosures`, `generatedAt`, `lifecycles`, `metrics`, `providers`, and `version` (1).
Use the current reference rows below for source locations
cit:([`activeWorktreeGroups`], dashboard/src/fixtures/snapshot.json:2-2).

The CCR-R03@v1 curation entry records a formatting-only reserialization at source commit
`fbc89847233b1c5959f56475f2cb51f936d5ef0b`. That historical statement does not describe
all later fixture changes: the current operation sample also carries the L15 meaningful revision
field described below. The current lifecycle sample is
cit:(["\"lifecycles\": ["], dashboard/src/fixtures/snapshot.json:1791-1928);
the current metrics sample is cit:(["\"metrics\": {"], dashboard/src/fixtures/snapshot.json:1929-1940).

### Conventions

- Shaped like the **persisted** `latest-state.json`, not like an HTTP response: the two app-injected
  response-time fields `servingBuild` and `agentNotifierHeartbeat` are deliberately absent and are the
  entire content of `contract.test.ts::KnownUnsampled`; the fourth serve-time field,
  `terminalObserverHealth` (`LOCR-R17@v1`), is now SAMPLED here and therefore deliberately NOT on that
  residue. `data/store.test.ts` exercises the two absent ones by construction instead, including the
  "never ticked" (`lastTickAt: null`) reading that a payload always carrying a heartbeat could not
  express.
- Non-uniform on purpose. Arrays are keyed by TYPE in the mirror walk, so one lifecycle carrying
  `staleSeconds` samples it for all of them. The payload does not have to be uniform; it has to be
  COMPLETE between its rows.
- Timestamps sit in a single fabricated window around `2026-06-14T09:00`, and identifiers are
  `sim-`/`SIM`-prefixed, so nothing in it reads as a captured production workspace.

### Invariants And Boundaries

- **Every declared mirror path must stay sampled.** Deleting a field, or emptying an array, is not a
  neutral edit. A reviewer proved the cost during this leaf: deleting `stateEnteredAt` and
  `gate.evidenceRefs` and emptying `expectationRows` and `landing` produced zero new `tsc` errors and a
  green suite. **An empty array is worse than a missing field** — it is blindness in both directions at
  once, because `AsJsonModule` accepts `never[]` as assignable to anything and `ServedOnlyPaths<never, …>`
  is `never`. `MirrorOnlyPaths` now names any path that stops being reached, so this is enforced, not
  merely asked for.
- **Every sampled vocabulary value must be legal, and every registered path must be non-vacuous.**
  The fixture is representative rather than exhaustive. New producer enum members flow through schema
  generation and stale-output validation without forcing unrelated full-object rows into this file.
- **The rows the builders anchor on must keep existing.** `fixtures/wire.ts` calls `demandServed(…)` on
  `lifecycles[0]`, `enclosures[0]`, `providers[0]`, `analytics.taskDocuments[0]`,
  `analytics.engineProcesses[0]`, `analytics.agentPickups[0]`, `analytics.attentionQueue[0]`, and a
  lifecycle carrying a gate — each throwing a named error rather than spreading `undefined`.
- This file is the ORACLE, not a scenario. Dev-gallery scenarios live in `src/dev/`; per-suite shapes
  are built with `test/fixtures/wire.ts`. Do not add rows here to make one test convenient — a row added
  here changes what every direction of the contract guard measures.
- Edit it against `observer/projection.py` (and the reducer that fills each field), never against the
  TypeScript mirror. Shaping it from the mirror would make the guard measure the mirror against itself.

### Todos

**What this fixture cannot cover, stated so a clean contract run is not read as more than it is.**

1. **It is a sample, not a schema.** A server field typed `T | None` that happens to be null is *omitted*
   by `exclude_none=True`, so no sampled payload can reveal it. Only the schema can.
2. **It does not establish producer vocabulary.** Schema generation owns exhaustive
   producer-to-mirror vocabulary. This sample proves only that values it carries are legal.
3. **It cannot separate two field-identical models.** `SeriesSectionNode` and `TaskSectionNode` declare
   the same three fields, so no payload and no structural walk distinguishes them.
4. **The sample remains manual while the mirror is generated.** Do not describe this JSON payload as
   generated, and do not describe its coverage limits as a missing producer-to-TypeScript contract.
5. **Provenance wording must preserve that split.** `test/fixtures/wire.ts`, `contract.test.ts`, and
   `e2e-production/cockpit.production.spec.ts` all distinguish manual sample coverage from generated
   mirror provenance.

## Evidence

### Docs References

No Domain Documentation source is configured in the resolved memory repository. The local
serialization and typecheck contracts are supported by the source references below; this pass
makes no separately verified external-library documentation claim.

No configured external documentation source applies.

### Repo-Internal References

The payload's shape is fixed by pydantic serialization behaviour on this repository's own models —
`model_dump(by_alias=True, exclude_none=True)` — which is what makes a null-valued optional field
absent from the file rather than present as `null`.

- Ledger analytics remain a consumer sample after the retired Git-operation phase is removed. [1]
- Removed the retired ledger-commit operation sample while preserving downstream ledger analytics and real publication phases. [2]
- `exclude_none=True` omits fields whose value is `None` from the serialized output — the rule that makes an omitted key here indistinguishable from a field the server does not have. [3]

- Six lifecycles covering the six represented states and phases, two gates with `evidenceRefs`, `stateEnteredAt` on every row. [4]
- Representative enclosure rows, two providers, and the `activeWorktreeGroups` join value. [5]
- `metrics` with one bucket per live state and no bucket for the terminal pair. [6]
- All thirteen analytics keys, none empty, including `expectationRows` and eight `engineProcesses` pods spanning all eight healths. [7]
- The writer of the persisted payload this file is shaped like: `write_projection` dumps with `by_alias=True, exclude_none=True` into `latest-state.json`. [8]
- The models that define every key here, and the `extra="forbid"` rule that makes an invented field impossible on the wire. [9]
- The three-direction guard: `mirror ⊇ served`, `served ⊇ mirror`, and `fixture ⊇ mirror` — the last of which exists because this payload is the oracle. [10]
- The derived `VOCABULARIES` registry and its non-vacuous sampled-value membership assertion. [11]
- `INDEX_SIGNATURE_SITES` — the seven absorbing nodes this payload must carry a value at, each with a written reason. [12]
- `KnownUnsampled` — the two app-injected fields deliberately absent here, and why. [13]
- The snapshot is manual; the projection command generates and stale-checks the schema and TypeScript mirror. [14]
- `demandServed` and the eight anchor rows the builders require this payload to keep. [15]
- The narrowing every reader comes through, and why a second `as unknown as` elsewhere would re-open the hole. [16]
- Store-suite consumer, which also constructs the two app-injected fields this payload omits. [17]
- Production e2e consumer, which reads this manual sample off disk and states that it is checked against the generated mirror while the projection generator/stale gate hold that mirror to the Pydantic schema. [18]

### Cross-Repo References

No cross-repository boundary. The payload imitates this repository's own Python serving layer; both
sides live in `agents-remember`.

The producer and fixture both belong to this repository; their implementation evidence is listed above.

## L23 Source-Lineage Samples

Engine Process fixtures now sample aggregate `current`, `blocked`, and
`unavailable` states, every edge relation/side/state, and one
contract-addressed `worktree_sync` recovery. These are wire-contract examples,
not frontend-derived Git facts.


## 260815-DAG-L12 Fixture Graph View

The sprint fixture (`sim-master` / `sim-master-b` scenario) carries the render-ready `executionGraphView` (L12-R4): a segmented master with a joined title and an early leaf, plus a dependent second master waiting on it with a recorded predecessor reason and judgment id. Those rows remain representative contract examples; complete enum ownership stays with schema generation.


## 260815-DAG Master Full-Gate Repair

The snapshot fixture gained a super-to-leaf source-relation entry (`relation: "super-to-leaf"`, state `current`) and two execution-graph view nodes (a `segment` with `frontierState: "landed"` and a `lump` with `frontierState: "ready"`) as representative dashboard contract examples.

## 260831-CCR-L15 Fixture Cursor Sample

The hand-kept fixture snapshot now seeds `meaningfulRevision: 1` on the lifecycle
operation node that previously carried only the revision-less projection fields, so dashboard and
wire-fixture consumers have a cursor-carrying sample matching the regenerated schema.
