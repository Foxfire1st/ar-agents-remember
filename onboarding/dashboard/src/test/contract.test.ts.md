# dashboard/src/test/contract.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/contract.test.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-15T20:42+02:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e`      |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
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
cit:(["the mirror declares everything the server sends"], dashboard/src/test/contract.test.ts:476-490).

## Code Commentary

### Logic

The lifecycle-operation phase registry contains no `ledger-commit` or `direct-ledger-commit`.
It follows the two-output Python/generated contract, while the same sampled-value membership
and non-vacuity assertions still cover the registered phase path. This retires obsolete values,
without requiring a fictitious ledger publication sample.

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
over derived path unions, replacing prose lists cit:([`INDEX_SIGNATURE_SITES`, `VOCABULARIES`], dashboard/src/test/contract.test.ts:225-249; dashboard/src/test/contract.test.ts:289-430).
`valuesAt` reads every value at a dotted path, fanning out over arrays
cit:([`valuesAt`], dashboard/src/test/contract.test.ts:459-474).

**The runtime suites** (`the mirror declares everything the server sends`; `the fixture
samples everything the mirror declares`; `every closed vocabulary in the mirror is checked
against the payload`; `projection contract fixture`; `metrics bucket every live
lifecycle state`; `mirror does not invent fields the server cannot send`) carry
the runtime membership, non-vacuity, bucket-uniqueness, spelling-parity, and inverted-pin checks
cit:(["the served payload carries a bucket per live state"], dashboard/src/test/contract.test.ts:559-564).

### 260831-LOCR-L17 — the observer-health vocabulary entries

`VOCABULARIES` gained the five `projection.terminalObserverHealth.*` paths (the closed unions
`status`, `schemaVersion`, `activeFailureCategory`, `activeFailureSummary`, `activeFailureType`),
and `KnownUnsampled` is deliberately UNCHANGED at its two entries: the new field is sampled by
`fixtures/snapshot.json`, so allowlisting it instead would have failed
`allowlistMustStayEarned` and left the mirror's new surface unmeasured. Two consequences are worth
recording, because both were live failure modes in this leaf's review round. First, this registry is
the reason a serve-time key cannot be added to the mirror by the producer alone: `ClosedUnionPaths`
and `VOCABULARIES` are `Record`s over derived path unions, so an unregistered closed union is a
compile error (`TS2344`/`TS2739`) rather than a silent gap — and a type-only allowlist patch turns
`tsc` green while the RUNTIME walk still fails with `no served value at
projection.terminalObserverHealth.status`. Second, the runtime check is what makes the entry
evidence rather than paperwork: it asserts a non-zero sample count first, so an entry whose fixture
value is missing or null reads as a failure instead of passing vacuously.

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

No Domain Documentation source is configured in the resolved memory repository. The local
serialization and typecheck contracts are supported by the source references below; this pass
makes no separately verified external-library documentation claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external documentation source applies. | — | — |

## Repo-Internal References

Two external behaviours are load-bearing: pydantic's `exclude_none` serialization and TypeScript's
rule that an unused `@ts-expect-error` is itself an error. Both rows anchor on the in-repo fact that
makes the behaviour load-bearing HERE.

| Finding | Anchor | Source |
| --- | --- | --- |
| Reconciled the phase registry with retired ledger publication phases; sample membership and coverage checks remain. | `VOCABULARIES` | dashboard/src/test/contract.test.ts:289-430 |
| Persisted projection state is written by `write_projection` with omitted `None` values. | `write_projection` | mcp/src/agents_remember/serving/projections/projection_store.py:158-159 |
| The contract test's inverted TypeScript pins are registered as an explicit fixture-guard allowance. | `error` | dashboard/src/test/wireFixtureGuard.test.ts:183-187 |

| Finding | Anchor | Source |
| --- | --- | --- |
| The header: three fixture-coverage seams, the double cast that disabled checking, and the boundary now closed by schema codegen. | `directions` | dashboard/src/test/contract.test.ts:30 |
| `ServedOnlyPaths` + `mirrorMustDeclare` — the `mirror ⊇ served` direction, naming the path. | `mirrorMustDeclare` | dashboard/src/test/contract.test.ts:127-128 |
| `MirrorOnlyPaths` + `KnownUnsampled` + `fixtureMustSample` + `allowlistMustStayEarned` — the oracle guarded, including why an empty array is worse than a missing field. | `fixtureMustSample` | dashboard/src/test/contract.test.ts:193-194 |
| `AbsorbingPaths` + `INDEX_SIGNATURE_SITES` — the seven absorbing nodes, derived and closed. | `INDEX_SIGNATURE_SITES` | dashboard/src/test/contract.test.ts:225-248 |
| `ClosedUnionPaths` + `VOCABULARIES` — every registered path bound to its value set, replacing hand-written checks. | `VOCABULARIES` | dashboard/src/test/contract.test.ts:289-291 |
| Sample vocabulary assertion: every registered path is reached and every carried value is declared by its vocabulary. | `UnsampledMirrorPaths` | dashboard/src/test/contract.test.ts:493-502 |
| Bucket suites: a bucket per live state, per-state counting, non-injectivity, and spelling parity with the server. | `expect` | dashboard/src/test/contract.test.ts:535-540 |
| The three inverted pins for `createdAt`, `linkedLifecycleId` and `refusedPolarity`. | `distinct` | dashboard/src/test/contract.test.ts:626 |
| The generated mirror's metric and analytics declarations. | `number` | dashboard/src/types/projection.ts:460-464 |
| The generated mirror's gate and lifecycle projection declarations. | `string` | dashboard/src/types/projection.ts:289-299 |
| The sanctioned narrowing the fixture enters through. | `asServedProjection` | dashboard/src/test/servedProjection.ts:41-43 |
| The independent fixture supplies the lifecycle rows sampled by the contract. | `false` | dashboard/src/fixtures/snapshot.json:1791-1928 |
| The independent fixture supplies the metrics rollup checked against generated count fields. | `awaitingDeveloperCount` | dashboard/src/fixtures/snapshot.json:1929-1940 |
| The server's own bucket-name rule and its refusal of a non-injective mapping, which the spelling and uniqueness assertions mirror. | `state_count_field` | mcp/src/agents_remember/observer/projection.py:249-264 |
| The producer's typed lifecycle vocabularies. | `State` | mcp/src/agents_remember/models/lifecycles/responses.py:19 |
| The registry entry sanctioning exactly three `@ts-expect-error` directives in this file, with its reason. | `error` | dashboard/src/test/wireFixtureGuard.test.ts:183-187 |
| The other half of the claim: this file makes the MIRROR honest; the guard makes the FIXTURES honest. | `projection` | dashboard/src/test/wireFixtureGuard.test.ts:20 |

## Cross-Repo References

No cross-repository boundary. The contract's producer (`observer/projection.py`) and its consumer (the
dashboard mirror) both live in `agents-remember`; the seam this file guards is a language boundary
inside one repository, not a repository boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The Python source of truth is in-repo, and its docstring states the served contract is client-agnostic rather than owned by any external consumer. | `dashboard` | mcp/src/agents_remember/observer/projection.py:11 |

## L23 Lineage Contract Coverage

Contract parity now registers recovery `args` as the lineage projection's one
open index-signature site and checks every aggregate, edge, relation, side, and
recovery-tool vocabulary against fixture samples and the server schema.

## 260815-DAG-L4 Projection Contract

The L4 delta keeps the generated dashboard contract aligned with the backend's organizational `super-to-leaf` lineage and lifecycle-operation guidance. The dashboard remains a projection consumer: it does not gain branch-mutation authority.


## 260815-DAG-L12 Vocabulary Additions

The closed-vocabulary registry includes the two `executionGraphView` node-union paths (L12-R4): `projection.analytics.taskDocuments[].executionGraphView.nodes[].kind` and `...nodes[].frontierState`. The fixture must reach both paths and carry only declared values; schema generation owns their complete member sets.

## CCR-R18@v1 Envelope Contract Vocabulary

260831-CCR-L18 extended the fixture-coverage guard: `INDEX_SIGNATURE_SITES` now registers `projection.enclosures[].lifecycleOperation.recommendedAction.arguments` as an index-signature site, and the closed-vocabulary registry adds `schemaVersion` / `stateMatrixVersion` (single-member v1 literals), the `incoherent` status member, `identity.operationKind`, `worker.state` (live/termination-requested/termination-required/exited), and `approval.state` (claimed/unclaimed). The exhaustive path registry still requires the representative fixture sample to reach every newly registered path with only legal values.

## Update History
- 2026-09-15T20:42+02:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`, base
  `99534dc5`, `contract.test.ts` +24/−0): the generated mirror's new closed unions were bound in
  `VOCABULARIES`, so a current-contract section was added. Recorded the five new
  `projection.terminalObserverHealth.*` paths, that `KnownUnsampled` stays at its two entries because
  the field is sampled by `fixtures/snapshot.json`, and both failure modes this registry produces when
  a serve-time key is added to the mirror without its companion: a compile error from the derived
  `Record`s (`TS2344`/`TS2739`) and, if the entry is allowlisted instead of sampled, a green `tsc`
  with a RED runtime walk (`no served value at projection.terminalObserverHealth.status`). The
  non-vacuity rule is what makes each entry evidence. Verification metadata remains closeout-owned;
  the `lastVerifiedCommitHash` pin is deliberately unchanged. No stamp advanced.


- 2026-09-15T01:01+00:00 — LCA-L9 R7 current candidate: Reconciled the phase registry with retired ledger publication phases; sample membership and coverage checks remain. Reviewed the uncommitted source; existing verification commit/date and all prior history are retained. This documentation pass adds no test-execution claim.


- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 7 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-05T06:38:58+00:00 — CCR L31 dashboard citation curation: re-read the scoped claims against frozen source `ea35964985f30080488270e71ac81657ac40682b`, split pooled evidence and corrected current source boundaries. Historical claims retain their recorded provenance. This is scoped claim review; existing whole-file verification metadata is unchanged.

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the new envelope signature site and closed-vocabulary registrations (recommendedAction.arguments, version literals, incoherent status, worker/approval states). Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

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
