# dashboard/src/test/fixtures/wire.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/fixtures/wire.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T04:42+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a` |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

**The one place a dashboard test may build a node of the served projection.** Fifteen builders plus
`SERVED` and `EMPTY_ANALYTICS`, each bound to `types/projection.ts`.

R6 in one sentence: a test whose fixture is authored by the consumer cannot detect producer drift. This
leaf proved it twice — a test asserted `refusedPolarity === "amber"` against a fixture that set the
field itself, on a model that is `extra="forbid"` server-side; and three tests built a master
`TaskSubTaskRefNode` carrying `createdAt`, which its server model omits
cit:(["tests built a master", `TaskSubTaskRefNode`, "which its server model omits"], dashboard/src/test/fixtures/wire.ts:6-6). **Both fixtures were written with
`as SomeWireType`, and an assertion skips excess-property checking, so both compiled.**

## Code Commentary

### How Far A Green Build Actually Reaches

The source separates two authorities. `snapshot.json` remains a hand-maintained sampled payload,
while the producer-to-TypeScript link is generated and checked from the Pydantic schema.
`BE PRECISE ABOUT WHAT PINS WHAT` states that distinction directly.
cit:(["is NOT generated; it remains a hand-maintained", "producer-to-TypeScript link is generated and checked"], dashboard/src/test/fixtures/wire.ts:22-34)

The generated `types/projection.ts` header names both regeneration and drift-check commands
cit:(["GENERATED FILE; DO NOT EDIT", "Canonical core model", "Schema artifact", "Served-only tail", "Generator:", "Regenerate:", "Drift check:"], dashboard/src/types/projection.ts:1-7), and the generator
implements both update and check modes cit:([`check`, `main`], scripts/sync-projection-types.py:43-51; scripts/sync-projection-types.py:54-65).
The fixture contract documents that `snapshot.json` is the independent hand-authored sample while
schema generation closes producer fields and vocabulary a sample can miss
cit:(["has no served field the mirror is missing"; "reaches every declared path except the named residue"; "carries only values the mirror's vocabulary declares, at every registered path"; "keeps the master and series sub-task row models distinct"], dashboard/src/test/contract.test.ts:446-448; dashboard/src/test/contract.test.ts:462-466; dashboard/src/test/contract.test.ts:486-495; dashboard/src/test/contract.test.ts:598-628).
The Python drift suite executes the same generator in `--check` mode and rejects stale generated
files cit:([`test_documented_check_command_runs_with_its_exact_checkout_environment`, `test_committed_generated_files_are_current`], mcp/tests/test_projection_types_codegen.py:247-271; mcp/tests/test_projection_types_codegen.py:273-278).

The chain, as drawn in the source:

```text
snapshot.json --hand-maintained sample--> this fixture --type-checked against--> generated types/projection.ts
                                                                                         ↑
observer/projection.py Pydantic schema --generator + drift check--------------------------┘
```

So a green build claims two different things: the generated wire contract agrees with the producer
schema, and this fixture remains type-correct against that contract while exercising the independent
sample. The sample does not become generated authority; it remains coverage evidence for runtime
shapes and vocabularies the fixture contract explicitly measures.

### Logic

- **`SERVED`** cit:(["export const SERVED: WorkspaceProjection = asServedProjection(snapshot)"], dashboard/src/test/fixtures/wire.ts:66-66) — `asServedProjection(snapshot)`, the fixture read as the projection the server
  would have sent.
- **`demandServed(row, what)`** cit:([`demandServed`, `SERVED_LIFECYCLE`, `SERVED_ENCLOSURE`, `SERVED_PROVIDER`, `SERVED_TASK_DOC`, `SERVED_ENGINE_PROCESS`, `SERVED_PICKUP`, `SERVED_ATTENTION`, `SERVED_GATE`], dashboard/src/test/fixtures/wire.ts:73-76; dashboard/src/test/fixtures/wire.ts:78-91) throws `snapshot.json no longer carries ${what}` rather than
  spreading `undefined`. Eight anchors are pulled through it: `lifecycles[0]`, `enclosures[0]`,
  `providers[0]`, `analytics.taskDocuments[0]`, `analytics.engineProcesses[0]`,
  `analytics.agentPickups[0]`, `analytics.attentionQueue[0]`, and `SERVED.lifecycles.find(entry =>
  entry.gate !== undefined)?.gate`. A snapshot that stops sampling one of them fails loudly here instead
  of producing a base quietly missing every field.
- **The bases** cit:([`BASE_LIFECYCLE`, `BASE_GATE`, `BASE_ENCLOSURE`, `BASE_PROVIDER`, `BASE_TASK_DOC`, `BASE_ENGINE_PROCESS`, `BASE_PICKUP`, `BASE_ATTENTION`], dashboard/src/test/fixtures/wire.ts:95-107; dashboard/src/test/fixtures/wire.ts:109-117; dashboard/src/test/fixtures/wire.ts:119-136; dashboard/src/test/fixtures/wire.ts:138-144; dashboard/src/test/fixtures/wire.ts:146-167; dashboard/src/test/fixtures/wire.ts:169-198; dashboard/src/test/fixtures/wire.ts:200-208; dashboard/src/test/fixtures/wire.ts:210-216) — `BASE_LIFECYCLE`, `BASE_GATE`, `BASE_ENCLOSURE`, `BASE_PROVIDER`,
  `BASE_TASK_DOC`, `BASE_ENGINE_PROCESS`, `BASE_PICKUP`, `BASE_ATTENTION`. Since 260815-DAG-L14 `BASE_TASK_DOC` also defaults `seats: []` (the new required
`TaskDocNode` field). Each is annotated with the
  mirror type AND assembled from a served row, so it is pinned from both sides at once: a required field
  the server adds fails to compile until it is filled, and it can only be filled from a served row.
  **Only REQUIRED fields are carried.** Optionals (`gate`, `ask`, `staleSeconds`, `carryoverDoneAt`, …) are left
  off on purpose — a default gate nobody asked for would silently change what an attention-queue test is
  measuring.
- **`EMPTY_ANALYTICS`** cit:([`EMPTY_ANALYTICS`], dashboard/src/test/fixtures/wire.ts:223-237) — every analytics list present and empty. The reducer always sends
  every key (they are list defaults server-side), so "empty" is a shape the server produces — unlike an
  object that omits them, which is what a `{} as Analytics` fixture claimed.
- **The builders** cit:([`lifecycle`, `gate`, `lifecycleWithGate`, `enclosure`, `provider`, `taskDoc`, `engineProcess`, `agentPickup`, `attentionItem`, `action`, `analytics`, `observerEvent`], dashboard/src/test/fixtures/wire.ts:241-246; dashboard/src/test/fixtures/wire.ts:248-253; dashboard/src/test/fixtures/wire.ts:256-266; dashboard/src/test/fixtures/wire.ts:268-273; dashboard/src/test/fixtures/wire.ts:275-280; dashboard/src/test/fixtures/wire.ts:282-287; dashboard/src/test/fixtures/wire.ts:289-294; dashboard/src/test/fixtures/wire.ts:296-301; dashboard/src/test/fixtures/wire.ts:303-308; dashboard/src/test/fixtures/wire.ts:310-315; dashboard/src/test/fixtures/wire.ts:317-322; dashboard/src/test/fixtures/wire.ts:373-385) — `lifecycle`, `gate`, `lifecycleWithGate`, `enclosure`, `provider`,
  `taskDoc`, `engineProcess`, `agentPickup`, `attentionItem`, `action`, `analytics`. Each takes
  `Overrides<O, Node>` and widens it to a plain `Partial<Node>` locally before spreading. `action` and
  `observerEvent` differ: their override is REQUIRED rather than optional, via
  `Partial<T> & Pick<T, "…">`.
- **`projection`** cit:([`projection`], dashboard/src/test/fixtures/wire.ts:329-345) — destructures `lifecycles`, `analytics` and `metrics` out of the
  override, then sets `metrics: metrics ?? metricsFor(lifecycles)`. **`metrics` is DERIVED from the
  lifecycles by the mirror's own rollup rather than restated beside them** — the hand-kept bucket lists
  are where the `awaiting-developer` gap kept reappearing, on both sides of the wire.
- **`agentNotifierHeartbeat`** cit:(["The app-injected agent-notifier tick", "absent from the snapshot", "base is a typed literal", `agentNotifierHeartbeat`], dashboard/src/test/fixtures/wire.ts:349-354) — a typed literal, not a served row, because the field is
  app-injected and therefore absent from the snapshot (`contract.test.ts::KnownUnsampled` names it).
- **`observerEvent`** cit:(["An observer-event envelope", "separate contract from the projection", "base cannot come from", `observerEvent`], dashboard/src/test/fixtures/wire.ts:370-375) — same reasoning: the event channel (`types/event.ts` ←
  `observer/events.py`) is a separate contract from the projection, so its base cannot come from
  `snapshot.json`.
- **`reparsed(source)`** cit:(["A byte-fresh copy of a projection", "tests need in order to prove", "on purpose. The round-trip answers", "routing it through", "parameter type cannot narrow", "clone keeps the source's type honestly", `reparsed`], dashboard/src/test/fixtures/wire.ts:389-398) — `structuredClone`, deliberately not `JSON.parse(JSON.stringify(…))`.
  The round-trip answers `any`, and `any` assigns to anything, so routing it through
  `asServedProjection` LOOKS like a check and is vacuous — a parameter type cannot narrow an argument
  that is already `any`. This exact function was making that mistake before rule 3 was written, and
  `wireFixtureGuard.test.ts` cites `fixtures/wire.ts::reparsed` by name when it plants the `any` probe.

### Conventions

- Every builder's override is checked twice over at the CALL SITE: a field the mirror does not declare
  is an excess property on a fresh literal (which is exactly where both proven defects would have died),
  and a REQUIRED field written as an explicit `undefined` is rejected by `Overrides<O, Node>` — which
  plain `Partial<Node>` allows whenever `exactOptionalPropertyTypes` is off, and it is off here.
- Bases carry required fields only; a test that needs an optional names it.
- This module contains **no** `as WireType` assertion. Its whole purpose is to be the alternative to one.

### Invariants And Boundaries

- A test builds a projection node here or annotates/`satisfies` it — it does not cast it.
  `wireFixtureGuard.test.ts`'s failure message says so in as many words.
- The bases must stay served-derived. Replacing a `SERVED_*.field` with a literal removes the second
  pin and leaves only "the mirror could produce this".
- `projection()` must keep deriving `metrics`. Passing a hand-written `metrics` override is possible and
  is the escape hatch, not the default.
- The conversation grammar is NOT here — it lives in `fixtures/conversationWire.ts`, which mirrors a
  different pair of server modules.

### Todos

**What building a fixture here does not prove.**

1. **The snapshot remains a sample, not generated authority.** `contract.test.ts` measures the
   generated mirror against `snapshot.json` in three fixture directions, while schema generation and
   its drift check independently bind `types/projection.ts` to the Pydantic producer. A green sample
   test therefore proves exercised runtime coverage, not that the sample itself is exhaustive.
2. **Nothing about a pre-widened override.** `Overrides` binds a FRESH literal at the call site; an
   override that has been through a variable admits an explicit `undefined` again.
   `wireFixtureGuard.ts` covers some of that residue and `fixtureOverrides.test.ts` asserts the rest as a
   known pass.

No stale "generated snapshot" wording remains: the source now explicitly pairs the hand-maintained
sample with the generated producer-to-TypeScript contract
cit:(["is NOT generated; it remains a hand-maintained", "producer-to-TypeScript link is generated and checked"], dashboard/src/test/fixtures/wire.ts:22-23). The two `generatedAt` field
references remain ordinary projection data cit:(["generatedAt: SERVED.generatedAt", "ts: SERVED.generatedAt"], dashboard/src/test/fixtures/wire.ts:338-338; dashboard/src/test/fixtures/wire.ts:382-382). The three docstrings that used to contradict the header now read "the sampled
payload" cit:(["The sampled payload"], dashboard/src/test/fixtures/wire.ts:65-65), "A row the snapshot is expected to carry" cit:(["A row the snapshot is expected to carry"], dashboard/src/test/fixtures/wire.ts:69-69) and "absent from the snapshot" cit:(["absent from the snapshot"], dashboard/src/test/fixtures/wire.ts:350-350).

## Docs References

The guarantee rests on TypeScript behaviours, not on external domain documentation: an assertion skips
excess-property checking (which is what let both proven defects compile), excess-property checking
applies to fresh literals, and `structuredClone` preserves a value's static type where a JSON round-trip
does not.

| Finding | Anchor | Source |
| --- | --- | --- |
| A type assertion performs no check and removes excess-property checking — the mechanism by which `as SomeWireType` let a `refusedPolarity` and a master-row `createdAt` compile. | "as SomeWireType" | dashboard/src/test/fixtures/wire.ts:7-7 |
| Excess-property checking applies to fresh object literals, which is why an override written inline at the call site is checked and one routed through a variable is not. | `Overrides` | dashboard/src/test/fixtures/overrides.ts:60-66 |
| `structuredClone` deep-clones a value at runtime; unlike a `JSON.parse(JSON.stringify(…))` round-trip it does not launder the value's static type into `any`. | `reparsed` | dashboard/src/test/fixtures/wire.ts:396-398 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| R6 and the two proven defects, both of which compiled because they were written with `as SomeWireType`. | "R6 in one sentence"; "drift. This leaf proved it twice"; "fixture that set the field itself"; "tests built a master"; "fixtures were written with"; "both compiled" | dashboard/src/test/fixtures/wire.ts:3-8 |
| `snapshot.json` remains the hand-maintained sample while the source names the producer-to-TypeScript link as generated and checked. | "is NOT generated; it remains a hand-maintained"; "producer-to-TypeScript link is generated and checked" | dashboard/src/test/fixtures/wire.ts:22-23 |
| `projection.ts` marks itself generated and names its schema, generator, regeneration command, and drift check. | "GENERATED FILE; DO NOT EDIT"; "Canonical core model"; "Schema artifact"; "Served-only tail"; "Generator:"; "Regenerate:"; "Drift check:" | dashboard/src/types/projection.ts:1-7 |
| The projection generator implements both check and generation paths. | `check`; `main` | scripts/sync-projection-types.py:43-51; scripts/sync-projection-types.py:54-65 |
| The fixture contract distinguishes its independent sample checks from the producer-schema coverage codegen closes. | "has no served field the mirror is missing"; "reaches every declared path except the named residue"; "carries only values the mirror's vocabulary declares, at every registered path"; "keeps the master and series sub-task row models distinct" | dashboard/src/test/contract.test.ts:446-448; dashboard/src/test/contract.test.ts:462-466; dashboard/src/test/contract.test.ts:486-495; dashboard/src/test/contract.test.ts:598-628 |
| The Python drift test rejects stale committed generated files. | `test_committed_generated_files_are_current` | mcp/tests/test_projection_types_codegen.py:271-276 |
| How the defaults stay honest: required fields only, every value taken from a served row, optionals deliberately omitted. | "HOW THE DEFAULTS STAY HONEST"; "annotated with the mirror type"; "a required field the server adds fails to compile"; "Only the REQUIRED fields are carried"; "staleSeconds"; "silently change what an attention-queue test is measuring"; `BASE_LIFECYCLE`; `BASE_GATE`; `BASE_ENCLOSURE`; `BASE_PROVIDER`; `BASE_TASK_DOC`; `BASE_ENGINE_PROCESS`; `BASE_PICKUP`; `BASE_ATTENTION` | dashboard/src/test/fixtures/wire.ts:15-20; dashboard/src/test/fixtures/wire.ts:95-107; dashboard/src/test/fixtures/wire.ts:109-117; dashboard/src/test/fixtures/wire.ts:119-136; dashboard/src/test/fixtures/wire.ts:138-144; dashboard/src/test/fixtures/wire.ts:146-167; dashboard/src/test/fixtures/wire.ts:169-198; dashboard/src/test/fixtures/wire.ts:200-208; dashboard/src/test/fixtures/wire.ts:210-216 |
| `demandServed` and the eight served anchors it demands the snapshot keep. | `demandServed`; `SERVED_LIFECYCLE`; `SERVED_ENCLOSURE`; `SERVED_PROVIDER`; `SERVED_TASK_DOC`; `SERVED_ENGINE_PROCESS`; `SERVED_PICKUP`; `SERVED_ATTENTION`; `SERVED_GATE` | dashboard/src/test/fixtures/wire.ts:73-76; dashboard/src/test/fixtures/wire.ts:78-91 |
| The eight bases, each annotated with a generated mirror type and filled from `SERVED`. | `BASE_LIFECYCLE`; `BASE_GATE`; `BASE_ENCLOSURE`; `BASE_PROVIDER`; `BASE_TASK_DOC`; `BASE_ENGINE_PROCESS`; `BASE_PICKUP`; `BASE_ATTENTION` | dashboard/src/test/fixtures/wire.ts:95-107; dashboard/src/test/fixtures/wire.ts:109-117; dashboard/src/test/fixtures/wire.ts:119-136; dashboard/src/test/fixtures/wire.ts:138-144; dashboard/src/test/fixtures/wire.ts:146-167; dashboard/src/test/fixtures/wire.ts:169-198; dashboard/src/test/fixtures/wire.ts:200-208; dashboard/src/test/fixtures/wire.ts:210-216 |
| `EMPTY_ANALYTICS` — every key present and empty, which is a shape the reducer produces. | `EMPTY_ANALYTICS` | dashboard/src/test/fixtures/wire.ts:223-237 |
| `projection()` deriving `metrics` from the lifecycles via `metricsFor` rather than restating buckets. | "metrics: metrics ?? metricsFor(lifecycles)" | dashboard/src/test/fixtures/wire.ts:344-344 |
| `reparsed` using `structuredClone`, with the note that `asServedProjection(JSON.parse(…))` is a vacuous check. | `reparsed` | dashboard/src/test/fixtures/wire.ts:396-398 |
| `asServedProjection` — the sanctioned narrowing this module's `SERVED` constant is read through. | `asServedProjection` | dashboard/src/test/servedProjection.ts:41-43 |
| The hand-maintained oracle the bases are assembled from — `lifecycles`, `enclosures`, `providers` and the four `analytics` rows the anchors pull (`agentPickups`, `taskDocuments`, `attentionQueue`, `engineProcesses`). | "\"lifecycles\": ["; "\"enclosures\": ["; "\"analytics\": {"; "\"agentPickups\": ["; "\"taskDocuments\": ["; "\"attentionQueue\": ["; "\"engineProcesses\": [" | dashboard/src/fixtures/snapshot.json:5-6; dashboard/src/fixtures/snapshot.json:44-44; dashboard/src/fixtures/snapshot.json:98-98; dashboard/src/fixtures/snapshot.json:748-748; dashboard/src/fixtures/snapshot.json:1221-1221; dashboard/src/fixtures/snapshot.json:1800-1800 |
| The override constraint every builder takes, and the three limits it documents. | `Overrides` | dashboard/src/test/fixtures/overrides.ts:60-66 |
| The guard that catches the residue `Overrides` cannot — the smuggled field with no assertion to ban, and the `any` rule whose comment names `fixtures/wire.ts::reparsed` as the site that was making exactly that mistake. | "catches a smuggled field where there is no assertion to ban"; "fixtures/wire.ts::reparsed" | dashboard/src/test/wireFixtureGuard.test.ts:512-534 |
| `KnownUnsampled`, which names `agentNotifierHeartbeat` as absent from the snapshot and therefore a typed literal here. | `KnownUnsampled` | dashboard/src/test/contract.test.ts:188-191 |
| `ObserverEvent` — the separate event contract this module's `observerEvent` builder targets, mirroring `observer/events.py` rather than `projection.py`. | `ObserverEvent` | dashboard/src/types/event.ts:9-22 |
| The companion builder module for the conversation grammar. | `conversationPage` | dashboard/src/test/fixtures/conversationWire.ts:228-243 |

## Cross-Repo References

No cross-repository boundary. The wire this file builds against is a Python↔TypeScript seam inside
`agents-remember`; both the producing models and the consuming mirror are in this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| The in-repo `WorkspaceProjection` producer model uses `extra="forbid"` and declares the complete projection boundary. | `WorkspaceProjection` | mcp/src/agents_remember/observer/projection.py:1131-1153 |

## Update History


- 2026-08-20T10:45+02:00 — 260815-DAG-L12 curator: re-anchored citation range(s) to current source after the L12 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-20T04:42+02:00 — 260815-DAG-L14: `BASE_TASK_DOC` defaults `seats: []` (new required
  `TaskDocNode` field); all shifted citation ranges re-pinned to the current source. Verified at
  code commit 9c3180c1.


- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: the wire TaskDocNode fixture now includes the required
  empty `executionWaves` field; its existing transport scenario is unchanged.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-04T19:00:51+02:00 — 260731-EFA-L6 S18-B12 curator correction (reviewer-BLOCK repair + delta-verdict residual repair): distinguished the hand-maintained `snapshot.json` sample from the generated/drift-checked producer-to-TypeScript mirror (generator, drift tests, and fixture contract bound to their operative sources); restored operative fixture bodies (bases, `demandServed`, builders, `reparsed`); widened the pin-distinction citation to the full 22-34 comment; bound the `--check` drift execution to its exact test; bound both guard rules to the complete 512-534 evidence; narrowed the producer-model claim to the singular `WorkspaceProjection`. Residual repair per `260731-EFA-L6-S18-B12-reviewer-delta-verdict.md`: replaced `landing` with `carryoverDoneAt` in the bases bullet's optional-left-off examples (`landing` is a required `EngineProcessNode` field carried at `wire.ts:193`; `carryoverDoneAt?` is optional at `projection.ts:164` and absent from `wire.ts:169-198`), and corrected the Purpose defect narrative to the source's record of a master `TaskSubTaskRefNode` carrying `createdAt`, which its server model omits, now cited to `wire.ts:6`. The scoped fixer confirmed the final ranges with no writes.
- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 20 citation rows and normalized 17 prose citation groups; scoped citation check now passes.

- 2026-08-01T14:05+02:00 — 260731-EFA-L4 curator (correction pass). **Withdrew Todos item 3**, which
  told the next agent to fix wording that is already fixed. The item was written from the *staged* blob
  (`git show :dashboard/src/test/fixtures/wire.ts` still carries "the generated payload" L47, "A row the
  generated snapshot" L51, "absent from the generated" L285); the **working tree** — which is what a
  reader opens — was already corrected, and `grep -n generated` over it returns only the header's own
  `` `snapshot.json` is NOT generated `` cit:(["is NOT generated; it remains a hand-maintained"], dashboard/src/test/fixtures/wire.ts:22-22) and two `generatedAt` field references. Also
  noted there were **three** such phrases, not two: `SERVED`'s doc (now L68) was never in the count.
  Corrected the header quote's diffstat: the snapshot edit is **+642/-15**, not "+657 lines" (657 is
  insertions+deletions read as insertions; `git diff --numstat -- dashboard/src/fixtures/snapshot.json`
  answers `642 15`) — the source comment now carries the same figure. Repaired three citations, each of
  which started correctly and stopped short of a symbol its own claim names: `types/projection.ts`
  L156-L220 → **L1-L726** (`metricsFor` is at L250-L257, outside the old end, and the bases annotate node
  types as far down as `EngineProcessNode` L603); `wireFixtureGuard.test.ts` L520-L528 → **L513-L535**
  (the `any` test opens at L527 and names `fixtures/wire.ts::reparsed` at L530, both past the old end,
  while L520-L525 was the tail of the previous test); `fixtures/snapshot.json` L4-L168 → **L4-L737** (the
  old end stopped at `metrics` and excluded `analytics`, where four of the eight `demandServed` anchors
  live — `agentPickups` L229, `taskDocuments` L287, `attentionQueue` L348, `engineProcesses` L386).
  Finally, Todos item 1 said only "the mirror↔server link is hand-maintained"; it now also states that
  `contract.test.ts` *does* measure the mirror against `snapshot.json` in three directions, so the item
  cannot be read as "no test measures anything past the mirror". Verification metadata untouched.

- 2026-08-01T10:10+02:00 — 260731-EFA-L4 curator: created. Records the fifteen builders, the eight
  `demandServed` anchors, the served-derived bases (required fields only), `EMPTY_ANALYTICS` as a shape
  the reducer really produces, `projection()` deriving `metrics` via `metricsFor`, and `reparsed`'s
  `structuredClone` with the vacuous-check reasoning behind it. Carries the header's own precision about
  reach: `snapshot.json` is NOT generated and no in-repo generator exists, so the chain is `tsc -b` binding
  this fixture to the mirror, `contract.test.ts` measuring the mirror against `snapshot.json` in three
  directions, and the `snapshot.json` ↔ `observer/projection.py` crossing held by no test — the older
  "generated" framing is not restated. (The clause claiming two docstrings still contradict the header was
  read off the staged blob and is corrected in the 14:05 entry.) Verification
  metadata pinned to the leaf base `abc7cbcc74921cdcb57a61529445f61641e919e7` until closeout stamps the
  L4 code commit.