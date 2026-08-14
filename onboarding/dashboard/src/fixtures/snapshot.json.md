# dashboard/src/fixtures/snapshot.json

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/fixtures/snapshot.json`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T09:30+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The dashboard's stand-in for the server: one `WorkspaceProjection` payload, 764 lines, shaped like the
persisted `latest-state.json`. Three things read it — `test/contract.test.ts` (which measures the
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

L23 extends the manual sample with lifecycle-operation rows covering both operation kinds and every
closed status and phase member. The sample carries public progress/result/failure/guidance fields
but no operation key, candidate fingerprint, approval claim, or worker PID, preserving the
producer's private-plane boundary while making the generated dashboard contract measurable.

## Code Commentary

### Logic

Top-level keys in wire order: `version` (1), `generatedAt`, `lifecycles`, `enclosures`, `providers`,
`activeWorktreeGroups`, `metrics`, `analytics`.

- **cit:([`lifecycles`], dashboard/src/fixtures/snapshot.json:4-112) — six rows, one per state.** `blocked-001`, `running-000`, `paused-002`,
  `awaiting-003`, `completed-004`, `abandoned-005`, and their phases spread across all six of `build`,
  `reframe-research`, `request`, `trust-checkpoint`, `decide`, `close`. Two rows carry a `gate`
  (`GATE-1` open with `decisions: ["approve","revise"]`, `GATE-0` decided), both with a non-empty
  `evidenceRefs`. Every row carries `stateEnteredAt`. The `awaiting-developer` row is the state the
  mirror had never declared, and it is here so the vocabulary check can bite.
- **cit:(["\"enclosures\": ["], dashboard/src/fixtures/snapshot.json:113-135)** — one enclosure; **two providers** (a code provider and
  a memory provider) are pinned by cit:(["\"snapshotStaleSeconds\": 3.5"], dashboard/src/fixtures/snapshot.json:282-282),
  joined by `worktreeGroup: "sim-group"`; **cit:([`activeWorktreeGroups`], dashboard/src/fixtures/snapshot.json:288-288)** —
  `["sim-group"]`.
- **cit:([`metrics`], dashboard/src/fixtures/snapshot.json:289-289)** — `lifecycleCount: 6`, one bucket per LIVE state (`runningCount`,
  `blockedCount`, `pausedCount`, `awaitingDeveloperCount`, each 1), `totalTokens: 2800`, and a
  `stalenessHistogram` of `{ fresh, aging }`. The four buckets are exactly the keys `metricsFor([])`
  produces, which is what `contract.test.ts` asserts set-equality on — the terminal pair deliberately
  has no bucket.
- **`analytics`** cit:([`analytics`], dashboard/src/fixtures/snapshot.json:169-763) — all thirteen keys present and none empty: cit:([`driftSnapshots`], dashboard/src/fixtures/snapshot.json:299-299),
  cit:([`stalestSidecars`], dashboard/src/fixtures/snapshot.json:312-312), cit:([`setupSummaries`], dashboard/src/fixtures/snapshot.json:320-320), cit:([`setupProgress`], dashboard/src/fixtures/snapshot.json:331-331), cit:([`routeCoverage`], dashboard/src/fixtures/snapshot.json:341-341),
  cit:([`toolReports`], dashboard/src/fixtures/snapshot.json:350-350), cit:([`agentPickups`], dashboard/src/fixtures/snapshot.json:358-358), cit:([`expectationRows`], dashboard/src/fixtures/snapshot.json:396-396), cit:([`ledgers`], dashboard/src/fixtures/snapshot.json:413-413),
  cit:([`taskDocuments`], dashboard/src/fixtures/snapshot.json:431-431), `attentionQueue` (L368, three rows), `engineProcesses` (L406, eight pods),
  cit:(["\"series\": ["], dashboard/src/fixtures/snapshot.json:944-944).

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
2. **It cannot establish producer vocabulary.** The full-coverage assertion forces this sample to
   exercise every member the generated mirror knows; schema generation owns producer-to-mirror vocabulary.
3. **It cannot separate two field-identical models.** `SeriesSectionNode` and `TaskSectionNode` declare
   the same three fields, so no payload and no structural walk distinguishes them.
4. **The sample remains manual while the mirror is generated.** Do not describe this JSON payload as
   generated, and do not describe its coverage limits as a missing producer-to-TypeScript contract.
5. **Provenance wording must preserve that split.** `test/fixtures/wire.ts`, `contract.test.ts`, and
   `e2e-production/cockpit.production.spec.ts` all distinguish manual sample coverage from generated
   mirror provenance.

## Docs References

The payload's shape is fixed by pydantic serialization behaviour on this repository's own models —
`model_dump(by_alias=True, exclude_none=True)` — which is what makes a null-valued optional field
absent from the file rather than present as `null`.

| Finding | Anchor | Source |
| --- | --- | --- |
| `exclude_none=True` omits fields whose value is `None` from the serialized output — the rule that makes an omitted key here indistinguishable from a field the server does not have. | `write_projection` | mcp/src/agents_remember/serving/projections/projection_store.py:156-162 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Six lifecycles covering all six states and all six phases, two gates with `evidenceRefs`, `stateEnteredAt` on every row. | `lifecycles` | dashboard/src/fixtures/snapshot.json:4-112 |
| One enclosure, two providers, and the `activeWorktreeGroups` join value. | `activeWorktreeGroups` | dashboard/src/fixtures/snapshot.json:288-288 |
| `metrics` with one bucket per live state and no bucket for the terminal pair. | `metrics` | dashboard/src/fixtures/snapshot.json:289-289 |
| All thirteen analytics keys, none empty, including `expectationRows` and eight `engineProcesses` pods spanning all eight healths. | `analytics` | dashboard/src/fixtures/snapshot.json:169-763 |
| The writer of the persisted payload this file is shaped like: `write_projection` dumps with `by_alias=True, exclude_none=True` into `latest-state.json`. | `write_projection` | mcp/src/agents_remember/serving/projections/projection_store.py:156-162 |
| The models that define every key here, and the `extra="forbid"` rule that makes an invented field impossible on the wire. | `WorkspaceProjection` | mcp/src/agents_remember/observer/projection.py:53-53; mcp/src/agents_remember/observer/projection.py:990-1009 |
| The three-direction guard: `mirror ⊇ served`, `served ⊇ mirror`, and `fixture ⊇ mirror` — the last of which exists because this payload is the oracle. | "the mirror declares everything the server sends" | dashboard/src/test/contract.test.ts:367-381 |
| The derived `VOCABULARIES` registry (11 paths, 6 vocabularies) and the full-coverage assertion this payload is composed to satisfy. | `VOCABULARIES` | dashboard/src/test/contract.test.ts:268-293 |
| `INDEX_SIGNATURE_SITES` — the seven absorbing nodes this payload must carry a value at, each with a written reason. | `INDEX_SIGNATURE_SITES` | dashboard/src/test/contract.test.ts:221-229 |
| `KnownUnsampled` — the two app-injected fields deliberately absent here, and why. | `KnownUnsampled` | dashboard/src/test/contract.test.ts:186-186 |
| The provenance boundary: this snapshot is manual, while the TypeScript contract is generated and stale-checked from the Pydantic schema. | "is NOT generated" | dashboard/src/test/fixtures/wire.ts:22-35; scripts/sync-projection-types.py:43-65 |
| `demandServed` and the eight anchor rows the builders require this payload to keep. | `demandServed` | dashboard/src/test/fixtures/wire.ts:73-76 |
| The narrowing every reader comes through, and why a second `as unknown as` elsewhere would re-open the hole. | `asServedProjection` | dashboard/src/test/servedProjection.ts:22-43 |
| Store-suite consumer, which also constructs the two app-injected fields this payload omits. | "const projection = asServedProjection(snapshot);" | dashboard/src/data/store.test.ts:4-20; dashboard/src/data/store.test.ts:121-159 |
| Production e2e consumer, which reads this manual sample off disk and states that it is checked against the generated mirror while the projection generator/stale gate hold that mirror to the Pydantic schema. | "reuse"; "projection generator and stale gate" | dashboard/e2e-production/cockpit.production.spec.ts:12-19; dashboard/e2e-production/cockpit.production.spec.ts:31-34 |

## Cross-Repo References

No cross-repository boundary. The payload imitates this repository's own Python serving layer; both
sides live in `agents-remember`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The producer this fixture stands in for is in-repo (`observer/projection.py` via `observer/projection_store.py`), not a sibling repo or external service. | `write_projection` | mcp/src/agents_remember/observer/projection.py:990-990; mcp/src/agents_remember/serving/projections/projection_store.py:156-162 |

## L23 Source-Lineage Samples

Engine Process fixtures now sample aggregate `current`, `blocked`, and
`unavailable` states, every edge relation/side/state, and one
contract-addressed `worktree_sync` recovery. These are wire-contract examples,
not frontend-derived Git facts.

## Update History
- 2026-08-12T20:10+02:00 — L23 curator: recorded complete lineage vocabulary samples in the canonical snapshot; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: documented the fixture's complete lifecycle-operation kind/status/phase sample and private-identity boundary; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current data-contract card for `snapshot.json` with task-document identity, qualified seat state, and terminal projections represented by this source.
- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: re-anchored `series` to the analytics
  sub-key (730-762), corrected the `analytics` extent (169-763) and the file size in Purpose (764
  lines), generated final ranges for the S18-T3 provenance rows (wire.ts 22-35,
  sync-projection-types.py 43-65, e2e-production spec 12-19 + 31-34), replaced the external
  Pydantic URL with the in-repo `write_projection` evidence, and corrected the stale
  `attentionQueue`/`engineProcesses` line numbers (368/406). Zero findings remain.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: preserved this file's manual-sample
  provenance while correcting the surrounding contract: the TypeScript mirror is generated and
  stale-checked from the Pydantic schema. New ranges are explicit `:1-1` curator input.

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
