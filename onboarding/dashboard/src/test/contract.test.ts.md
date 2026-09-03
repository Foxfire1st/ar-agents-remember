# dashboard/src/test/contract.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/contract.test.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-09-03T12:30:00+02:00                        |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b`      |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00                        |
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

Under CCR-R03@v1 the R03 leaf reformatted this file (double quotes → single quotes and collapsed
multi-line literals) and re-synchronized the dashboard contract fixtures with the newly reserialized
snapshot; no assertion, registry entry, or pinned expectation changed
cit:([describe suites], dashboard/src/test/contract.test.ts:445-647).

## Code Commentary

### Logic

**Three seams, named in the header.**
cit:(["the server grows a field", "the mirror declares something the server never sends", "THE ORACLE ITSELF"], dashboard/src/test/contract.test.ts:32-32; dashboard/src/test/contract.test.ts:40-40; dashboard/src/test/contract.test.ts:45-45)

1. **`mirror ⊇ sampled payload`** — the sample carries a field the generated mirror does not.
   `ServedOnlyPaths<Served, Mirror, Path>` names the assertion; a non-`never` union fails `tsc -b`.
2. **`served ⊇ mirror`** — held by passing the fixture through `asServedProjection` plus the
   `@ts-expect-error` pins at the bottom.
3. **`fixture ⊇ mirror`** — **sample coverage** through `MirrorOnlyPaths` and `fixtureMustSample`;
   the residue (exactly `projection.servingBuild` and `projection.agentNotifierHeartbeat`) is named
   in `KnownUnsampled` and `allowlistMustStayEarned`.

**The walls of the walk, derived rather than described.**
`AbsorbingPaths`/`INDEX_SIGNATURE_SITES` (seven absorbing nodes) and
`ClosedUnionPaths`/`VOCABULARIES` (every literal-union path registered and sampled) are `Record`s
over derived path unions, replacing prose lists cit:([`INDEX_SIGNATURE_SITES`, `VOCABULARIES`], dashboard/src/test/contract.test.ts:226-260, 287-425).
`valuesAt` reads every value at a dotted path, fanning out over arrays
cit:([`valuesAt`], dashboard/src/test/contract.test.ts:428-442).

**The runtime suites** (`the mirror declares everything the server sends` L445-459; `the fixture
samples everything the mirror declares` L461-483; `every closed vocabulary in the mirror is checked
against the payload` L485-495; `projection contract fixture` L499-522; `metrics bucket every live
lifecycle state` L528-589; `mirror does not invent fields the server cannot send` L597-647) carry
the runtime membership, non-vacuity, bucket-uniqueness, spelling-parity, and inverted-pin checks
cit:([runtime suites], dashboard/src/test/contract.test.ts:445-647).

### Conventions

- All three structural directions are TYPE-level: free at runtime, enforced by `npm run typecheck`
  (`tsc -b`). The runtime vocabulary assertions cover the sample facts JSON-module widening hides.
- Every assertion reads a vocabulary or a derived registry rather than a hand-written list; the
  three `@ts-expect-error` directives are registered as one sanctioned site in
  `wireFixtureGuard.test.ts` (count 3).

### Invariants And Boundaries

- The fixture enters through `asServedProjection` and nowhere else.
- `INDEX_SIGNATURE_SITES` and `VOCABULARIES` are `Record`s over derived path unions; never convert
  their keys to an untyped list.
- `KnownUnsampled` is meant to stay two entries long.
- A vacuous check must read as a failure; both the per-path vocabulary loop and the absorbing-node
  loop assert a non-zero sample count first.

### Todos

**What schema codegen closes — and what this sample guard still cannot prove.**

1. Omitted nullable fields and complete producer vocabularies are covered by schema generation.
2. Two field-identical models (`SeriesSectionNode`/`TaskSectionNode`) remain structurally
   interchangeable in TypeScript.
3. The snapshot remains a manual sample; these assertions are coverage, not provenance.

## Docs References

Two external behaviours are load-bearing: pydantic's `exclude_none` serialization and TypeScript's
rule that an unused `@ts-expect-error` is itself an error. Both rows anchor on the in-repo fact that
makes the behaviour load-bearing HERE.

| Finding | Anchor | Source |
| --- | --- | --- |
| Persisted projection state is written by `write_projection` with omitted `None` values. | `write_projection` | mcp/src/agents_remember/serving/projections/projection_store.py:158-164 |
| The contract test's inverted TypeScript pins are registered as an explicit fixture-guard allowance. | "src/test/contract.test.ts :: @ts-expect-error" | dashboard/src/test/wireFixtureGuard.test.ts:183-183 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The header: three fixture-coverage seams, the double cast that disabled checking, and the boundary now closed by schema codegen. | "it does so at three seams"; "snapshot as unknown as WorkspaceProjection"; "WHAT SCHEMA CODEGEN CLOSES" | dashboard/src/test/contract.test.ts:30-30; dashboard/src/test/contract.test.ts:34-34; dashboard/src/test/contract.test.ts:62-62 |
| `ServedOnlyPaths` + `mirrorMustDeclare` — the `mirror ⊇ served` direction, naming the path. | `ServedOnlyPaths`; `mirrorMustDeclare` | dashboard/src/test/contract.test.ts:94-120; dashboard/src/test/contract.test.ts:126-128 |
| `MirrorOnlyPaths` + `KnownUnsampled` + `fixtureMustSample` + `allowlistMustStayEarned` — the oracle guarded, including why an empty array is worse than a missing field. | `MirrorOnlyPaths`; `KnownUnsampled`; `fixtureMustSample`; `allowlistMustStayEarned` | dashboard/src/test/contract.test.ts:148-176; dashboard/src/test/contract.test.ts:186-189; dashboard/src/test/contract.test.ts:192-194; dashboard/src/test/contract.test.ts:197-199 |
| `AbsorbingPaths` + `INDEX_SIGNATURE_SITES` — the seven absorbing nodes, derived and closed. | `AbsorbingPaths`; `INDEX_SIGNATURE_SITES` | dashboard/src/test/contract.test.ts:206-224; dashboard/src/test/contract.test.ts:226-260 |
| `ClosedUnionPaths` + `VOCABULARIES` — every registered path bound to its value set, replacing hand-written checks. | `ClosedUnionPaths`; `VOCABULARIES` | dashboard/src/test/contract.test.ts:262-283; dashboard/src/test/contract.test.ts:287-425 |
| Sample vocabulary assertion: every registered path is reached and every carried value is declared by its vocabulary. | "carries only values the mirror's vocabulary declares, at every registered path" | dashboard/src/test/contract.test.ts:485-495 |
| Bucket suites: a bucket per live state, per-state counting, non-injectivity, and spelling parity with the server. | "the served payload carries a bucket per live state"; "counts a lifecycle in each live state into its own bucket"; "gives each live state a bucket of its own"; "spells a bucket field the way the server spells it" | dashboard/src/test/contract.test.ts:528-589 |
| The three inverted pins for `createdAt`, `linkedLifecycleId` and `refusedPolarity`. | "a master's index row is never stamped with a creation time"; "masterRow.createdAt"; "a series row never carries a cross-series lifecycle link"; "seriesRow.linkedLifecycleId"; "never carried on the edge"; "edge.refusedPolarity" | dashboard/src/test/contract.test.ts:597-647 |
| The generated mirror's metric and analytics declarations. | `Metrics`; `Analytics` | dashboard/src/types/projection.ts:92-106; dashboard/src/types/projection.ts:396-400 |
| The generated mirror's gate and lifecycle projection declarations. | `GateNode`; `LifecycleProjection` | dashboard/src/types/projection.ts:290-300; dashboard/src/types/projection.ts:351-369 |
| The sanctioned narrowing the fixture enters through. | `asServedProjection` | dashboard/src/test/servedProjection.ts:41-43 |
| The hand-maintained oracle, composed to satisfy the coverage and vocabulary assertions above. | `lifecycles`; `metrics` | dashboard/src/fixtures/snapshot.json:1749-1749; dashboard/src/fixtures/snapshot.json:1887-1887 |
| The server's own bucket-name rule and its refusal of a non-injective mapping, which the spelling and uniqueness assertions mirror. | `state_count_field`; `state_count_fields` | mcp/src/agents_remember/observer/projection.py:239-254; mcp/src/agents_remember/observer/projection.py:257-279 |
| The producer's typed lifecycle vocabularies. | "State = Literal[LiveState, TerminalState]"; "Phase = Literal[" | mcp/src/agents_remember/models/lifecycles/responses.py:19-19; mcp/src/agents_remember/models/lifecycles/responses.py:20-27 |
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

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the R03 quote-reformat and dashboard fixture synchronization of this guard and refreshed the main seam anchor ranges; assertion semantics and registry entries are unchanged.

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

- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.
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