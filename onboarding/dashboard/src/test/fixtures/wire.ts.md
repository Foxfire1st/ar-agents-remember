# dashboard/src/test/fixtures/wire.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/fixtures/wire.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T14:05+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

**The one place a dashboard test may build a node of the served projection.** Fifteen builders plus
`SERVED` and `EMPTY_ANALYTICS`, each bound to `types/projection.ts`.

R6 in one sentence: a test whose fixture is authored by the consumer cannot detect producer drift. This
leaf proved it twice — a test asserted `refusedPolarity === "amber"` against a fixture that set the
field itself, on a model that is `extra="forbid"` server-side; and three tests built a master
`TaskDocNode` carrying `createdAt`, which no server model declares. **Both fixtures were written with
`as SomeWireType`, and an assertion skips excess-property checking, so both compiled.**

## Code Commentary

### How Far A Green Build Actually Reaches

The header does not overstate the guarantee, and neither should this document. `BE PRECISE ABOUT WHAT
PINS WHAT` (L22-L37) states it outright:

> **`snapshot.json` is NOT generated.** No generator exists — nothing under `mcp/`, `scripts/` or
> `dashboard/` writes it — and it is hand-maintained (this change alone edited it by +642/-15 lines).

The chain, as drawn in the source:

```text
this fixture  --type-checked against-->  types/projection.ts  --measured against-->  snapshot.json
               (`Overrides<O, Node>`,     (`contract.test.ts`, three directions)      ↕ BY HAND
                and every annotated                                            observer/projection.py
                base below)
```

So a green build claims exactly this: **the mirror could produce this shape, and the mirror agrees with
a payload a person wrote to stand in for the server.** The mirror↔server link is the hand-maintained
one, and it is the only link in the chain no test can hold up. A field the server starts sending that
neither the snapshot nor the mirror knows about is invisible to all of it.

### Logic

- **`SERVED`** (L69) — `asServedProjection(snapshot)`, the fixture read as the projection the server
  would have sent.
- **`demandServed(row, what)`** (L71-L79) throws `snapshot.json no longer carries ${what}` rather than
  spreading `undefined`. Eight anchors are pulled through it (L81-L94): `lifecycles[0]`, `enclosures[0]`,
  `providers[0]`, `analytics.taskDocuments[0]`, `analytics.engineProcesses[0]`,
  `analytics.agentPickups[0]`, `analytics.attentionQueue[0]`, and `SERVED.lifecycles.find(entry =>
  entry.gate !== undefined)?.gate`. A snapshot that stops sampling one of them fails loudly here instead
  of producing a base quietly missing every field.
- **The bases** (L96-L212) — `BASE_LIFECYCLE`, `BASE_GATE`, `BASE_ENCLOSURE`, `BASE_PROVIDER`,
  `BASE_TASK_DOC`, `BASE_ENGINE_PROCESS`, `BASE_PICKUP`, `BASE_ATTENTION`. Each is annotated with the
  mirror type AND assembled from a served row, so it is pinned from both sides at once: a required field
  the server adds fails to compile until it is filled, and it can only be filled from a served row.
  **Only REQUIRED fields are carried.** Optionals (`gate`, `ask`, `staleSeconds`, `landing`, …) are left
  off on purpose — a default gate nobody asked for would silently change what an attention-queue test is
  measuring.
- **`EMPTY_ANALYTICS`** (L214-L233) — every analytics list present and empty. The reducer always sends
  every key (they are list defaults server-side), so "empty" is a shape the server produces — unlike an
  object that omits them, which is what a `{} as Analytics` fixture claimed.
- **The builders** (L235-L318) — `lifecycle`, `gate`, `lifecycleWithGate`, `enclosure`, `provider`,
  `taskDoc`, `engineProcess`, `agentPickup`, `attentionItem`, `action`, `analytics`. Each takes
  `Overrides<O, Node>` and widens it to a plain `Partial<Node>` locally before spreading. `action` and
  `observerEvent` differ: their override is REQUIRED rather than optional, via
  `Partial<T> & Pick<T, "…">`.
- **`projection`** (L320-L341) — destructures `lifecycles`, `analytics` and `metrics` out of the
  override, then sets `metrics: metrics ?? metricsFor(lifecycles)`. **`metrics` is DERIVED from the
  lifecycles by the mirror's own rollup rather than restated beside them** — the hand-kept bucket lists
  are where the `awaiting-developer` gap kept reappearing, on both sides of the wire.
- **`supervisorHeartbeat`** (L343-L362) — a typed literal, not a served row, because the field is
  app-injected and therefore absent from the snapshot (`contract.test.ts::KnownUnsampled` names it).
- **`observerEvent`** (L364-L381) — same reasoning: the event channel (`types/event.ts` ←
  `observer/events.py`) is a separate contract from the projection, so its base cannot come from
  `snapshot.json`.
- **`reparsed(source)`** (L383-L394) — `structuredClone`, deliberately not `JSON.parse(JSON.stringify(…))`.
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

1. **Nothing about the server.** See the chain above: `contract.test.ts` *does* measure the mirror
   against `snapshot.json`, in three directions — but the crossing from `snapshot.json` to
   `observer/projection.py`, what the header calls the mirror↔server link, is hand-maintained and held
   by no test. This is the file's own framing, not a caveat added afterwards.
2. **Nothing about a pre-widened override.** `Overrides` binds a FRESH literal at the call site; an
   override that has been through a variable admits an explicit `undefined` again.
   `wireFixtureGuard.ts` covers some of that residue and `fixtureOverrides.test.ts` asserts the rest as a
   known pass.

No stale "generated snapshot" wording remains to clean up: `grep -n generated dashboard/src/test/fixtures/wire.ts`
answers only the header's own `` `snapshot.json` is NOT generated `` (L22) plus two `generatedAt` field
references (L332, L376). The three docstrings that used to contradict the header now read "the sampled
payload" (L68), "A row the snapshot is expected to carry" (L72) and "absent from the snapshot" (L344).

## Docs References

The guarantee rests on TypeScript behaviours, not on external domain documentation: an assertion skips
excess-property checking (which is what let both proven defects compile), excess-property checking
applies to fresh literals, and `structuredClone` preserves a value's static type where a JSON round-trip
does not.

| Finding | Citations | Source Path |
| --- | --- | --- |
| A type assertion performs no check and removes excess-property checking — the mechanism by which `as SomeWireType` let a `refusedPolarity` and a master-row `createdAt` compile. | Type Assertions | [TypeScript Handbook — Everyday Types / Type Assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) |
| Excess-property checking applies to fresh object literals, which is why an override written inline at the call site is checked and one routed through a variable is not. | Excess Property Checks | [TypeScript Handbook — Object Types / Excess Property Checks](https://www.typescriptlang.org/docs/handbook/2/objects.html#excess-property-checks) |
| `structuredClone` deep-clones a value at runtime; unlike a `JSON.parse(JSON.stringify(…))` round-trip it does not launder the value's static type into `any`. | `structuredClone` | [MDN — structuredClone()](https://developer.mozilla.org/en-US/docs/Web/API/Window/structuredClone) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| R6 and the two proven defects, both of which compiled because they were written with `as SomeWireType`. | L1-L13 | [wire.ts](wire.ts) |
| `BE PRECISE ABOUT WHAT PINS WHAT`: `snapshot.json` is NOT generated, no generator exists, and the chain diagram naming the link no test holds. | L22-L37 | [wire.ts](wire.ts) |
| How the defaults stay honest: required fields only, every value taken from a served row, optionals deliberately omitted. | L15-L20 | [wire.ts](wire.ts) |
| `demandServed` and the eight served anchors it demands the snapshot keep. | L71-L94 | [wire.ts](wire.ts) |
| The eight bases, each annotated with the mirror type and filled from `SERVED`. | L96-L212 | [wire.ts](wire.ts) |
| `EMPTY_ANALYTICS` — every key present and empty, which is a shape the reducer produces. | L214-L233 | [wire.ts](wire.ts) |
| `projection()` deriving `metrics` from the lifecycles via `metricsFor` rather than restating buckets. | L320-L341 | [wire.ts](wire.ts) |
| `reparsed` using `structuredClone`, with the note that `asServedProjection(JSON.parse(…))` is a vacuous check. | L383-L394 | [wire.ts](wire.ts) |
| The mirror every base and override is checked against — every node type the bases annotate, and `metricsFor` (L250-L257), which `projection()` derives with. | L1-L726 | [../../types/projection.ts](../../types/projection.ts) |
| `asServedProjection` — the sanctioned narrowing this module's `SERVED` constant is read through. | L34-L43 | [../servedProjection.ts](../servedProjection.ts) |
| The hand-maintained oracle the bases are assembled from — `lifecycles` (L4), `enclosures` (L113), `providers` (L136) and the four `analytics` rows the anchors pull (`agentPickups` L229, `taskDocuments` L287, `attentionQueue` L348, `engineProcesses` L386). | L4-L737 | [../../fixtures/snapshot.json](../../fixtures/snapshot.json) |
| The override constraint every builder takes, and the three limits it documents. | L23-L69 | [overrides.ts](overrides.ts) |
| The guard that catches the residue `Overrides` cannot — the smuggled field with no assertion to ban (L513-L525), and the `any` rule (L527-L535) whose comment names `fixtures/wire.ts::reparsed` at L530 as the site that was making exactly that mistake. | L513-L535 | [../wireFixtureGuard.test.ts](../wireFixtureGuard.test.ts) |
| `KnownUnsampled`, which names `supervisorHeartbeat` as absent from the snapshot and therefore a typed literal here. | L177-L187 | [../contract.test.ts](../contract.test.ts) |
| `ObserverEvent` — the separate event contract this module's `observerEvent` builder targets, mirroring `observer/events.py` rather than `projection.py`. | L1-L22 | [../../types/event.ts](../../types/event.ts) |
| The companion builder module for the conversation grammar. | L1-L28 | [conversationWire.ts](conversationWire.ts) |

## Cross-Repo References

No cross-repository boundary. The wire this file builds against is a Python↔TypeScript seam inside
`agents-remember`; both the producing models and the consuming mirror are in this repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The producing models are in-repo and `extra="forbid"`, which is what makes an invented fixture field impossible on the wire rather than merely unusual. | L1-L9 | [projection.py](../../../../mcp/src/agents_remember/observer/projection.py) |

## Update History

- 2026-08-01T14:05+02:00 — 260731-EFA-L4 curator (correction pass). **Withdrew Todos item 3**, which
  told the next agent to fix wording that is already fixed. The item was written from the *staged* blob
  (`git show :dashboard/src/test/fixtures/wire.ts` still carries "the generated payload" L47, "A row the
  generated snapshot" L51, "absent from the generated" L285); the **working tree** — which is what a
  reader opens — was already corrected, and `grep -n generated` over it returns only the header's own
  `` `snapshot.json` is NOT generated `` (L22) and two `generatedAt` field references (L332, L376). Also
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
