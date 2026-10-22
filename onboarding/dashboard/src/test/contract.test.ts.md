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

ServedOnlyPaths, asServedProjection and MirrorOnlyPaths guard the three sample/mirror directions. fixtureMustSample and allowlistMustStayEarned keep `KnownUnsampled` to the paths this guard genuinely cannot sample: `projection.servingBuild` and `projection.tasks[].providerLimit`; heartbeat allowances are removed. Exhaustive producer/client schema parity is the generator's and the stale-output check's, so this file is sample reach, assignability and sampled-vocabulary coverage, not schema equality.

Derived open-map/closed-union Record registries now walk native entry stage/activity, list-disagreement kind, summary and bound operations. The disagreement registry names `names-another-master`, `not-listed`, `listed-twice` and `unresolvable-master`; sampled-path nonvacuity and legal values remain distinct from exhaustive producer enum membership. valuesAt fans arrays; historical registry key counts are not a current quota.

Nonvacuous runtime checks retain sample paths/vocabularies. Native task assertions require qualified identity and forbid duplicate identity/status/children/progress in summary. Lifecycle bucket suites/master-series pins are removed; only the edge.refusedPolarity inverted pin remains.

The retired `projection.metrics.stalenessHistogram` is no longer an absorbing site; `projection.analytics.driftSnapshots[].counts` remains registered. The observed current registry has 12 keys, not a permanent quota. The local predecessor kept LifecycleProjection while retiring the gate model; L168 now replaces that lifecycle shape with native task entries, so that predecessor declaration is not a current contract.

### Historical 260831-LOCR-L17 — the retired observer-health vocabulary entries

The following account belongs to that historical source candidate. The current mirror, sample and VOCABULARIES registry have no terminal-observer-health field or five-path population.

Historical LOCR-L17 added terminalObserverHealth vocabulary paths to that epoch’s sample guard. The enduring rule is nonvacuous path reach plus earned allowances, not a historical residue quota; native entries now leave only servingBuild unsampled.

### Conventions

Structural guards are type-level; sample vocabulary assertions are runtime. The fixture guard sanctions one retained @ts-expect-error, not the former three. Source inspection runs neither gate.

### Invariants And Boundaries

Keep asServedProjection, derived Record registries, the two earned unsampled residues (`projection.servingBuild` and `projection.tasks[].providerLimit`) and nonzero sample reach. Do not restore removed heartbeat allowances.
A vacuous check remains a failure: absorbing-node reach and each vocabulary loop require nonzero samples before membership/reason checks. Registry keys stay typed as derived Records rather than untyped lists.

### Todos

**What schema codegen closes — and what this sample guard still cannot prove.**

Schema/stale-output checks own nullable-field and exhaustive vocabulary parity. A manual sample proves neither producer provenance nor nominal distinction between structurally equal models.


**L184 — INV-XZYGEB.** This contract case is sample reach, assignability and sampled-vocabulary coverage over the hand-maintained fixture; exhaustive producer/client schema parity belongs to the code generator and its stale-output check, and `projection.tasks[].providerLimit` is one of the paths this sample guard genuinely cannot reach. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

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
- AbsorbingPaths derives every string-index-signature boundary and INDEX_SIGNATURE_SITES is an exhaustive, closed Record of that derived path set, with reasons for opaque nodes in the current native-entry shape. The current literal registry has 12 keys; this is an observed census, not a fixed schema-count contract. The source test requires at least one sampled value and a nonempty reason at every registered site. Verification-age histogram and retired gate/ask sites remain absent; drift counts remain. [7]
- `ClosedUnionPaths` + `VOCABULARIES` — every registered path bound to its value set, replacing hand-written checks. [8]


- Sample vocabulary assertion: every registered path is reached and every carried value is declared by its vocabulary. [9]

- The retained inverted field pin is the single EngineProcessEdge.refusedPolarity case: an @ts-expect-error access must remain invalid while the example edge keeps state stale. The suite does not retain the former createdAt/linkedLifecycleId master/series pins; this is source-defined typecheck evidence, not a fresh typecheck or test run. [11]
- The generated mirror's metric and analytics declarations. [12]

- The sanctioned narrowing the fixture enters through. [14]





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

Execution-graph kind/frontierState paths move to projection.tasks[].summary.executionGraphView.nodes[]. Derived sample reach/value checks remain; schema generation owns complete vocabulary membership.

## CCR-R18@v1 Envelope Contract Vocabulary

260831-CCR-L18 extended the fixture-coverage guard: `INDEX_SIGNATURE_SITES` now registers `projection.enclosures[].lifecycleOperation.recommendedAction.arguments` as an index-signature site, and the closed-vocabulary registry adds `schemaVersion` / `stateMatrixVersion` (single-member v1 literals), the `incoherent` status member, `identity.operationKind`, `worker.state` (live/termination-requested/termination-required/exited), and `approval.state` (claimed/unclaimed). The exhaustive path registry still requires the representative fixture sample to reach every newly registered path with only legal values.

- The closed-vocabulary registry includes all four task-list disagreement kind values; its existing sample guard is not live record reconciliation. [22]
