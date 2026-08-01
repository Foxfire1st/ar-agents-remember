# dashboard/src/fixtures/snapshot.json

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/fixtures/snapshot.json`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T09:30+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The dashboard's stand-in for the server: one `WorkspaceProjection` payload, 737 lines, shaped like the
persisted `latest-state.json`. Three things read it — `test/contract.test.ts` (which measures the
TypeScript mirror against it in three directions), `test/fixtures/wire.ts` (which takes every builder
base from it), and `data/store.test.ts`; `e2e-production/cockpit.production.spec.ts` reads it off disk.

**It is NOT generated.** No generator exists — nothing under `mcp/`, `scripts/` or `dashboard/` writes
this file — and it is hand-maintained; 260731-EFA-L4 alone edited it by +642/-15 lines. That single
fact is the most important thing about the file, because it sets the reach of everything built on it.
`fixtures/wire.ts`'s header draws the chain (L22-L37):

```text
a fixture  --type-checked against-->  types/projection.ts  --measured against-->  snapshot.json
                                                                        ↕ BY HAND
                                                                observer/projection.py
```

So a green build claims: *the mirror could produce this shape, and the mirror agrees with a payload a
person wrote to stand in for the server.* **The mirror↔server link is the hand-maintained one, and it
is the only link in the chain no test can hold up.** A field the server starts sending that neither
this file nor the mirror knows about is invisible to all of it. `contract.test.ts` files generating
this payload from the pydantic models under `LEFT FOR CODEGEN (R3)`.

## Code Commentary

### Logic

Top-level keys in wire order: `version` (1), `generatedAt`, `lifecycles`, `enclosures`, `providers`,
`activeWorktreeGroups`, `metrics`, `analytics`.

- **`lifecycles` (L4-L112) — six rows, one per state.** `blocked-001`, `running-000`, `paused-002`,
  `awaiting-003`, `completed-004`, `abandoned-005`, and their phases spread across all six of `build`,
  `reframe-research`, `request`, `trust-checkpoint`, `decide`, `close`. Two rows carry a `gate`
  (`GATE-1` open with `decisions: ["approve","revise"]`, `GATE-0` decided), both with a non-empty
  `evidenceRefs`. Every row carries `stateEnteredAt`. The `awaiting-developer` row is the state the
  mirror had never declared, and it is here so the vocabulary check can bite.
- **`enclosures` (L113-L135)** — one enclosure; **`providers` (L136-L158)** — two (a code provider and
  a memory provider, joined by `worktreeGroup: "sim-group"`); **`activeWorktreeGroups` (L159)** —
  `["sim-group"]`.
- **`metrics` (L160-L168)** — `lifecycleCount: 6`, one bucket per LIVE state (`runningCount`,
  `blockedCount`, `pausedCount`, `awaitingDeveloperCount`, each 1), `totalTokens: 2800`, and a
  `stalenessHistogram` of `{ fresh, aging }`. The four buckets are exactly the keys `metricsFor([])`
  produces, which is what `contract.test.ts` asserts set-equality on — the terminal pair deliberately
  has no bucket.
- **`analytics` (L169-L736)** — all thirteen keys present and none empty: `driftSnapshots` (L170),
  `stalestSidecars` (L183), `setupSummaries` (L191), `setupProgress` (L202), `routeCoverage` (L212),
  `toolReports` (L221), `agentPickups` (L229), `expectationRows` (L255), `ledgers` (L269),
  `taskDocuments` (L287), `attentionQueue` (L348, three rows), `engineProcesses` (L386, eight pods),
  `series` (L703).

**The payload is composed to satisfy specific checks, not sampled at random.** `contract.test.ts`
requires that every closed vocabulary in the mirror is exercised in FULL, pooled per vocabulary rather
than per path, and this file is built to that requirement:

| Vocabulary | Members | Where the fixture spreads them |
| --- | --- | --- |
| `LIFECYCLE_STATES` | 6 | one lifecycle per state |
| `PHASES` | 6 | one phase per lifecycle |
| `ATTENTION_SEVERITIES` | 3 | the three `attentionQueue` rows |
| `ATTENTION_LANES` | 3 | the same three rows |
| `PROCESS_HEALTHS` | 8 | one health per `engineProcesses` pod |
| `PROCESS_FACT_STATES` | 6 | pooled across six registered paths — the four commit refs, `providers[].factState`, `landing[].factState` |

Likewise the seven absorbing nodes named in `INDEX_SIGNATURE_SITES` each carry at least one served
value here (`lifecycles[].ask`, `gate.packet`, `gate.evidenceRefs[]`, `metrics.stalenessHistogram`,
`driftSnapshots[].counts`, `setupSummaries[].resultCounts`, `engineProcesses[].retryArgs`) — a wall in
the type-level walk that the payload omitted would be an unreportable gap, so the assertion demands the
node be present.

### Conventions

- Shaped like the **persisted** `latest-state.json`, not like an HTTP response: the two app-injected
  response-time fields, `servingBuild` and `supervisorHeartbeat`, are deliberately absent and are the
  entire content of `contract.test.ts::KnownUnsampled`. `data/store.test.ts` exercises those two by
  construction instead, including the "never ticked" (`lastTickAt: null`) reading that a payload always
  carrying a heartbeat could not express.
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
- **Every vocabulary member must stay exercised.** Before this leaf the runtime check covered 2 of 6
  states, 2 of 6 phases and 1 of 3 severities, so deleting `"close"` from `PHASES` produced zero
  failures. `contract.test.ts` now asserts set-equality between each vocabulary and what the fixture
  samples, so both dropping a member from the mirror and dropping its sample from here fail.
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
2. **It cannot invent a vocabulary member the mirror never heard of.** The full-coverage assertion forces
   this file to exercise every member the MIRROR knows; a member the SERVER declares and the mirror does
   not is outside its reach in both directions.
3. **It cannot separate two field-identical models.** `SeriesSectionNode` and `TaskSectionNode` declare
   the same three fields, so no payload and no structural walk distinguishes them.
4. **No generator, no test on the mirror↔server link.** Restated because it is the ceiling on 1-3: this
   payload is a person's account of what the server sends. Codegen from the pydantic models is the fix
   and is deferred (R3).
5. **Provenance wording is consistent across the tree as of 260731-EFA-L4 — keep it that way.** Three
   places describe where this payload comes from, and all three now agree it is hand-maintained:
   `test/fixtures/wire.ts` L22-L37 ("BE PRECISE ABOUT WHAT PINS WHAT"), `test/contract.test.ts` L32
   and L44 ("measured against a hand-kept payload") plus L59 (`LEFT FOR CODEGEN (R3)`), and
   `e2e-production/cockpit.production.spec.ts` L12-L19. Both `wire.ts` and the production spec still
   said "GENERATED from the pydantic models" earlier **within this same leaf** — `wire.ts` in three
   docstrings, the spec at its line 12 — and both were corrected. **Nothing tests this wording**, so a
   fourth description reintroducing "generated" is the drift to watch for; it is the same false claim
   that has now been written and retracted three times.

## Docs References

The payload's shape is fixed by pydantic serialization behaviour on this repository's own models —
`model_dump(by_alias=True, exclude_none=True)` — which is what makes a null-valued optional field
absent from the file rather than present as `null`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `exclude_none=True` omits fields whose value is `None` from the serialized output — the rule that makes an omitted key here indistinguishable from a field the server does not have. | `exclude_none` | [Pydantic — Serialization / model_dump](https://docs.pydantic.dev/latest/concepts/serialization/) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Six lifecycles covering all six states and all six phases, two gates with `evidenceRefs`, `stateEnteredAt` on every row. | L4-L112 | [snapshot.json](snapshot.json) |
| One enclosure, two providers, and the `activeWorktreeGroups` join value. | L113-L159 | [snapshot.json](snapshot.json) |
| `metrics` with one bucket per live state and no bucket for the terminal pair. | L160-L168 | [snapshot.json](snapshot.json) |
| All thirteen analytics keys, none empty, including `expectationRows` and eight `engineProcesses` pods spanning all eight healths. | L169-L736 | [snapshot.json](snapshot.json) |
| The writer of the persisted payload this file is shaped like: `write_projection` dumps with `by_alias=True, exclude_none=True` into `latest-state.json`. | L157-L164 | [projection_store.py](../../../mcp/src/agents_remember/observer/projection_store.py) |
| The models that define every key here, and the `extra="forbid"` rule that makes an invented field impossible on the wire. | L1-L9 | [projection.py](../../../mcp/src/agents_remember/observer/projection.py) |
| The three-direction guard: `mirror ⊇ served`, `served ⊇ mirror`, and `fixture ⊇ mirror` — the last of which exists because this payload is the oracle. | L24-L73 | [../test/contract.test.ts](../test/contract.test.ts) |
| The derived `VOCABULARIES` registry (11 paths, 6 vocabularies) and the full-coverage assertion this payload is composed to satisfy. | L269-L284; L358-L376 | [../test/contract.test.ts](../test/contract.test.ts) |
| `INDEX_SIGNATURE_SITES` — the seven absorbing nodes this payload must carry a value at, each with a written reason. | L222-L230; L333-L343 | [../test/contract.test.ts](../test/contract.test.ts) |
| `KnownUnsampled` — the two app-injected fields deliberately absent here, and why. | L177-L187 | [../test/contract.test.ts](../test/contract.test.ts) |
| The statement that this file is hand-maintained with no generator, and the chain diagram showing which link no test holds. | L22-L37 | [../test/fixtures/wire.ts](../test/fixtures/wire.ts) |
| `demandServed` and the eight anchor rows the builders require this payload to keep. | L71-L94 | [../test/fixtures/wire.ts](../test/fixtures/wire.ts) |
| The narrowing every reader comes through, and why a second `as unknown as` elsewhere would re-open the hole. | L1-L43 | [../test/servedProjection.ts](../test/servedProjection.ts) |
| Store-suite consumer, which also constructs the two app-injected fields this payload omits. | L7 | [../data/store.test.ts](../data/store.test.ts) |
| Production e2e consumer, which reads the file off disk (`readFileSync`) rather than importing it — and whose header now states this file's provenance outright: hand-maintained, no generator, type-checked against a mirror that is itself hand-maintained, so the chain ends at a human. | L12-L19; L32-L33 | [../../e2e-production/cockpit.production.spec.ts](../../e2e-production/cockpit.production.spec.ts) |

## Cross-Repo References

No cross-repository boundary. The payload imitates this repository's own Python serving layer; both
sides live in `agents-remember`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The producer this fixture stands in for is in-repo (`observer/projection.py` via `observer/projection_store.py`), not a sibling repo or external service. | L1-L9 | [projection.py](../../../mcp/src/agents_remember/observer/projection.py) |

## Update History

- 2026-08-01T09:50+02:00 — 260731-EFA-L4 curator (second pass): re-verified the card created earlier
  this leaf and repaired the two claims that had gone stale *after* it was written. (1) The
  production-e2e citation was `L28`; that spec was edited later in the leaf to replace a false
  "GENERATED from the pydantic models" comment with an accurate provenance statement, which pushed
  the `readFileSync` call from L28 to **L32-L33** — L28 is now a comment line about fault-injection
  payloads. Re-anchored to `L12-L19; L32-L33` and recorded that the spec's header is now a fourth
  in-tree statement of this file's provenance. (2) Todos item 5 claimed `test/fixtures/wire.ts` still
  calls this payload "the generated snapshot" in two docstrings. It no longer does: the staged version
  carried **three** such phrases (`SERVED` doc, `demandServed` doc, `supervisorHeartbeat` doc) and all
  three were corrected in the working tree; `grep -n generated` on it now returns only the `generatedAt`
  field and the L22 sentence "`snapshot.json` is NOT generated". Replaced the item with the standing
  hazard that matters — three places describe this file's provenance, nothing tests that wording, and
  the "generated" claim has now been written and retracted three times in this leaf alone.
  **The card's central claim was already correct and is unchanged: this file is hand-maintained, no
  generator exists, and the mirror↔server link is held by no test.** Re-verified every citation
  against the current sources: all 13 `analytics` sub-key line numbers, the four `snapshot.json`
  ranges (L4-L112 / L113-L159 / L160-L168 / L169-L736 — confirmed against the actual key offsets in
  the 737-line file), `store.test.ts` L7, `projection_store.py` L157-L164, and the six
  `contract.test.ts` ranges are all exact; only the production-e2e one had moved.
  Verification metadata pinned until closeout stamps the L4 code commit.

- 2026-08-01T09:30+02:00 — 260731-EFA-L4 curator: created. Records the payload's composition (six
  lifecycles covering all six states and phases, eight engine-process pods covering all eight healths,
  thirteen non-empty analytics keys, values at all seven absorbing nodes) and — as the file's central
  fact — that it is HAND-maintained with no generator anywhere, so the mirror↔server link is held by no
  test. States the four coverage limits (omitted `T | None`, a member the mirror never heard of,
  field-identical models, no generator) and flags that `test/fixtures/wire.ts` still calls it "the
  generated snapshot" in two docstrings that contradict its own header. Verification metadata pinned to
  the leaf base `abc7cbcc74921cdcb57a61529445f61641e919e7` until closeout stamps the L4 code commit.
