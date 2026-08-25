# dashboard/src/test/contract.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/contract.test.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-25T16:21:43+02:00 |
| lastVerifiedCommitHash |                                                  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |                                                  2026-08-25T17:21:45+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The fixture-coverage guard for the generated TypeScript mirror. `types/projection.ts` is generated
and stale-checked from the Pydantic projection schema; this file instead measures the hand-maintained
`dashboard/src/fixtures/snapshot.json` sample against that generated contract in three directions.

L23 registers the lifecycle operation result's open value map as an index-signature site and adds
the operation kind, status, and phase paths to the closed-vocabulary registry. The registry is
exhaustive over paths; the representative sample must reach each path and carry only legal values.
The generated schema and stale-output check, not fixture row count, own exhaustive enum membership.

**This file is also the file that failed.** It was supposed to prevent this leaf's defect and could
not: it consumed the fixture as `snapshot as unknown as WorkspaceProjection`, a double cast that turns
off assignability, excess-property checking and everything else at once. So a served field the mirror
had never heard of typechecked and passed. That is how `State` stayed five members long while the
server declared six, and how `Metrics` bucketed three states out of six — an `awaiting-developer`
lifecycle rendered as healthy and was counted in no bucket at all. The rewrite replaces the double cast
with `asServedProjection` and adds the two directions that were missing.

## Code Commentary

### Logic

**Three seams, named in the header.**
cit:(["the server grows a field", "the mirror declares something the server never sends", "THE ORACLE ITSELF"], dashboard/src/test/contract.test.ts:32-32; dashboard/src/test/contract.test.ts:40-40; dashboard/src/test/contract.test.ts:45-45)

1. **`mirror ⊇ sampled payload`** — the sample carries a field the generated mirror does not.
   `ServedOnlyPaths<Served, Mirror, Path>`
   cit:([`ServedOnlyPaths`], dashboard/src/test/contract.test.ts:92-102)
   walks the fixture's own JSON-module type against the mirror and produces a union of dotted paths the
   mirror does not declare; `mirrorMustDeclare<ServedOnly extends never>()`
   cit:([`mirrorMustDeclare`], dashboard/src/test/contract.test.ts:126-128) is the assertion
   — a non-`never` union fails `tsc -b` naming the path
   (`Type '"projection.metrics.awaitingReviewCount"' does not satisfy the constraint 'never'`). It
   recurses through objects and arrays and stops at an index signature, which is correct: the server
   really can put anything there.
2. **`served ⊇ mirror`** — the mirror declares something the server never sends, so a renderer branch
   ships permanently dead. Held by passing the fixture through `asServedProjection`
   cit:([`asServedProjection`], dashboard/src/test/servedProjection.ts:41-43), whose
   parameter type demands every required mirror field be present, plus the `@ts-expect-error` pins at
   the bottom.
3. **`fixture ⊇ mirror`** — **sample coverage.** Both directions above are measured against a
   hand-kept payload, so a field the fixture does not exercise is a field neither direction can see. A
   reviewer proved the cost: deleting `stateEnteredAt` and `gate.evidenceRefs`, and emptying
   `expectationRows` and `landing`, produced zero new `tsc` errors and a green suite. An empty array is
   worse than a missing field — blindness in BOTH directions at once, because `AsJsonModule` accepts
   `never[]` as assignable to anything and `ServedOnlyPaths<never, …>` is `never`.
   `MirrorOnlyPaths<Mirror, Served, Path>`
   cit:([`MirrorOnlyPaths`], dashboard/src/test/contract.test.ts:146-160) closes it by walking the
   mirror against the fixture's OWN type (`typeof snapshot` — empty arrays and all) and naming every
   declared path the payload does not reach.
   `fixtureMustSample` cit:([`fixtureMustSample`], dashboard/src/test/contract.test.ts:192-194) is the
   assertion.

   A path is reported once, at the highest level that is missing. Arrays are keyed by TYPE, so one
   lifecycle carrying `staleSeconds` samples it for every lifecycle: the fixture need not be uniform, it
   must be COMPLETE between its rows. The scalar test comes first and the empty-array test second on
   purpose
   cit:(["The scalar test comes FIRST and the empty-array test second"], dashboard/src/test/contract.test.ts:142-142)
   — an empty array of strings hides nothing, an empty array of OBJECTS hides a whole model.

**The residue, named.** `KnownUnsampled`
cit:([`KnownUnsampled`], dashboard/src/test/contract.test.ts:186-186) is exactly two entries:
`projection.servingBuild` and `projection.agentNotifierHeartbeat`, both injected by the serving app at
RESPONSE time and both absent from the persisted payload this fixture is shaped like.
`allowlistMustStayEarned`
cit:([`allowlistMustStayEarned`], dashboard/src/test/contract.test.ts:197-199) checks the
other direction, so an entry that becomes sampled — or that names a path the mirror dropped — fails too.

**The walls of the walk, derived rather than described.**
cit:([`AbsorbingPaths`, `INDEX_SIGNATURE_SITES`], dashboard/src/test/contract.test.ts:206-219; dashboard/src/test/contract.test.ts:221-229; dashboard/src/test/contract.test.ts:226-234)
`AbsorbingPaths<Mirror, Path>` finds every path the mirror types with a string index signature;
`INDEX_SIGNATURE_SITES` is a
`Record<AbsorbingPaths<…>, string>`, which is exhaustive AND closed. The comment records why this
replaced prose: the old comment listed four such nodes and there were actually **seven** — and one of
the three it missed (`GateNode.evidenceRefs[]`, a `Record<string, unknown>[]`, so every key of every
evidence ref) was added by the same change that wrote the comment. The seven, each with its written
reason: `lifecycles[].ask`, `lifecycles[].gate.packet`, `lifecycles[].gate.evidenceRefs[]`,
`metrics.stalenessHistogram`, `analytics.driftSnapshots[].counts`,
`analytics.setupSummaries[].resultCounts`, `analytics.engineProcesses[].retryArgs`.

This test owns a different boundary: whether the hand-maintained sample actually exercises those
generated closed unions. `ClosedUnionPaths` finds every literal-union path in the mirror and
`VOCABULARIES` is a `Record` over it: the path registry is exhaustive and closed, so a
new closed union fails `tsc -b` until it is bound to the sample check, and a vocabulary bound to a path
that has opened to `string` fails too cit:([`ClosedUnionPaths`, `VOCABULARIES`], dashboard/src/test/contract.test.ts:270-285; dashboard/src/test/contract.test.ts:287-425). Runtime membership and
per-path non-vacuity catch illegal or structurally absent sample data. They deliberately do not force
the fixture to exhaust enum membership, which belongs to producer schema generation.

**`valuesAt(root, path)`** cit:([`valuesAt`], dashboard/src/test/contract.test.ts:350-365) reads every
value at a dotted path, fanning out over `[]`, so `…engineProcesses[].health` returns every process's
health rather than the first.

**The runtime suites.**

- `the mirror declares everything the server sends`
  cit:(["the mirror declares everything the server sends"], dashboard/src/test/contract.test.ts:367-381):
  the type-level walk, plus a set-equality between
  `Object.keys(served.metrics)` and `Object.keys(metricsFor([]))` — "the served rollup and the
  modelled rollup have the same fields", with no third copy to drift. A bucket only the server has fails;
  so does a bucket only the mirror has.
- `the fixture samples everything the mirror declares`
  cit:(["the fixture samples everything the mirror declares"], dashboard/src/test/contract.test.ts:395-417):
  the two type-level assertions, plus a runtime pass over
  `INDEX_SIGNATURE_SITES` demanding a served value and a non-empty reason at each — the
  one thing types cannot say, because `MirrorOnlyPaths` deliberately stops at an index signature.
- `every closed vocabulary in the mirror is checked against the payload`
  cit:(["every closed vocabulary in the mirror is checked against the payload"], dashboard/src/test/contract.test.ts:485-495):
  membership at every registered path with an explicit non-vacuity check per path. It rejects illegal
  sampled values without manufacturing full fixture objects solely to exercise unused enum members.
- `projection contract fixture`
  cit:(["projection contract fixture"], dashboard/src/test/contract.test.ts:452-475): top-level shape
  and the per-row lifecycle fields a JSON import cannot state.
- `metrics bucket every live lifecycle state`
  cit:(["metrics bucket every live lifecycle state"], dashboard/src/test/contract.test.ts:481-543): a
  bucket per live state in the served payload;
  one lifecycle per live state counted into its own bucket; **bucket uniqueness** (`stateCountField` is
  not injective — `a-b` and `aB` both bucket into `aBCount`, and a collision silently overwrites because
  `Metrics` is keyed by field; the server refuses it at `state_count_fields`, the mirror cannot refuse at
  runtime, so it fails here); and **spelling parity** with the server's rule, pinned by
  `camel("awaiting-DEVELOPER") === "awaitingDEVELOPERCount"`, `camel("a-b-c") === "aBCCount"`.
- `mirror does not invent fields the server cannot send`
  cit:(["mirror does not invent fields the server cannot send"], dashboard/src/test/contract.test.ts:538-588):
  the three inverted pins, all TYPE-level and free at runtime.
  `masterRow.createdAt` and `seriesRow.linkedLifecycleId` each carry a
  `@ts-expect-error`, and so does `edge.refusedPolarity`. **An unused `@ts-expect-error` is itself a
  compile error**, so each one fails `tsc -b` the moment the field comes back.

### Conventions

- All three structural directions are TYPE-level: free at runtime, enforced by `npm run typecheck`
  (`tsc -b`). The runtime vocabulary assertions cover the sample facts JSON-module widening hides:
  membership and non-vacuity. Schema generation and its stale-output check own exhaustive
  producer-to-TypeScript vocabulary agreement.
- Every assertion reads a vocabulary or a derived registry rather than a hand-written list. `ACTIVE_STATES`,
  `stateCountField` and `metricsFor` are imported from the mirror precisely so this file does not become
  the seventh copy of the bucket list.
- The three `@ts-expect-error` directives are registered as a single sanctioned site in
  `wireFixtureGuard.test.ts` (`src/test/contract.test.ts :: @ts-expect-error`, count 3) with a written
  reason; the count makes a fourth fail.

### Invariants And Boundaries

- The fixture enters through `asServedProjection` and nowhere else. Restoring `as unknown as
  WorkspaceProjection` reinstates the exact defect this file exists to have caught.
- `INDEX_SIGNATURE_SITES` and `VOCABULARIES` are `Record`s over derived path unions. Never convert
  their keys to an untyped list: exhaustive path registration is the mechanism. Vocabulary arrays
  validate sampled values; they do not require the sample to instantiate every member.
- `KnownUnsampled` is meant to stay two entries long. An entry added there is a field no assertion in
  this file can see; it is a hole being accepted, not a formality.
- A vacuous check must read as a failure. Both the per-path vocabulary loop and the absorbing-node loop
  assert a non-zero sample count before asserting anything about the values.

### Todos

**What schema codegen closes — and what this sample guard still cannot prove.**

1. **Omitted nullable fields and complete producer vocabularies are covered by schema generation.**
   They do not depend on a sampled payload being non-null or exhaustive. cit:(["WHAT SCHEMA CODEGEN CLOSES", "sample cannot, even a sample this file polices", "currently null is *omitted*", "only the schema can", "schema and stale-output check own that exhaustive proof"], dashboard/src/test/contract.test.ts:62-68)
2. **Two field-identical models remain structurally interchangeable in TypeScript.** The generator
   emits distinct `SeriesSectionNode` and `TaskSectionNode` declarations from distinct schemas, but
   structural assignment cannot distinguish declarations with identical fields. cit:(["two field-identical models", "matching the server's two", "declare the same three fields", "structural typing keeps them interchangeable", "collapse this file pins at the", "generation still emits both named model declarations"], dashboard/src/test/contract.test.ts:67-72)
3. **The snapshot remains a manual sample.** These assertions measure how completely that sample
   exercises the generated contract; they are not its provenance and do not generate it. cit:(["The fixture-coverage guard", "scripts/sync-projection-types.py --check", "remains a hand-authored sampled payload", "generated contract against that independent sample", "runtime vocabulary", "coverage cannot disappear", "THE ORACLE ITSELF", "field the fixture does not exercise", "reviewer proved the cost: deleting", "produced zero new", "blindness in BOTH directions at once", "as assignable to anything", "ExpectationRowNode", "below closes that", "the JSON module's exact shape", "declared path the payload does not reach"], dashboard/src/test/contract.test.ts:24-28; dashboard/src/test/contract.test.ts:45-54)

## Docs References

Two external behaviours are load-bearing: pydantic's `exclude_none` serialization (which is why an
omitted key is unreadable as evidence) and TypeScript's rule that an unused `@ts-expect-error` is itself
an error (which is what makes the inverted pins fail when a field returns). Neither has a path in either
tree, so each row is anchored on the in-repo fact that makes the behaviour load-bearing HERE — the call
that dumps the served payload, and the version this repository pins — and the vendor's own page stays in
the Finding, where a pointer belongs.

| Finding | Anchor | Source |
| --- | --- | --- |
| Persisted projection state is written by `write_projection` with omitted `None` values. | `write_projection` | mcp/src/agents_remember/serving/projections/projection_store.py:158-164 |
| The contract test's inverted TypeScript pins are registered as an explicit fixture-guard allowance. | "src/test/contract.test.ts :: @ts-expect-error" | dashboard/src/test/wireFixtureGuard.test.ts:183-183 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The header: three fixture-coverage seams, the double cast that disabled checking, and the boundary now closed by schema codegen. | "it does so at three seams"; "snapshot as unknown as WorkspaceProjection"; "WHAT SCHEMA CODEGEN CLOSES" | dashboard/src/test/contract.test.ts:30-30; dashboard/src/test/contract.test.ts:34-34; dashboard/src/test/contract.test.ts:60-60 |
| `ServedOnlyPaths` + `mirrorMustDeclare` — the `mirror ⊇ served` direction, naming the path. | `ServedOnlyPaths`; `mirrorMustDeclare` | dashboard/src/test/contract.test.ts:92-102; dashboard/src/test/contract.test.ts:126-128 |
| `MirrorOnlyPaths` + `KnownUnsampled` + `fixtureMustSample` + `allowlistMustStayEarned` — the oracle guarded, including why an empty array is worse than a missing field. | `MirrorOnlyPaths`; `KnownUnsampled`; `fixtureMustSample`; `allowlistMustStayEarned` | dashboard/src/test/contract.test.ts:146-160; dashboard/src/test/contract.test.ts:186-189; dashboard/src/test/contract.test.ts:192-194; dashboard/src/test/contract.test.ts:197-199 |
| `AbsorbingPaths` + `INDEX_SIGNATURE_SITES` — the seven absorbing nodes, derived and closed, replacing a prose list of four that missed three. | `AbsorbingPaths`; `INDEX_SIGNATURE_SITES` | dashboard/src/test/contract.test.ts:206-219; dashboard/src/test/contract.test.ts:221-229; dashboard/src/test/contract.test.ts:226-234 |
| `ClosedUnionPaths` + `VOCABULARIES` — 15 paths bound to 10 array identities and 8 distinct value sets, replacing two hand-written checks. | `ClosedUnionPaths`; `VOCABULARIES` | dashboard/src/test/contract.test.ts:251-266; dashboard/src/test/contract.test.ts:268-293 |
| Sample vocabulary assertion: every registered path is reached and every carried value is declared by its vocabulary. | "carries only values the mirror's vocabulary declares, at every registered path" | dashboard/src/test/contract.test.ts:485-495 |
| Bucket suites: a bucket per live state, per-state counting, non-injectivity, and spelling parity with the server. | "the served payload carries a bucket per live state"; "counts a lifecycle in each live state into its own bucket"; "gives each live state a bucket of its own"; "spells a bucket field the way the server spells it" | dashboard/src/test/contract.test.ts:470-475; dashboard/src/test/contract.test.ts:477-500; dashboard/src/test/contract.test.ts:502-510; dashboard/src/test/contract.test.ts:512-530 |
| The three inverted pins for `createdAt`, `linkedLifecycleId` and `refusedPolarity`. | "a master's index row is never stamped with a creation time"; "masterRow.createdAt"; "a series row never carries a cross-series lifecycle link"; "seriesRow.linkedLifecycleId"; "never carried on the edge"; "edge.refusedPolarity" | dashboard/src/test/contract.test.ts:575-578; dashboard/src/test/contract.test.ts:596-597 |
| The generated mirror's metric and analytics declarations. | `Metrics`; `Analytics` | dashboard/src/types/projection.ts:92-106; dashboard/src/types/projection.ts:356-360 |
| The generated mirror's gate and lifecycle projection declarations. | `GateNode`; `LifecycleProjection` | dashboard/src/types/projection.ts:254-264; dashboard/src/types/projection.ts:311-329 |
| The sanctioned narrowing the fixture enters through. | `asServedProjection` | dashboard/src/test/servedProjection.ts:41-43 |
| The hand-maintained oracle, composed to satisfy the coverage and vocabulary assertions above. | `lifecycles`; `metrics` | dashboard/src/fixtures/snapshot.json:1618-1618; dashboard/src/fixtures/snapshot.json:1761-1761 |
| The server's own bucket-name rule and its refusal of a non-injective mapping, which the spelling and uniqueness assertions mirror. | `state_count_field`; `state_count_fields` | mcp/src/agents_remember/observer/projection.py:239-254; mcp/src/agents_remember/observer/projection.py:257-279 |
| The producer's typed lifecycle vocabularies. | "State = Literal[LiveState, TerminalState]"; "Phase = Literal[" | mcp/src/agents_remember/models/lifecycles/responses.py:19-19; mcp/src/agents_remember/models/lifecycles/responses.py:20-27 |
| The producer's typed attention and process vocabularies. | `AttentionSeverity`; `AttentionLane`; `ProcessFactState`; `ProcessHealth` | mcp/src/agents_remember/observer/projection.py:38-45 |
| The schema generator derives mirror tuples and rejects stale generated output. | `workspace_projection_schema`; `_vocabulary_block`; `stale_generated_files` | mcp/src/agents_remember/code_quality/projection_types.py:59-61; mcp/src/agents_remember/code_quality/projection_types.py:382-421; mcp/src/agents_remember/code_quality/projection_types.py:509-515 |
| The two separate `extra="forbid"` sub-task models the inverted pins keep distinct, and the two section models that cannot be pinned. | `TaskSubTaskRefNode`; `TaskSectionNode`; `SeriesSubTaskNode`; `SeriesSectionNode` | mcp/src/agents_remember/observer/projection.py:585-606; mcp/src/agents_remember/observer/projection.py:626-636; mcp/src/agents_remember/observer/projection.py:797-812; mcp/src/agents_remember/observer/projection.py:815-822 |
| The registry entry sanctioning exactly three `@ts-expect-error` directives in this file, with its reason. | "src/test/contract.test.ts :: @ts-expect-error" | dashboard/src/test/wireFixtureGuard.test.ts:183-183 |
| The other half of the claim: this file makes the MIRROR honest; the guard makes the FIXTURES honest. | "makes the MIRROR honest"; "This file makes the FIXTURES honest" | dashboard/src/test/wireFixtureGuard.test.ts:20-21 |

## Cross-Repo References

No cross-repository boundary. The contract's producer (`observer/projection.py`) and its consumer (the
dashboard mirror) both live in `agents-remember`; the seam this file guards is a language boundary
inside one repository, not a repository boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The Python source of truth is in-repo, and its docstring states the served contract is client-agnostic rather than owned by any external consumer. | "The shapes are client-agnostic" | mcp/src/agents_remember/observer/projection.py:11-11 |

## L23 Lineage Contract Coverage

Contract parity now registers recovery `args` as the lineage projection's one
open index-signature site and checks every aggregate, edge, relation, side, and
recovery-tool vocabulary against fixture samples and the server schema.

## 260815-DAG-L4 Projection Contract

The L4 delta keeps the generated dashboard contract aligned with the backend's organizational `super-to-leaf` lineage and lifecycle-operation guidance. The dashboard remains a projection consumer: it does not gain branch-mutation authority.


## 260815-DAG-L12 Vocabulary Additions

The closed-vocabulary registry includes the two `executionGraphView` node-union paths (L12-R4): `projection.analytics.taskDocuments[].executionGraphView.nodes[].kind` and `...nodes[].frontierState`. The fixture must reach both paths and carry only declared values; schema generation owns their complete member sets.


## Update History

- 2026-08-25T16:21:43+02:00 — 260824-PDLS-L12 curator: removed the redundant pooled
  full-vocabulary fixture assertion and its stale rationale. The guard still proves exhaustive path
  registration, non-vacuity, and legality of sampled values; generated schema/codegen owns exhaustive
  producer enum membership. Also removed obsolete `not-created` from the invalidation vocabulary.
  Verification awaits the candidate code commit.


- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   closed-vocabulary registry adds the `executionGraphView` node kind and frontier state unions (L12-R4). Verified at code commit b7f2c8e2.

- 2026-08-15T23:38+02:00 — Reconciled projection parity for organizational direct-super lineage and lifecycle guidance. Verification metadata remains closeout-owned.

- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: the generated-contract registry now forces the exact
  `organizational|atomic` execution-nature vocabulary exported by the server schema.
- 2026-08-12T20:10+02:00 — L23 curator: documented complete server/dashboard lineage contract coverage; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: added the lifecycle result index-signature wall and exhaustive operation kind/status/phase vocabulary coverage; verification provenance remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-04T13:49:32+02:00 — 260731-EFA-L6 S18-B02 curator: split the Todos claims across their complete codegen, structural-typing, and manual-sample/oracle spans; extended vocabulary coverage through path/value population and comparison loops while preserving the passing inverted-pin evidence; regenerated the final ranges with the scoped fixer.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: re-scoped this file to its current job:
  coverage of a manual sample against the generated mirror. Schema codegen now closes nullable-field
  and producer-vocabulary drift; structural identity and sample completeness remain separate limits.
  The two existing header anchors/ranges in row 212 were preserved, and only the obsolete codegen
  anchor is handed off through the scoped citation fixer.

- 2026-08-02T07:20+02:00 — 260731-EFA-L6 curator (citation migration): moved all 37 citations in this
  card onto the anchored format. Nineteen prose ranges became `cit:([<anchor>], <path>:<start>-<end>)`
  and eighteen table rows gained an Anchor and a `path:start-end` Source. Three kinds of anchor were
  needed and the mix is the TypeScript story: type aliases, functions and `const` registries resolve as
  DEFINITIONS (`ServedOnlyPaths`, `MirrorOnlyPaths`, `AbsorbingPaths`, `ClosedUnionPaths`,
  `INDEX_SIGNATURE_SITES`, `VOCABULARIES`, `valuesAt`, `sampledByVocabulary`); every `describe` / `it`
  name is a STRING LITERAL, not a binding, so the six runtime-suite bullets and the bucket/pin rows are
  anchored on double-quoted literals; and the file header — three seams, the double cast, the
  `LEFT FOR CODEGEN (R3)` limits — is a comment, so it is anchored on quoted lines of its own prose.
  `asServedProjection` was the one citation that had silently meant another file: its old `L75` pointed
  inside this card's own file, and the definition is in `servedProjection.ts`, which the row and the
  prose now name. The three inverted pins are anchored on the `@ts-expect-error` reason strings rather
  than on `createdAt` / `linkedLifecycleId` / `refusedPolarity`, because those are field MENTIONS here
  (declared in `types/projection.ts`) and each occurs at several unrelated lines. The two Docs
  References rows named URLs, which `path:start-end` cannot express: the vendor page moved into the
  Finding and each row is now anchored on the in-repo fact that makes the behaviour load-bearing — the
  `write_projection` dump for `exclude_none`, and the `typescript` pin in `dashboard/package.json` for
  `@ts-expect-error`. No claim was re-pointed and no claim text was changed; ranges were regenerated
  from the anchors by the fixer rather than typed.
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
