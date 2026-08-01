# dashboard/src/test/contract.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/contract.test.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T10:40+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The contract guard: the only thing binding the TypeScript mirror (`types/projection.ts`) to the served
projection (`observer/projection.py`). `dashboard/src/fixtures/snapshot.json` stands in for the server —
a payload shaped by the *pydantic models*, not by the mirror — and the mirror is measured against it.

**This file is also the file that failed.** It was supposed to prevent this leaf's defect and could
not: it consumed the fixture as `snapshot as unknown as WorkspaceProjection`, a double cast that turns
off assignability, excess-property checking and everything else at once. So a served field the mirror
had never heard of typechecked and passed. That is how `State` stayed five members long while the
server declared six, and how `Metrics` bucketed three states out of six — an `awaiting-developer`
lifecycle rendered as healthy and was counted in no bucket at all. The rewrite replaces the double cast
with `asServedProjection` and adds the two directions that were missing.

## Code Commentary

### Logic

**Three seams, named in the header (L29-L53).**

1. **`mirror ⊇ served`** — the server grows a field and the hand-kept mirror does not. *This is the
   direction that happens*, and it was unguarded. `ServedOnlyPaths<Served, Mirror, Path>` (L93-L119)
   walks the fixture's own JSON-module type against the mirror and produces a union of dotted paths the
   mirror does not declare; `mirrorMustDeclare<ServedOnly extends never>()` (L121-L129) is the assertion
   — a non-`never` union fails `tsc -b` naming the path
   (`Type '"projection.metrics.awaitingReviewCount"' does not satisfy the constraint 'never'`). It
   recurses through objects and arrays and stops at an index signature, which is correct: the server
   really can put anything there.
2. **`served ⊇ mirror`** — the mirror declares something the server never sends, so a renderer branch
   ships permanently dead. Held by passing the fixture through `asServedProjection` (L75), whose
   parameter type demands every required mirror field be present, plus the `@ts-expect-error` pins at
   the bottom.
3. **`fixture ⊇ mirror`** — **the oracle itself.** Both directions above are measured against a
   hand-kept payload, so a field the fixture does not exercise is a field neither direction can see. A
   reviewer proved the cost: deleting `stateEnteredAt` and `gate.evidenceRefs`, and emptying
   `expectationRows` and `landing`, produced zero new `tsc` errors and a green suite. An empty array is
   worse than a missing field — blindness in BOTH directions at once, because `AsJsonModule` accepts
   `never[]` as assignable to anything and `ServedOnlyPaths<never, …>` is `never`.
   `MirrorOnlyPaths<Mirror, Served, Path>` (L147-L175) closes it by walking the mirror against the
   fixture's OWN type (`typeof snapshot` — empty arrays and all) and naming every declared path the
   payload does not reach. `fixtureMustSample` (L189-L192) is the assertion.

   A path is reported once, at the highest level that is missing. Arrays are keyed by TYPE, so one
   lifecycle carrying `staleSeconds` samples it for every lifecycle: the fixture need not be uniform, it
   must be COMPLETE between its rows. The scalar test comes first and the empty-array test second on
   purpose (L143-L146) — an empty array of strings hides nothing, an empty array of OBJECTS hides a whole
   model.

**The residue, named.** `KnownUnsampled` (L177-L187) is exactly two entries: `projection.servingBuild`
and `projection.supervisorHeartbeat`, both injected by the serving app at RESPONSE time and both absent
from the persisted payload this fixture is shaped like. `allowlistMustStayEarned` (L194-L197) checks the
other direction, so an entry that becomes sampled — or that names a path the mirror dropped — fails too.

**The walls of the walk, derived rather than described** (L199-L230). `AbsorbingPaths<Mirror, Path>`
finds every path the mirror types with a string index signature; `INDEX_SIGNATURE_SITES` is a
`Record<AbsorbingPaths<…>, string>`, which is exhaustive AND closed. The comment records why this
replaced prose: the old comment listed four such nodes and there were actually **seven** — and one of
the three it missed (`GateNode.evidenceRefs[]`, a `Record<string, unknown>[]`, so every key of every
evidence ref) was added by the same change that wrote the comment. The seven, each with its written
reason: `lifecycles[].ask`, `lifecycles[].gate.packet`, `lifecycles[].gate.evidenceRefs[]`,
`metrics.stalenessHistogram`, `analytics.driftSnapshots[].counts`,
`analytics.setupSummaries[].resultCounts`, `analytics.engineProcesses[].retryArgs`.

**The string vocabularies, derived rather than listed** (L232-L284). A closed union in the mirror is a
claim the server sends nothing else — and every one of them is a bare `str` in `projection.py`, so the
claim is NARROWER than the server by construction and nothing type-level can notice (the JSON import
widens literals to `string`, so a served `severity: "critical"` assigns to `"alarm" | "warn" | "info"` in
silence). Only a runtime membership check bites, and it used to cover **two** of six vocabularies
(`state`, `phase`), hand-written, leaving `severity`, `lane`, `EngineProcessNode.health` and `factState`
unguarded — `factState` alone reaching six of the eleven registered paths. So `ClosedUnionPaths` finds
every literal-union path in the mirror and `VOCABULARIES` is a `Record` over it: **11 paths bound to 6
vocabularies**, exhaustive and closed, so a new closed union anywhere in the mirror fails `tsc -b` until
it is bound, and a vocabulary bound to a path that has opened up to `string` fails too.

**`valuesAt(root, path)`** (L286-L304) reads every value at a dotted path, fanning out over `[]`, so
`…engineProcesses[].health` returns every process's health rather than the first.

**The runtime suites.**

- `the mirror declares everything the server sends` (L306-L320): the type-level walk, plus a set-equality
  between `Object.keys(served.metrics)` and `Object.keys(metricsFor([]))` — "the served rollup and the
  modelled rollup have the same fields", with no third copy to drift. A bucket only the server has fails;
  so does a bucket only the mirror has.
- `the fixture samples everything the mirror declares` (L322-L344): the two type-level assertions, plus a
  runtime pass over `INDEX_SIGNATURE_SITES` demanding a served value and a non-empty reason at each — the
  one thing types cannot say, because `MirrorOnlyPaths` deliberately stops at an index signature.
- `every closed vocabulary in the mirror is checked against the payload` (L346-L377): membership at every
  registered path (with an explicit non-vacuity check per path), then **full coverage** — members pooled
  per VOCABULARY, not per path, asserting set-equality between the vocabulary and what the fixture
  samples. The comment records the half that was missing: `toContain` over whatever the fixture happened
  to hold covered 2 of 6 states, 2 of 6 phases and 1 of 3 severities, so deleting `"close"` from `PHASES`
  produced zero failures from this file.
- `projection contract fixture` (L379-L402): top-level shape and the per-row lifecycle fields a JSON
  import cannot state.
- `metrics bucket every live lifecycle state` (L404-L469): a bucket per live state in the served payload;
  one lifecycle per live state counted into its own bucket; **bucket uniqueness** (`stateCountField` is
  not injective — `a-b` and `aB` both bucket into `aBCount`, and a collision silently overwrites because
  `Metrics` is keyed by field; the server refuses it at `state_count_fields`, the mirror cannot refuse at
  runtime, so it fails here); and **spelling parity** with the server's rule, pinned by
  `camel("awaiting-DEVELOPER") === "awaitingDEVELOPERCount"`, `camel("a-b-c") === "aBCCount"`.
- `mirror does not invent fields the server cannot send` (L471-L526): the three inverted pins, all
  TYPE-level and free at runtime. `masterRow.createdAt` and `seriesRow.linkedLifecycleId` each carry a
  `@ts-expect-error`, and so does `edge.refusedPolarity`. **An unused `@ts-expect-error` is itself a
  compile error**, so each one fails `tsc -b` the moment the field comes back.

### Conventions

- All three directions are TYPE-level: free at runtime, enforced by `npm run typecheck` (`tsc -b`). The
  runtime assertions cover only what types cannot — the string vocabularies, which the JSON import widens
  to `string`.
- Every assertion reads a vocabulary or a derived registry rather than a hand-written list. `ACTIVE_STATES`,
  `stateCountField` and `metricsFor` are imported from the mirror precisely so this file does not become
  the seventh copy of the bucket list.
- The three `@ts-expect-error` directives are registered as a single sanctioned site in
  `wireFixtureGuard.test.ts` (`src/test/contract.test.ts :: @ts-expect-error`, count 3) with a written
  reason; the count makes a fourth fail.

### Invariants And Boundaries

- The fixture enters through `asServedProjection` and nowhere else. Restoring `as unknown as
  WorkspaceProjection` reinstates the exact defect this file exists to have caught.
- `INDEX_SIGNATURE_SITES` and `VOCABULARIES` are `Record`s over DERIVED key unions. Never convert either
  to a hand-written list — being exhaustive and closed in both directions is the whole mechanism.
- `KnownUnsampled` is meant to stay two entries long. An entry added there is a field no assertion in
  this file can see; it is a hole being accepted, not a formality.
- A vacuous check must read as a failure. Both the per-path vocabulary loop and the absorbing-node loop
  assert a non-zero sample count before asserting anything about the values.

### Todos

**What this file cannot reach** — recorded in its own header (L59-L73) under `LEFT FOR CODEGEN (R3)`,
and none of it is closed here:

1. **An omitted `T | None`.** A server field that is currently null is dropped by `exclude_none=True`,
   so no sampled payload can reveal it. Only the schema can.
2. **A vocabulary member the mirror never heard of.** `VOCABULARIES` forces the fixture to exercise every
   member the MIRROR knows, which makes deleting one bite. It cannot make up a member the server declares
   and the mirror does not.
3. **Two field-identical models.** The mirror now declares `SeriesSectionNode` separately from
   `TaskSectionNode`, matching the server's two `extra="forbid"` models — but they declare the same three
   fields, so structural typing keeps them interchangeable and no walk over any payload can tell them
   apart. It is the `TaskSubTaskRefNode` / `SeriesSubTaskNode` collapse this file pins at the bottom,
   standing one model over. Only a mirror generated per model makes the distinction load-bearing.

To which the oracle's own limit must be added: **`snapshot.json` is hand-maintained and no generator
exists**, so everything above is measured against a person's account of the server. Generating the
fixture from the pydantic models is what turns "the server grew a field" into a fact rather than a
hand-edit someone has to remember. None of the assertions here change when that lands — they already
read the fixture as the server's word.

## Docs References

Two external behaviours are load-bearing: pydantic's `exclude_none` serialization (which is why an
omitted key is unreadable as evidence) and TypeScript's rule that an unused `@ts-expect-error` is itself
an error (which is what makes the inverted pins fail when a field returns).

| Finding | Citations | Source Path |
| --- | --- | --- |
| `exclude_none=True` omits `None`-valued fields from the dump, so a nullable server field simply does not appear in a sampled payload — limit (1) above. | `exclude_none` | [Pydantic — Serialization / model_dump](https://docs.pydantic.dev/latest/concepts/serialization/) |
| A `@ts-expect-error` that suppresses nothing is reported as an error — the property that turns each inverted pin into a failing typecheck the moment the field comes back. | `@ts-expect-error` | [TypeScript 3.9 Release Notes — // @ts-expect-error Comments](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-9.html#-ts-expect-error-comments) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The header: three seams, the double cast that disabled all checking, and the `LEFT FOR CODEGEN` limits. | L24-L73 | [contract.test.ts](contract.test.ts) |
| `ServedOnlyPaths` + `mirrorMustDeclare` — the `mirror ⊇ served` direction, naming the path. | L88-L129 | [contract.test.ts](contract.test.ts) |
| `MirrorOnlyPaths` + `KnownUnsampled` + `fixtureMustSample` + `allowlistMustStayEarned` — the oracle guarded, including why an empty array is worse than a missing field. | L131-L197 | [contract.test.ts](contract.test.ts) |
| `AbsorbingPaths` + `INDEX_SIGNATURE_SITES` — the seven absorbing nodes, derived and closed, replacing a prose list of four that missed three. | L199-L230 | [contract.test.ts](contract.test.ts) |
| `ClosedUnionPaths` + `VOCABULARIES` — 11 paths bound to 6 vocabularies, replacing two hand-written checks. | L232-L284 | [contract.test.ts](contract.test.ts) |
| Full-coverage assertion: members pooled per vocabulary, set-equal to what the fixture samples. | L358-L376 | [contract.test.ts](contract.test.ts) |
| Bucket suites: a bucket per live state, per-state counting, non-injectivity, and spelling parity with the server. | L404-L469 | [contract.test.ts](contract.test.ts) |
| The three inverted pins for `createdAt`, `linkedLifecycleId` and `refusedPolarity`. | L471-L526 | [contract.test.ts](contract.test.ts) |
| The mirror this file measures: the vocabulary tuples, the derived `Metrics` buckets, the two split model pairs and the `LATE MIRROR` fields. | L14-L70; L156-L220; L324-L379 | [../types/projection.ts](../types/projection.ts) |
| The sanctioned narrowing the fixture enters through. | L34-L43 | [servedProjection.ts](servedProjection.ts) |
| The hand-maintained oracle, composed to satisfy the coverage and vocabulary assertions above. | L4-L168 | [../fixtures/snapshot.json](../fixtures/snapshot.json) |
| The server's own bucket-name rule and its refusal of a non-injective mapping, which the spelling and uniqueness assertions mirror. | L230-L273 | [projection.py](../../../mcp/src/agents_remember/observer/projection.py) |
| The six-state vocabulary and the partition check this mirror is measured against. | L101-L146 | [lifecycle_state.py](../../../mcp/src/agents_remember/observer/lifecycle_state.py) |
| The two separate `extra="forbid"` sub-task models the inverted pins keep distinct, and the two section models that cannot be pinned. | L552-L582; L634-L659 | [projection.py](../../../mcp/src/agents_remember/observer/projection.py) |
| The registry entry sanctioning exactly three `@ts-expect-error` directives in this file, with its reason. | L176-L182 | [wireFixtureGuard.test.ts](wireFixtureGuard.test.ts) |
| The other half of the claim: this file makes the MIRROR honest; the guard makes the FIXTURES honest. | L18-L24 | [wireFixtureGuard.test.ts](wireFixtureGuard.test.ts) |

## Cross-Repo References

No cross-repository boundary. The contract's producer (`observer/projection.py`) and its consumer (the
dashboard mirror) both live in `agents-remember`; the seam this file guards is a language boundary
inside one repository, not a repository boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Python source of truth is in-repo, and its docstring states the served contract is client-agnostic rather than owned by any external consumer. | L1-L14 | [projection.py](../../../mcp/src/agents_remember/observer/projection.py) |

## Update History

- 2026-08-01T10:40+02:00 — 260731-EFA-L4 curator (citation pass): re-verified the two ranged
  `projection.py` citations after a worker inserted ten lines above them, and widened both ends that
  were already stopping short of a named symbol. The bucket-rule row L220-L263 → L230-L273
  (`state_count_field` L230-L245, `state_count_fields` L248-L270 with the non-injective `raise` at
  L264-L267, `STATE_COUNT_FIELDS` L273). The split-pairs row L542-L568; L624-L645 → L552-L582;
  L634-L659: the old ends landed inside `TaskSectionNode` and `SeriesSectionNode` rather than past
  them, so the two section models the claim names were only half covered — the ranges now run
  `TaskSubTaskRefNode` L552-L569 + `TaskSectionNode` L572-L582 and `SeriesSubTaskNode` L634-L649 +
  `SeriesSectionNode` L652-L659. The `L1-L14` docstring citation sits above the insertion point and
  still reads back ("client-agnostic" at L11), so it was left alone. No body text changed.
- 2026-08-01T09:40+02:00 — 260731-EFA-L4 curator: created. Records the three seams and, plainly, that
  this file is the guard that failed — the `as unknown as WorkspaceProjection` double cast is what let
  the five-member `State` union and the three-bucket `Metrics` pass. Documents `ServedOnlyPaths` /
  `MirrorOnlyPaths` (including why an empty array is worse than a missing field), the derived and closed
  `INDEX_SIGNATURE_SITES` (seven nodes, replacing a prose list of four that missed three) and
  `VOCABULARIES` (11 paths, 6 vocabularies, replacing two hand-written checks), the full-coverage
  assertion, the bucket suites and the three inverted `@ts-expect-error` pins. Carries the file's own
  three `LEFT FOR CODEGEN` limits unflattened, plus the oracle's limit — the fixture is hand-maintained,
  so the mirror↔server link is held by no test. Verification metadata pinned to the leaf base
  `abc7cbcc74921cdcb57a61529445f61641e919e7` until closeout stamps the L4 code commit.
