# dashboard/src/test/fixtures/wire.ts

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
The sample introduces no served field missing from the mirror. cit:(["has no served field the mirror is missing"], dashboard/src/test/contract.test.ts:477-479); The sample covers declared structural paths except explicit residue. cit:(["reaches every declared path except the named residue"], dashboard/src/test/contract.test.ts:493-497); Every sampled registered vocabulary value must be legal. cit:(["carries only values the mirror's vocabulary declares, at every registered path"], dashboard/src/test/contract.test.ts:517-526); The contract keeps master and series sub-task row fields distinct. cit:(["keeps the master and series sub-task row models distinct"], dashboard/src/test/contract.test.ts:606-636).
The generator’s explicit `--check` command remains available. The former Python drift-test module was retired; it is not current acceptance evidence.

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
- **demandServed and required bases.** Six retained sample anchors cover lifecycles, enclosures, providers, task documents, engine processes and attention. Missing rows fail loudly rather than spreading undefined. BASE_LIFECYCLE, BASE_ENCLOSURE, BASE_PROVIDER, BASE_TASK_DOC, BASE_ENGINE_PROCESS and BASE_ATTENTION are annotated with generated mirror types. Gate/pickup anchors and bases are removed. Only required fields are supplied; optional behavior is deliberately requested. Copied served values, derived values and neutral defaults remain separate provenance: BASE_TASK_DOC form is recomputed, type is empty, headerNotes is empty and statusNoteTruncated is false under the bounded Owner mark52. The source header's stronger every-value-from-served sentence remains mark52, not a universal copied-value guarantee. Do not broaden the admitted neutral/recomputed defaults or cast past the contract.
- **`EMPTY_ANALYTICS`** cit:([`EMPTY_ANALYTICS`], dashboard/src/test/fixtures/wire.ts:223-237) — every analytics list present and empty. The reducer always sends
  every key (they are list defaults server-side), so "empty" is a shape the server produces — unlike an
  object that omits them, which is what a `{} as Analytics` fixture claimed.
- **Retained builders.** lifecycle, enclosure, provider, taskDoc, engineProcess, attentionItem and analytics take Overrides over their actual mirror nodes. action and observerEvent require their action/kind override. Local widening to Partial before spread does not authorize an absent required field at a fresh call site. No gate, lifecycleWithGate, agentPickup or agentNotifierHeartbeat builder remains.
- **`projection`** cit:([`projection`], dashboard/src/test/fixtures/wire.ts:329-345) — destructures `lifecycles`, `analytics` and `metrics` out of the
  override, then sets `metrics: metrics ?? metricsFor(lifecycles)`. **`metrics` is DERIVED from the
  lifecycles by the mirror's own rollup rather than restated beside them** — the hand-kept bucket lists
  are where the `awaiting-developer` gap kept reappearing, on both sides of the wire.
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
- Keep wire-shape authority distinct from initializer provenance: copied served fields retain the
  sample pin; a derived or neutral default supplies type-correct construction, not producer-value
  evidence. BASE_TASK_DOC's four stated defaults are the scoped Owner-admitted exception; do not
  broaden it into arbitrary consumer-authored semantics or an undocumented exception elsewhere.
- `projection()` must keep deriving `metrics`. Passing a hand-written `metrics` override is possible and
  is the escape hatch, not the default.
- The removed conversationWire fixture grammar has no current builder/consumer home; this module targets only retained projection/event contracts.

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

## Evidence

### Docs References

The guarantee rests on TypeScript behaviours, not on external domain documentation: an assertion skips
excess-property checking (which is what let both proven defects compile), excess-property checking
applies to fresh literals, and `structuredClone` preserves a value's static type where a JSON round-trip
does not.

- A type assertion performs no check and removes excess-property checking — the mechanism by which `as SomeWireType` let a `refusedPolarity` and a master-row `createdAt` compile. [1]
- Excess-property checking applies to fresh object literals, which is why an override written inline at the call site is checked and one routed through a variable is not. [2]
- `structuredClone` deep-clones a value at runtime; unlike a `JSON.parse(JSON.stringify(…))` round-trip it does not launder the value's static type into `any`. [3]

### Repo-Internal References

- R6 and the two proven defects, both of which compiled because they were written with `as SomeWireType`. [4]
- `snapshot.json` remains the hand-maintained sample while the source names the producer-to-TypeScript link as generated and checked. [5]
- `projection.ts` marks itself generated and names its schema, generator, regeneration command, and drift check. [6]
- The projection generator implements both check and generation paths. [7]
- The sample introduces no served field missing from the mirror. [8]
- The sample covers declared structural paths except explicit residue. [9]
- Every sampled registered vocabulary value must be legal. [10]
- The contract keeps master and series sub-task row fields distinct. [11]
- Required base fields are typed, with copied, derived and explicitly neutral defaults distinguished; optional behavior is requested deliberately. [12]
- demandServed requires six current sample anchors for lifecycle/enclosure/provider/task/engine/attention, without removed gate/pickup rows. [13]

- Six current bases retain generated type checks and scoped copied/derived/neutral origins, not a universal copied-value guarantee. [14]
- `EMPTY_ANALYTICS` — every key present and empty, which is a shape the reducer produces. [15]
- `projection()` deriving `metrics` from the lifecycles via `metricsFor` rather than restating buckets. [16]
- `reparsed` using `structuredClone`, with the note that `asServedProjection(JSON.parse(…))` is a vacuous check. [17]
- `asServedProjection` — the sanctioned narrowing this module's `SERVED` constant is read through. [18]
- The fixture bases draw their lifecycle sample from the hand-maintained oracle. [19]
- The fixture bases draw their enclosure sample from the same oracle. [20]
- The wire oracle carries the hand-maintained sampled analytics payload. [21]
- The task-document builder takes its sample from analytics. [23]
- The attention-item builder takes its sample from analytics. [24]
- The engine-process builder takes its sample from analytics. [25]
- The provider builder takes its sample from the top-level providers array. [26]
- The served snapshot supplies the code provider and memory provider in its top-level provider array.
- The override constraint every builder takes, and the three limits it documents. [28]
- The guard that catches the residue `Overrides` cannot — the smuggled field with no assertion to ban, and the `any` rule whose comment names `fixtures/wire.ts::reparsed` as the site that was making exactly that mistake. [29]
- `ObserverEvent` — the separate event contract this module's `observerEvent` builder targets, mirroring `observer/events.py` rather than `projection.py`. [31]

### Cross-Repo References

No cross-repository boundary. The wire this file builds against is a Python↔TypeScript seam inside
`agents-remember`; both the producing models and the consuming mirror are in this repository.

- The in-repo `WorkspaceProjection` producer model uses `extra="forbid"` and declares the complete projection boundary. [33]
