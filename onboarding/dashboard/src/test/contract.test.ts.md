# dashboard/src/test/contract.test.ts

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

## Evidence

### Docs References

No Domain Documentation source is configured in the resolved memory repository. The local
serialization and typecheck contracts are supported by the source references below; this pass
makes no separately verified external-library documentation claim.

No configured external documentation source applies.

### Repo-Internal References

Two external behaviours are load-bearing: pydantic's `exclude_none` serialization and TypeScript's
rule that an unused `@ts-expect-error` is itself an error. Both rows anchor on the in-repo fact that
makes the behaviour load-bearing HERE.

- Reconciled the phase registry with retired ledger publication phases; sample membership and coverage checks remain. [1]
- Persisted projection state is written by `write_projection` with omitted `None` values. [2]
- The contract test's inverted TypeScript pins are registered as an explicit fixture-guard allowance. [3]

- The header: three fixture-coverage seams, the double cast that disabled checking, and the boundary now closed by schema codegen. [4]
- `ServedOnlyPaths` + `mirrorMustDeclare` — the `mirror ⊇ served` direction, naming the path. [5]
- `MirrorOnlyPaths` + `KnownUnsampled` + `fixtureMustSample` + `allowlistMustStayEarned` — the oracle guarded, including why an empty array is worse than a missing field. [6]
- `AbsorbingPaths` + `INDEX_SIGNATURE_SITES` — the seven absorbing nodes, derived and closed. [7]
- `ClosedUnionPaths` + `VOCABULARIES` — every registered path bound to its value set, replacing hand-written checks. [8]
- Sample vocabulary assertion: every registered path is reached and every carried value is declared by its vocabulary. [9]
- Bucket suites: a bucket per live state, per-state counting, non-injectivity, and spelling parity with the server. [10]
- The three inverted pins for `createdAt`, `linkedLifecycleId` and `refusedPolarity`. [11]
- The generated mirror's metric and analytics declarations. [12]
- The generated mirror's gate and lifecycle projection declarations. [13]
- The sanctioned narrowing the fixture enters through. [14]
- The independent fixture supplies the lifecycle rows sampled by the contract. [15]
- The independent fixture supplies the metrics rollup checked against generated count fields. [16]
- The server's own bucket-name rule and its refusal of a non-injective mapping, which the spelling and uniqueness assertions mirror. [17]
- The producer's typed lifecycle vocabularies. [18]
- The registry entry sanctioning exactly three `@ts-expect-error` directives in this file, with its reason. [19]
- The other half of the claim: this file makes the MIRROR honest; the guard makes the FIXTURES honest. [20]

### Cross-Repo References

No cross-repository boundary. The contract's producer (`observer/projection.py`) and its consumer (the
dashboard mirror) both live in `agents-remember`; the seam this file guards is a language boundary
inside one repository, not a repository boundary.

- The Python source of truth is in-repo, and its docstring states the served contract is client-agnostic rather than owned by any external consumer. [21]

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
