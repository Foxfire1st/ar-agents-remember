# dashboard/src/fixtures/snapshot.json

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/fixtures/snapshot.json`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The dashboard's stand-in for the server: one `WorkspaceProjection` payload, 1,923 lines at the R03
commit, shaped like the persisted `latest-state.json`. Three things read it — `test/contract.test.ts` (which measures the
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
but no operation key, candidate fingerprint, approval claim, or worker PID, preserving the
producer's private-plane boundary while making the generated dashboard contract measurable.

## Code Commentary

### Logic

Top-level keys in wire order: `version` (1), `generatedAt`, `lifecycles`, `enclosures`, `providers`,
`activeWorktreeGroups`, `metrics`, `analytics`. `analytics` now begins at line 3 and `lifecycles` at
line 1749, `metrics` at line 1887 in the reserialized file
cit:([`activeWorktreeGroups`], dashboard/src/fixtures/snapshot.json:2-2).

Under CCR-R03@v1 the R03 leaf reserialized this fixture (arrays collapsed to single-line JSON and
empty/edge rows normalized) to re-synchronize it with the regenerated dashboard contract fixtures;
no served field, row, or value semantics changed — the mirror guard and wire builders still read the
same payload cit:([`lifecycles`, `metrics`], dashboard/src/fixtures/snapshot.json:1749-1749; dashboard/src/fixtures/snapshot.json:1887-1887).

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
| Six lifecycles covering all six states and all six phases, two gates with `evidenceRefs`, `stateEnteredAt` on every row. | `lifecycles` | dashboard/src/fixtures/snapshot.json:1749-1749 |
| One enclosure, two providers, and the `activeWorktreeGroups` join value. | `activeWorktreeGroups` | dashboard/src/fixtures/snapshot.json:2-2 |
| `metrics` with one bucket per live state and no bucket for the terminal pair. | `metrics` | dashboard/src/fixtures/snapshot.json:1887-1887 |
| All thirteen analytics keys, none empty, including `expectationRows` and eight `engineProcesses` pods spanning all eight healths. | `analytics` | dashboard/src/fixtures/snapshot.json:3-3 |
| The writer of the persisted payload this file is shaped like: `write_projection` dumps with `by_alias=True, exclude_none=True` into `latest-state.json`. | `write_projection` | mcp/src/agents_remember/serving/projections/projection_store.py:156-162 |
| The models that define every key here, and the `extra="forbid"` rule that makes an invented field impossible on the wire. | `WorkspaceProjection` | mcp/src/agents_remember/observer/projection.py:1131-1153 |
| The three-direction guard: `mirror ⊇ served`, `served ⊇ mirror`, and `fixture ⊇ mirror` — the last of which exists because this payload is the oracle. | "the mirror declares everything the server sends" | dashboard/src/test/contract.test.ts:435-449 |
| The derived `VOCABULARIES` registry and its non-vacuous sampled-value membership assertion. | `VOCABULARIES` | dashboard/src/test/contract.test.ts:287-425; dashboard/src/test/contract.test.ts:485-495 |
| `INDEX_SIGNATURE_SITES` — the seven absorbing nodes this payload must carry a value at, each with a written reason. | `INDEX_SIGNATURE_SITES` | dashboard/src/test/contract.test.ts:221-229 |
| `KnownUnsampled` — the two app-injected fields deliberately absent here, and why. | `KnownUnsampled` | dashboard/src/test/contract.test.ts:187-190 |
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


## 260815-DAG-L12 Fixture Graph View

The sprint fixture (`sim-master` / `sim-master-b` scenario) carries the render-ready `executionGraphView` (L12-R4): a segmented master with a joined title and an early leaf, plus a dependent second master waiting on it with a recorded predecessor reason and judgment id. Those rows remain representative contract examples; complete enum ownership stays with schema generation.


## 260815-DAG Master Full-Gate Repair

The snapshot fixture gained a super-to-leaf source-relation entry (`relation: "super-to-leaf"`, state `current`) and two execution-graph view nodes (a `segment` with `frontierState: "landed"` and a `lump` with `frontierState: "ready"`) as representative dashboard contract examples.

## 260831-CCR-L15 Fixture Cursor Sample

The hand-kept fixture snapshot now seeds `meaningfulRevision: 1` on the lifecycle
operation node that previously carried only the revision-less projection fields, so dashboard and
wire-fixture consumers have a cursor-carrying sample matching the regenerated schema.

## Update History

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded the `meaningfulRevision: 1` fixture sample on the lifecycle operation node.
- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the R03 fixture reserialization (single-line array formatting; 1,979 → 1,923 lines) and refreshed the top-level key anchor ranges; no served-field or value semantics changed.

- 2026-08-25T16:21:43+02:00 — 260824-PDLS-L12 curator: removed the stale claim that this
  representative payload must instantiate every closed-vocabulary member. The generated schema and
  stale-output check own exhaustive producer vocabulary; this fixture remains responsible for
  structural path coverage and legality of sampled values. Verification awaits the candidate code
  commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: snapshot fixture extended with the super-to-leaf relation and two execution-graph view nodes. Verified at code commit e5cb139f.



- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   the sprint fixture carries the render-ready `executionGraphView` scenario (L12-R4). Verified at code commit b7f2c8e2.

- 2026-08-20T04:40+02:00 — 260815-DAG-L14: the sprint fixture carries non-empty `seats` (both
  identity-present and identity-absent members) and two typed `masterRef` rows whose master targets
  exist in the same fixture; every other task document defaults `seats: []`. Verified at code
  commit 9c3180c1.


- 2026-08-18T13:00+02:00 — No content impact: 260815-DAG-L8 added the closeout-queue projection surface (closeoutQueues); the behavior this card describes is unchanged.

- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: the canonical dashboard snapshot now includes a
  reasoned sprint execution graph, derived waves, and both organizational and atomic commanded
  master examples; ordinary masters publish empty derived waves. Verification remains closeout-owned.
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